#Day 16: exceptions
S = input().strip()
try:
    assert int(S)
    print(int(S))
except:
    print('bad string')