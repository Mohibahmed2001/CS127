from PIL import Image
x = int(input('Size'))
i = 0
while i < x:
    if (i%2)==0:
        img = Image.new("RGB",(i,x), "blue")
    else:
        img = Image.new("RGB",(i,x), "green")

img.show()
