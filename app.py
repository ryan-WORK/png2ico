from PIL import Image
filename = r'c4is.png'
img = Image.open(filename)
img.save('c4is.ico')
