# Rotate an image by 90 degrees in the clockwise direction.

import image

myimg = image.Image("https://upload.wikimedia.org/wikipedia/commons/1/1b/Greenwich_clock.jpg")
win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)
myimg.setDelay(1,1000)

def rotate_90_right(img):
    w = img.getWidth()
    h = img.getHeight()
    newimg = image.EmptyImage(h, w)
    for row in range(h):
        for col in range(w):
            newimg.setPixel(h-row-1, col, img.getPixel(col,row))
    return newimg

newwin = image.ImageWin(myimg.getHeight(), myimg.getWidth())
rotate_90_right(myimg).draw(newwin)