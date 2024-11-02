import random
name=input("What is your name? ")
print("Good Luck!",name)
words=['umbrella','rain','window','bucket','roses','Dhalia','chicken','love','marriage','relation','ring','ornaments']
word=random.choice(words)
print("Guess the word")
guesses=""
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed+=1
    if failed==0:
        print(" You win")
        print("The word is ",word)
        break
    print()
    guess=input("Guess a character")
    guesses+=guess
    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")

