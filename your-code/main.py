#1. Import the NUMPY package under the name np.

#[your code here]
import numpy as np

#2. Print the NUMPY version and the configuration.

#[your code here]
print(np.__version__)
print(np.show_config())

def numpy_info(arr):
    print("\nThe dimension is:", arr.ndim)
    print("The shape is:", arr.shape)
    print("The size is:", arr.size)
    print("Array:")
    print (arr)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#[your code here]

#Alternative 1
a=np.random.randint(0, 25, (2, 3, 5))

#Alternative 2
#a=np.random.normal(0, 1, (2, 3, 5))

#Alternative 3
#a=np.random.rand(2, 3, 5)

#Alternative 4
#a=np.random.random((2, 3, 5))

#4. Print a.
#[your code here]
print (numpy_info(arr=a))

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

#[your code here]
b=np.ones((5, 2, 3))

#6. Print b.

#[your code here]
print (numpy_info(arr=b))

#7. Do a and b have the same size? How do you prove that in Python code?

#[your code here]
if a.size==b.size: #arrays size comparrison
    print(f"Both arrays, a and b, have the same size of {a.size}.")
else:
    print("Arrays, a and b, have different size.")

#8. Are you able to add a and b? Why or why not?

#[your code here]

try:
    Arrays_addition= a + b
    print("The arrays wer added successfully:")
    print(Arrays_addition)
except ValueError as e:
    print("Error:", e)
    print("The arrays cannot be added because their shapes are different.")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

#[your code here]
c=np.transpose(b, (1, 2, 0))
#c=b.T
print (numpy_info(arr=c))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

#[your code here]
try:
    d= a + c
    print("\nThe arrays were added successfully:")
    print(d)
except ValueError as e:
    print("\nError:", e)
    print("\nThe arrays cannot be added because their shapes are different.")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#[your code here]

print("\nArray a:")
print(a)

print("\nArray d:")
print(d)

# My explanation: Since array c was transposed from b and all values on b are ones (1), the new array (d) resulted from the sum of arrays a and c cand be defined as d = a+1.

#12. Multiply a and c. Assign the result to e.

#[your code here]

try:
    e_mult= a * c
    print("\nThe arrays were multiplied successfully:")
    print(e_mult)
except ValueError as e:
    print("\nError:", e)
    print("\nThe arrays cannot be multiplied because their shapes are different.")


#13. Does e equal to a? Why or why not?

#[your code here]

is_equal = np.array_equal(e_mult, a)

print("Does e equal to a?", is_equal)

#These arrays are equal because evry value from array a was multiplied by one (1), therefore each value on array e are the same as in a.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

#[your code here]

d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)

print(f"\nThe maximum value of the Array d is: {d_max}.")
print(f"\nThe minimum value of the Array d is: {d_min}.")
print(f"\nThe mean value of the Array d is: {d_mean}.")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

#[your code here]

f=np.empty(d.shape)
print(f"\nThe shape for the Array f is:{f.shape}.")

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

for index, value in np.ndenumerate(d):
    if value == d_min:
        f[index] = 0
    elif value == d_max:
        f[index] = 100
    elif value == d_mean:
        f[index] = 50
    elif value > d_min and value < d_mean:
        f[index] = 25
    elif value > d_mean and value < d_max:
        f[index] = 75

print (numpy_info(arr=f))


#17. Print d and f. Do you have your expected f?
"""For instance, if your d is:"""

d=np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

"""
Your f should be:
f= array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]]) """


#[your code here]

print("\nArray d:")
print(d)

print("\nArray f:")
print(f)

d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)

print(f"\nThe maximum value of the Array d is: {d_max}.")
print(f"\nThe minimum value of the Array d is: {d_min}.")
print(f"\nThe mean value of the Array d is: {d_mean}.")

f=np.empty(d.shape)

for index, value in np.ndenumerate(d):
    if value == d_min:
        f[index] = 0
    elif value == d_max:
        f[index] = 100
    elif value == d_mean:
        f[index] = 50
    elif value > d_min and value < d_mean:
        f[index] = 25
    elif value > d_mean and value < d_max:
        f[index] = 75

print (numpy_info(arr=d))
print (numpy_info(arr=f))

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

f_labels = [[[
    "A" if value == d_min else
    "E" if value == d_max else
    "C" if value == d_mean else
    "B" if d_min < value < d_mean else
    "D"
    for value in row]
    for row in matrix]
    for matrix in d]

# Imprimir el resultado
print("\nArray f with string labels:")
for matrix in f_labels:
    print(matrix)