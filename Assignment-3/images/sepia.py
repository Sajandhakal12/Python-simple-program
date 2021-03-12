
# converts image into greyscale 
def greyscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b)=image.getPixel(x,y)
            r=int(r * 0.299)
            g=int(g * 0.587)
            b=int(b * 0.114)
            lum= r+g+b
            # alternatively we can also do
            #     average=(r+g+b)//3
            #     image.setPixel(x,y,(average,average,average))
            image.setPixel(x,y,(lum,lum,lum))

# converts image into sepia 
def sepia(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()): 
            (r,g,b)=image.getPixel(x,y)
            if(r<63):
                r=int(r*1.1)
                b=int(b*0.9)
            elif(r<192):
                r=int(r*1.15)
                b=int(b*0.85)
            else:
                r=min(int(r*1.08),255)
                b=int(b*0.93)
            image.setPixel(x,y,(r,g,b))


from images import Image

def main(filename):
    image =  Image(filename)
    print('Close the image window to continue. ')
    image.draw()
    greyscale(image)
    print('Close the image window to continue. ')
    image.draw()
    sepia(image)
    print('Close the image window to quit. ')
    image.draw()


main('Assignment-3/images/smokey.gif')