import re
string1 = input()
txt = re.sub(r'([A-Z])', r' \1', string1)
print(txt)