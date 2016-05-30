from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previout_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    day_ago = (7 + day_num - day_num_target) % 7
    if day_ago == 0:
        day_ago = 7
    target_date = start_date - timedelta(days=day_ago)
    return target_date

print datetime.today()
print get_previout_byday('Monday')
print get_previout_byday('Tuesday')
print get_previout_byday('Friday')
print get_previout_byday('Sunday', datetime(2012, 12, 21))