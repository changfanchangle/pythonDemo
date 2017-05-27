import urllib.request
import re

def get_htmlBody(url):
	html_content = urllib.request.urlopen(url).read()
	html_content = html_content.decode('GBK')
	r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
	result = r.findall(html_content)
	return result

if __name__ == '__main__':
	body = get_htmlBody('http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html')
	file_object = open("out.txt","w")
	for line in body:
		file_object.write(line + "\n")
	file_object.close()
