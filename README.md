Pyhon samples and tutorial exercises.

For the Python documentation exercise (python05.py), follow these instructions:

1. Install sphinx:

http://www.sphinx-doc.org/en/stable/install.html

2. Sphinx quickstart

http://www.sphinx-doc.org/en/stable/tutorial.html

$ sphinx-quickstart

3. Sphinx apidoc

http://scriptsonscripts.blogspot.com.es/2012/09/quick-sphinx-documentation-for-python.html

$ sphinx-apidoc -F -o doc src

4. Modify sys path to point to modules

- Edit conf.py under 'doc'
- Add the following where appropriate:
sys.path.insert(0, os.path.abspath('../../src'))

4. Build the doc

$ sphinx-build.exe -b html doc/source/ doc/build/

5. Make the html

$ cd doc
$ make html
