#! python3

# Bullet Point Adder

from pyperclip import copy, paste

text = paste()
print('Text copied from clipboard...',text,sep='\n')

lines = text.split('\n')

for i  in range(len(lines)):
    lines[i] = '* '+lines[i]

text = '\n'.join(lines)

copy(text)

print('Successfully added bullet points and copied text to clipboard...',text,sep='\n')
