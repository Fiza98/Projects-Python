LAB EXERCISE – NUMPY

#Exercise 1

#Write down the correct output based on the given Python scripts.

import numpy as np
month = np.array([“Jul”, “Aug”,”Sep”,”Oct])
x1, x2, x3 = np.split(month, [1,3]) #array is split into subarray x1 = month[:1] x2 = month[1:3] x3 = month[3:]
mat = np.matrix(‘1 2; 3 4’)
left, right = np.hsplit(mat, [1])
top, bottom = np.vsplit(mat, [1])

i) print (month[-1]) #from right to left
out:
Oct

ii) print(mat) #matrix 2x2 with item [1:] and [3 4]
[[1 2]
 [3 4]]

iii) print(x2) #subarray moth[1:3] 1st index until before 2nd index
out:
['Aug' 'Sep']

iv) print(left) #vertical split of matrix on left side
out:
[[1]
 [3]]

v) print(top) #horizontal split of matrix top side
[[1 2]] 

vi) print(bottom) #horizontal split of matrix bottom side
[[3 4]]

print(x3) #subarray moth[3:] 1st index until last index
out:
['Oct']

print(x1) #subarray month[:1] until before 2nd index
['Jul']

#for each of the output, understand how Python executes the script.

#Exercise 2

#Write down a Python script for the following instructions:

#i) Import the numpy package as np
import numpy as np

#ii) Create list height_centimeters [180, 215, 210,210,188, 176, 209, 200]
height_centimeters = [180, 225, 210, 188, 176, 209, 200]

#iii) Create a numpy array from height_centimeters and assign to np_height_cm
np_height_cm = np.array(height_centimeters)

#iv) Convert the numpy array np_height_cm to metres and assign to np_height_m
np_height_m = np_height_cm/100

#v) Print out the type of np_height_m
type(np_height_m)

#vi) Print out the values/elements of np_height_m
 print(np_height_m)
out:-
[1.8 2.15 2.1 2.1 1.88 1.76 2.09 2.]

