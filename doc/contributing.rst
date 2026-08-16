=================
How to contribute
=================

`Leer en español </es/stable/contributing.html>`_

To contribute, just fork this repository, make a new branch and open a `pull request`_.

.. _`pull request`: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

**cpanel-cli** is written in Python (version 3.11 or later required). The repository is organized
as follows (groups of similar generated files and command modules are abbreviated with ``*``)::

    cpanel-cli
    ├── .devcontainer
    │   └── devcontainer.json
    ├── .editorconfig
    ├── .gitignore
    ├── .github
    │   └── workflows
    │       └── ci.yml
    ├── .readthedocs.yaml
    ├── AGENTS.md
    ├── CONTRIBUTING.rst
    ├── cpanel
    │   ├── caller
    │   │   └── *.py
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── cli.py
    │   ├── core.py
    │   ├── dispatcher.py
    │   ├── util.py
    │   ├── REFERENCE
    │   └── USAGE
    ├── doc
    │   ├── _static
    │   │   ├── *.png
    │   │   └── *.svg
    │   ├── locale
    │   │   └── es
    │   │       └── LC_MESSAGES
    │   │           ├── reference
    │   │           │   └── *.po
    │   │           └── *.po
    │   ├── reference
    │   │   └── *.rst
    │   ├── conf.py
    │   ├── contributing.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── reference.rst
    │   ├── reference.sh
    │   └── requirements.txt
    ├── test
    │   ├── cpanelrc.test.example
    │   ├── test_cli.py
    │   ├── test_core.py
    │   ├── test_dispatcher.py
    │   ├── test_package.py
    │   └── test_uapi.py
    ├── LICENSE
    ├── Makefile
    ├── pyproject.toml
    ├── pyrightconfig.json
    ├── README.rst
    ├── tox.ini
    └── UAPI.md

``cpanel`` contains the application source. ``__main__.py`` is the console entry point,
``cli.py`` parses options and configuration, ``core.py`` wraps the cPanel API client,
``dispatcher.py`` routes commands to the modules in ``cpanel/caller/``, and ``util.py`` contains
shared command helpers. ``cpanel/__init__.py`` holds package metadata.

``REFERENCE`` and ``USAGE`` contain the help text used by the ``--help`` flag and the ``help``
command. They are external files so the text is easy to maintain and ``REFERENCE`` can also be
used to generate the Sphinx command reference. ``UAPI.md`` tracks which upstream cPanel UAPI
operations the client supports.

The standard ``pyproject.toml`` file contains project metadata, dependencies, the console-script
entry point, and build backend configuration. (See `Writing your pyproject.toml`_ for further
information.)

.. _`Writing your pyproject.toml`: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

The project uses the `Hatchling`_ build backend. Most package metadata is static and Hatchling
reads the version directly from ``cpanel/__init__.py``.

.. _`Hatchling`: https://pypi.org/project/hatchling/

``pyrightconfig.json`` configures the `Pyright`_ static type checker, while ``pyproject.toml``
contains the `Ruff`_ lint configuration and ``.editorconfig`` contains editor-independent
formatting settings. ``.devcontainer/devcontainer.json`` defines an optional development
container.

.. _Ruff: https://docs.astral.sh/ruff/

``test`` contains tests written with Python’s ``unittest`` framework. ``test/test_core.py`` tests
response and upload behavior, ``test/test_cli.py`` tests configuration and secret-safe logging,
``test/test_dispatcher.py`` tests command aliases and argument validation, and
``test/test_package.py`` verifies built artifact contents. These tests are isolated and require no
cPanel credentials. ``test/test_uapi.py`` is the separate integration suite; it runs against a
*live* cPanel instance using a local ``test/cpanelrc.test`` configuration file. See `Running tests`_
below for further details.

.. _`tox automation framework`: https://tox.wiki/en/latest/index.html

``doc`` contains the documentation sources, written in `reStructuredText`_ and processed using
`Sphinx`_. ``doc/conf.py`` is the Sphinx configuration, and ``doc/requirements.txt`` specifies the
documentation dependencies.

.. _`reStructuredText`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/

