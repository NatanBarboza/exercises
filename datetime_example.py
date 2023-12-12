import datetime

date_1 = datetime.datetime(2023, 4, 18, 18, 00, 00)
datetime_now = datetime.datetime.now()

if date_1 > (datetime_now * 60 * 60):
    print(date_1)
else:
    print(datetime_now)