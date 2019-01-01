#! python3
from pyperclip import copy
import sys

# An insecure password locker program.

PASSWORDS = {
                'gmail':'xyz1234',
                'blog':'xyxyxy12',
                'luggage':'1445'
            }
'''
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument
'''

print('*********** PASSWORD LOCKER ***********')
account = ''
while account == '':
    account = input('Enter the account name : ')

if account in PASSWORDS:
    copy(PASSWORDS[account])
    print('Password for account '+account+' copied to clipboard successfully!')

else:
    print('Could not find an account with name '+account+'.')
