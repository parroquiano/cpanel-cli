BIN = ./venv/bin

LOCALIZER = sphinx-intl
DOCBUILDER = sphinx-build
TYPECHECKER = pyright
LINTER = ruff
UNITTESTER = tox
PUBLISHER = twine
LOCALES = $(shell ls -1 doc/locale )
TAG = $(shell git describe --tags --always --abbrev=0)

install: venv dist
	$(BIN)/pip3 install dist/cpanel*.whl

typecheck: venv
	. $(BIN)/activate && $(TYPECHECKER) cpanel/*.py cpanel/caller/*.py test/*.py

lint: venv
	$(BIN)/$(LINTER) check cpanel test

unit: venv
	PYTHONPATH=. $(BIN)/python -m unittest discover -v -s test -p 'test_core.py'
	PYTHONPATH=. $(BIN)/python -m unittest discover -v -s test -p 'test_cli.py'
	PYTHONPATH=. $(BIN)/python -m unittest discover -v -s test -p 'test_dispatcher.py'

test: venv dist
	$(BIN)/cpanel version
	$(BIN)/$(UNITTESTER)

integration: venv
	@test -f test/cpanelrc.test || ( echo "Missing test configuration file test/cpanelrc.test" && exit 1 )
	$(BIN)/$(UNITTESTER) -e integration

package: venv
	rm -f dist/*
	. $(BIN)/activate && $(BIN)/python3 -m build --wheel --sdist

package-check: package
	CPANEL_DIST_DIR=dist PYTHONPATH=. $(BIN)/python -m unittest discover -v -s test -p 'test_package.py'

dist:
	$(MAKE) package

doc: venv doc/build/gettext doc/reference.rst
	$(BIN)/$(DOCBUILDER) -b html doc doc/build/html/en
	$(foreach iso,$(LOCALES),$(BIN)/$(DOCBUILDER) -b html -D language=$(iso) doc doc/build/html/$(iso);)

publish: venv
	$(BIN)/$(PUBLISHER) upload dist/*

venv:
	python3 -m venv venv
	$(BIN)/pip3 install .[dev]

doc/build/gettext: venv install
	$(BIN)/$(DOCBUILDER) -b gettext doc doc/build/gettext

doc/reference.rst: cpanel/REFERENCE cpanel/USAGE
	bash ./doc/reference.sh $< doc/reference

locale: doc/build/gettext
	$(BIN)/$(LOCALIZER) -c doc/conf.py update -p doc/build/gettext -l $(iso)

releases:
	gh release create $(TAG)

clean:
	rm -rf venv build doc/build $$( find doc/locale/ -name *.mo ) *.egg-info .tox dist */__pycache__ ./__pycache__

.PHONY: install doc typecheck lint unit test integration package package-check publish locale releases clean
