a = [2,3,4]
def mult(arr):
        total = arr*2
        return total
new = map(mult, a)
print(list(new))
new = list(map(lambda x: x * 2, a))
print(new)