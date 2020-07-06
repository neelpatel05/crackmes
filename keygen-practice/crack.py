final = 52650
divisible = []

for i in range(65, 90):
	if final % i == 0:
		divisible.append(i)

quotient = []
for i in divisible:
	x = final / i
	quotient.append(x)

print(quotient)
for i,j in zip(divisible, quotient):
	print(chr(i)*j)

