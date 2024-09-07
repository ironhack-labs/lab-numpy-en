#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.__version__)

np.show_config()


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"

a = np.random.rand(2, 3, 5)

# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randn(2, 3, 5)  # standard normal distribution
a = np.random.randint(0, 9, (2, 3, 5))  # random integers within a specified range
a = np.random.uniform(1, 10, (2, 3, 5))  # values uniformly distributed between specified lower and upper bounds
a = np.random.choice([1, 2, 3, 4, 5], (2, 3, 5))  # random values from a list
a = np.random.random((2, 3, 5))  # similar to random.rand() but passing shape as a tuple
a = np.random.beta(0.5, 0.5, (2, 3, 5))  # random values from a beta distribution
a = np.random.normal(0, 1, (2, 3, 5))  # mean = 0, standard deviation = 1
a = np.random.poisson(5, (2, 3, 5))  # values from a Poisson distribution with lambda = 5
a = np.random.binomial(n = 10, p = 0.5, size = (2, 3, 5))  # values from a binomial distribution with n = 10, p = 0.5
a = np.random.f(5, 2, (2, 3, 5))  # values from the F-distribution with dfn = 5 and dfd = 2


#4. Print a.

print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))


#6. Print b.

print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

# Using numpy:
print(a.size == b.size)

# Pythonic way:
a = np.random.f(5, 2, (2, 3, 5))
b = np.ones((5, 2, 3))
len_a = len([value for sublist_1 in a for sublist_2 in sublist_1 for value in sublist_2])
len_b = len([value for sublist_1 in b for sublist_2 in sublist_1 for value in sublist_2])
print(len_a == len_b)


#8. Are you able to add a and b? Why or why not?

# print(a + b)  # We get a ValueError for them having different shapes.


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1, 2, 0))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c  # Working: they now do have the same shape.


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

# In d all values are increased by 1 compared to a, because c consisted only of ones.


#12. Multiply a and c. Assign the result to e.

e = a * c


#13. Does e equal to a? Why or why not?

print(np.array_equal(a, e))

# They are equal because all the values were simply multiplied by the 1s in c.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty(d.shape)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# Using numpy:
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100

# Pythonic way:
for i in range(len(d)):
    for j in range(len(d[i])):
        for k in range(len(d[i][j])):
            if d_mean > d[i][j][k] > d_min:
                f[i][j][k] = 25
            elif d_max > d[i][j][k] > d_mean:
                f[i][j][k] = 75
            elif d[i][j][k] == d_mean:
                f[i][j][k] = 50
            elif d[i][j][k] == d_min:
                f[i][j][k] = 0
            else:
                f[i][j][k] = 100


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

f = np.empty(d.shape, dtype = '<U1')  # '<U1' to allow for strings of length 1 in a (new) numpy array

# Using numpy:
f[(d > d_min) & (d < d_mean)] = 'B'
f[(d > d_mean) & (d < d_max)] = 'D'
f[d == d_mean] = 'C'
f[d == d_min] = 'A'
f[d == d_max] = 'E'

# Pythonic way:
for i in range(len(d)):
    for j in range(len(d[i])):
        for k in range(len(d[i][j])):
            if d_mean > d[i][j][k] > d_min:
                f[i][j][k] = 'B'
            elif d_max > d[i][j][k] > d_mean:
                f[i][j][k] = 'D'
            elif d[i][j][k] == d_mean:
                f[i][j][k] = 'C'
            elif d[i][j][k] == d_min:
                f[i][j][k] = 'A'
            else:
                f[i][j][k] = 'E'

print(f)
