encrypted = "arln_pra_dfgafcchsrb_l{ieeye_ea}"
print(encrypted)

string1 = []
string2 = []
string3 = []

string1 = encrypted[0:11]

string2 = encrypted[11:22]

string3 = encrypted[22:32]

print(string1[-1],string2[-1])
mainstring = []
for i,j,k in zip(string1, string2, string3):
	mainstring.append(j)
	mainstring.append(k)
	mainstring.append(i)

print("".join(mainstring))