The documentation pages live in ``doc/*.rst``. ``doc/index.rst`` is the main page.
``doc/reference.sh`` parses ``cpanel/REFERENCE`` to generate ``doc/reference.rst`` and the files in
``doc/reference/``; do not edit those generated files manually. ``doc/_static`` contains the image
assets used by the documentation.

``.readthedocs.yaml`` is the `configuration file for Read the Docs`_ used by the remote Sphinx
build system.

.. _`configuration file for Read the Docs`: https://docs.readthedocs.io/en/stable/config-file/index.html

The Spanish translation catalogs are in ``doc/locale/es/LC_MESSAGES/``. See `Translations`_ for
further information.

Finally, the ``Makefile`` automates the development lifecycle, ``tox.ini`` defines isolated Python
3.11 and 3.12 unit environments plus an explicit integration environment, and
``.github/workflows/ci.yml`` runs the automated pull-request checks. (`Make and Makefiles are
awesome`_.)

.. _`Make and Makefiles are awesome`: https://mplanchard.com/posts/make-and-makefiles-are-awesome.html


Development environment
=======================

I developed **cpanel-cli** on Ubuntu Linux 26.04 “Resolute Raccoon” with Python 3.
**cpanel-cli**, however, has no special requirements, so any Linux distro
supporting at least Python 3.11 should work. You can also use macOS “Ventura”
or a later macOS release.

*To create a development environment on macOS*:

Install Python 3:

.. code:: sh

    $ brew install python

Homebrew will install the latest Python version available. In addition, I strongly recommend installing the `uv`_
utility and using it to install Python 3.11 and Python 3.12 alongside the current Python version:

.. code:: sh

    $ brew install uv
    $ uv python install 3.11 3.12

.. _`uv`: https://docs.astral.sh/uv/

Install GNU Make:

.. code:: sh

    $ brew install make

*To create a development environment on Linux:*

On a Debian-based distro (Ubuntu, Mint), install Python 3 using:

.. code:: sh

    $ sudo apt install python3 python3-pip python3-venv

On a RPM-based distro (RHEL, Fedora), install Python 3 using:

.. code:: sh

    $ sudo dnf install python3 python3-pip

``apt`` and ``dnf`` will install the latest Python version available. In addition, I strongly recommend installing the
modern `uv`_ utility and using it to install Python 3.11 and Python 3.12 alongside the current Python
version:

.. code:: sh

    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    $ uv python install 3.11 3.12

GNU Make is installed by default on most Linux distros. Check its availability using:

.. code:: sh

    $ make --version

Building a local ``cpanel-cli`` package from source
===================================================

Build and install a local ``cpanel-cli`` package:

.. code:: sh

    $ make install

This will:

1. Create a new virtual Python 3 environment in a ``venv`` directory

2. Locally install in ``venv`` the development packages listed on the ``[project.optional-dependencies]`` section of ``pyproject.toml``

3. Build a local Python package ``cpanel-cli``

Running the local executable
============================

To run the executable, first activate the virtual environment
(you need to run this only once per session):

.. code:: sh

    $ source venv/bin/activate

Then run the ``cpanel`` utility:

.. code:: sh

    $ cpanel --help

If you edit the sources, just run ``pip3 install .`` (note the dot ``.``) to rebuild
the local package.

Running static checks
=====================

The Python source code is annotated using type hints. Read the
`Python Type Checking Guide`_ for an introduction to Python type hints.

.. _`Python Type Checking Guide`: https://realpython.com/python-type-checking/

Type hints are not checked by the Python runtime, so this project uses Pyright_. Ruff_ provides a
separate lint pass. Both tools are installed by ``make venv`` as development dependencies.

.. _Pyright: https://github.com/Microsoft/pyright

Run both checks before submitting a change:

.. code:: sh

    $ make typecheck
    $ make lint

The type checker configuration is in ``pyrightconfig.json`` and the lint configuration is in
``pyproject.toml``. Ruff is configured as a linter only; it does not reformat the repository’s
tab-indented Python files. Use built-in generic annotations such as ``list[str]`` and
``dict[str, object]``, union syntax such as ``str | None``, and precisely parameterized callbacks.


Command and logging safety
==========================

Command-line values can contain API tokens, passwords, email addresses, message bodies, and filter
rules. Never log raw command arguments or API parameter dictionaries. Prefer structural diagnostic
messages; if a value must be represented in a log, pass it through the central ``redact()`` helper
in ``cpanel/util.py``. Add a regression test whenever logging behavior changes.

Commands are declared as specifications in ``cpanel/dispatcher.py``. Each specification contains
exact aliases, minimum and maximum argument counts, and a handler. Add or change the specification
and its focused tests together. Do not use prefix matching for command names, and validate arguments
before invoking cPanel API code.

Reusable application and dispatch code must raise ``CPanelError`` for expected failures. It must not
call ``die()`` or ``sys.exit()``; process termination belongs exclusively to the console entry point
in ``cpanel/__main__.py``. When handling cPanel responses, support the documented error payload
shapes explicitly and avoid incidental exceptions such as ``IndexError``.

Configuration discovery is a read operation. It must not create ``~/.config/cpanel/`` or any other
directory merely because the CLI looked for a configuration file.

Running tests
=============

The default test suite is isolated and does not require cPanel credentials. For a quick run using
the Python interpreter in ``venv``, use:

.. code:: sh

    $ make unit

Before submitting a change, run the default tox suite on both supported Python versions:

.. code:: sh

    $ make test

``tox.ini`` defines the Python 3.11 and 3.12 environments. Add focused unit coverage for local
logic, including configuration precedence, option parsing, exact command aliases and arity,
response error shapes, HTTP failures, and secret redaction. Tests must not depend on a network
connection, a home-directory configuration file, or cPanel credentials.

Live cPanel integration tests are kept separately in ``test/test_uapi.py``. Run them only when API
interaction is essential and you have access to a test account on a reachable cPanel host.

To set the remote hosts credentials, make a copy of the provided ``cpanelrc.test.example`` file
and name it ``cpanelrc.test`` (keep in the ``test`` directory):

.. code:: sh

    $ cp test/cpanelrc.test.example test/cpanelrc.test

Then edit ``cpanelrc.test`` and set:

- The hostname of your cPanel instance
- The username of your cPanel account
- An `API token`_ associated to that username

**Token-based authentication is the only supported authentication method.**

.. _`API token`: https://docs.cpanel.net/knowledge-base/security/how-to-use-cpanel-api-tokens/

To run the live integration suite, use:

.. code:: sh

    $ make integration

This command uses tox’s explicit ``integration`` environment and hits the
`cPanel UAPI REST interface`_ with many of the functions implemented in **cpanel-cli**. Tests that
cannot run because the account lacks suitable data must use ``skipTest()`` so the omission is
visible.

Integration tests that change remote state must register cleanup before making the change or use
``try``/``finally``. Generate unique test values, restore preexisting settings, and never commit
``test/cpanelrc.test`` or real hostnames, usernames, passwords, or API tokens.

.. _`cPanel UAPI REST interface`: https://api.docs.cpanel.net/cpanel/introduction/

Packaging
=========

Packaging is done via the `Hatchling`_ build backend, as specified on the ``[build-system]``
section of ``pyproject.toml``.

To run the packager, use:

.. code:: sh

    $ make package

The above command should generate the following two distribution files in the
temporary ``dist`` directory:

.. code:: sh

    cpanel_cli-<version>-py3-none-any.whl
    cpanel_cli-<version>.tar.gz

where ``<version>`` is the release number set in ``cpanel/__init__.py``.

The tarball is the source archive; the wheel file is the built distribution archive. The
included files for these distribution packages are listed on the ``[tool.hatch.build.targets.sdist]`` and
``[tool.hatch.build.targets.wheel]`` sections of ``pyproject.toml`` respectively.

To build both artifacts and verify their manifests, use:

.. code:: sh

    $ make package-check

The wheel must contain every ``cpanel/caller`` command module plus ``cpanel/USAGE`` and
``cpanel/REFERENCE``. The source distribution must additionally contain the tests, documentation,
and ``UAPI.md``. Update ``test/test_package.py`` whenever the required artifact contents change.

These packages are ready to be uploaded to the `Python Package Index`_.

.. _`Python Package Index`: https://pypi.org/


Continuous integration
======================

GitHub Actions runs the isolated unit suite, Pyright, Ruff, package builds, and artifact-content
checks on Python 3.11 and 3.12. Live integration tests are intentionally excluded because pull
requests must not receive cPanel credentials. A pull request should pass the same checks locally
and list the verification performed.

Building the documentation
==========================

The API documentation source files are in the ``doc`` directory. These comprise `reStructuredText`_
(``.rst``) files which are processed using `Sphinx`_ into groups of static HTML trees.

To build the documentation, use:

.. code:: sh

    $ make doc

The above command will generate several static HTML trees in ``doc/build/html``.
For example, it generates the default English documentation in ``doc/build/html/en`` —
the start page is a conventional ``index.html`` file.

This GitHub repository is currently connected to my `Read the Docs`_ account, so that
any committed (or merged) change that updates the documentation sources will automatically
trigger a remote Sphinx rebuild. The resulting updated HTML documentation will always be
available at https://cpanel-cli.readthedocs.io/en/stable/

.. _`Read the Docs`: https://readthedocs.org/

The main configuration file for Sphinx is ``doc/conf.py``. The Sphinx version and theme used
to build the documentation are in ``doc/requirements.txt``.

Translations
============

The English language ``*.rst`` files in ``doc`` are the source documentation files. Any
translation is based on these documents. Translation is done on a string-by-string basis,
using the original English string as a key (``msgid``), and the corresponding translated
string as a value (``msgstr``). For example, for Spanish:

.. code::

    msgid "To be, or not to be, that is the question"
    msgstr "Ser o no ser, he ahí el dilema"

These ``msgid`` and ``msgstr`` pairs are kept in a *catalog* file (``*.po``), which is a
simple text file. These catalog files are stored in the ``doc/locale`` subdirectory.

I personally maintain a Spanish translation of the documentation in catalog files
``doc/locale/es/LC_MESSAGES/*.po``.

Catalog ``.po`` files are compiled into ``.mo`` files using the Sphinx internationalization
utility. These compiled ``.mo`` files are later used to compose translated versions when
`Building the documentation`_.

Adding a translation
--------------------

To add a new translation:

1. Create a new catalog using:

   .. code:: sh

       $ make locale iso=<language code>

   where ``<language code>`` is the `ISO 639-1 code`_ corresponding to the new language. For
   example, to add a French translation you would use:

   .. code:: sh

       $ make locale iso=fr

   This would add a new ``locale/fr/LC_MESSAGES/index.po`` directory with several ``.po``
   files in it.

2. Edit the ``.po`` files created in step 1 and insert the translated strings as
   ``msgstr`` fields. For example:

   .. code:: sh

       msgid "Indices and tables"
       msgstr "Indices et tableaux"

3. Rebuild the documentation:

   .. code:: sh

       $ make doc

   The above command will create a new static HTML tree in ``doc/build/html/<language code>``.
   For example, for French, it will create a new tree in ``doc/build/html/fr``.

Correcting and expanding an existing translation
------------------------------------------------

if you edit the original ``doc/*.rst`` source documentation files, you need to update the
translations as well:

1. Run the following to update the catalog files:

   .. code:: sh

       $ make locale iso=<language code>

   where ``<language code>`` is the `ISO 639-1 code`_. You need to run it for every
   translated language.

2. The previous step will emit a report telling you which ``.po`` files need to be updated,
   for example:

   .. code::

       Update: doc/locale/es/LC_MESSAGES/reference.po +5, -2
       Update: doc/locale/es/LC_MESSAGES/contributing.po +9, -0

   Open the mentioned ``.po`` files and edit or add new ``msgstr`` strings. Be advised that some
   entries might get annotated as ``#, fuzzy``, which means the internationalization
   engine is not sure if there already exists a translation for the entry because of similarities
   with another entry. Just edit the ``msgstr`` text and delete the ``fuzzy`` line.

For further information, see the `Internationalization Guide`_

.. _`ISO 639-1 code`: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
.. _`Internationalization Guide`: https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
