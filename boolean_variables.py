# I check to see if the requirements for honour roll are met
cgpa = float(input('What was your cureent grade (cgpa) '))
lowest_grade = float(input('What was your lowest grade '))

# Boolean variables allow you to remember a True/False value
if cgpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

# Somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
	print('You made it')
