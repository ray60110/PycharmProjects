def counting_birthDay(x,y,z):
    try:
        yearday=x*365
        monthday=y*30
        total=yearday+monthday+z
    except ValueError:
        return None
    else:
        return total


print(counting_birthDay(1990,3,15))
