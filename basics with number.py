# You can use variables to store numeric values
pi = 1230
print(pi)

# since the input function returns a string, the variables it populates
# will hold string values
first_number = input('Enter first number here : ')
second_number = input('Enter second number here : ')

print(first_number + second_number)
# Here you will find the output as a string
# Because first_number and second_number are string variables the + operator  does concatenation only

# lets do conversion of these input strings to numbers or integer

first_num = input('Enter first number ')
second_num = input('Enter second number ')

# int() is used to convert the input String into integer value eg 1, 2, ,3, 1000
print(int(first_num) + int(second_num))

# float() converts a string to a decimal or float number e.g. 3.71937, 89.5, 1.0, 100.979
print(float(first_num) + float(second_num))

# converting the integer into String
print(str(first_num) + 'is the first number')

# converting the integer into String
print(str(first_num) + 'is the second number')


# let's perform some basic Mathematical funstions on them also

first = 6
second = 2

print('addition')
print(first + second)
print('subtraction')
print(first - second)
print('multiplication')
print(first * second)
print('division')
print(first / second)
print ('exponent')
print(first ** second)



