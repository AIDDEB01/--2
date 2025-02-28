import re
string1 = input()
txt = re.match(r"ab{2,3}", string1)
return bool(txt)