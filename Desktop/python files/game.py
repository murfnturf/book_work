import random

num = random.randint(1, 10) 
guess = None 

while guess != num: 
	guess = input("guess a number between 1 and 10: ")
	guess = int(guess)

	if guess == num:
		print("congratulations! You won!")
		break
	else:
		print("nope, sorry. Try again")