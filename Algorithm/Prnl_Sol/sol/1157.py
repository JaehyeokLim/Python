import sys
from collections import Counter

str = sys.stdin.readline()

str_c = Counter(str.lower()).most_common()

if len(str_c) == 2 and str_c[1][0] == '\n':
    print(str_c[0][0].upper())
elif str_c[0][1] == str_c[1][1]:
    print('?')
elif len(str_c) == 1:
    print(str_c[0][0].upper())
else:
    print(str_c[0][0].upper())




