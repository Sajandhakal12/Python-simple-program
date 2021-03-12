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


'''
created a menu to choose what type of image you want to convert
'''
MENU = """1 invert color image
2 invert black in white image
3 invert grayscale image
"""

print(MENU)
type_image=input('Choose an option!')

if type_image=='1':
    # color gif
    main('smokey.gif')
elif type_image=='2':
    # black in white gif
    main('smokey-black.gif')
elif type_image=='3':
    # grey gif
    main('smokey-grey.gif')
else:
    print('Invalid input')