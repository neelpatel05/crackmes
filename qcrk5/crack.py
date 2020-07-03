def key(i):
	x = i + 101
	x<<8
	x = x - (i+101)
	x = x * 9474192
	return x

i = 0
while True:
	x = key(i)
	if x == 1266630048:
		print(i)
		break
	i=i+1
