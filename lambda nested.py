f = lambda a,b: lambda c: a+b+c
b = f(2,3)(4)
print(b)
a = 'hola'
b = lambda f, s: s in f
d = b('perro', 'e')
print(d)