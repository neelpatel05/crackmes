import random
import string

def randomString(stringLength=4):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def differentString(str):
	string1 = ""
	letters = string.ascii_lowercase
	for i in range(len(str)):
		while True:
			letter = random.choice(letters)
			if letter not in str:
				break;
		string1 += letter
	return string1

for i in range(8,19,2):
	half = i//2
	x = randomString(half)
	twin1_second_half = randomString(half)
	twin1 = x + twin1_second_half
	twin2 = x + differentString(twin1_second_half)
	print("Twin 1 (Arg 1): {}".format(twin1))
	print("Twin 2 (Arg 2): {}".format(twin2))
