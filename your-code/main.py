#1. Import the NUMPY package under the name np.

import numpy as np
import random as r

print("\n1.")
print("Import success")

#2. Print the NUMPY version and the configuration.

print("\n2.")
print('Print the NUMPY version and the configuration:')
print(f"NumPy version is {np.version.version}")
print("NumPy configuration")
np.show_config()

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

print("\n3.")
print('A 2x3x5 3-dimensional array with random values:')
print('- 1st Way') # First Way 
print('  a = np.random.random(30)\n  a.shape = (2,3,5)')
a = np.random.random(30)
a.shape = (2,3,5)

print('\n- 2nd Way') # Second Way 
print(  'a = np.empty((2,3,5))\n  a[:] = np.random.rand()')
a = np.empty((2,3,5))
a[:] = np.random.rand(2,3,5)

print('\n- 3rd Way') # Third Way 
print('  a = np.random.random(30).reshape(2,3,5)')
a = np.random.random(30).reshape(2,3,5)

print('\n- 4th Way')
print('  a = np.random.random(size=(2,3,5)) or the simple way')
print('  a = np.random.random((2,3,5))')
a = np.random.random( (2,3,5) ) # np.random.random(size=(2,3,5))
             
#4. Print a.

print("\n4.")
print(f"a is {a}")

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

print("\n5.")
print('b was created with 5x2x3 shape (a 3-dimensional array) with all values equaling 1:')
print('  b = np.ones((5,2,3))')
b = np.ones((5,2,3))

#6. Print b.

print("\n6.")
print(f"b is {b}")

#7. Do a and b have the same size? How do you prove that in Python code?

print("\n7.")
print(f"Is a & b have the same size: {b.size == a.size}")
print(f"a size is {a.size} and for b is {b.size}\n")

#8. Are you able to add a and b? Why or why not?

print("\n8.")
print("Are you able to add a and b? Why or why not?")
print(f"a shape is {a.shape} and for b is {b.shape}.")
print("to add a and b, they need to be the same shape.\n")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".

print("\n9.")
c = np.transpose(b, axes=(1, 2, 0))
print(f"a shape is {a.shape}, and c shape is {c.shape}\n")

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

print("\n10.")
print("It work because a and c shapes and dimension are the same")
print(f"a shape is {a.shape}, and c shape is {c.shape}")
print(f"a dimension is {a.ndim}, and c dimension is {c.ndim}")
print("   d = a + c")
d = a + c
print(f"d is: {d}\n")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("\n11.")
print(f"a is {a}")
print(f"d is {d}\n")

#12. Multiply a and c. Assign the result to e.

print("\n12.")
e = a * c
print(f"e is {e}")

#13. Does e equal to a? Why or why not?

print("\n13.")
print(f"a size is {a.shape}, e size is {e.shape}")
print(f"a shape is {a.size}, e shape is {e.size}")
print("a and e are equals in shape because we multiply each element on a to c in the same index")

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

print("\n14.")
d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print(f"For 'd', the max values is {d_max}, the min value is {d_min}, and the mean is {d_mean}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

print("\n15.")
f = np.empty_like( d, dtype=str )
print(f"f shape is {f.shape}")
print(f"f size is {f.size}")

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

print("\n16.")
f = np.empty_like(d, dtype=int)

f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] =  75
f[d == d_mean] = 50 
f[d == d_min] = 0
f[d == d_max] = 100

print(f'f is {f}')

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

print("\n17.")
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

print("\n18.")

f_str = np.empty_like(d, dtype=str)

f_str[d == d_min] = "A"
f_str[d == d_max] = "E"
f_str[(d > d_min) & (d < d_mean)] = "B"
f_str[(d > d_mean) & (d < d_max)] =  "D"
f_str[d == d_mean] = "C"

print("Array f with Labels")
print(f_str)
print()