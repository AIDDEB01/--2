import re
string1 = str(input())
txt = re.match(r"ab*", string1 )
if txt:
  return True
else:
  return False             