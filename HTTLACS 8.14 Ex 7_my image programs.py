import cImage as image
import math

# to use this program, your target image must be in the same folder as this .py file.
# to run a particular function, uncomment the function execution row
# the function will prompt for an image name: enter any image that you added to the same folder as this .py file

def removeRed():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            r = 0
            g = p[1]
            b = p[2]

            newPixel = image.Pixel(r,g,b)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# removeRed()

def negative():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            r = 255 - p[0] # using index[0] to access red intensity, instead of newred = 255 - p.getRed()
            g = 255 - p[1]
            b = 255 - p[2]

            newPixel = image.Pixel(r,g,b)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# negative()

def greyScale():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            avg_pixel = int((p[0] + p[1] + p[2]) / 3)

            newPixel = image.Pixel(avg_pixel, avg_pixel, avg_pixel)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# greyScale()

def black_and_white():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            avg_pixel = int((p[0] + p[1] + p[2]) / 3)

            if avg_pixel > 255 / 2:
                newPixel = image.Pixel(255, 255, 255)
            else:
                newPixel = image.Pixel(0,0,0)

            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# black_and_white()

def sepiaTone():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            newRed = int(p[0] * .393 + p[1] * .769 + p[2] * .189)
            newGreen = int(p[0] * .349 + p[1] * .686 + p[2] * .168)
            newBlue = int(p[0] * .272 + p[1] * .534 + p[2] * .131)

            newPixel = image.Pixel(newRed, newGreen, newBlue)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# sepiaTone()

def enlarge2():

    file = input("Enter the image name, including extension: ")
    img = image.Image(file)
    imgw = img.getWidth()
    imgh = img.getHeight()
    newimg = image.EmptyImage(imgw*2, imgh*2)

    for x in range(imgw):
        for y in range(imgh):

            pixel = img.getPixel(x,y)
            newimg.setPixel(2*x, 2*y, pixel)
            newimg.setPixel(2*x+1, 2*y, pixel)
            newimg.setPixel(2*x, 2*y+1, pixel)
            newimg.setPixel(2*x+1, 2*y+1, pixel)

    win = image.ImageWin(title=("{0}_enlarge2".format(file)), width=(imgw*2), height=(imgh*2))
    newimg.draw(win)
    win.exitonclick()

# enlarge2()

def smooth():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()-1):
        for y in range(img.getHeight()-1):

            p0 = img.getPixel(x,y)
            p1 = img.getPixel(x+1, y)
            newRed = int(((p0.getRed()) + (p1.getRed())) / 2)
            newGreen = int(((p0.getGreen()) + (p1.getGreen())) / 2)
            newBlue = int(((p0.getBlue()) + (p1.getBlue())) / 2)

            newPixel = image.Pixel(newRed, newGreen, newBlue)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# smooth()

