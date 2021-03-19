# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa

def is_merge(s, part1, part2):
    for c in s:
        s = s[1:]
        if part1.startswith(c) and part2.startswith(c):
            if is_merge(s, part1[1:], part2) or is_merge(s, part1, part2[1:]):
                return True
        elif part1.startswith(c):
            part1 = part1[1:]
        elif part2.startswith(c):
            part2 = part2[1:]
        else:
            return False
    part1, part2 = part1.strip(), part2.strip()
    if part1 or part2:
        return False
    return True
