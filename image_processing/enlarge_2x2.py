# Double the size of an image.

import image

myimg = image.Image("golden_gate.png")
win = image.ImageWin(2*myimg.getWidth(), 2*myimg.getHeight())
myimg.draw(win)
myimg.setDelay(1, 100)

def enlarge_2x2(img):
    imgScale = image.EmptyImage(2*img.getWidth(), 2*img.getHeight())
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            imgScale.setPixel(2*col, 2*row+1, p)
            imgScale.setPixel(2*col+1, 2*row+1, p)
            imgScale.setPixel(2*col, 2*row, p)
            imgScale.setPixel(2*col+1, 2*row, p)
    return imgScale

enlarge_2x2(myimg).draw(win)
win.exitonclick()