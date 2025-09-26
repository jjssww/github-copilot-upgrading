
# Python 3 및 최신 setuptools 환경에 맞게 setup.py 전체 교체
from setuptools import setup

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="guachi",
    version="0.0.6",
    packages=["guachi"],
    include_package_data=True,
    package_data={
        '': ['distribute_setup.py'],
    },
    author="Alfredo Deza",
    author_email="alfredodeza@gmail.com",
    description="Global, persistent configurations as dictionaries",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=["pytest"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    license="MIT",
    keywords="configuration management persistent dictionaries dictionary parse map mapping",
    url="https://github.com/jjssww/github-copilot-upgrading",
)

