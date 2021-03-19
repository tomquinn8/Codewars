# https://www.codewars.com/kata/52742f58faf5485cae000b9a

from math import floor
def format_duration(seconds):
    if seconds == 0: return "now"
    years = floor(seconds / (60 * 60 * 24 * 365))
    seconds -= years * 60 * 60 * 24 * 365
    days = floor(seconds / (60 * 60 * 24))
    seconds -= days * 60 * 60 * 24
    hours = floor(seconds / (60 * 60))
    seconds -= hours * 60 * 60
    minutes = floor(seconds / 60)
    seconds -= minutes * 60
    duration = [('year', years), ('day', days), ('hour', hours), ('minute',minutes), ('second', seconds)]
    duration = [item for item in duration if item[1] > 0]
    if len(duration)==1:
        return format_string(duration[0])
    elif len(duration) == 2:
        return "{0} and {1}".format(format_string(duration[0]), format_string(duration[1]))
    else:
        items = [format_string(item) for item in duration]
        returnstring = items[0]
        for item in items[1:-1]:
            returnstring += ", {0}".format(item)
        returnstring += " and {0}".format(items[-1])
        return returnstring
def format_string(item):
    return "{0} {1}{2}".format(item[1], item[0], "s" if item[1] > 1 else '')
