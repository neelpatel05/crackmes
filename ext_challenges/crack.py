compared_string = [0x10, 0x14, 0x0a, 0x05, 0x0c, 0x17, 0x0a, 0x02, 0x06]

key = "badbeef12"
key = [ord(i) for i in key]

answer = [chr(i^j) for i,j in zip(compared_string,key)]
print(answer)
print("".join(answer))
