#Basic Programming Python

x=10
print(x)
ans:10

x=45.678
x="saya ada buku"
x=19j
print(x)
ans:
19j

type(x)
ans: 
complex

x=100
type(x)
ans:
int

x="saya ada buku"
type(x)
ans:
str

x=y=z=15
print(x,y,z)
ans:
15 15 15

w="saya"
x=y=z=50
print(w,x+y+z)
ans:
saya 150

r =  "hantu"
print(w+r)
ans:
sayahantu

x = 5
print(x)
ans:
5

type(x)
ans:
int

x = float(5) #typecasting
print(x)
ans:
5.0

type(x)
ans:
float

a,b,c = 10,20,30
print(a,b,c)
ans:
10 20 30

#arithmetic expression
2*3
ans:
6

2/3
ans:
0.6666666666666

2 // 3
ans:
0

1234 // 10
ans:
123

1234 % 10
ans:
4

2 ** 3
ans:
8

3 > 4
ans:
False

3 < 4
ans:
True

#formatting

a = "saya"  #string data type
b = 25  #integer data type
c = 56.85 #float data type

print(a,b,c)

ans:
saya 25 56.85

print("%s umur %d dan berat adalah %6.2fkg" %(a,b,c))
ans:
saya umur 25 dan berat adalah 56.85kg

#input 2 integer numbers, sum the numbers, display the sum

n1 = input("Enter a number:")
n2 = input("ENter a number:")

s = int(n1) + int(n2)

print(s)

ans:
Enter a number:34
Enter a number: 56
90

#atau

n1 = int(input("Enter a number:"))
n2 = int(input("ENter a number:"))

s = n1 + n2

print(s)

ans:
Enter a number:34
Enter a number: 56
90


#EXAMPLE DICT

w = {'Tim':18,'Chuck':12,'TIffany':15,'Sam':25}
male = {'Tim':18, 'Chuck':12, 'Sam':25}

