import random
print 'Guess the right number between 0 to 100 !'
n = random.randint(0,100)
g = int(raw_input('Please enter your 1. guess:'))
if g == n:
	print 'Congrats!'
# while g != n:

#	g = int(raw_input('Please enter your guess:'))
	if g < n:
		print 'Too low'
	elif g > n:
		print 'Too high'
