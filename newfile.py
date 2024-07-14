
import random
maxi = int(input("Enter the max number of guessing: "))
ans = random.randint(1,maxi)
guesscount=0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except:
        print("Invalid guess try again")
        continue
    guesscount+=1
    if ans == guess:
        print("Yay correct, your guesses: "+str(guesscount))
        break
    elif ans < guess:
        print("smaller")
    else:
        print("bigger")
    guesscount+=1