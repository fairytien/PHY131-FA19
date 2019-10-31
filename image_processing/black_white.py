# Turn a color image into a black and white one by setting a threshold value for its gray_value.

import image

myimg = image.Image("golden_gate.png")
myimg.setDelay(1, 200)   # setDelay(0) turns off animation

win = image.ImageWin(myimg.getWidth(), myimg.getHeight())
myimg.draw(win)

def black_white(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            gray_value = (p.getRed() + p.getBlue() + p.getGreen())/3
            if gray_value >= 255/2:
                new_pixel = image.Pixel(0,0,0)
                img.setPixel(col, row, new_pixel)
            else:
                new_pixel = image.Pixel(255,255,255)
                img.setPixel(col, row, new_pixel)
    return img

black_white(myimg).draw(win)