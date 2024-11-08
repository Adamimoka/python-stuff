from PIL import Image

image_path1 = "C:/Desktop/img1.png"
image_path2 = "C:/Desktop/img2.png"
image = Image.open(image_path1)
otherImage = Image.open(image_path2)

pixels = image.load()
otherPixels = otherImage.load()

width, height = image.size

myBool = False
for y in range(height):
    for x in range(width):
        if myBool:
            pixels[x, y] = otherPixels[x, y]
        myBool = not myBool
    myBool = not myBool

image.save("C:/Desktop/combined_image.png")