def add_time(startTime, durationTime, day=None):
    resultTime = []
    durationDay = 0
    weekDay = {
        0:'monday', 
        1:'tuesday', 
        2:'wednesday', 
        3:'thursday', 
        4:'friday', 
        5:'saturday', 
        6:'sunday'
    }

    #convert 12-hours format to 24-hours
    #separates the hours and the minutes
    startTime = startTime.split()
    convertedTime = startTime[0].split(':')
    if startTime[1] == 'PM':
        convertedTime[0] = int(convertedTime[0]) + 12

    #startTime + durationTime
    durationTime = durationTime.split(':')
    resultTime.append(int(convertedTime[0]) + int(durationTime[0]))
    resultTime.append(int(convertedTime[1]) + int(durationTime[1]))

    #add to hours if minutes is more than 59
    additionalHours = resultTime[1] // 60
    resultTime[0] = resultTime[0] + additionalHours
    if additionalHours > 0:
        resultTime[1] = resultTime[1] % 60

    #count Day(s) if hours is more than 23
    if resultTime[0] > 47:
        durationDay = resultTime[0] // 24
        resultTime.append(' (' + str(durationDay) + ' days later)')
    elif resultTime[0] > 23:
        durationDay = 1
        resultTime.append(' (next day)')
    else:
        resultTime.append('')
    resultTime[0] = resultTime[0] % 24
        
    #re-convert 24-hours format to 12-hours
    if resultTime[0] > 11:
        resultTime.insert(2, 'PM')
        resultTime[0] = resultTime[0] % 12
    else:
        resultTime.insert(2, 'AM')

    #if time is 00:xx, shows 12:xx instead
    if resultTime[0] == 0:
        resultTime[0] = 12

    #shows Day if it is not None
    if day is not None:
        for key, value in weekDay.items():
            if str(day).lower() == value:
                day = key
        resultDay = int(day)+durationDay
        if resultDay < 7:
            resultTime.insert(3, str(weekDay[resultDay]).capitalize())
        else:
            resultDay = resultDay % 7
            resultTime.insert(3, str(weekDay[resultDay]).capitalize())
        
        results = str(resultTime[0]) + ':' + str(resultTime[1]).zfill(2) + ' ' + resultTime[2] + ', ' + resultTime[3] + resultTime[4]
    else:
        results = str(resultTime[0]) + ':' + str(resultTime[1]).zfill(2) + ' ' + resultTime[2] + resultTime[3]

    return results

# print(add_time("3:00 PM", "3:10"))  >>>  6:10 PM
# print(add_time("11:30 AM", "2:32", "Monday"))  >>>  2:02 PM, Monday
# print(add_time("11:43 AM", "00:20"))  >>>  12:03 PM
# print(add_time("10:10 PM", "3:30"))  >>>  1:40 AM (next day)
# print(add_time("11:43 PM", "24:20", "tueSday"))  >>>  12:03 AM, Thursday (2 days later)
# print(add_time("6:30 PM", "205:12"))  >>>  7:42 AM (9 days later)
# print(add_time("2:59 AM", "24:00", "saturDay"))  >>>  2:59 AM, Sunday (next day)