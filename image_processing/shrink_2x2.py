# Half-size an image.

import image

myimg = image.Image("http://reputablejournal.com/images/ComputerHistory/TeleType.png")
win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)
myimg.setDelay(1,100)

def shrink_2x2(img):
    w = img.getWidth() // 2
    h = img.getHeight() // 2
    newimg = image.EmptyImage(w, h)
    for row in range(h):
        for col in range(w):
            p1 = img.getPixel(col*2, row*2)
            p2 = img.getPixel(col*2, row*2 + 1)
            p3 = img.getPixel(col*2 + 1, row*2)
            p4 = img.getPixel(col*2 + 1, row*2 + 1)
            plist = []

            for i in range(3):
                plist.append((p1[i] + p2[i] + p3[i] + p4[i])//4)

            newp = image.Pixel(plist[0], plist[1], plist[2])
            newimg.setPixel(col, row, newp)
    return newimg

newwin = image.ImageWin(myimg.getWidth() // 2, myimg.getHeight() // 2)
shrink_2x2(myimg).draw(win)