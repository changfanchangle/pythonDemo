#coding:utf8
import sys,os,re

def cal(path):
	listFile = (item for item in os.listdir(path) if item.endswith(".py"))
	ret = [0,0,0]
	for item in listFile:
		resoure = calfile(path,item)
		for i in (0,1,2):
			ret[i] += resoure[i]
	return tuple(ret)

def calfile(path,filename):
	totLine = 0
	blankLine = 0
	commentLine = 0

	fileObj = open(os.path.join(path, filename), "r", encoding="utf8")
	listLine = fileObj.readlines()
	totLine = len(listLine)
	for line in listLine:
		pattern = re.compile(r'(\s*)#')
		pattern1 = re.compile(r'(\s*)$')
		if pattern.match(line):
			commentLine += 1
		if pattern1.match(line):
			blankLine += 1
		fileObj.close()
		return totLine,blankLine,commentLine

if __name__ == "__main__":
	data = cal("demo")
	dic = dict(zip(['total line','blank line','comment line'],list(data)))
	print(dic)