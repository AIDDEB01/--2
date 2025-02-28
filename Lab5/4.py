import re
string1 = str(input())
txt = re.findall(r"[a-z]+(?:_[a-z]+)*", string1)
return bool(txt)