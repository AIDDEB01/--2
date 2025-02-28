import re
string1 = str(input())
txt = re.match(r"[a-z_]", string1)
return bool(txt)