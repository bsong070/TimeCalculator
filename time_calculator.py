def add_time(start, duration, day=None):

    modifyAMPM = 0
    daysLater = 0

    dayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday', 'Sunday']

    modifier = start.split(" ")[1]
    initialAMPM = modifier

    start = start.split(' ')
    start.pop(1)
    start="".join(start)

    hour = int(start.split(":")[0])+int(duration.split(":")[0])
    minute = int(start.split(":")[1])+int(duration.split(":")[1])

    if minute > 59:
      minute -=60
      hour += 1

    hoursAMPM = hour
    while hour > 12:
      hour -=12
    
    while hoursAMPM > 11:
      hoursAMPM -=12
      modifier = 'PM' if modifier == "AM" else "AM"
      modifyAMPM+=1

    if modifyAMPM %2 != 0:
      if initialAMPM == "PM":
        modifyAMPM += 1
      else:
        modifyAMPM -= 1

    daysLater = modifyAMPM/2

    newTime = f"{hour}:{str(minute).zfill(2)} {modifier}"

    if day:
      weekday = dayList.index(day.title())
      newWeekDay = int((weekday + daysLater) % 7)
      newTime += f", {dayList[newWeekDay]}"

    if daysLater == 1:
      newTime += " (next day)"
    if daysLater > 1:
      newTime += f" ({int(daysLater)} days later)"

    return newTime