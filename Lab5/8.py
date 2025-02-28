import re
string1 = input()
txt = re.split(r'[A-Z]', string1)
print(txt)