import functools

a = [2,3,4]
new_list = functools.reduce(lambda x, y: x**2 + y, a)
print(new_list)

results = [1,2,3]
results_1 = ['bajo' if results[i] == 1 else 'medio' if results[i]==2 
    else 'alto' for i in range(3)]
print(results_1)