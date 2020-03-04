
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

day = str(input())

if day == "SUN":
    result = 7
else:
    result = week.index("SUN") - week.index(day)

print(result)
