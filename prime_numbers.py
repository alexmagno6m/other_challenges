#day 25 hackerrank
from math import sqrt
t = int(input())
numbers = []
for j in range(t):
    num = int(input())
    numbers.append(num)
l = len(numbers)
for j in range(l):
    n = numbers[j]
    len =  int(sqrt(n))
    result = True
    acum = 0
    if n == 1:
        print('Not prime')
    elif n>1 and  n <= 3:
        print('Prime')
    else:
        for j in range(2,len+1):
            if n % j == 0:
                prime = False
                print('Not prime')
                break
            else:
                prime = True
                acum += 1
        if acum>=1 and prime==True:
            print('Prime')