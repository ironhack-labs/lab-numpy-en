#1. Import the NUMPY package under the name np.

#[your code here]
import numpy as np

#2. Print the NUMPY version and the configuration.

#[your code here]
print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#[your code here]
# a = np.random.random(size=(2, 3, 5))
a:np.array = np.random.randint(100, size=(2, 3, 5))
#4. Print a.

#[your code here]
print(f"a:\n{a}")

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

#[your code here]
# b = np.ones(shape=(5, 2, 3))
b:np.array = np.full(shape=(5, 2, 3), fill_value=1)

#6. Print b.

#[your code here]
print(f"b:\n {b}")

#7. Do a and b have the same size? How do you prove that in Python code?

#[your code here]
print(f"Size of a: {np.size(a)}")
print(f"Size of b: {np.size(b)}")
#8. Are you able to add a and b? Why or why not?

#[your code here]

if a.shape==b.shape:
    print(f"We can add a and b because they have the same shape {a.shape}=={b.shape}")
else:
    print(f"We can't add a and b because they don't have the same shape {a.shape}!={b.shape}")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

#[your code here]

c:np.array = b.transpose((1, 2, 0))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

#[your code here]
if a.shape == c.shape:
    d = a + c
    print(f"We can add a and c because they have the same shape {a.shape}=={c.shape}")
else:
    print(f"We can't add a and c because they don't have the same shape {a.shape}!={c.shape}")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#[your code here]
print(f"a:\n{a}")
print(f"d:\n{d}")

print("Each value from the `a` array has been incremented by 1")
#12. Multiply a and c. Assign the result to e.

#[your code here]
e = a * c
print(f"e:\n{e}")

#13. Does e equal to a? Why or why not?

#[your code here]
equals_check = (a == e)
if equals_check.all():
    print("`a` and `e` are equal, as `e` is just the product of `a` multiplied with `1`")
else:
    print("a and e are not equal")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

#[your code here]
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print('d_max: ', d_max)
print('d_min: ', d_min)
print('d_mean: ', '{:.2f}'.format(d_mean))

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

#[your code here]
f = np.empty(shape=(2, 3, 5))

# print(f"f:\n{f}")

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

# your code here

# for i in range(0, d.shape[0]):
#     for j in range(0, d.shape[1]):
#         for k in range(0, d.shape[2]):
#             if d[i, j, k] == d_max:
#                 f[i, j, k] = 100
#             elif d[i, j, k] > d_mean:
#                 f[i, j, k] = 75
#             elif d[i, j, k] == d_mean:
#                 f[i, j, k] = 50
#             elif d[i, j, k] > d_min:
#                 f[i, j, k] = 25
#             else:
#                 f[i, j, k] = 0

conditions = [d == d_max, d > d_mean, d == d_mean, d > d_min]
values = [100, 75, 50, 25]
f = np.select(conditions, values, default = 0)

print(f"f:\n{f}")

# [0, 25, 50, 75, 100]
# ['A', 'B', 'C', 'D', 'E']

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

# we create a new array `g` from `f`, with datatype set to `np.string_`

# g = f.astype(np.string_)
# for i in range(0, d.shape[0]):
#     for j in range(0, d.shape[1]):
#         for k in range(0, d.shape[2]):
#             if d[i, j, k] == d_max:
#                 g[i, j, k] = 'E'
#             elif d[i, j, k] > d_mean:
#                 g[i, j, k] = 'D'
#             elif d[i, j, k] == d_mean:
#                 g[i, j, k] = 'C'
#             elif d[i, j, k] > d_min:
#                 g[i, j, k] = 'B'
#             else:
#                 g[i, j, k] = 'A'

g = np.select(conditions, ['E', 'D', 'C', 'B'], default=['A'])

print(f"g:\n{g}")
