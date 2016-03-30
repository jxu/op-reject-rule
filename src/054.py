# Finally got around to doing this one
# Exercise in python idioms

value_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def eval_hand(hand):
    # Return ranking: high card = 0, ... royal flush = 9
    # Also return high card(s) of rank

    values = sorted([c[0] for c in hand])
    suits = [c[1] for c in hand]
    straight = (values == range(min(values), max(values)+1))
    flush = all(s == suits[0] for s in suits)

    if straight and flush:
        if values[0] == 10:
            return (9, None)
        else: return (8, max(values))

    pairs = []
    pair_present = False
    three_of_a_kind = False
    three_value = None
    for v in set(values):
        if values.count(v) == 4:
            return (7, v)
        if values.count(v) == 3:
            three_of_a_kind = True
            three_value = v
        if values.count(v) == 2:
            pair_present = True
            pairs.append(v)

    if three_of_a_kind and pair_present: return (6, (three_value, pairs[0]))
    if flush: return (5, None)
    if straight: return (4, max(values))
    if three_of_a_kind: return (3, three_value)
    if len(pairs) == 2: return (2, pairs)
    if len(pairs) == 1: return (1, pairs[0])
    return (0, max(values))

def tiebreaker(hand1, hand2):
    pass


player1_wins = 0
with open("p054_poker.txt") as f:
    for line in f:
        s = line.split(' ')
        line_pairs = []
        for card in s:
            try:
                value = int(card[0])
            except:
                value = value_dict[card[0]]

            line_pairs.append((value, card[1]))

        hand1 = line_pairs[:5]
        hand2 = line_pairs[5:]
        hand1_rank, hand1_info = eval_hand(hand1)
        hand2_rank, hand2_info = eval_hand(hand2)

        print(hand1, hand2)
        if hand1_rank > hand2_rank: player1_wins += 1
        elif tiebreaker(hand1, hand2): player1_wins += 1

print(player1_wins)

#print(eval_hand([(10,'H'), (10,'H'), (2,'D'), (13,'H'), (14,'H')]))