for i in w.keys():
	print(i,(w[i])
output:
Tim 18
Chuck 12
Tiffany 15
Sam 25

print(w.items())
dict_items([('Tim', 18),('Chuck', 12),('Tiffany', 15),('Sam', 25)])

list(w.keys())
output:
['Tim', 'Chuck', 'Tiffany', 'Sam']

w.keys()
dict_keys(['Tim', 'Chuck', 'Tiffany', 'Sam'])

w.items()
dict_items([('Tim', 18),('Chuck', 12),('Tiffany', 15),('Sam', 25)])

#EXAMPLE FUNCTION
        
#function - user-defined function
#write a function that receives 2 numbers and returns the sum of the sumbers

def myfunc1(n1,n2):
	z = n1 + n2
	return z

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(myfunc1(a,b))

output:
Enter first number: 45
Enter second number: 60
105

#write a python function that receives a string
#count how many 'a' in a string
#display the count

def myfunc2(s):
	count_a = s.count('a')
	print(count_a)

sentence = input("Enter your sentence: ")
myfunc(sentence)

output:
Enter your sentence: saya ada buku
4

#count how many 'a' in a sentence entered by user
#loop until user do not want to enter anymore

ans = 'yes'
while (ans == 'yes'):
	sentence = input("ENter your sentence: ")
	myfunc2(sentence)

	ans = input("Do you want to continue yes/no?")

print("end of program")
output:
Enter your sentence: saya ada buku
4
Do you want to continue yes/no?yes
Enter your sentence: do you want to sleep
1
Do you want to continue yes?no?yes
Enter your sentence: book is boring
0
Do you want to continue yes/no?no
end of program

#function tat receives a number, returns square, cube, division
def myfunc3(n):
	return n*n, n*n*n, n/10

z = int(input("enter a number: "))
print(myfunc3(z))

output:
enter a number:10
(100, 1000, 1.0)
        
#EXAMPLE OF LIST
        
x = [90,8,4,7,15,45,60,25,2,5,10]

x[4]
ans:15

x[-4]
ans:25

x[2:5]
ans:[4,7,15]

x[-4:-1]
ans:[25,2,5]

x[1:9:2] #rejump 2
ans:[8,7,45,25]

x=[1:10:3]
ans:[8,15,25]

#EXAMPLE TUPLE DICT
        
TP = 8,'abc',250,3.142	#packing - tp
print(tp)

output:
(8, 'abc', 250, 3.142)

person = 'abu','M',25,500	#packing to person
print(person)

output:
('abu', 'M', 25, 500)

name,gender,age,salary = person 	#unpack tuple person into specific variable

print(name)
print(gender)
print(age)
print(salary)

output:
abu
M
25
500

print(person)
('abu', 'M', 25, 500)

#dict contains key and values - key single element and immutable, values - list elements
a = {age:25,gender:'F',name:'sara'}

print(a)
{25: 25, 'M': 'F', 'abu': 'sara'}

b = {subject:'dsc551',credhr:3,faculty:'CS'}
 
#EXAMPLE REPETITION
        
#range() - generate a sequence of number
#range(n) - generate a sequence of number from 0 to n-1
#range(a,b) - generate a sequence of number from a to b-1
#range(a,b,c) - generate a sequence of a number from a to b-1, step c

a=range(4)
print(a)
ans: range(0, 4)

#for loop - for variablename in sequence:

for i in range(4):
	print(i)

ans: it will generate no from 0 to 4-1.
0
1
2
3

for i in range(2,6):
	print(i)

ans: it will generate no from 2 to 6-1.
2
3
4
5

for i in range(4,10,2):
	print(i)
ans:start 4, addition of 2, should be stop at 9.
4
6
8

#print the odd numbers within th e1st 100 numbers

for i in range(100):
	if(i % 2 != 0):
		print(i)

ans:
1
3
...
99

#nested looping
for i in range(4):
	for j in range(3):
		print(i, j)

ans:
0 0
0 1
0 2
1 0
1 1
1 2
...
3 2

# to find the number that is divisible by 5
for i in range(10,30):
	if(i % 5 == 0):
		print(i)

ans:
10
15
20
25

# break - exit the loop without completing the loop
for i in range(10)
	if (i % 5 ==0):
		break
	print(i)

print("This is outside the loop")

ans:
1
2
3
4
This is outside the loop

# continue - skip if meets certain condition, and continue the loop
for i in range(10)
	if (i % 5 ==0):
		continue
	print(i)

print("This is outside the loop")

ans:
1
2
3
4
6
7
8
9
This is outside the loop

for i in "snakes":
	print(i)

ans:
s
n
a
k
e
s

for i in [2,4,6,'a','z','d']
	print(i)

ans:
2
4
6
a
z
d

#find a factorial of a number 4! = 4x3x2x1 = 24
n = int(input("enter a number"))
fac=1
for i in range(1,n+1):
	fac = fac *1

print(fac)

ans:
enter a number:

#while loop
i = 0 #initialize your loop variable
while(i<5): #condition to check whether to exit or continue loop
	print(i)
	i = i + 1 #update loop variable

ans:
0
1
2
3
4


#EXAMPLE SELECTION
        
8 > 4
ans:
True

4+8==10
ans:
False

4>6 and 7==7
ans:
False

4>6 or 7 == 7
True

age = int(input("Enter your age: "))

#check whether you have entered age within 12 - 18

12<= age <= 18
ans:
Enter your age: 15

True

#membership operators  is - is not - in - not in
x = 'abc'
y = 'a'
y in x
ans:
True

y not in x
ans:
False

a=2
b=2
c=2

b is a 
ans:
True

c is not a
ans:
True

#input the age, display whether child<12, youth< 17, adult < 30, other old 

age = int(input("ENter your age: "))

if (0 < age <=12):
	print("You are still a child")
elif(age<=17):
	print("You are still in your youth")
elif (age <= 30):
	print("You are an adult now")
else:
print("You are old already")

#restart the kernel
ans:
Enter your age: 10
You are still a child

#EXAMPLE STRING RECORDING
x = "saya ada buku"

#slicing
x[3:]

ans:
'a ada buku'

x[3:6]
ans: 
'a a'

x[0] = 'b'
-------
type error

#replace() - to replace a character/word in string
x.replace('s','b')
ans:
'baya ada buku'

xreplace('a','z')
ans: 'szyz zdz buku'

print(x)
ans:
saya ada buku

x = x.replace('a','z')
print(x)
ans:
szyz zdz buku

#reversed() - returns the reversed object of the stirng
x.reversed()
----
attributeError


reversed(x)
ans:
<reversed at 0x1ca0d0947c8>

list(reversed(x))
ans:
['u','k','u','b',' ','z','d','z',' ','z','y','z','s']

"".join(reversed(x))
ans:
'ukub zsz zyzs'

"bantal".join("katil")
ans:
' bantalkbantalabantaltbantalibantall '

"bantal".join(reversed(x))
ans:
' ubantalkbantalubantalbbantal bantalxbantaldbantlzbantal bantalzbantalybantalzbantals'

"bantal".join('@')
ans:
'@'

"bantal".join("@")
ans:
'@'

"".join("a")
ans:
'a'


#ADVANCED FUNCTION
        
KEYWORD ARGUEMENT

#the value is passed according to its variable and matched with function definition variables, irregardles of the order,
#since the caller specify the variable names

def p_hello(fname = "", lname=""):
    print("Hello %s %s" %(fname,lname))
    
p_hello(lname = "Arun", fname = "Jay")

out:-
Hello Jay Arun

#we can omit the variable names in the function call, however, the order/sequence is important
def p_hello(fname = "", lname=""):
    print("Hello %s %s" %(fname,lname))
    
p_hello("Arun", "Jay")

out:-
Hello Arun Jay

PASSING TUPLE AS ARGUEMENTS

def s(*alist):
    result = 0
    for i in alist:
        result+=i
    return result
    
print(s(3,4,5,6,8,10))

out:-
36

PASSING DICTIONARIES AS ARGUEMENTS

def p_dict(**adict):
    for i in adict.keys():
        print(i, " is ",adict[i])
        
user_info = {"name":"David","uid":593,"access": "Guest"}
p_dict(**user_info)

out:-
name  is  David
access  is  Guest
uid  is  593

LAMBDA FUNCTION

def f(a,b):
    return a*b
    
print(f(4,10))

out:-
40

x = lambda a,b : a*b
print(x(4,10))


out:-
40

def myfunc(n):
    return lambda a: a*n
    
x = myfunc(2)
print(x(11))

out:-
22

y = lambda a,b: a if a>b else b

print(y(10,60))

out:-
60

MAP FUNCTIONS

def f1(a):
    return len(a)
    
x = map(f1,('apple','abc','oranges','pillowcase'))
print(list(x))

out:-
[5, 3, 7, 10]


def f2(a,b):
    return a+b
    
x = map(f2,(1,2,3),(10,20,30))
print(list(x))

out:-
[11, 22, 33]


REDUCE FUNCTION

from functools import reduce
z = [1,3,5,7,2]
print(reduce(lambda a,b:a+b, z))

out:-
18

from functools import reduce
z = [1,3,5,7,2]
print(reduce(lambda a,b:a if a>b else b, z))

out:-
7

FILTER FUNCTION

def f2(x):
    if x < 18: return True
    else: return False
    
age = [5,12,17,18,23,32]
adult = filter(f2,age)

for i in adult:
    print(i)

out:-
5
12
17


fib = [0,1,1,2,3,5,8,13,21,34,55]

result = filter(lambda x: x%2, fib)
print(list(result))

out:-
[1, 1, 3, 5, 13, 21, 55]



