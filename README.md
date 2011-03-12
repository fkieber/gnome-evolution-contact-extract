#Extraction[/Display/Printing] contacts of gnome-evolution.

###Dependencies
[dev-python/evolution-python](http://live.gnome.org/Conduit/evolution-python)

###Description
For now, only the extraction of a contacts list in "CSV" format is supported.

- Configuration is done via a dictionary in the source print_tel.py.
- Multiple address books to treat or omit.
- Multiple categories to include or exclude contacts.
- Creating fields to extract.
- Each field can come from several properties of the contact. In this case, the first non-empty property that is taken.

###To Do:

- A graphical interface for configuring an extraction.
- Save/restore a extraction.
- Display/printing of extracted data.

###License
Refer to the LICENSE file