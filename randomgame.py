import sys
from random import randint

# Generate a number between value input and value input
first_number = int(sys.argv[1]) # need int because sys.argv is a string
last_number = int(sys.argv[2])
answer = randint(first_number,last_number)

# Input from user
# guess = input('guess a number between 1 and 10:   ') can not put here because it gonna cause infinite loop if you input wrong

# Check that input is a number between value input and value input
while True:
	try:
		print(f'hint : answer = {answer}')
		guess = int(input(f'guess a number between {first_number} and {last_number}:   '  )) # Make the user enter integer numbers
		if first_number < guess < last_number : # if 0 < int(guess) < 11:
			if guess == answer :
				print('all good, you are a genius')
				break
		else:
			print(f'yo, please make it right, the number BETWEEN {first_number} AND {last_number}. ')
	except ValueError:
		print('please enter a number')
		continue