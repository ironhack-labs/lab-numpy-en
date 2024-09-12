#1. Import the NUMPY package under the name np.

#[your code here]
import numpy as np

#2. Print the NUMPY version and the configuration.

#[your code here]
np.show_config()
print(np.__version__).

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#[your code here]
a = np.random.random((2,3,5))


#4. Print a.
#[your code here]
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

#[your code here]
b = np.ones((5,2,3))

#6. Print b.

#[your code here]
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

#[your code here]
if a.size == b.size:
    print("Yes, they have the same size")
else:
    print("No, they don't have the same size")

#8. Are you able to add a and b? Why or why not?
# Arrays a and b cannot be added directly because their shapes (2, 3, 5) and (5, 2, 3) don't align.
#[your code here]
print("Shape of a: ", a.shape)
print("Shape of b: ", b.shape)
# c = a + b #it doesn't work it gives an error

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

#[your code here]
c = np.transpose(b, (1,2,0))
print("Shape of c: ", c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

#[your code here]
result = a + c
print("Shape of d: ", result.shape)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#[your code here]
print("Shape of d: ", result.shape)

#12. Multiply a and c. Assign the result to e.
# The array d adds 1 to each corresponding element of array a due to the addition to array c which is made up of ones.
#[your code here]
e = a * c
print("Array a:", a)
print("Array c:", c)
print("Result of a * c:", e)

#13. Does e equal to a? Why or why not?
#Yes, because multiplying by one doesn't change the values.
#[your code here]


#Its not equal because the shape of a is (2,3,5) and the shape of e is (2,3,5)

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

#[your code here]
d = np.array([10, 20, 30, 40, 50])
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

# Print the results
print(f"Maximum value: {d_max}")
print(f"Minimum value: {d_min}")
print(f"Mean value: {d_mean}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

#[your code here]
d = np.random.rand(2, 3, 5)  # Example array, you can replace this with your actual array

f = np.empty(d.shape)

print(f"Shape of f: {f.shape}")
print(f"Array f:\n{f}"))


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
d = np.array([[[10, 20, 30, 40, 50],
               [15, 25, 35, 45, 55],
               [12, 22, 32, 42, 52]],
              
              [[11, 21, 31, 41, 51],
               [14, 24, 34, 44, 54],
               [13, 23, 33, 43, 53]]])

# Calculate d_min, d_max, and d_mean
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

# Create an empty array f with the same shape as d
f = np.empty(d.shape)

# Populate the values in f based on the conditions
for index, value in np.ndenumerate(d):
    if value == d_min:
        f[index] = 0
    elif value == d_max:
        f[index] = 100
    elif value == d_mean:
        f[index] = 50
    elif d_min < value < d_mean:
        f[index] = 25
    elif d_mean < value < d_max:
        f[index] = 75

# Print the result
print(f"Array d:\n{d}")
print(f"Array f:\n{f}")



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
print(f"Array d:\n{d}")
print(f"Array f:\n{f}")


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