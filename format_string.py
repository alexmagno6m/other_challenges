#challenge format_string


def number_formatted(number):
    #la longitud de la tabulacion se determina por la longitud del elemento mas grande en este caso el numero binario
    w = len(str(bin(number)[2:]))
    for i in range(1,(number+1)):
        dec = str(i)
        bi = bin(i)
        octa = oct(i)
        hexa = hex(i)
        #la alineacion derecha rjust, debe ir con dos parametros, el espacio en caracteres, y el caracter que la reemplaza
        print(dec.rjust(w,' '), octa[2:].rjust(w,' '), hexa[2:].upper().rjust(w,' '), bi[2:].rjust(w,' '))




a1 = number_formatted(50)
print(a1)
#
# a = [['hola', 'buenos', 'dias'],['como', 'estas']]
# b = list(map(lambda x: x[2:], a))
# print(b)
# c = [['mi'], ['perro']]
# f = ['hola']
# c.append(f)
# print(c)

# def formatted(n):
#     w = len("{0:b}".format(n))
#     for i in range(1, n+1):
#         print("{0:{width}d}".format(i, width=w))
# b = formatted(5)
# print(b)


