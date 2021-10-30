import datetime 

def timestamp(days):
    tod = datetime.datetime.now()
    d = datetime.timedelta(days = days)
     a = tod - d
    timestamp = a.replace(tzinfo=datetime.timezone.utc).timestamp()

    return timestamp

print(timestamp(100))
