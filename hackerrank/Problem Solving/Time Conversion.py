time = input()
hh, mm, ss, ampm = time[:2], time[3:5], time[6:8], time[8:]
if ampm == 'PM': 
    if hh != '12': hh = str(int(hh) + 12)
elif hh == '12': hh = '00'
print(hh+':'+mm+':'+ss)
