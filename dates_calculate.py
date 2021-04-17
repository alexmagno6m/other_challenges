# day 26
import datetime
ret_input = input().split(' ')
due_input = input().split(' ')
returned = [int(e) for e in ret_input]
due = [int(e) for e in due_input]
returned.reverse()
due.reverse()
day_ret = datetime.date(returned[0], returned[1], returned[2])
day_due = datetime.date(due[0], due[1], due[2])
days = (day_ret -  day_due).days
anio = returned[0] - due[0]
if days <= 0:
    print(0)
elif days <= 30 and anio == 0:
    print(days * 15)
elif days > 30 and anio == 0:
    mul = int(days/30)
    print(mul * 500)
else:
    print(10000)





