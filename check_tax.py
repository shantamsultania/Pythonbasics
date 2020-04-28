# Calculate the tax

price = input('how much did you pay? ')

# Convert the string to a number
price = float(price)

if price >= 100.00:
	tax = 70/100
	print('Tax rate is: ' + str(tax))
else:
	# Anything else we do not charge any tax for now
	tax = 0
	print('Tax rate is: ' + str(tax))
