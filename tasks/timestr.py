__all__ = (
    'seconds_to_str',
)

def seconds_to_str(seconds: int) -> str:
    days, seconds = divmod(seconds, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)

    days = str(days).zfill(2)
    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)


    if days == '00':
        if hours == '00':
            if minutes == '00':
                stroka = f'{seconds}s'
            else:
                stroka = f'{minutes}m' + f'{seconds}s'
        else:
            stroka = f'{hours}h' + f'{minutes}m' + f'{seconds}s'
    else:
        stroka = f'{days}d' + f'{hours}h' + f'{minutes}m' + f'{seconds}s'


    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """


    return stroka


