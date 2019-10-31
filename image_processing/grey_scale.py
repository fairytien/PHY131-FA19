# Create a grayscale version of a color image.

import image

myimg = image.Image("golden_gate.png")
myimg.setDelay(1,100)   # setDelay(1, 2000) will speed up a lot                      # img.setDelay(delay, number of pixels between delay)

win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)
    
def greyscale(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            gray_value = (p.getRed() + p.getGreen() + p.getBlue())/3
            newpixel = image.Pixel(gray_value, gray_value, gray_value)
            img.setPixel(col, row, newpixel)
    return img

greyscale(myimg).draw(win)