string = "/root/crackmes/save-scooby"
crack_string = []

for i in string:
	if i == "/":
		crack_string.append("$")
	elif i == "-":
		crack_string.append("-")
	else:
		x = ord(i) - 30
		crack_string.append(chr(x))

print(crack_string)
print("".join(crack_string))
