# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    args = [int(i) for i in sorted(args)]
    returnargs = [(i, item) for i, item in enumerate(args[:-1]) if item - 1 != args[i - 1] or item + 1 != args[i + 1]] + [(len(args) - 1, args[-1])]
    returnstring = ""
    for i, item in enumerate(returnargs[:-1]):
        returnstring += str(item[1])
        returnstring += "," if returnargs[i + 1][0] == item[0] + 1 else "-"
    returnstring += str(returnargs[-1][1])
    return returnstring
