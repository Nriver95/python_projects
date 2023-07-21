import datetime
import pytz


for timezone in pytz.all_timezones:
    if timezone =='America/New_York':
        print(timezone);
    else:
        pass

for timezone in pytz.all_timezones:
    if timezone =='Europe/London':
        print(timezone);
    else:
        pass

for timezone in pytz.all_timezones:
    if timezone =='US/Pacific':
        print(timezone);
    else:
        pass
