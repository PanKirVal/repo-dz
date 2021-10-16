minute = 60
hour = 3600
day = 84900
week = 604800
duration = int(input('Укажите время в секунда до недели:'))
if minute <= duration:
    if hour > duration:
        print('{} сек '.format(duration))
    elif minute <= duration < hour:
        my_minute = duration // minute
        my_second = duration % minute
        print('{}мин {} сек'.format(my_minute, my_minute))
    elif hour <= duration < day:
        my_hour = duration // hour
        duration = duration % hour
        my_minute = duration // minute
        my_second = duration % minute
        print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second))
    elif day <= duration < week:
        my_day = duration // day
        duration = duration % day
        my_hour = duration // hour
        my_minute = duration // minute
        my_second = duration % minute
        print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second))

























