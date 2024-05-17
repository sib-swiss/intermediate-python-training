# Course 2 - Notebook 1 micro-exercise corrections
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 1
# ****************
# Look at the profile. Where should optimization efforts go first?
# What would be the effect of using our better implementation of the GC%
# computing function?

# Answer: 95% of the time is spent in `compute_sequence_similarity`
#
# The `compute_GC` function only represents a tiny fraction of the total time,
# so while optimizing it by replacing it with `compute_GC_better` does make
# function much faster, it only represents a tiny fraction of the overall time.
# Therefore `compute_GC` is not the main bottleneck in our code here.


# Original profiling.
"""
      505089 function calls in 18.820 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1    0.000    0.000   18.820   18.820 {built-in method builtins.exec}
      1    0.000    0.000   18.820   18.820 <string>:1(<module>)
      1    0.472    0.472   18.820   18.820 3941327906.py:50(main_script)
 250000   18.156    0.000   18.198    0.000 3941327906.py:37(compute_sequence_similarity)
    501    0.144    0.000    0.144    0.000 {built-in method builtins.print}
 250503    0.042    0.000    0.042    0.000 {built-in method builtins.len}
      1    0.000    0.000    0.004    0.004 3941327906.py:28(computeGC_dict)
   500    0.001    0.000    0.003    0.000 3941327906.py:1(computeGC_better)
   1000    0.003    0.000    0.003    0.000 {method 'count' of 'str' objects}
      1    0.002    0.002    0.003    0.003 3941327906.py:7(read_fasta)
      2    0.000    0.000    0.001    0.000 interactiveshell.py:275(_modified_open)
      2    0.001    0.000    0.001    0.000 {built-in method io.open}
      2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
   1000    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
   1000    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
      1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
     33    0.000    0.000    0.000    0.000 codecs.py:319(decode)
      1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
     33    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
    500    0.000    0.000    0.000    0.000 3941327906.py:59(<lambda>)
      1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
      1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
      1    0.000    0.000    0.000    0.000 codecs.py:186(__init__)
      1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
"""


# Profiling using the `computeGC_better()` function.
"""
      504589 function calls in 18.224 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000   18.224   18.224 {built-in method builtins.exec}
     1    0.000    0.000   18.224   18.224 <string>:1(<module>)
     1    0.450    0.450   18.224   18.224 1705322247.py:54(mainScript)
250000   17.575    0.000   17.616    0.000 1705322247.py:41(compute_sequence_similarity)
   501    0.122    0.000    0.122    0.000 {built-in method builtins.print}
251003    0.041    0.000    0.041    0.000 {built-in method builtins.len}
     1    0.000    0.000    0.033    0.033 1705322247.py:32(computeGC_dict)
   500    0.032    0.000    0.032    0.000 1705322247.py:22(computeGC)
     1    0.002    0.002    0.003    0.003 1705322247.py:1(read_fasta)
  1000    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
  1000    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
    33    0.000    0.000    0.000    0.000 codecs.py:319(decode)
     2    0.000    0.000    0.000    0.000 interactiveshell.py:275(_modified_open)
     2    0.000    0.000    0.000    0.000 {built-in method io.open}
     1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
    33    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
     2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
   500    0.000    0.000    0.000    0.000 1705322247.py:63(<lambda>)
     1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
     1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
     1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
     1    0.000    0.000    0.000    0.000 codecs.py:186(__init__)
     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
     1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
"""


# ******************************************************************************


# *****************************************************************************
# Micro-Exercise 2
# ****************
# 1. Find out the largest square matrix your RAM can reasonably accommodate.

# Let's first look at the relation between matrix size and memory usage.
import sys
import numpy as np
import matplotlib.pyplot as plt

Ns = [10, 100, 200, 500, 750, 1000, 2000, 5000, 7500, 10_000]
memory_usage = []
for n in Ns:
    c = np.zeros((n,) * 2)  # Create a NxN matrix filled with 0s
    memory_usage.append(
        sys.getsizeof(c) / (1024**2)
    )  # Get the memory size of that matrix.

plt.plot(Ns, memory_usage)
# -> From the plot, we see that the relation is of the 2nd order.

# Let's now compute the memory usage in Mb for 1 element of the matrix.
mem_usage = sys.getsizeof(np.zeros((1000, 1000))) / (1024**2)
mem_per_element = mem_usage / 1000**2
print("Memory usage per element:", mem_per_element)  # -> 7.62e-06 Mb

# Alternatively we can also get the size of an element by computing the
# difference in size between a numpy array of a element and of 2 elements.
# (the size of a numpy array with 1 element will correspond to the size of
#  a single element + the overhead of the array itself).
mem_per_element = (sys.getsizeof(np.zeros(2)) - sys.getsizeof(np.zeros(1))) / (1024**2)
print("Memory usage per element:", mem_per_element)  # -> 7.62e-06 Mb

# Knowing that we have say 32Gb of memory on our computer, we can now
# compute the max (uni-directional) dimension N of a matrix that we can
# store in 32 GB of RAM.
np.sqrt((1024 * 32) / mem_per_element)  # -> ~65'000 rows/columns.
# The result we obtain is that the max size N (number of rows/columns) of
# a matrix that fits in 32Gb of RAM is of about 65'000 x 65'000.


# Additional task:
# How could we modify the "main_script()" to make it less memory hungry?

# Solution: don't store the whole similarity matrix in memory (at step 4).
# Basically we could merge together steps 4 and 5, and write directly the
# output of each call to `compute_sequence_similarity()` without saving it
# to a matrix before writing it.

# Step 4: compute pairwise distance matrix.
with open(output_filename, "w") as OUT:
    print(",".join(ordered_seq), file=OUT)

    for i, s1 in enumerate(ordered_seq):
        for j, s2 in enumerate(ordered_seq):
            s = compute_sequence_similarity(Dseq[s1], Dseq[s2])
            print(s if j == 0 else ", " + s, file=OUT, end="")
        print("\n", file=OUT, end="")

# Another, smaller, optimization would be to not read the whole input file at
# once, but read only the lines necessary to compute the sequence similarity
# between 2 sequences at a time. This would however create an overhead in
# time spent reading the file, because we would probably go over it multiple
# times in order to compute all pairwise similarities.
# *****************************************************************************
