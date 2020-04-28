branch = input("What province do you live in? ")

if branch in('cse IBM','CSE IOT'):
	block = 14
elif branch == 'CSE 2nd year':
	block = 1
else:
	block = " can be any block"
print(block)