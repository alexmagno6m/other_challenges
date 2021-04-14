alpha = ['a', 'b', 'c', 'd', 'e']
print(alpha[2:0:-1])
print(alpha[1:3])
a = len(alpha)
n = a - 1
char = '-'
print(char.rjust(4*2-1, char)+char.join(alpha[5:4:-1])+char+alpha[a-1]+char+char.join(alpha[5:5])+char.rjust((4*2)-1, char))
print(char.rjust(4*2-2, char)+char.join(alpha[5:3:-1])+char+alpha[a-2]+char+char.join(alpha[4:5])+char.rjust(4*2-2, char))
print(char.rjust(3*2-2, char)+char.join(alpha[5:2:-1])+char+alpha[a-3]+char+char.join(alpha[3:5])+char.rjust(3*2-2, char))
print(char.rjust(2*2-2, char)+char.join(alpha[5:1:-1])+char+alpha[a-4]+char+char.join(alpha[2:5])+char.rjust(2*2-2, char))
print(char.join(alpha[5:0:-1])+char+alpha[a-5]+char+char.join(alpha[1:5]))