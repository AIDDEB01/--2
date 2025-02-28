import re

snake = input()
txt = re.split(r'_', snake)
camel = txt[0] + ''.join(word.capitalize() for word in txt[1:])
print(camel)