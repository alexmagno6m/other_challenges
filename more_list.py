Notas = [4,3, 2]
def calif(notas):
    c = []
    for j in range(len(notas)):
        if notas[j] == 2:
            c.append('bad')
        elif notas[j]== 3:
            c.append('good')
        else:
            c.append('very')
    return c
a = calif(Notas)
print(a)
#multiple conditional statements into list comprehension
new_notas = ['bad' if i == 2 else 'good' if i==3 else 'very' for i in Notas]
print(new_notas)