def pixelMapper(rgbFunction):

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            originalpixel = img.getPixel(x,y)
            newpixel = rgbFunction(originalpixel)
            newimg.setPixel(x,y, newpixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

def graypixel(p):

    intensitysum = p[0] + p[1] + p[2]
    aveRGB = intensitysum // 3
    newPixel = image.Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel

# pixelMapper(graypixel)

def median(list):

    list.sort()
    mid = len(list) // 2
    return (list[mid] + list[~mid]) / 2

def noise_reduction(median):

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(1,img.getWidth()-1): # ignore the edge pixels for simplicity
        for y in range(1,img.getHeight()-1): # ignore the edge pixels for simplicity

            p0 = img.getPixel(x-1,y-1)
            p1 = img.getPixel(x-1,y)
            p2 = img.getPixel(x-1,y+1)
            p3 = img.getPixel(x,y-1)
            p4 = img.getPixel(x,y)
            p5 = img.getPixel(x,y+1)
            p6 = img.getPixel(x+1,y-1)
            p7 = img.getPixel(x+1,y)
            p8 = img.getPixel(x+1,y+1)

            r = int(median([p0[0],p1[0],p2[0],p3[0],p4[0],p5[0],p6[0],p7[0],p8[0]]))
            g = int(median([p0[1],p1[1],p2[1],p3[1],p4[1],p5[1],p6[1],p7[1],p8[1]]))
            b = int(median([p0[2],p1[2],p2[2],p3[2],p4[2],p5[2],p6[2],p7[2],p8[2]]))

            newPixel = image.Pixel(r,g,b)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# noise_reduction(median)

def nul_change_image():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            r = int(p[0])
            g = int(p[1])
            b = int(p[2])

            newPixel = image.Pixel(r,g,b)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# nul_change_image()

def sobel_edge():

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(1, img.getWidth()-1):  # ignore the edge pixels for simplicity (1 to width-1)
        for y in range(1, img.getHeight()-1): # ignore edge pixels for simplicity (1 to height-1)

            # x gradient kernel:
            #[-1][0][1]
            #[-2][0][2]
            #[-1][0][1]

            # y gradient kernel:
            #[-1][-2][-1]
            #[0][0][0]
            #[1][2][1]

            # initialise Gx to 0 and Gy to 0 for every pixel
            Gx = 0 # Gx is the horizontal derivative
            Gy = 0 # Gy is the vertical derivative

            # apply the x and y kernels simultaneously
            # accumulate pixel intensities into Gx and Gy for every kernel value

            # top left pixel
            p = img.getPixel(x-1, y-1)
            r,g,b = p[0],p[1],p[2]

            Gx += -(r+g+b)
            Gy += -(r+g+b)

            # middle left pixel
            p = img.getPixel(x-1, y)
            r,g,b = p[0],p[1],p[2]

            Gx += -2 * (r + g + b)

            # bottom left pixel
            p = img.getPixel(x-1, y+1)
            r,g,b = p[0],p[1],p[2]

            Gx += -(r + g + b)
            Gy += (r + g + b)

            # top middle pixel
            p = img.getPixel(x, y-1)
            r,g,b = p[0],p[1],p[2]

            Gy += -2 * (r + g + b)

            # bottom middle pixel
            p = img.getPixel(x, y+1)
            r,g,b = p[0],p[1],p[2]

            Gy += 2 * (r + g + b)

            # top right pixel
            p = img.getPixel(x+1, y-1)
            r,g,b = p[0],p[1],p[2]

            Gx += (r + g + b)
            Gy += -(r + g + b)

            # middle right pixel
            p = img.getPixel(x+1, y)
            r,g,b = p[0],p[1],p[2]

            Gx += 2 * (r + g + b)

            # middle bottom pixel
            p = img.getPixel(x+1, y+1)
            r,g,b = p[0],p[1],p[2]

            Gx += (r + g + b)
            Gy += (r + g + b)

            # We have the Gx and Gy values as two sides opposed by 90 degrees (like two sides of a right-angled triangle),
            # therefore we can use pythagoras' theorem to give us the gradient magnitude (length) as represented by the
            # hypotenuse.

            G = math.sqrt((Gx * Gx) + (Gy * Gy)) # this returns the un-normalised gradient

            # to normalise the gradient to a range suitable for displaying (max 255), we need to divide the gradient
            # by the maximum possible value, then multiply it by 255. The max possible value of G is based on the function
            # above, so we need to find the maximum possible values of Gx and Gy. Each pixel's intensity is at most 765,
            # which is 3 * 255 (highest value for each of r,g,b). Based on the kernels, the highest new pixel value is
            # 4 x 765 = 3060, therefore the highest G value = math.sqrt((3060 * 3060) + (3060 * 3060)) = 4327 (floor)

            G = G / 4327 * 255 # normalised

            G = int(G) # convert to int for pixel intensity compatibility

            # draw the length in the edge image
            newPixel = image.Pixel(G,G,G)
            newimg.setPixel(x, y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# sobel_edge()

# def change_column(col):

def green_line_along_column(column):

    img = image.Image(input("Enter image name, including file extension: "))
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            p = img.getPixel(x,y)
            r = p[0]
            if x == column:
                g = 255
            else:
                g = p[1]
            b = p[2]

            newPixel = image.Pixel(r,g,b)
            newimg.setPixel(x,y, newPixel)

    win = image.ImageWin()
    newimg.draw(win)
    win.exitonclick()

# green_line_along_column(10)
