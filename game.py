import random
import math

lower = int(input("Enter the lower bound "))
upper = int(input("Enter the upper bound "))
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("You've only", total_chances, "chances to guess the number")
count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("Enter the guess number "))

    if x == guess:
        print("congrats! you did it in", count, "try")
        flag = True
        break
    elif x > guess:
        print("Your guess number is too small")
    elif x < guess:
        print("Your guess number is too high")
if not flag:
    print("The number is ", x)
    print("Better luck next time!")

