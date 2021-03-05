'''

'''
octal_number = 0
decimal_output = 0
is_octal=1  #works as a flag to detemine if input is valid octal number

#checking if input is valid if not runs in a loop until valid octal is given
while True:
    if is_octal==0:
        break
    octal_number=input('Enter an octal number')
    characters=str(octal_number)
    is_octal=0
    for character in characters:
        if int(character)>7:
            is_octal=is_octal+1
            break
       
    
#find out the length of the octal number
length = len(str(octal_number))

#conversion
for x in octal_number:
    length = length-1                        
    decimal_output += pow(8,length) * int(x)
    
print('The conversion of',octal_number,' is ',decimal_output)