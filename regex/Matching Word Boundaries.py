Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
