# simple simulation
# shortcut: don't bother taking chest and chance cards in order

from enum import Enum
from random import randint, sample

BOARD = ("GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
      "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
      "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
      "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2")

TURNS = 1000000
counter = [0] * len(BOARD)

pos = 0
doubles = 0

for turn in range(TURNS):
    # roll dice
    d1 = randint(1, 4)
    d2 = randint(1, 4)
    d = d1 + d2

    if d1 == d2:
        doubles += 1
    else:
        doubles = 0

    print(f"dice {d1}+{d2}={d} doubles:{doubles}")


    if doubles == 3:
        print("3 doubles! go to jail!")
        doubles = 0
        pos = BOARD.index("JAIL")

    else:
        # make move
        pos = (pos + d) % len(BOARD)

    # G2J square
    if pos == BOARD.index("G2J"):
        pos = BOARD.index("JAIL")



    # chance card
    if BOARD[pos].startswith("CH"):
        card = randint(0, 15)
        print("chance", card)
        if card == 0:
            pos = BOARD.index("GO")
        elif card == 1:
            pos = BOARD.index("JAIL")
        elif card == 2:
            pos = BOARD.index("C1")
        elif card == 3:
            pos = BOARD.index("E3")
        elif card == 4:
            pos = BOARD.index("H2")
        elif card == 5:
            pos = BOARD.index("R1")
        elif card in (6, 7):
            while not BOARD[pos].startswith("R"):
                pos = (pos + 1) % len(BOARD)
        elif card == 8:
            while not BOARD[pos].startswith("U"):
                pos = (pos + 1) % len(BOARD)
        elif card == 9:
            pos = (pos - 3) % len(BOARD)


    # handle community chest card after chance
    if BOARD[pos].startswith("CC"):
        card = randint(0, 15)
        print("chest", card)
        if card == 0:
            pos = BOARD.index("GO")
        elif card == 1:
            pos = BOARD.index("JAIL")


    # record position after roll
    print("position", pos, BOARD[pos])
    counter[pos] += 1

print("counter", counter)

most_visited = sorted(range(len(BOARD)),
                      key=lambda i:counter[i],
                      reverse=True)

for i in range(3):
    sq = most_visited[i]
    print(BOARD[sq], counter[sq])

for i in range(3):
    print(str(most_visited[i]).zfill(2), end='')

