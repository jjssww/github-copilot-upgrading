import os
import pytest
from guachi import ConfigMapper
from guachi.database import dbdict

DEFAULT_CONFIG = {
    'frequency': 60,
    'master': 'False',
    'host': 'localhost',
    'ssh_user': 'root',
    'ssh_port': 22,
    'hosts_path': '/opt/pacha',
    'hg_autocorrect': 'True',
    'log_enable': 'False',
    'log_path': 'False',
    'log_level': 'DEBUG',
    'log_format': '%(asctime)s %(levelname)s %(name)s %(message)s',
    'log_datefmt': '%H:%M:%S'
}

@pytest.fixture(autouse=True)
def cleanup_db():
    for f in ['/tmp/guachi.db', '/tmp/foo_guachi.db']:
        try:
            os.remove(f)
        except Exception:
            pass
    yield
    for f in ['/tmp/guachi.db', '/tmp/foo_guachi.db']:
        try:
            os.remove(f)
        except Exception:
            pass

def test_init():
    foo = ConfigMapper('/tmp')
    expected = '/tmp/guachi.db'
    actual = foo.path
    assert actual == expected

def test_call():
    foo = ConfigMapper('/tmp')
    actual = foo()
    expected = {}
    assert actual == expected

def test_set_ini_options():
    foo = ConfigMapper('/tmp')
    my_config = {'config.db.port': 'db_port'}
    foo.set_ini_options(my_config)
    db = dbdict(path='/tmp/guachi.db', table='_guachi_options')
        actual = db.get_all()
        assert actual == my_config


    def test_set_default_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'db_port':1234}
        foo.set_default_options(my_config)
        db = dbdict(path='/tmp/guachi.db', table='_guachi_defaults')
            actual = db.get_all()
            assert actual == my_config


    def test_get_ini_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'config.db.port':'db_port'}
        foo.set_ini_options(my_config)
        defaults = foo.get_ini_options()
        actual = defaults['config.db.port']
            assert actual == 'db_port'


    def test_get_default_options(self):
        foo = ConfigMapper('/tmp')
        my_config = {'db_port':1234}
        foo.set_default_options(my_config)
        defaults = foo.get_default_options()
        actual = defaults['db_port']
            assert actual == 1234


    def test_path_verify_file(self):
        foo = ConfigMapper('/tmp/foo_guachi.db')
        actual = foo._path_verify('/tmp/foo_guachi.db')
            assert actual == '/tmp/foo_guachi.db'


    def test_path_verify_dir(self):
        foo = ConfigMapper('/tmp')
        actual = foo._path_verify('/tmp')
            assert actual == '/tmp/guachi.db'

    def test_update_config_dict_empty(self):
        """Pass an empty dict and get defaults back"""
        foo = ConfigMapper('/tmp')
        foo.update_config({})
        db = dbdict('/tmp/guachi.db')
        actual = db.get_all()
            assert actual == {}
        

    def test_update_config_dict(self):
        foo = ConfigMapper('/tmp')
        foo.update_config(DEFAULT_CONFIG)
        db = dbdict('/tmp/guachi.db')
        actual = db.get_all()
            assert actual == DEFAULT_CONFIG
 
        
    def test_set_config_dict_empty(self):
        """Pass an empty dict and get defaults back"""
        foo = ConfigMapper('/tmp')
        foo.set_config({})
        db = dbdict('/tmp/guachi.db')
        actual = db.get_all()
            assert actual == {}
        

    def test_set_config_dict(self):
        foo = ConfigMapper('/tmp')
        foo.set_config(DEFAULT_CONFIG)
        db = dbdict('/tmp/guachi.db')
        actual = db.get_all()
            assert actual == DEFAULT_CONFIG
 

    def test_get_dict_config(self):
        foo = ConfigMapper('/tmp')
        foo.set_config(DEFAULT_CONFIG)
        actual = foo.get_dict_config()
            assert actual == DEFAULT_CONFIG


    def test_integrity_check(self):
        foo = ConfigMapper('/tmp')
        foo.set_config(DEFAULT_CONFIG)
        actual = foo.integrity_check()
            assert actual


    def test_stored(self):
        foo = ConfigMapper('/tmp')
        bar = foo.stored_config()
            assert bar == {}


    def test_stored_get_data(self):
        """Verify we can actually get data by using stored"""
        foo = ConfigMapper('/tmp')
        bar = foo.stored_config()
        bar['a'] = 1
            assert dict(bar) == {'a': 1}


