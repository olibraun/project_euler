#!/usr/bin/python

import datetime

current = datetime.date(1901,01,01)
oneday = datetime.timedelta(days=1)

end_date = datetime.date(2000,12,31)

count = 0
while current <= end_date:
  if current.weekday() == 6 and current.day == 1:
    count += 1
  current = current + oneday

print count