#string validatos challange
s = input()
b = list(filter(lambda i: str(i).isalnum(),s))
if len(b)>0:
    print('True')
else:
    print('False')
b = list(filter(lambda i: str(i).isalpha(),s))
if len(b)>0:
    print('True')
else:
    print('False')
b = list(filter(lambda i: str(i).isdigit(),s))
if len(b)>0:
    print('True')
else:
    print('False')
b = list(filter(lambda i: str(i).islower(),s))
if len(b)>0:
    print('True')
else:
    print('False')
b = list(filter(lambda i: str(i).isupper(),s))
if len(b)>0:
    print('True')
else:
    print('False')