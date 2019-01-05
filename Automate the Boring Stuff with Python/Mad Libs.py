import re

madLibsRead = open('madlibs.txt','r')
linesList = madLibsRead.readlines()
madLibsWrite = open('madlibs.txt','w')

checkRegex = re.compile(r'NOUN|ADJECTIVE|ADVERB|VERB')

for line in linesList:
    for i in checkRegex.findall(line):
        if i == 'NOUN' or i=='VERB':
            print('Enter a '+i.lower()+' :')
        else:
            print('Enter an '+i.lower()+' :')
        ans = input()
        line = checkRegex.sub(ans,line,1)
    madLibsWrite.write(line)

madLibsRead.close()
madLibsWrite.close()
