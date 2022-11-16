from math import floor
import time


def convert(seconds):
    hm = time.strftime("%H:%M", time.gmtime(seconds))
    hour, min = (int(val) for val in hm.split(':'))
    if hour > 0:
        if min > 0:
            display = f'{hour} hours and {min} minutes'
        else:
            display = f'{hour} hours'
    else:
        display = f'{min} minutes'
        
    return display

    
    
try:
    delay = int(input('Enter the session timeout value in seconds: '))
except ValueError:
    raise Exception("Please enter a whole number for this to work. ")
    
print(convert(delay))

# time = delay / 60
# if time > 60:
#     time = time / 60
# hour = floor(time)
# min = round((time % 1) * 60)
# if min == 60:
#     min = 0
#     hour = hour + 1
# if hour > 0 and min > 0:
#     time = f'{hour} hours {min} minutes'
# elif hour > 0:
#     time = f'{hour} hours'
# else:
#     time = f'{round(time)} minutes'
    
# print(time)


