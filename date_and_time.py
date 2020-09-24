import datetime
now = datetime.datetime.now()
print(now)

report_minutes = 5
print(now + datetime.timedelta(minutes=report_minutes))


tijd = '2020-08-03 10:55:54.123456'
date_time_obj = datetime.datetime.strptime(tijd, '%Y-%m-%d %H:%M:%S.%f')
print(tijd)
tijd = date_time_obj + datetime.timedelta(minutes=report_minutes)
if tijd < now :
    print('tijd is in het verleden')