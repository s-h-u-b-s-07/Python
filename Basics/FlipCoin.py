import random

def flipCoin():
    
    coin = [0,1]
    if random.choice(coin) == 0:
        print("Heads")
    else:
        print("Tails")

flipCoin()