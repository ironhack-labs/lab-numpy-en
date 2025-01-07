#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

# Print the NumPy version
print("NumPy Version:", np.__version__)

# Print the NumPy configuration
print("\nNumPy Configuration:")
np.show_config()


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

# Method 1: Using np.random.rand to generate random values between 0 and 1
a = np.random.rand(2, 3, 5)
print("\nRandom a:")
print(a)

# method 2: using np.random.randn
b= np.random.randn (2,3,5)
print("\nRandom b:")
print (b)

# Methos 3: using np.random.randint
#c= np.random.randint (2, 3, 5)
#print (c)
#output [2 2 2 2 2]

# Generate a random 2D NumPy array with dimensions 3 x 4 x 5
c = np.random.randint(3, size=(2, 3, 5)) # (block, rows, columns)

# Print the generated vector
print("\nRandom c:")
print(c)


#4. Print a.

print("\nRandom a:")
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

# Create a 3-dimensional array with all values equal to 1
b = np.ones((5, 2, 3))

#6. Print b.

# Print the array
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

import numpy as np

# Define array a
a = np.random.rand(2, 3, 5)

# Print the shape and size of array a
print("Shape of a:", a.shape)
print("Size of a:", a.size)

# Define array b
b = np.ones((5, 2, 3))

# Print the shape and size of array b
print("Shape of b:", b.shape)
print("Size of b:", b.size)

# Compare the sizes of arrays a and b
if a.size == b.size:
    print("Array a and b have the same size.")
else:
    print("Array a and b have different sizes.")
    

#8. Are you able to add a and b? Why or why not?
'''In NumPy, arrays must have the same shape in order to be added together. The shape of an array is defined by the number of elements along each axis. Given that the shapes of a and b are (2, 3, 5) and (5, 2, 3) respectively, they do not have the same shape, and therefore cannot be added together.
If you attempt to add arrays a and b using the + operator, it will result in a ValueError because the shapes are not compatible for addition.'''
#[your code here]


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1, 2, 0)
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

'''The addition between arrays a and c should work now because they have the same shape after transposing b. The shapes of a and c are both (2, 3, 5), which makes them compatible for element-wise addition in NumPy.'''
d = a + c
print(d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
'''The values in array d are the element-wise sum of the values in arrays a and c. This is because when performing addition with NumPy arrays, the operation is applied element-wise, meaning that corresponding elements from each array are added together to form the resulting array.'''
print("Array a:")
print(a)
print("Array d (result of addition between a and c):")
print(d)

#12. Multiply a and c. Assign the result to e.

# Multiply arrays a and c and assign the result to e
e = a * c
print(e)

#13. Does e equal to a? Why or why not?

'''The variable e does not necessarily equal a because it represents the result of element-wise multiplication between arrays a and c. Since the values in c were initially all 1, the resulting array e is equal to array a.
Element-wise multiplication between an array and another array containing all 1 results in the original array, which is why in this specific case e is equal to a.
However, it's important to note that had c contained values different from 1, the resulting array e would not necessarily be equal to a. The specific values in c directly affect the result of the element-wise multiplication.'''



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

import numpy as np

# Calculate the max, min, and mean values in array d
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("Max value in d:", d_max)
print("Min value in d:", d_min)
print("Mean value in d:", d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

import numpy as np

# Create an empty array f with the same shape as array d
f = np.empty_like(d)

print(f)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# Iterate over the values of array d and update array f
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = 75
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100

print(f)



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print ("\n Array d:", d)

print ("\n Array f:", f)


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

# Create an empty array f with the same shape as array d and dtype 'U1' for strings
f = np.empty((2, 3, 5), dtype='<U1')

# Iterate over the values of array d and update array f with string values
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = "B"
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = "D"
            elif d[i, j, k] == d_mean:
                f[i, j, k] = "C"
            elif d[i, j, k] == d_min:
                f[i, j, k] = "A"
            elif d[i, j, k] == d_max:
                f[i, j, k] = "E"
print("\nConvert numeric values to string values for f:" )
print(f)