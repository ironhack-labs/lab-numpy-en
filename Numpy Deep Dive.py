#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

# Print NumPy version
print("NumPy Version:", np.__version__)

# Print NumPy configuration
np.show_config()


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2, 3, 5)
print("Method 1 - np.random.rand:\n", a)

a = np.random.randint(0, 100, (2, 3, 5))  # Random integers from 0 to 99
print("Method 2 - np.random.randint:\n", a)
 
a = np.random.normal(loc=5, scale=2, size=(2, 3, 5))  # Mean=5, Std=2
print("Method 3 - np.random.normal:\n", a)


#4. Print a.

print('a = ', a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

# Create a 5x2x3 3D array filled with ones
b = np.ones((5, 2, 3))


#6. Print b.

# Print the array
print("Array b:\n", b)

#7. Do a and b have the same size? How do you prove that in Python code?

# Check if a and b have the same size
print("Size of a:", a.size)
print("Size of b:", b.size)

# Check if they are equal
same_size = a.size == b.size
print("Do a and b have the same size?", same_size)


#8. Are you able to add a and b? Why or why not?

# Add a and b
try:
    c = a + b
    print("Addition successful:\n", c)
except ValueError as e:
    print("You are not able to add a and b, because: ", e)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# Transpose b to match the shape of a (2x3x5)
c = np.transpose(b, (1, 2, 0))  # Reorder axes

# Print shapes to confirm
print("Shape of a:", a.shape)
print("Shape of b (original):", b.shape)
print("Shape of c (transposed):", c.shape)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

try:
    d = a + c
    print("Addition successful, because the shapes are the same.")
except ValueError as e:
    print("You are not able to add a and c, because: ", e)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

# The difference between each element is 1 since "c" values are all 1.

#12. Multiply a and c. Assign the result to e.

try:
    e = a*c
    print("Multiplication of a and c was succesful.")
except ValueError:
    print("Could not munltiply a and c.")

#13. Does e equal to a? Why or why not?

print('a: ',a)
print('e: ', e)

# "a" and "e" are the same, since e is a multiplied by "c" and "c" values are all 1, so a*1 == a.

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

# Identify max, min, and mean values in d
d_max = np.max(d)  # Maximum value
d_min = np.min(d)  # Minimum value
d_mean = np.mean(d)  # Mean value

# Print results
print("Maximum value in d:", d_max)
print("Minimum value in d:", d_min)
print("Mean value in d:", d_mean)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

# Create an empty array f with the same shape as d
f = np.empty(d.shape)

# Print shape to confirm
print("Shape of f:", f.shape)



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# Assign values based on conditions
f[d == d_min] = 0      # Assign 0 for the minimum value in d
f[(d > d_min) & (d < d_mean)] = 25  # Assign 25 for values between d_min and d_mean
f[d == d_mean] = 50    # Assign 50 for values equal to d_mean
f[(d > d_mean) & (d < d_max)] = 75  # Assign 75 for values between d_mean and d_max
f[d == d_max] = 100    # Assign 100 for the maximum value in d


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

print(d)
print(f)



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
# Create an empty array of the same shape as d, but with string type
f_str = np.empty(d.shape, dtype=object)

# Assign values based on conditions
f_str[d == d_min] = "A"      # Assign "A" for the minimum value in d
f_str[(d > d_min) & (d < d_mean)] = "B"  # Assign "B" for values between d_min and d_mean
f_str[d == d_mean] = "C"    # Assign "C" for values equal to d_mean
f_str[(d > d_mean) & (d < d_max)] = "D"  # Assign "D" for values between d_mean and d_max
f_str[d == d_max] = "E"    # Assign "E" for the maximum value in d

# Print the labeled array
print("Labeled array f_str:\n", f_str)


