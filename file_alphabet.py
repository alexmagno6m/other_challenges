import os
import sys
import string
char = '-'
n = 5
letras = list(string.ascii_lowercase)
if n == 1:
    print(letras[n-1])
else:
    for i in range(n-1):
        j = i + 1
        width = (n-j)*2
        if i == 0:
            print(char.rjust(width,char) + char.join(reversed(letras[n-1-i:n]))+ char +char.join(letras[n-i:n]) +char.rjust(width-1,char))
        else:
            print(char.rjust(width, char) + char.join(reversed(letras[n - 1 - i:n])) + char + char.join(
                letras[n - i:n]) + char.rjust(width, char))
    print(char.join(reversed(letras[:n]))+char+char.join(letras[1:n]))
    for i in range(n-2, -1, -1):
        j = i + 1
        width = (n-j)*2
        if i == 0:
            print(char.rjust(width,char) + char.join(reversed(letras[n-1-i:n]))+ char +char.join(letras[n-i:n]) +char.rjust(width-1,char))
        else:
            print(char.rjust(width, char) + char.join(reversed(letras[n - 1 - i:n])) + char + char.join(
                letras[n - i:n]) + char.rjust(width, char))