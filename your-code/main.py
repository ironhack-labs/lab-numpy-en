import numpy as np

#2. Print the NUMPY version and the configuration.
np.show_config()

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))

#4. Print a.
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))



#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
if a.size == b.size:
    print("yes, they have the same size")
else:
    print("No they don't have the same size")

#8. Are you able to add a and b? Why or why not?

if a.shape == b.shape:
    result = a + b
    print("Addition Result:")
    print(result)
else:
    print("Arrays have different shapes and cannot be added.")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1, 2, 0))
print("Array c (transposed b):")
print(c)
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print("Addition of a and c:")
print(d)
print("The addition works because 'a' and 'c' now have the same shape.")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("Array a:")
print(a)
print("Array d (a + c):")
print(d)
print("Explanation: 'd' is the result of adding each element of 'a' with the corresponding element of 'c', which is an array of ones. Thus, 'd' is simply 'a' with 1 added to each element.")


#12. Multiply a and c. Assign the result to e.

e = a*c
print("Multiplication of a and c results in 'e':")
print(e)

#13. Does e equal to a? Why or why not?

if np.array_equal(e, a):
    print("Yes, e equals a.")
else:
    print("No, e does not equal a.")

print("Explanation: 'e' equals 'a' because multiplying any number by 1 results in the same number. Since 'c' is an array of ones, the multiplication doesn't change the values of 'a'.")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("d_max:", d_max)
print("d_min:", d_min)
print("d_mean:", d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty(d.shape)
print("Array f (empty):")
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

print("Array f after populating values:")
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

# 18. Populate the values in f with string labels.
f = np.empty(d.shape, dtype=str)  
for i in range(d.shape[0]):  
    for j in range(d.shape[1]):  
        for k in range(d.shape[2]):  

            if d[i, j, k] == d_min:
                f[i, j, k] = 'A'  
            elif d[i, j, k] == d_max:
                f[i, j, k] = 'E' 
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 'C' 
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 'B' 
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 'D'  

print("Array f after populating string labels:")
print(f)
