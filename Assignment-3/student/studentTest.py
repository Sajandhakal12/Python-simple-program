from student import Student

# initialization of value
s = Student("Maria", 5)

print("the current name is: ",s.getName())

new_name=input('Enter a new name: ')

# changed name through mutation 
s.setName(new_name)
print("New name",s.getName())


