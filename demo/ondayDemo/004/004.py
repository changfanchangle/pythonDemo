import re
inFile = open("demo.txt","r", encoding='UTF-8')
outFile = open("outFile.txt","w")
#利用正则，匹配单词
str = inFile.read()
replx = re.compile("\b?([a-zA-z0-9]+)\b?")
words = replx.findall(str)
#统计
word_dict = {}
for word in words:
	if(word in word_dict):
		word_dict[word] += 1
	else:
		word_dict[word] = 1

for (word,number) in word_dict.items():
	outFile.write(word+":%d\n"%number)



