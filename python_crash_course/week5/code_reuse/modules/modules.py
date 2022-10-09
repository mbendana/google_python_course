import random
import datetime

print(random.randint(1, 10))
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
#print(now.minutes)
#print(now.seconds)
print(now + datetime.timedelta(30))
