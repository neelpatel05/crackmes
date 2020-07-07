username = raw_input("Enter the username lowercase between 3 to 9: ")
key = []
K = len(username)
for ch in username:
	encch = (ord(ch)-97+K) < 25 and chr(((ord(ch)-97+K)%26)+97) or chr(((ord(ch)-97+K-26)%26)+97)
	key.append(encch)

print("The Key is: {}".format("".join(key)))
