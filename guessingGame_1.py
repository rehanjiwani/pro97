import random
num = random.randint(1,9)
print("NUMBER GUESSING GAME")

chances=0

while chances < 5:
    chances+=1
    guess = int(input("Enter your guess: "))

    if  (guess==num):
        print("Congradulations YOU WON!!")
    elif (guess>num):
        print("The number is too high, PLEASE TRY AGAIN!!")
    elif (guess<num):
        print("The number is too low, PLEASE TRY AGAIN!!")
    else:
        print("Please TRY AGAIN")