import re

Regex_Pattern = r'^[\D][A-Zbcdfghjklmnpqrstvwxyz][ad-zABCEG-Z][\S][a-zBCDFGHJKLMNPQRSTVWXYZ][^.,]'	 # Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, input()))).lower())