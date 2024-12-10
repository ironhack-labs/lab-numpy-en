#1. Import the NUMPY package under the name np.

#[your code here]

import numpy as np  # Importing numpy as a shorthand `np


#2. Print the NUMPY version and the configuration.

#[your code here]

print(np.__version__)  # Prints the version of numpy installed
print(np.show_config())  # Displays the configuration of numpy (e.g., build info)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#[your code here]

# Way #1: Using np.random.random()
# This method generates random float values between 0 and 1 from a uniform distribution.
# Generates a 3D array with random float values in the range [0, 1).
a = np.random.random((2, 3, 5))

# Way #2: Using np.random.rand()
# This method generates random float values between 0 and 1 from a uniform distribution.
# Generates a 3D array with random float values in the range [0, 1).
a1 = np.random.rand(2, 3, 5)

# Way #3: Using np.random.uniform()
# This method generates random float values from a uniform distribution within a specified range.
# Generates a 3D array with random float values in the range [0, 1) (can set custom range if needed).
a2 = np.random.uniform(0, 1, (2, 3, 5))

# Way #4: Using np.random.randint()
# This method generates random integer values within a specified range.
# Generates a 3D array with random integer values in the range [0, 100).
a3 = np.random.randint(0, 100, (2, 3, 5))

# Way #5: Using np.random.randn()
# This method generates random float values from a standard normal distribution (mean=0, std=1).
# Generates a 3D array with random float values that can be negative, zero, or positive.
a4 = np.random.randn(2, 3, 5)

# Way #6: Using np.random.normal()
# This method generates random float values from a normal distribution with a specified mean and standard deviation.
# Generates a 3D array with random float values centered around mean=0 with std=1 (default).
a5 = np.random.normal(0, 1, (2, 3, 5))

# Way #7: Using np.random.choice()
# This method selects random values from a given set or range, with or without replacement.
# Generates a 3D array with random integer values selected from the range [0, 100).
a6 = np.random.choice(range(100), (2, 3, 5))


#4. Print a.

#[your code here]

print(a)

print(a1)

print(a2)

print(a3)

print(a4)

print(a5)

print(a6)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

#[your code here]

b = np.ones((5, 2, 3))  # Creates a 3D array filled with the value `1`


#6. Print b.

#[your code here]

print(b)  # Prints the contents of array `b`


#7. Do a and b have the same size? How do you prove that in Python code?

#[your code here]

print(a.size == b.size)  # Checks if both arrays have the same number of elements

print(f"Size of a: {a.size}")
print(f"Size of b: {b.size}")

'''
Explanation:

* a.size: Returns the total number of elements in the array a.
* b.size: Returns the total number of elements in the array b.
* The comparison a.size == b.size evaluates to True because:
    * a is a 2x3x5 array, so its size is 2×3×5=30.
    * b is a 5x2x3 array, so its size is 5×2×3=30.
* Since both arrays have the same total number of elements, the result is True.
'''

#8. Are you able to add a and b? Why or why not?

#[your code here]

print(f"Shape of a: {a.shape}")
print(f"Shape of b: {b.shape}")

# Trying to add a and b will raise a ValueError due to shape mismatch
try:
    result = a + b
except ValueError as e:
    print(f"Addition error: {e}")  # Outputs the error message

'''
Explanation:

* Shapes of a and b:

    * a has the shape (2, 3, 5).
    * b has the shape (5, 2, 3).

* Why can't they be added?

    * In NumPy, element-wise addition requires arrays to have the same shape or be broadcastable to a common shape.
    * Broadcasting rules require dimensions to match or one of them to be 1. In this case:
        * The shapes (2, 3, 5) and (5, 2, 3) are not compatible for broadcasting because none of the dimensions align.

Broadcasting in NumPy

Broadcasting refers to how NumPy handles element-wise operations (like addition, subtraction, etc.) on arrays of different shapes. It allows NumPy to perform operations on arrays of different sizes in a way that makes them compatible without needing to explicitly reshape the arrays.

Key Principles of Broadcasting:

1. Align dimensions: NumPy will "stretch" or "broadcast" smaller arrays to match the shape of the larger array, if possible.

2. Matching shapes: For two arrays to be broadcast together, their dimensions must be compatible in a specific way:

    * Starting from the trailing dimensions, the sizes must either be the same, or one of them must be 1 (which allows it to be broadcast).

    * If the dimensions are different and neither is 1, broadcasting will not work, and you will get an error.
'''

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

#[your code here]

c = b.transpose(1, 2, 0)  # Rearranges axes to change shape from (5, 2, 3) to (2, 3, 5)
print(c)

'''
Explanation:

* Objective: Transpose the array b, which has the shape (5, 2, 3), into a new shape of (2, 3, 5).

* The transpose() method: This method rearranges the axes of a NumPy array.

* The argument (1, 2, 0):
    
    * This tells NumPy how to permute the axes of the array.

    * Axis 1 (size 2) comes first, axis 2 (size 3) comes second, and axis 0 (size 5) comes last.

    * After transposing, the new shape of b is (2, 3, 5), and the resulting array c has this shape.

In summary, this step rearranged the dimensions of b to match the shape of a, which is (2, 3, 5).
'''


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

