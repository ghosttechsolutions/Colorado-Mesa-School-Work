import random
class Coin:
    sideup = 'Heads'
    heads = 0
    tails = 0
    def FlipCoin(obj):
        i = 1
        while i != 51:
            list = [0,1]
            flipcoin = random.choice(list)
            if flipcoin == 0:
                side = "Heads"
                obj.heads += 1
            else:
                side = "Tails"
                obj.tails +=1
            i += 1
            if i == 50:
                obj.heads /= 50
                obj.tails /= 50
                obj.heads *= 100
                obj.tails *= 100
                print("Heads: " + str(obj.heads) + "% Tails: " + str(obj.tails) + "%")

Coin.FlipCoin = classmethod(Coin.FlipCoin)
Coin.FlipCoin()