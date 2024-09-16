#1. Import the NUMPY package under the name np.

#[your code here]

import numpy as np


#2. Print the NUMPY version and the configuration.

print("NumPy version:", np.__version__)

np.show_config()

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2, 3, 5))


#4. Print a.

print (a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print (b)


#7. Do a and b have the same size? How do you prove that in Python code?

# Generate array 'a' for demonstration
a = np.random.rand(2, 3, 5)  # 2x3x5 array

# Generate array 'b' for demonstration
b = np.ones((5, 2, 3))  # 5x2x3 array

# Check if 'a' and 'b' have the same size
same_size = a.size == b.size

print(f"Array 'a' size: {a.size}")
print(f"Array 'b' size: {b.size}")
print(f"Do 'a' and 'b' have the same size? {same_size}")

#8. Are you able to add a and b? Why or why not?


# Assuming a and b are already defined as NumPy arrays
a = np.random.rand(2, 3, 5)  # 2x3x5 array
b = np.ones((5, 2, 3))  # 5x2x3 array

# Check if they have the same shape
print(f"Shape of a: {a.shape}")
print(f"Shape of b: {b.shape}")

# Try adding a and b
try:
    c = a + b
    print("Addition successful.")
    print(c)
except ValueError as e:
    print("Addition failed:", e)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# Assuming b is already defined as a 5x2x3 array
b = np.ones((5, 2, 3))  # 5x2x3 array

# Transpose b to have the shape (2, 3, 5)
c = np.transpose(b, (1, 2, 0))

# Print the shape of the new array
print(f"Shape of c: {c.shape}")
print(c)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

# Assuming a and c are defined
a = np.random.rand(2, 3, 5)  # Shape (2, 3, 5)
b = np.ones((5, 2, 3))  # Shape (5, 2, 3)
c = np.transpose(b, (1, 2, 0))  # Transposed to shape (2, 3, 5)

# Add a and c
d = a + c

# Print the result
print("Array a:")
print(a)
print("\nArray c:")
print(c)
print("\nArray d (a + c):")
print(d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print ('this is it')
print (a)
print (b)

#12. Multiply a and c. Assign the result to e.

e = a * c

#13. Does e equal to a? Why or why not?

# Assuming a and e are already defined
# Check if e is equal to a
are_equal = np.array_equal(a, e)
print(f"Is e equal to a? {are_equal}")



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


# Identify the max, min, and mean values in d
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(f"Max value in d: {d_max}")
print(f"Min value in d: {d_min}")
print(f"Mean value in d: {d_mean}")


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty(d.shape)

print (f)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# Assuming d and f are already defined
# Assuming d_max, d_min, d_mean are already calculated

# Populate f based on the conditions
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 75

# Print the resulting array f
print("Array f:")
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

import numpy as np

# Given example array d
d = np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
               [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
               [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

              [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
               [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
               [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

# Calculate d_max, d_min, and d_mean
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

# Create an empty array f with the same shape as d
f = np.empty(d.shape)

# Populate f based on the conditions
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 75

# Print d and f to verify
print("Array d:")
print(d)
print("\nArray f:")
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

# Assuming d is already defined and has the shape (2, 3, 5)
# Calculate d_max, d_min, and d_mean
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

# Create an empty array f with the same shape as d but to store strings
f = np.empty(d.shape, dtype=str)

# Populate f based on the conditions using string labels
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 'A'  # Assign 'A' for the minimum value
            elif d[i, j, k] == d_max:
                f[i, j, k] = 'E'  # Assign 'E' for the maximum value
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 'C'  # Assign 'C' for the mean value
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 'B'  # Assign 'B' for values between min and mean
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 'D'  # Assign 'D' for values between mean and max

# Print the resulting array f
print("Array d:")
print(d)
print("\nArray f with string labels:")
print(f)
