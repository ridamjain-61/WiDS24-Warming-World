# Part 1: Let's Matplot!!

---

### References/Links

1. [NumPy Random Legacy Documentation](https://numpy.org/doc/stable/reference/random/legacy.html)

---

### Problem

NumPy is also used widely for the various and commonly occurring mathematical and probabilistic distributions and sampling. Combined with PyPlot from Matplotlib, they provide a good API for data analysis and interpretation.

Your task would be to sample each of the below six distributions 10,000 times and then plot the frequency histograms for these samples. You need to create a single figure that has six subplots arranged as follows:

- 1 and 2 in the first row,
- 3 and 4 in the second row,
- 5 and 6 in the third row (i.e., a 3x2 layout).

For sampling each distribution, the input size should be set to 10,000. You can refer to the documentation link provided above to find the appropriate parameters to set in the NumPy functions.

#### Clarifications for Terminology:

1. **Parameters (a, b, scale, loc, etc.):** Statistical variables used to adjust the shape of the distributions (refer to the documentation for more details, as all these distributions are commonly used).
2. **Values:** The outputs obtained from the distributions. There will be 10,000 values for each distribution, which you need to scale as indicated.
3. **Range and Step:** These specify the x-axis of the plots and indicate the range of input. The histogram will show how many samples fall within each range.

---

### Distributions

1. **Beta**
   - Parameters: `a = 4, b = 20`
   - Scaling: Multiply the values by 100
   - X-axis: Range `-5 to 50`, Step `1`

2. **Exponential**
   - Parameters: `scale = 0.1`
   - Scaling: Multiply the values by 100
   - X-axis: Range `-1 to 50`, Step `1`

3. **Gamma**
   - Parameters: `scale = 0.1, shape = 2`
   - Scaling: Multiply the values by 100
   - X-axis: Range `-1 to 50`, Step `1`

4. **Laplace**
   - Parameters: `scale = 0.5, loc = 0`
   - Scaling: Multiply the values by 100
   - X-axis: Range `-1 to 50`, Step `1`

5. **Normal (Gaussian)**
   - Parameters: `loc = 0, scale = 3`
   - X-axis: Range `-10 to 11`, Step `1`

6. **Poisson**
   - Parameters: `lam = 3`
   - X-axis: Range `-1 to 11`, Step `1`
