def w_rev(sen):
    a = sen.split(" ")
    a.reverse()
    sen1 =""

    for words in a:
        sen1+=words
        sen1+=" "
    return sen1

s = input()
print(w_rev(s))