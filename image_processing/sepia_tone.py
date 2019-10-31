# Convert a photo into Sepia tone.

import image

myimg = image.Image("golden_gate.png")
myimg.setDelay(1,1000)   # setDelay(0) turns off animation
win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)

def sepia_tone(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()
            newr = r*0.393 + g*0.769 + b*0.189
            newg = r*0.349 + g*0.686 + b*0.168
            newb = r*0.272 + g*0.534 + b*0.131
            new_pixel = image.Pixel(newr, newg, newb)
            img.setPixel(col,row,new_pixel)
    return img

sepia_tone(myimg).draw(win)