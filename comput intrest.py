# Code starts here

# store variable names
P = 1000
r = 10
n = 2

# compound interest formula
A = P * ((1 + r/100) ** n)
A = round(A,2)
# display compound interest
print(A)

# display interest
interest = A - P 
interest = round(interest,2)
print(interest)

# Code ends here