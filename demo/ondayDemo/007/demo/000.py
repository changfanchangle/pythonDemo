from PIL import Image,ImageDraw,ImageFont

im = Image.open('touxiang.png')
#绘制用对象
draw = ImageDraw.Draw(im)
myFont = ImageFont.truetype('arial.ttf',size=72)
draw.text((350,60),'4',font=myFont, fill='red')
im.save('touxiang_out.png')
