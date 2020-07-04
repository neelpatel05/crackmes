import sys
import random

choices = []
for i in range(65, 91):
	choices.append(chr(i))

for i in range(48, 58):
	choices.append(chr(i))

x=16
key = ""
while len(key) < 15:
        key += random.choice(choices)
	x+=1
print(key)

character_sum = 0
for k in key:
	character_sum += ord(k)
	character_sum = character_sum >> 1
	character_sum %= 3840
	character_sum += 10
print(character_sum)

final_letter = chr(character_sum)
if final_letter in choices:
	key+=final_letter
	print("key is {}".format(key))
