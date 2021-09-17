duration = int(input("Введите значение в секундах, duration = "))
if duration < 60:
    second = duration
    print(second, ' сек.')
elif duration < 3600:
    minute = duration // 60
    second = duration - (minute * 60)
    print(minute, ' мин.', second, ' сек.')
elif duration < 86400:
    hour = duration // 3600
    minute = (duration - (hour * 3600)) // 60
    second = (duration - ((hour * 3600) + (minute * 60)))
    print(hour, ' час.', minute, ' мин.', second, ' сек.')
elif duration > 86400:
    data = duration // 86400
    hour = (duration - (data * 86400)) // 3600
    minute = (duration - ((data * 86400) + hour * 3600)) // 60
    second = (duration - ((data * 86400) + (hour * 3600) + (minute * 60)))
    print(data, ' дн.', hour, ' час.', minute, ' мин.', second, ' сек.')
