import os, re, sys

os.chdir(r'C:\Users\DELL\Desktop\MCACODES\Python\Practice\RegexSearch')

search = ''
while search is '':
    search = input('Enter a regular expression : ')

try:
    searchRegex = re.compile(r''+search, re.I)
except:
    print('There is an error in the regular expression.')
    sys.exit()

for fileName in os.listdir(os.getcwd()):
    currentFile = open(fileName)
    lines = currentFile.readlines()
    for currentLine in lines:
        result = searchRegex.findall(currentLine)
    for each in result:
        print(each)
