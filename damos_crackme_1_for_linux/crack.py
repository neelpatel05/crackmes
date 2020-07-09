import string
import random

letters = string.ascii_uppercase

def first_condition():
	_0 = random.choice(letters)
	for i in range(0,255):
		if ord(_0) == i-3:
			_9 = chr(i)
			break
	return _0,_9

def second_condition():
	_1 = random.choice(letters)
	for i in range(0, 255):
		if ord(_1) == i + 0xe:
			_8 = chr(i)
			break

	return _1,_8

def third_condition():
	_2 = random.choice(letters)
	for i in range(0, 255):
		if ord(_2) == i - 0x14:
			_7 = chr(i)
			break
	return _2,_7

def fourth_condition():
	_3 = random.choice(letters)
	for i in range(0, 255):
		if ord(_3) == i + 6:
			_6 = chr(i)
			break
	return _3,_6

def fifth_condition(_0):
	_4 = random.randint(0, 255)
	_5 = 2*ord(_0) - _4

	_4 = chr(_4)
	_5 = chr(_5)

	return _4,_5

def find_key():
	while True:
		try:
			a = first_condition()
			b = second_condition()
			c = third_condition()
			d = fourth_condition()
			e = fifth_condition(a[0])

			str = a[0] + b[0] + c[0] + d[0] + e[0] +e[1] + d[1] + c[1] + b[1] + a[1]
			flag = 0
			for i in str:
				if i not in letters:
					flag = 1
			if flag == 0:
				print(str)
				break
		except:
			pass

if __name__ == "__main__":
	print("Use any one of the following keys: ")
	for i in range(0,10):
		find_key()

