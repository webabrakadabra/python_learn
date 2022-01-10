pattern = r'[[1][2][3]][120][xs0][30Aa][xsu][.,]$'	# Do not delete 'r'.
sting = '1000u.'
import re


print(str(bool(re.search(pattern, sting))).lower())
