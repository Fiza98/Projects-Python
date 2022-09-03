#1.

# function which return reverse of a string 
  
def isPalindrome(s): 
    return s == s[::-1] 
  
  
# Driver code 
s = input("Please enter the word: ")
ans = isPalindrome(s) 
  
if ans: 
    print("Yes") 
else: 
    print("No")

#2.

#Take the input from the user:   
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)

#3.

list1 = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())
list2 = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())
print("User List 1: ", list1)
print("User List 2: ", list2)

# Python program to merge and sort two list 
def Merge(list1, list2): 
    final_list = list1 + list2 
    final_list.sort() 
    return(final_list) 
  
# Driver Code 

print(Merge(list1, list2)) 

#4.

# Program to sort alphabetically the words form a string provided by the user

my_str = input("Please Enter the Sentence: ")

# To take input from the user
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
