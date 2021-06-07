#Generate ramdom integers (1~100)
#Let user to guess the number
#If right, print "Good Job"
#If wrong, tell them it is bigger or smaller than anwser.

import random

r = random.randint(1, 10)
print(r)
count = 0

while True:
	num = input('Please enter your anwser: ')
	num = int(num)
	count = count + 1
	print('This is ', count, 'times.')	
	if num == r:
		print('Good Job')
		break
	elif num > r:
		#print(r)
		print('It is too big!! Try again')
	elif num < r:
		#print(r)
		print('It is too small!! Try again')

