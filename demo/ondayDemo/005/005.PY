from PIL import Image
import os 

for jpgName in os.listdir("demo"):
	jpgFile = os.path.join("demo", jpgName);
	with Image.open(jpgFile) as im:
		w, h = im.size
		n = w/1366 if (w/1366) >= (h/640) else h/640
		im.thumbnail((w/n,h/n))
		im.save('out_'+jpgName.split('.')[0]+'.jpg', 'jpeg')