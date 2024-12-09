#1. Import the NUMPY package under the name np.

#[your code here]
import numpy as np
import random

#2. Print the NUMPY version and the configuration.

#[your code here]
print('The version of Numpy is: ',np.__version__)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
#[your code here]
a = np.random.random((2,3,5)) #random values between 0 - 1

a1 = np.random.rand(2, 3, 5) # same as above

a2 = np.random.randn(2, 3, 5) #random values with a normal distribution

a3 = np.random.randint(0, 10, size=(2, 3, 5))

#4. Print a.
print('\n===========4============\n')
print('Random values between 0-1:\n',a)
print('\nRandom values between 0-1:\n',a1)
print('\nRandom values with normal distribution:\n',a2)
print('\nRandom integers:\n',a3)

#[your code here]
#5. Create a 5x3x2 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
#[your code here]
b = np.ones((5,3,2))

#6. Print b.
#[your code here]
print('\n===========6============\n')
print('5x3x2 3-dimensional array with all values equaling 1:\n',b)

#7. Do a and b have the same size? How do you prove that in Python code?

#[your code here]
print('\n===========7============\n')

print('The size of a array is: ',a.size)

print('The size of b array is: ',b.size)

if a.size == b.size:
        print("\n'a' and 'b' are of the same size")

#8. Are you able to add a and b? Why or why not?
#[your code here]
# we cant preform ab_sum = np.sum(a,b) because they might be of the same size but they are not of the same shape to be added.
print('\n===========8============\n')

print(f"'a' is of shape {a.shape} and 'b' is of shape {b.shape} since they have different shapes they cant be added.")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".
#[your code here]
c = b.T

print('\n===========9============\n')


print(f'The shape of b is {b.shape} and the shape of the transpose of be is {c.shape}')
print('\nThe transpose of b is: \n',c)


#10. Try to add a and c. Now it should work. Assign the sum to variable "d". But why does it work now?
#[your code here]

d = np.add(a, c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
#[your code here]

print('\n===========11============\n')

print("'a' added to the transpose of 'b' ('c') is: \n", d)

#12. Multiply a and c. Assign the result to e.
#[your code here]
print('\n===========12============\n')

e = np.multiply(a, c)
print("Multiply 'a' times 'c': \n",e)

#13. Does e equal to a? Why or why not?
#[your code here]

is_equal = np.array_equal(e, a)

print('\n===========13============\n')
print(f"Does 'e' equal 'a'? {is_equal}")

if is_equal:
    print("'e' equals 'a' because element-wise multiplication of 'a' and 'c' did not change the values of 'a'.")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

#[your code here]
print('\n===========14============\n')


d_min = np.min(d)
print("Minimum Value of 'd':", d_min)

d_max = np.max(d)
print("Maximum Value of 'd':", d_max)

d_mean = np.mean(d)
print("Mean Value of 'd':", d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
#[your code here]

print('\n===========15============\n')

f = np.empty((2,3,5))
print("Print the empty array 'f': ", f)

"""
#16. Populate the values in f. 
1. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
2. If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
3. If a value equals to d_mean, assign 50 to the corresponding value in f.
4. Assign 0 to the corresponding value(s) in f for d_min in d.
5. Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

#[your code here]

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        if d[i,j,k] == d_min:
                                f[i,j,k] = 0
                        elif d[i,j,k] > d_min and d[i,j,k] < d_mean:
                                f[i,j,k] = 25
                        elif d[i,j,k] == d_mean:
                                f[i,j,k] = 50
                        elif d[i,j,k] > d_mean and d[i,j,k] < d_max:
                                f[i,j,k] = 75
                        elif d[i,j,k] == d_max:
                                f[i,j,k] = 100

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

print('\n===========17============\n')

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
print('\n===========BONUS============\n')

#[your code here]


f2 = np.empty((2,3,5), str)


for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        if d[i,j,k] == d_min:
                                f2[i,j,k] = "A"
                        elif d[i,j,k] > d_min and d[i,j,k] < d_mean:
                                f2[i,j,k] = "B"
                        elif d[i,j,k] == d_mean:
                                f2[i,j,k] = "C"
                        elif d[i,j,k] > d_mean and d[i,j,k] < d_max:
                                f2[i,j,k] = "D"
                        elif d[i,j,k] == d_max:
                                f2[i,j,k] = "E"

print("Array d:")
print(d)
print("\nArray f:")
print(f2)