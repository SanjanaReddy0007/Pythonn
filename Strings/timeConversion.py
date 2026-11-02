
T = input()
seconds = T[-1] == "S"
T = T[:-1]
T = int(T)

if seconds:
    seconds_to_hour = T / 3600
    seconds_to_hour = round(seconds_to_hour,2)
    hours = str(seconds_to_hour) + "H"
else:
    minutes_to_hour = T / 60
    minutes_to_hour = round(minutes_to_hour,2)
    hours = str(minutes_to_hour) + "H"
print(hours)

