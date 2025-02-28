import re
string1 = str(input())
txt = re.findall(r"(?:[A-Z][a-z]+)*", string1)
           return bool(txt)