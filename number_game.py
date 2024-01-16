import math
import random

def num_guess_function (lower,upper,diff):
    res = round(math.log(upper - lower + 1, diff))
    return res 

lower_range = int(input("give the lower bound of the range: "))
upper_range = int(input("give the upper bound of the range: "))

x = random.randint(lower_range, upper_range)

cond = False
while cond == False :
    diff = int(input("select difficulty between 1 and 3 where 1 is easiest: "))
    cond = diff in [1,2,3]

max_guess_num = num_guess_function(lower_range,upper_range,diff)
print("\n\tYou've only ",max_guess_num," chances to guess the integer!\n")

count = 0
 
while count < max_guess_num:
    count += 1
    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
        
if count >= max_guess_num:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")