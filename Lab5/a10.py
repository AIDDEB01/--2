import re
camel = input()
txt = re.split(r'(?=[A-Z])', camel) 
snake = '_'.join(txt).lower()
  
print(snake)