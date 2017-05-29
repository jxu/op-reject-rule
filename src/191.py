# BIG MONEY BIG PRIZES

memo = dict()

def prizes(day, lates, last_absent, s):
    if lates < 0 or day < 0: return 0
    if day == 0:
        print(s)
        return 1

    strings =  prizes(day-1, lates, False, 'O'+s)
    strings += prizes(day-1, lates-1, False, 'L'+s)
    if not last_absent:
        strings += prizes(day-1, lates, True, 'A'+s)
        strings += prizes(day-2, lates, True, 'AA'+s)

    return strings


print(prizes(4, 1, False, ''))

