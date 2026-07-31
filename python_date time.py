from datetime import date
d=date (2026,6,1)
print(d)

from datetime import time
t=time(10,40,59)
print(t)

from datetime import datetime
now=datetime.now()
print(now)

from datetime import datetime
today=datetime.today()
print(today)

from datetime import timedelta
td=timedelta(days=5)
print(td)

from datetime import date
today=date.today()

print(today.year)
print(today.month)
print(today.day)

from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow)