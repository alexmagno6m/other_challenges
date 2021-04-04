#challenge tuples hackerrank
n = int(input())
integer_list = map(int, input().split())
new_tuple = tuple(integer_list)
print(hash(new_tuple))