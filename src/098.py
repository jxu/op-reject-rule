# Showing off python's string abilities
# Also over-complicating things because why not
from itertools import permutations

with open("p098_words.txt") as f:
    text = f.readline()

words = [word[1:-1] for word in text.split(',')]
word_letters = dict()
word_pairs = []
for word in words:
    sorted_word = tuple(sorted(word))
    if sorted_word in word_letters:
        word_pairs.append((word_letters[sorted_word], word))
    else:
        word_letters[sorted_word] = word


print(word_pairs)

squares = set(i**2 for i in range(10**5))
max_square = 0

for word1, word2 in word_pairs:
    if len(word1) < 4: continue

    unique_letters = tuple(set(word1))
    for num_assign in permutations(range(10), len(unique_letters)):
        # Probably horribly inefficient but inputs are small enough
        num_letters = dict()
        for i in range(len(num_assign)):
            num_letters[unique_letters[i]] = num_assign[i]

        if num_letters[word1[0]] == 0: continue
        if num_letters[word2[0]] == 0: continue

        n1 = 0
        for l in word1:
            n1 = 10*n1 + num_letters[l]

        if n1 in squares:
            n2 = 0
            for l in word2:
                n2 = 10*n2 + num_letters[l]

            if n2 in squares:
                print(word1, word2, n1, n2)
                max_square = max(max_square, n1, n2)

print(max_square)
