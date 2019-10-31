# Turn the image into neon blue.

import image

myimg = image.Image("golden_gate.png")
myimg.setDelay(1,500)   # setDelay(0) turns off animation
win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)

def neon(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            new_pixel = image.Pixel(0, p.getGreen(), 2*p.getBlue())
            img.setPixel(col,row,new_pixel)
    return img

neon(myimg).draw(win)