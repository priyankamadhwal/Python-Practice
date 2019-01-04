import re

def checkPassword(password):
    passRegex = re.compile(r'''(^
                                (?=.*[a-z])   # atleast one lowercase letter
                                (?=.*[A-Z])   # atleast one uppercase letter
                                (?=.*[0-9])   # atleast one digit
                                .{8,}         # length 8 or more
                                $)''', re.VERBOSE)
    if passRegex.match(password):
        print('OK')
    else:
        print('NOPE')
