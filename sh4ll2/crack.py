import random

final_output = 4550.79980469

for i in range(1,100):
	print("Input: {}".format(i))

	adding_float = 3.56399989
	init_to_zero = 0.00000000
	final = 0

	after_adding_float = i + adding_float

	while init_to_zero < after_adding_float:
		final = after_adding_float + init_to_zero + final
    		init_to_zero = init_to_zero + 0.80000001
