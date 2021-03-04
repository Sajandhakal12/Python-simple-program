```

```
decimal_number = int(input("Enter a decimal number :"))
decimal_input=decimal_number

octal_output = 0
i = 1
while (decimal_number != 0):
    octal_output = octal_output + (decimal_number % 8) * i
    decimal_number = int(decimal_number / 8)
    i = i * 10

print("The octal number of ",decimal_input ," is",octal_output)