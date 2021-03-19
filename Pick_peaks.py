# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

def pick_peaks(arr):
    retdict = dict()
    retdict['pos'] = []
    retdict['peaks'] = []
    for item in enumerate(arr[1:-1], 1):
        if arr[item[0]-1] < item[1] >= arr[item[0]+1]:
            retdict['pos'].append(item[0])
            retdict['peaks'].append(item[1])
        if retdict['peaks'] and item[1] == arr[item[0]-1] and item[1] == retdict['peaks'][-1] and item[1] < arr[item[0]+1]:
            retdict['pos'] = retdict['pos'][:-1]
            retdict['peaks'] = retdict['peaks'][:-1]
    if retdict['peaks'] and arr[-1] == arr[-2] == retdict['peaks'][-1]:
        retdict['pos'] = retdict['pos'][:-1]
        retdict['peaks'] = retdict['peaks'][:-1]
    return retdict
