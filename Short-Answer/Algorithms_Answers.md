#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

    ```python
    a)  a = 0
        while (a < n * n * n):
        a = a + n * n
    ```
    - This runtime of this operation is a linear one because the number of operations grows in direct proportion to the input size


b) sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
    - 0(2^n)
    - This run time of this operation is an exponential one because the number of operations grows as a function of its input size


c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)

    - This run time of this operation is a quadratic one


## Exercise II


