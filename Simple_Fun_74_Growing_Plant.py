# https://www.codewars.com/kata/58941fec8afa3618c9000184

def growing_plant(upSpeed, downSpeed, desiredHeight):
    #your code heredef growing_plant(upSpeed, downSpeed, desiredHeight):
    currentHeight = upSpeed
    day = 1
    while currentHeight < desiredHeight:
        currentHeight += upSpeed
        currentHeight -= downSpeed
        day+=1
    return day
