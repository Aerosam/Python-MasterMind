import random
import collections

length = 4
guesses = 13
colors = ["r", "g", "b", "y", "c", "m"]

while 1:
    pattern = [random.choice(colors) for _ in range(length)]
    y = []
    check = list(set(pattern))
    for x in check:
        y.append(pattern.count(x))
    if y[0] > 2 or y[1] > 2:
        continue
    else:
        print(pattern)
        break


counted = collections.Counter(pattern)
print("Please, enter your color code.\nYou can use (r)ed, (g)reen, (b)lue, (y)ellow, (c)yan and (m)agenta.")


def running():
    while 1:
        guess = input("MasterMind: ")
        if len(guess) != 4:
            print("Error! Enter Only 4 characters!")
            continue
        else:
            break

    guess_count = collections.Counter(guess)
    for a in guess:
        if a not in colors:
            print("Error! Only letters (r)ed, (g)reen, (b)lue, (y)ellow, (c)yan and (m)agenta allowed.")
            break

    partial_match = sum(min(counted[k], guess_count[k]) for k in counted)
    exact_match = sum(a == b for a, b in zip(pattern, guess))
    partial_match -= exact_match
    print('b : {}. w : {}.'.format(exact_match, partial_match))
    return exact_match != length


for attempt in range(guesses):
    if not running():
        print('you win!')
        break
    else:
        print('Guesses remaining: ', guesses - 1 - attempt)
else:
    print('Game over. The code was {}.'.format(''.join(pattern)))
