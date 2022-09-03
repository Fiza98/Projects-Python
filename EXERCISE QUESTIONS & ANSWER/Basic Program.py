#1. 
x=6
y=3
c=5
d=6
print(d%y*c>5 or c%y*d<7)

ans: FALSE

#2.
a = 10.6; b = 12.4; m = 15; n = 3
k= (m + n) * (m / b) + (a + b )-m % 4 * a / n
print(k)

ans: 34.174193548387095

#3.
# Python Program to find Area of a Trapezoid

b = float(input('Please Enter the First Base of a Trapezoid: '))
a = float(input('Please Enter the Second Base of a Trapezoid: '))
h = float(input('Please Enter the Height of a Trapezoid: '))

# calculate the area
Area = 0.5 * (a + b) * h

print(Area)

ans:
Please Enter the First Base of a Trapezoid:5
Please Enter the Second Base of a Trapezoid:5
Please Enter the Height of a Trapezoid:2
10.0

#4.
YARD1 = float(input("Please Enter the Height of yard:"))
YARD2 = float(input("Please Enter the Length of yard:"))
HOUSE1 = float(input("Please Enter the Height of house:"))
HOUSE2 = float(input("Please Enter the Length of house:"))
Area_yard = YARD1*YARD2
Area_House = HOUSE1*HOUSE2
REMAIN_AREA = Area_yard - Area_House
Rate = REMAIN_AREA * 2
print(Rate)

ans: 
Please Enter the Height of yard:15
Please Enter the Length of yard:30
Please Enter the Height of house:5
Please Enter the Length of house:10
800.0

#5.
basicsalary = float(input("Please Enter the basic salary: RM "))
houseallowance = 0.10 * basicsalary
generalallowance = 0.12 * basicsalary
grosssalary = basicsalary + houseallowance + generalallowance
EPF = grosssalary * 0.11
netsalary = grosssalary - EPF 
print(netsalary)

ans:
Please Enter the basic salary: RM 2500
2714.5

#6.
orange = raw_input("Enter number of oranges plucked : ")
owner = 0.40 * orange
Print'Total oranges for the owner is ' + Print(owner)
worker = orange / 4
Print 'Total oranges for each worker is' + worker
Balance = orange - owner - worker
Print 'Balance of oranges to make juice is' + Balance
