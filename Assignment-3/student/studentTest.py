from student import Student
s = Student("Maria", 5)

print("the current name is: ",s.getName())
new_name=input('Enter a new name: ')

s.setName(new_name)
print("New name",s.getName())


