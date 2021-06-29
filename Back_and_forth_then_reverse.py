# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

def arrange(s):
    t = []
    for i in range(len(s) // 2 + len(s) % 2):
        if i % 2 == 0:
            t.append(s[i])
        else:
            t.append(s[-(i+1)])
        if len(t) < len(s):
            if i % 2 == 0:
                t.append(s[-(i+1)])
            else:
                t.append(s[i])
    return t
