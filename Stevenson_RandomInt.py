import random
i = 0
while i < 5:
    generatedNumber = random.randint(1,10)
    print("Number " + str(i) + " is " + str(generatedNumber))
    i = i + 1
    if i  == 5:
        break