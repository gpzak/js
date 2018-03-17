import time
from datetime import date

yyyy=int(input("Rok: "))
mm=int(input("Miesiąc: "))
dd=int(input("Dzień: "))

d=date(yyyy,mm,dd)
today=date.today()

t=abs(d-today)
print(t.days)

input()