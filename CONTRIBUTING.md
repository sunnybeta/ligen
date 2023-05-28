# Contributon

Hey.

Contirbuting to this project is easy.

Simply create a file which will 

- uniquely represent the license (does not clash with any other names in use) `pie.py`
- consist of a variable within the file with the same name whose value is the entire license string and `pie="""my cool {name} license {year}"""`
- this variable, if requires name and year, must be wrapped by curl braces for f-strings to go to work
- Finally, in the `template/__init__.py` file, add a new line which imports this new file `from ligen.templates import pie`

Thank you.

