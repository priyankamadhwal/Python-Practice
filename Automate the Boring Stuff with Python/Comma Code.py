def commaCode(myList):
    if myList == []: return ''
    elif len(myList) == 1: return myList[0]
    else: return '{}, and {}'.format(', '.join(myList[:-1]), myList[-1])
