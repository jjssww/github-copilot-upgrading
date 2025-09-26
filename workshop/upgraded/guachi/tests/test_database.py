import os
import sqlite3
import pytest
from guachi import database

@pytest.fixture(autouse=True)
def cleanup_db():
    try:
        os.remove('/tmp/test_guachi')
    except Exception:
        pass
    yield
    try:
        os.remove('/tmp/test_guachi')
    except Exception:
        pass

def test_create_database():
    foo = database.dbdict('/tmp/test_guachi')
    assert os.path.isfile('/tmp/test_guachi')

def test_init():
    foo = database.dbdict('/tmp/test_guachi')
    assert foo.db_filename == '/tmp/test_guachi'
    assert foo.table == '_guachi_data'
    assert foo.select_value == 'SELECT value FROM _guachi_data WHERE key=?'
    assert foo.select_key == 'SELECT key FROM _guachi_data WHERE key=?'
    assert foo.update_value == 'UPDATE _guachi_data SET value=? WHERE key=?'
    assert foo.insert_key_value == 'INSERT INTO _guachi_data (key,value) VALUES (?,?)'
    assert foo.delete_key == 'DELETE FROM _guachi_data WHERE key=?'

def test_init_guachi_table():
    foo = database.dbdict('/tmp/test_guachi', table='_guachi_options')
    assert foo.table == '_guachi_options'

def test_get_item_keyerror():
    foo = database.dbdict('/tmp/test_guachi')
    with pytest.raises(KeyError):
        foo['meh']

def test_get_item():
    foo = database.dbdict('/tmp/test_guachi')
    foo['bar'] = 'beer'
    assert foo['bar'] == 'beer'

def test_setitem_update():
    foo = database.dbdict('/tmp/test_guachi')
    foo['a'] = 1
    foo['a'] = 2
    assert foo['a'] == 2

def test_close_db():
    foo = database.dbdict('/tmp/test_guachi')
    foo['bar'] = 'beer'
    foo._close()
    with pytest.raises(sqlite3.ProgrammingError):
        foo.__setitem__('bar', {'a': 'b'})

def test_setitem_typeerror():
    foo = database.dbdict('/tmp/test_guachi')
    with pytest.raises(sqlite3.InterfaceError):
        foo.__setitem__('bar', {'a': 'b'})
        foo = database.dbdict('/tmp/test_guachi')
        self.assertRaises(KeyError, foo.__delitem__, 'meh')

    def test_delitem(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo['bar'], 'beer')
        del foo['bar']
        self.assertRaises(KeyError, foo.__delitem__, 'bar')

    def test_key_empty(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertEqual(foo.keys(), [])

    def test_keys_get_none(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertEqual(foo.get('does-not-exist'), None)

    def test_keys_get_value(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'value'
        self.assertEqual(foo.get('bar'), 'value')

    def test_keys_get_value_w_default(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertTrue(foo.get('foobar', True))

    def test_keys(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo.keys(), ['bar'])

    def test_integrity_check_true(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertTrue(foo._integrity_check())

#    def test_integrity_check_false(self):
#        foobar = open('/tmp/test_guachi', 'w')
#        foobar.write('meh')
#        foobar.close()
#        foo = database.dbdict('/tmp/test_guachi')
#        self.assertEquals(foo._integrity_check()[0], 'file is encrypted or is not a database')
#
        
