cadena = 'abcdfghjklm'


sep = 4
# for j in range(len(cadena)):
#     strap = 0
#     cad = ''
#     while strap < sep:
#         cad = cad + cadena[j]
#         strap += 1
#     #print(cad)
#new_cadena  = [cadena[a:j] for a in range(0, 8, 4) for j in range(4,8, 4)]



def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        new_string = string[i:i + max_width]
        print( new_string)

# result = wrap(cadena, sep)
# print(result)
# esta es la solucion empleada
def wrap_2(string, max_width):
    return "\n".join([string[j:j+max_width] for j in range(0, len(string), max_width)])


result2 = wrap_2(cadena,sep)
print(result2)

cadena3 = ['mi perro', 'es  buen guardian']
a = '\n'.join(cadena3)
print(a)