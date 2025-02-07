a = str(input())
def isPalyndrome(word):
    word = word.lower().replace(" ", "")
    if(word == word[::-1]):
        print("True")
    else:
        print("False")


isPalyndrome(a)