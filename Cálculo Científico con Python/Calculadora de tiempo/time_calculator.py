
def add_time(start: str, duration: str, day_of_week: str=None) -> str:
    startOn24 = _strTo24str(start)
    durationOn24 = _strTo24str(duration)
    rawAddition = _addDuration(startOn24, durationOn24)
    normalizedDate = _normalizeRawDate(rawAddition)
    response = _formatResponse(normalizedDate, day_of_week)
    return response

def _strTo24str(strDate: str) -> tuple :
    arrDate = strDate.split(" ")
    timeSplit = arrDate[0].split(":")
    if (len(arrDate) == 2) and (arrDate[1] == "PM"):
        return (int(timeSplit[0]) + 12, int(timeSplit[1]))        
    else:
        return (int(timeSplit[0]), int(timeSplit[1]))

def _strTo12str(tupleDate: tuple) -> str:
    min = ""
    if (tupleDate[2] < 10):
        min = "0" + str(tupleDate[2])
    else:
        min = str(tupleDate[2])

    if (tupleDate[1] > 12):
        return str(tupleDate[1] -12) + ":" + min + " PM"
    elif (tupleDate[1] == 0):
        return str(12) + ":" + min + " AM"
    elif (tupleDate[1] == 12):
        return str(12) + ":" + min + " PM"
    return str(tupleDate[1]) + ":" + min + " AM"

def _addDuration(tupleDate: tuple, tupleDuration: tuple):
    addedTupleDate = (tupleDate[0] + tupleDuration[0], tupleDate[1] + tupleDuration[1])
    return addedTupleDate

def _normalizeRawDate(rawTuple: tuple) -> tuple:
    hoursAdded = rawTuple[0] + int(rawTuple[1] / 60)
    minutesLeft = rawTuple[1] % 60
    daysAdded = int(hoursAdded / 24)
    hoursLeft = hoursAdded % 24
    normalized = (daysAdded, hoursLeft, minutesLeft)
    return normalized

def _formatResponse(normalizedDate: tuple, day_of_the_week: str) -> str:
    result = _strTo12str(normalizedDate)

    if (day_of_the_week != None):
        days = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        numDay = days.get(day_of_the_week.lower())
        numDay += normalizedDate[0]
        newDayKey = numDay % 7
        newDay = list(days.keys())[list(days.values()).index(newDayKey)]
        newDay = ", " + newDay[0].upper() + newDay[1:]
        result += newDay
    
    if (normalizedDate[0] == 1):
        result += " (next day)"
    elif (normalizedDate[0] > 1):
        result += " (" + str(normalizedDate[0]) + " days later)"

    return result
