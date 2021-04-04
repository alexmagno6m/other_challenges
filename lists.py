#list challenge hackerrank python
n = 3
lista = []
for i in range(n):
    command = input().split()
    if command[0] == 'insert':
        lista.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(lista)
    elif command[0] == 'remove':
        lista.remove(int(command[1]))
    elif command[0] == 'append':
        lista.append(int(command[1]))
    elif command[0] == 'sort':
        lista.sort()
    elif command[0] == 'pop':
        lista.pop()
    elif command[0] == 'reverse':
        lista.reverse()

