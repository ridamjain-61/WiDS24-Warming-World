# Part 2: NumPy in some Depth!!

---

### References/Links

1. [Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)  
2. [Sorting](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)  
3. [Matrix Operations](https://towardsdatascience.com/top-10-matrix-operations-in-numpy-with-examples-d761448cb7a8)  
4. [Padding](https://numpy.org/doc/stable/reference/generated/numpy.pad.html)  

---

### Problem

**CAUTION:**

**Avoid using loops as much as possible, use inbuilt functions only if possible**

Your friend Rockstar is too good at coding and playing with arrays, but you know that Rockstar only knows C programming language, while you are comfortable with Python. You want to show your friend that there are faster ways of array and matrix operations using vectorization. Using the power of `numpy`, you challenge your friend for the title of "Coding God."

You are given a CSV file (`matrix.csv`) containing a 2D matrix. You must read this file, convert it to a NumPy array, and perform the following operations.

---

### Given Matrix (matrix.csv)

The given matrix:
5,5,84,3,9 <br>
6,11,1,55,58 <br>
1,20,48,12,36 <br>
8,4,41,93,98 <br>
6,17,64,0,13 <br>

All expected outputs are given for this input matrix. Do not hardcode the outputs, otherwise
they will fail for almost all other matrices!

### Task 1:
Print only the elements that belong to the upper diagonal matrix (including the diagonal
elements) in column-wise fashion.

Expected output (present in task1.txt):
5 <br>
5 11 <br>
84 1 48 <br>
3 55 12 93 <br>
9 58 36 98 13 <br>

### Task 2:
Print mean, median and standard deviation (all along x-axis), determinant and inverse of the
matrix. You need to print the inverse if the determinant is non-zero. If the determinant is
zero, there is pseudo-inverse in numpy (Moore Penrose Pseudo Inverse) which needs to be
printed instead. For the standard deviation, determinant and inverse, keep the precision
as 2 decimals (check the "around" function in numpy).

Expected output (present in task2.txt):
[ 5.2 11.4 47.6 32.6 42.8] <br>
[ 6. 11. 48. 12. 36.] <br>
[ 2.32  6.34 27.6  36.09 32.73] <br>
[[-0.58 -0.53 -0.26  0.37  0.74] <br>
 [ 0.23  0.29  0.08 -0.19 -0.24] <br>
 [ 0.05  0.03  0.01 -0.02 -0.05] <br>
 [ 0.32  0.34  0.06 -0.21 -0.34] <br>
 [-0.29 -0.31 -0.05  0.2   0.29]] <br>

 ### Task 3:
 Print the following:
(a) original matrix sorted along vertical
(b) original matrix sorted along horizontal
(c) original matrix after flattening and sorting

The first output matrix should correspond to sorting along vertical, then along horizontal
and then the sorted flattened matrix. Each output should appear in a new line. It is fine
if one output takes multiple lines.

Expected output (present in task3.txt):
[[ 1  4  1  0  9] <br>
 [ 5  5 41  3 13] <br>
 [ 6 11 48 12 36] <br>
 [ 6 17 64 55 58] <br>
 [ 8 20 84 93 98]] <br>
[[ 3  5  5  9 84] <br>
 [ 1  6 11 55 58] <br>
 [ 1 12 20 36 48] <br>
 [ 4  8 41 93 98] <br>
 [ 0  6 13 17 64]] <br>
[ 0  1  1  3  4  5  5  6  6  8  9 11 12 13 17 20 36 41 48 55 58 64 84 93
 98]  

### Optional:
These two tasks are slightly more involved and are only for additional learning and reference.

### Task 4:
Flatten the 2-D array into 1-D array, print list of unique elements of the array in sorted order
with their respective frequencies in the next line, and report (print) the frequency of the
second largest element in the next line. For this task, you should use only numpy operations,
and no loops.

Expected output (present in task4.txt):
[ 0  1  1  3  4  5  5  6  6  8  9 11 12 13 17 20 36 41 48 55 58 64 84 93 98] <br>
[1 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]


### Task 5:
You will be given an integer "n" and you 
need to pad (with value 0), in top, bottom, right and left, which will lead to an increase in
the row and column size by 2 * n. Essentially, this means that if you have a matrix of size
N x M, and you want to pad the matrix with dimension "n" and value "0", the matrix would be
changed to size (n + N + n) x (n + M + n), where the n top and n bottom rows, as well as n left
and n right columns will be 0. The matrix would be at the center, and will still be of size
N x M. 

Expected output (present in task5.txt):
[[ 0  0  0  0  0  0  0  0  0] <br>
 [ 0  0  0  0  0  0  0  0  0] <br>
 [ 0  0  5  5 84  3  9  0  0] <br>
 [ 0  0  6 11  1 55 58  0  0] <br>
 [ 0  0  1 20 48 12 36  0  0] <br>
 [ 0  0  8  4 41 93 98  0  0] <br>
 [ 0  0  6 17 64  0 13  0  0] <br>
 [ 0  0  0  0  0  0  0  0  0] <br>
 [ 0  0  0  0  0  0  0  0  0]] <br>
