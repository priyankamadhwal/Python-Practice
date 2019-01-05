#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe Multiclipboard.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe Multiclipboard.pyw <keyword> - Loads keyword to clipboard.
#           py.exe Multiclipboard.pyw list - Loads all keywords to clipboard.
#           py.exe Multiclipboard.pyw delete <keyword> - Delete a keyword from the shelf.
#           py.exe Multiclipboard.pyw delete - Delete all keywords from the shelf.

import pyperclip, shelve, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.pop(sys.argv[2], None)

elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
