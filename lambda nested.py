f = lambda a,b: lambda c: a+b+c
b = f(2,3)(4)
print(b)