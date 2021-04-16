






def solve(cadena):
    b = str(cadena).split(' ')
    # por list comprehension
    #new = [b[i].capitalize() for i in range(len(b))]
    # por map
    new2 = list(map(lambda x: x.capitalize(), b))
    return ' '.join(new2)


a = solve('luisa es hermosa')
print(a)