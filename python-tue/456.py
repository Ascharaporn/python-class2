import random
HEADS = 1
TAILS = 2
tosses = 10

def tosses_coin():
    for toss in range(tosses):
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")
tosses_coin()