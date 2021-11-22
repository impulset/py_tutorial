# https://www.delftstack.com/howto/python/python-datetime-day-of-week/
from datetime import date, datetime
print(date.fromisoformat('2021-10-18').strftime('%A'))
print(datetime.fromisoformat('2021-10-18').isoweekday())
print(datetime.now().isoformat(timespec='minutes')) #2021-11-09T13:37

#get current time
print(datetime.now().strftime("%Y-%m-%d %H:%M")) #2021-11-09 13:44

name = ['Monday', 'Tuesday', 'Friday']
ind = 0
try:
    ind = name.index('Freiday')

except:
    ind = 1
print(ind+1)    