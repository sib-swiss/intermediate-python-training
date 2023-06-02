
# Important: if not already done, you must run
#
#   %load_ext Cython
# 
# In a cell of its own before running the code below.

%%cython --annotate 
# Put that at the top of the cell.

# Here we will use the cython tricks we have already seen. Mostly typing,
# python string can simply be typed 'str' for simplicity .

import numpy as np
cimport numpy as np
cimport cython
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

cdef DTYPE_t compute_sequence_similarity_cython( str seqA  , str seqB):
    """Compute similarity between 2 sequence as the fraction of
    position where they have the same value.
    """
    cdef int l = len(seqA)
    cdef DTYPE_t similar = 0
    for i in range(l):
        if seqA[i] == seqB[i]:
            similar += 1
    return similar/l

def sequence_similarity_mat_cython(lseq):
    # Here, typing a lseq as a list of string is quite tedious,
    # so we did not do it.
    cdef int l = len(lseq)
    cdef DTYPE_t[:, ::1] sim = np.empty((l, l), dtype=DTYPE)
    
    # Note: Enumerate does not translate well into C with cython, so use
    # "range()" instead.
    for i in range(l):
        for j in range(l):
            sim[i,j] = compute_sequence_similarity_cython( lseq[i] , lseq[j] )
    return sim


# Important: the code below must be run in a different cell from the
# code above.

# Verify that both implementations give the same result.
# Create a test dataset
lseq = [''.join(np.random.choice(list("ATGC"), 500)) for x in range(100)]
print(
    "Do both implementation give the same result?",
    np.allclose(
        sequence_similarity_mat(lseq), np.array(sequence_similarity_mat_cython(lseq))
    )
)
# Another possibility to check that both implementations give the same result
# is to use a small test dataset.
test_lseq = ["AAAGC", "ATAGG", "TTACC"]
print("Native implementation:\n", sequence_similarity_mat(test_lseq))
print("Cython implementation:\n", np.array(sequence_similarity_mat_cython(test_lseq)))


# Benchmark the 2 implementations.
lseq = [''.join(np.random.choice(list("ATGC"), 500)) for x in range(100)]
time_python = %timeit -n 10 -r 3 -o sequence_similarity_mat(lseq)
time_cython = %timeit -n 10 -r 3 -o np.array(sequence_similarity_mat_cython(lseq))
print(f"Speedup factor: {(time_python.average / time_cython.average):.2f}")
# from 270ms to 24ms -> x11 speedup!
