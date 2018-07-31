import random, time
import locale, datetime

print('Here are 10 random dates and time from year 2000 till 2017')
for i in range(10):
    year = random.randrange(2000, 2017)
    month = random.randrange(1, 12)
    day = random.randrange(1,31)

    hour = random.randrange(0, 24)
    minute = random.randrange(0, 60)
    second = random.randrange(0,60)

    local = locale.setlocale(locale.LC_ALL,'Finnish_Finland')

    dateTimeFormat = '%d.%m.%Y %H:%M:%S'
    dateTimeString = str(day) + '.' + str(month) + '.' + str(year)\
                     + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)

    dateTimeStruct = time.strptime(dateTimeString, dateTimeFormat)
    print(time.strftime('%d %B %Y %H:%M:%S', dateTimeStruct))

