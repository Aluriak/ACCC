all:
	python3 -m accc

upload: 
	python setup.py sdist upload

install: _build
	python setup.py install

_build: 
	python setup.py build

tt:
	python tests/simple_use.py
