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

### Task 2:
Print mean, median and standard deviation (all along x-axis), determinant and inverse of the
matrix. You need to print the inverse if the determinant is non-zero. If the determinant is
zero, there is pseudo-inverse in numpy (Moore Penrose Pseudo Inverse) which needs to be
printed instead. For the standard deviation, determinant and inverse, keep the precision
as 2 decimals (check the "around" function in numpy).

Expected output (present in task2.txt):

 ### Task 3:
 Print the following:
(a) original matrix sorted along vertical
(b) original matrix sorted along horizontal
(c) original matrix after flattening and sorting

The first output matrix should correspond to sorting along vertical, then along horizontal
and then the sorted flattened matrix. Each output should appear in a new line. It is fine
if one output takes multiple lines.

Expected output (present in task3.txt): 

### Optional:
These two tasks are slightly more involved and are only for additional learning and reference.

### Task 4:
Flatten the 2-D array into 1-D array, print list of unique elements of the array in sorted order
with their respective frequencies in the next line, and report (print) the frequency of the
second largest element in the next line. For this task, you should use only numpy operations,
and no loops.

Expected output (present in task4.txt):

### Task 5:
You will be given an integer "n" and you 
need to pad (with value 0), in top, bottom, right and left, which will lead to an increase in
the row and column size by 2 * n. Essentially, this means that if you have a matrix of size
N x M, and you want to pad the matrix with dimension "n" and value "0", the matrix would be
changed to size (n + N + n) x (n + M + n), where the n top and n bottom rows, as well as n left
and n right columns will be 0. The matrix would be at the center, and will still be of size
N x M. 

Expected output (present in task5.txt):

### Check the expected_outputs folder for the expected outputs for each task
