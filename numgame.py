import random
import math
import sys

try:
    l, u = [int(l) for l in input("Enter your desired range : ").split()]
except:
    print("Please Enter initial and final guess")
    sys.exit()
d = (u - l)+1
points = 0
guess = ""
guess_limit = int(math.log2(d))
ch = guess_limit
guess_count = 0
r = str(random.randrange(l, u))
x = int(r)
array = set()
print('ans', r)
for i in range(1, 10):
    if (x % 2) == 0:
        m = "even"
    else:
        m = "odd"
        break
while guess != r and guess_count <= guess_limit:
    if guess != "hint":
        guess_count += 1
        print("You have", ch, "guesses.\n")
        ch -= 1
    else:
        print("The number is an", m, "number")
        points -= 20
    if guess_count != 1:
        points -= 10
        print("You have :", points, "points")
    guess = input("Enter your guess : ")
    array.add(guess)
    j = len(array)
    if j == guess_count:
        if guess > r:
            print("Try again, You guessed too high!")
        elif guess < r:
            print("Try again, You guessed too low!")
        else:
            print("Congratulations, You guessed correct!")
            points += 100
            print("You have", points, "points")
    else:
        print("You've guessed that already! Try again")
        guess_count -= 1
        ch += 1

if guess_count > guess_limit:
    print("The number is : %d" % x)
    print("Out of guesses")
