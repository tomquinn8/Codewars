# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

def race(v1, v2, g):
    if v1 >= v2:
        return None
    totalseconds = (g / (v2 - v1)) * 60 * 60
    hours, totalminutes = divmod(totalseconds, 3600)
    minutes, seconds = divmod(totalminutes, 60)
    return [int(hours), int(minutes), int(seconds)]

print(str(race(720, 850, 70)) + " should be [0, 32, 18]")
print(str(race(80, 91, 37)) + " should be  [3, 21, 49]")
print(str(race(820, 81, 550)) + " should be  None")