#[your code here]

d = a + c  # Adds corresponding elements of a and c

'''
Adding a and c now works because after transposing b to create c, both arrays a and c have the same shape (2, 3, 5), making them compatible for element-wise addition.
'''


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#[your code here]

print("Array a:")
print(a)  # Prints the original random array `a`

print("Array d:")
print(d)  # Prints the result of adding `a` and `c`

'''
Explanation of the difference and relationship between `a` and `d`:
 - `a` contains random values.
 - `c` is a transposed version of `b`, which contains all 1's.
 - When `a` and `c` are added together, each value in `a` is increased by 1 because `c` is filled with 1's.
 - Therefore, `d` is exactly 1 greater than `a` in every corresponding element.
'''


#12. Multiply a and c. Assign the result to e.

#[your code here]

e = a * c  # Performs element-wise multiplication between `a` and `c`


#13. Does e equal to a? Why or why not?

#[your code here]

print(np.array_equal(e, a))  # Checks if `e` and `a` are identical

'''
Explanation:
    - Since c is an array of 1's, multiplying a by c doesn't change the 
      values in a.
    - In other words, multiplying any value by 1 leaves it unchanged.
    - Therefore, e is identical to a, and the result of np.array_equal(e,a) 
      is True.
'''


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

#[your code here]

d_max = np.max(d)  # Finds the maximum value in `d`
d_min = np.min(d)  # Finds the minimum value in `d`
d_mean = np.mean(d)  # Finds the mean value of all elements in `d`

print(d_max)
print(d_min)
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

#[your code here]

f = np.empty_like(d)  # Creates an empty array with the same shape and type as `d`

print(f)

'''
Explanation:

* np.empty_like(d) creates an array f with the same shape and type as d, but without initializing the entries. The values in this array will be whatever happens to be in memory at that point, and they are not necessarily zeros or ones.

* This is often used when you want to create an array to store results without immediately filling it with specific values, especially when it will be updated or populated later.

So, the array f will have the same structure (shape of 2x3x5) as d but with uninitialized (random) values.
'''

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

#[your code here]

# Print the original d, min, mean, and max values
print("Original array d:")
print(d)
print("d_min:", d_min)
print("d_mean:", d_mean)
print("d_max:", d_max)

# Print f before modification
print("Array f before modification:")
print(f)

# Assign values to f based on the conditions
f[(d > d_min) & (d < d_mean)] = 25  # Assign 25 for values between d_min and d_mean
print("f after assigning 25:")
print(f)

f[(d > d_mean) & (d < d_max)] = 75  # Assign 75 for values between d_mean and d_max
print("f after assigning 75:")
print(f)

f[d == d_mean] = 50  # Assign 50 for values equal to d_mean
print("f after assigning 50:")
print(f)

f[d == d_min] = 0  # Assign 0 for the minimum value
print("f after assigning 0:")
print(f)

f[d == d_max] = 100  # Assign 100 for the maximum value
print("f after assigning 100:")
print(f)

'''
Explanation:

The code populates the array f based on conditions applied to the values in array d:

* If a value in d is greater than d_min but smaller than d_mean, assign 25 to f.

* If a value in d is greater than d_mean but smaller than d_max, assign 75 to f.

* If a value in d is equal to d_mean, assign 50 to f.

* If a value in d is equal to d_min, assign 0 to f.

* If a value in d is equal to d_max, assign 100 to f.

The result is that f will contain only the values 0, 25, 50, 75, and 100, based on the thresholds in d. The code uses element-wise comparisons with logical operators to assign these values.
'''


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

#[your code here]

print("Array d:")
print(d)  # Prints the original array `d`

print("Array f:")
print(f)  # Prints the labeled array `f` with values 0, 25, 50, 75, and 100

'''
* Array d consists of floating-point values in a 3x3x5 shape.
* Array f is populated based on the values in d, using thresholds d_min, 
  d_mean, and d_max.
    * For values between d_min and d_mean, f is assigned 25.
    * For values between d_mean and d_max, f is assigned 75.
    * Values equal to d_mean get assigned 50.
    * Values equal to d_min are assigned 0, and values equal to d_max get 
      assigned 100.

The printed output shows that f contains the expected values (0, 25, 50, 75, 100) based on the specified conditions. Your f array corresponds to the rules for mapping the values from d correctly.
'''

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

#[your code here]

# Create an empty array of object type to store strings
f_strings = np.empty_like(d, dtype=object)

# Populate the array based on conditions
f_strings[(d > d_min) & (d < d_mean)] = "B"  # Assign "B" for values between d_min and d_mean
f_strings[(d > d_mean) & (d < d_max)] = "D"  # Assign "D" for values between d_mean and d_max
f_strings[d == d_mean] = "C"  # Assign "C" for values equal to d_mean
f_strings[d == d_min] = "A"  # Assign "A" for the minimum value
f_strings[d == d_max] = "E"  # Assign "E" for the maximum value

# Print the result
print(f_strings)