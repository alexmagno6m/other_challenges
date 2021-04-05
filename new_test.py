#ejemplo de uso lambda en lugar de for
a = [1,2,3,4]
b = []
#b.append(lambda x:a[x]>2)
b = list(filter(lambda x: x>2, a))
print(b)