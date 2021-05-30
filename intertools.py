from itertools import product
a = [1, 2]
b = [3, 4]

axb = ((a[x], b[y]) for x in range(2) for y in range(2))
print(tuple(axb))


# for each input value to separated element on list or tuple
def power():
    a = map(int, input().rstrip().split())
    b = map(int, input().rstrip().split())
    if 0 < len(a) < 30 and 0 < len(b) < 30:
        axb = tuple((a[x], b[y]) for x in range(len(a)) for y in range(len(b)))


a = ['mi', 'perro', 'es', 'mi', 'mejor', 'amigo']
b = ' '.join(a)
print(b)
tupla = (('1', '2'), ('3', '4'))
b = ' '.join(tupla[0])
print(b)
a = map(int, input().rstrip().split())
b = map(int, input().rstrip().split())
# el asterisco permite desempaquetar el contenedor principal, en este caso
# el corchete de la lista.
print(*list(product(a,b)))