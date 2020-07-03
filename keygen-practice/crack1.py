import sys

input_string = sys.argv[1]

x = 0
y = 0
while True:
	if len(input_string) <= y:
		break;
	c = y + ord(input_string[y])
	x = x + c*len(input_string)*len(input_string)
	y = y + 1

print(x)
print("required: {}".format(52650-x))
