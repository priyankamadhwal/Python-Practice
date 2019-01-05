def stripRegex(string,toStrip='\s'):
    import re
    return re.sub(r'^[{0}]+|[{0}]+$'.format(toStrip), '', string)
