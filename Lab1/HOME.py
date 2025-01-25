'''PYTHON Intro'''
print("Hello, World!")
#our first command


'''PYTHON GET STARTED'''
import sys
print(sys.version)
# exit()
#version of our python


'''PYTHON SYNTAX'''
if 10 > 5:
   print("Five + Five Equals Ten") #Отступ обязателен, иначе ошибка
print("Так нельзя") #В каждом блоке одинаковое количество отсутпов

#Variables
a = 120
b = "five"
#Не нужно давать тип переменной



'''PYTHON COMMENTS'''
# можно ставить комменты "#" этим символом
#print("why it is not working?") в окмментах команды не работают.

"""
Можно писать коммент так на несколько строк.
И не важно сколько строк можешь занять.
"""



'''PYTHON VARIABLES'''
x = 123
y = "oneTwoThree"
print(x)
print(y)

#можно изменять тип переменной
c = 15 #был int, стал str
c = "Home" #И никто ничего не сделает за это

#Now we will be printing type of variable
z = 567
d = "ytrt"
print(type(z))
print(type(d))#It is so easy

#It doesn't matter what quotes do you use
x = "azzza"
#no difference from
x = 'azzza'

# you can create two variables using one letter
T = 25
t = "KING JARLES"
# variables are case sensitive

'''Variable names'''
print('WHEN YOU NAME A VARIABLE, IT HAS SOME RULES')
print('It is illegal to name your variables like:')
print("0ho = 56\n" + "h o = 56\n" +"h-o = 56")

print('Only using letters or underscore___')

TheGameBolmayd = 'bolad'
theGameBolmayd = 'bolad'
the_game_bolmayd = 'bolad'

#Multiple Values
s,t,o,o_2,l = 'first', 'second', 'third', 'fourth', 'fifth'
print(s)
print(t)
print(o)
print(o_2)
print(l)
#do this
s=t=o=o_2=l='stoo_2l'
print(s)
print(t)
print(o)
print(o_2)
print(l)



#Output variables
x = 'This is print function'
print(x)
#we can add variables
x = 9
y = 10
print(x + y)
x = 'hello'
z = ' '
y = 'world'
print(x + z + y)


'''Global Variables'''
x = 'global variable' # this is global variable
def fst():
   global x
   print('this is ' + x)
   x = 'global variable' # this is global variable
def fst_1():
   x = "local variable"
   print('this is ' + x)
   fst()
print("this is " + x)
fst()
fst_1()


'''
Python Datatypes
'''
x = "this is text"	#str	
x = 10	#int	
x = 10.5	#float	#плавающая запятая
x = 2j	#complex	 #комплексные числа
x = ["a", "b", "c"]	#list 	
x = ("a", "b", "c")	#tuple	"can be changed"
x = range(2)	#range	
x = {"a" : "b", "c" : 2}	#dict	
x = {"a", "b", "c"}	#set	
x = frozenset({"a", "b", "c"})	#frozenset	
x = True	#bool	
x = b"abd"	#bytes	
x = bytearray(7)	#bytearray	
#x = memoryview(apples(7))	#memoryview	
x = None	#NoneType

'''
Python Numbers
'''

x = 2025 # int
b = 2.025  # float
c = 2025j   # complex, а вообще j = -1^0.5
print(x)
print(c)
print(b)
 # convertation
x = 5 #int
x = 0.5 #int to float
x = 0.5j #float to complex

'''
Python Casting
'''
a = int(3)   # a will be 3
z = float("3")   # z will be 3.0
r = str(3.0)  # r will be '3.0'

'''
Python Strings
'''
print('This is string')
a = 'this is also string'
print(a)
a = """And
This
Is
Also
String"""
print (a)
#positions of string
a = "Happy New Year"
print(a[4]) # y will be answer
print(len(a)) #length of string
print("year" in a) #check if there is this word in a
print("Year" in a) #check if there is this word in a


#Slicing strings
ghost = "I am ghost 12313"
print(ghost[0:9])

#Modify Strings
r = "you"
print(r.upper()) #uppercase
print(r.lower()) #lowercase
print(r.strip()) # removes space
print(r.replace("u", "o"))
print(a.split(",")) # разделяет


#Concentrate strings

a = "Hello"
b = "World"
c = a + b
print(c)

#Format strings

age = 18
text = f"My name is Attila, I am {age}" # так можно совмещать строки с цифрами
print(txt)


#Escape characters

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value



#String Methods


'''capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning'''