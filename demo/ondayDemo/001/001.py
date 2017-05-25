import random, string

randomKey = string.ascii_letters + "1234567890"
print(randomKey)

def makeGenerate(count, length):
	listRet = []
	for x in range(count):
		strRandom = ""
		for y in range(length):
			strRandom += random.choice(randomKey)
		listRet.append(strRandom)
		print(strRandom)
	return listRet

if __name__ == "__main__":
	makeGenerate(200, 20)
