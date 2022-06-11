from time import strftime


def time():
    str_time = strftime('%H:%M:%S %p')
    return str_time

def date():
    str_date = strftime('%d/%m/%Y')
    return str_date