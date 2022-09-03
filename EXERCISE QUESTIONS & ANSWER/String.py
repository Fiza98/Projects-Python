LOOPING AND COUNTING

word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print(count)

Exercise 1
Based on the given Python code:
z = “Tuesday, 20:06:2018,13:20:23,Malaysia,Shah Alam”

Write the correct Python scripts to produce the following output:
a) Count how many times ‘,’ is in the string
print(z.count(","))

b) Split the word using “,” as a delimiter
print(z.split(','))

c) Print the time stated in the string
print(z[21:28])

d) Replace “Tuesday” with “Thursday”
new_z = 'Thursday' + z[1:]
print(new_z)

e) Capitalize the whole string
new_z = z.upper()
print(new_z)


Exercise 2
Based on the given Python code below:
word = “Python a large heavy-bodied non-venomous snake occurring through
out the Old World tropics, killing prey by constriction and asphyxiation.”

Write down the correct Python scripts to produce the following output:
a) Count how many times ‘a’ is in the string
print(word.count("a"))

b) Find the location of ‘x’ in the string
word.find("x")

c) Split the word using ‘,’ as a delimiter
print(z.split(","))

d) Replace the string ‘Python’ to ‘Anaconda’
print('Anaconda' + data[1:])

e) Capitalize first letter of each word
f) Print the length of the string
len(word)

g) Find ‘World’ in the string
word.find('World')

Exercise 3
Based on the given Python code below:
User_string = “ID:2002 User:Zuliana Age:37 Sex:Female Auth:Moderator.”

Write down the correct Python scripts to produce the following output:
a) Count how many times colon appear in the given string
print(User_string.count(":"))

b) Split the string User_string using whitespace as delimiter
print(User_string.split(' '))

c) Find the user Authorization level
print ("Authorization level", User_string[45:53])

d) Replace the string ‘Moderator’ to ‘Guest’
new_User_string = 'Guest' + User_string[45:]
print(new_User_string)

e) Append the string with the text “ Address: 20, Jalan Masjid, 83700”
text = “ Address: 20, Jalan Masjid, 83700”
print(User_string[:53] + text)

Exercise 4
Based on the given Python code:
data = “Time 2019-03-13 11:49:27, User Fahim, Access Guest”

Write the correct Python scripts to produce the following desired output:
a) Count how many whitespaces are in the string
print(data.count(" "))

b) Split the string data using comma as a delimiter
print(data.split(","))

c) Print the string in b) that contains the username
print("Username", data[28:55])

d) Replace the string ‘Guest’ to ‘Moderator’
new_data = 'Moderator' + data[46:]
print(new_data)

e) Print the year in data
print(data[6:9])


Exercise 5
Based on the given Python code:
word = “the brown fox jumped over the lazy dog”

Write the correct Python scripts to produce each of the following desired output:
a) Count how many times ‘o’ is in the string
print(word.count("o"))

b) Find the location of ‘x’ in the string
word.find('x')

c) Split a word using whitespace
print(word.split(" "))

d) Replace the string ‘fox’ to ‘cat’
new_word = 'cat' + word[11:]
print(new_word)

e) Capitalize the whole word
print(word.upper())

Exercise 6
Write out the correct output from the given python syntax:
a) 8 % 3
2

b) not 2 == 5
True

c) 2 != 5
True

d) (2 > 1) and (5 < 8)
True

e) ((not 3 > 2) and (8 < 9)) or (9 > 2)
True

f) "ram" in "Programming is fun"
True

g) print("This has a\nline break")
This has a
line break

h) print("Razif\'s student said, \"I like this course.\"")
Razif's student said, "I like this course."

i) print("%-8.3f" %10. + "\n" + "%-8.3f" %100.)
10.000
100.000


Exercise 7

Write a python program to do the following:
1. input a string
2. count how many words in the given string
3. calculate the frequency of each word in the string

example:  let say user has input this string or sentence
     "twinkle twinkle little star"

the output will be:
    there are 4 words in the sentence
    frequency of each word:
       twinkle 2
       little 1
       star 1

ANSWER:

METHOD 1

import re

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

#input
a = input("Please enter the sentence: ")
#count the words
count = len(re.findall(r'\w+', a))
#print how many words in the string
print ("There are ",count,"words in the sentence")
#print the frequency of each word
print( "Frequency of each word: \n", word_count(a))

OUTPUT:

Please enter the sentence: entah la labu
There are  3 words in the sentence
Frequency of each word: 
 {'la': 1, 'labu': 1, 'entah': 1}


Exercise 8

Write a python program to do the following:
1. input a string
2. reverse the given string
3. display the reversed string

ANSWER:

#input
a = input("Please enter the sentence: ")


def reverse_slicing(s):
    return s[::-1]

input_str = a

if __name__ == "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))

OUTPUT:
Please enter the sentence: afriza
Reverse String using slicing = azirfa
