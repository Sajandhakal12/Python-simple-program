# inverting a image
def invertImage(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b)=image.getPixel(x,y)
            image.setPixel(x,y,(255-r,255-g,255-b)) # substraction eact r,g,b value with 255


from images import Image
def main(filename):
    image =  Image(filename)
    print('Close the image window to continue. ')
    image.draw()
    invertImage(image)
    print('Close the image window to quit. ')
    image.draw()


main('Assignment-3/images/smokey.gif')