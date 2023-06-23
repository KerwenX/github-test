import datetime
import time

before = datetime.datetime.now()
print(before)

time.sleep(10)

after = datetime.datetime.now()
print(after)

delta = after - before

print(delta)
print(delta.seconds)
print(delta/60)