import  string


def listAlphabet():
   
    return list (string.ascii_lowercase)




print (listAlphabet())

ch = listAlphabet()
lc = len(ch)
i = lc - 1
nch = ""

while i >= 0:
    nch = nch + ch [i]
    i = i - 1
    
print(nch)
