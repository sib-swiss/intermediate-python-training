import numpy as np
from numba import jit

@jit(nopython=True)
def sequence_similarity_numba(seq_A  ,seq_B):
    """Compute similarity between 2 sequence as the fraction of
    position where they have the same value.
    """
    l = len(seq_A)
    return sum([seq_A[i] == seq_B[i] for i in range(l)]) / l

@jit(nopython=True)
def sequence_similarity_mat_numba(lseq):
    # compute similarity between all sequence pair
    sim = np.zeros((len(lseq), len(lseq)))
    
    for i, s1 in enumerate(lseq):
        for j, s2 in enumerate(lseq):
            sim[i, j] = sequence_similarity_numba(s1, s2)
    return sim


# If we run the function `sequence_similarity_mat_numba()` directly, we
# get a warning of future deprecation pointing toward this webpage:
# https://numba.readthedocs.io/en/stable/reference/deprecation.html#deprecation-of-reflection-for-list-and-set-types
# Following the recommendation, let's write an interfacing function.
from numba.typed import List
def interface_numba_sequence_similarity(lseq):
    typed_a = List()
    [typed_a.append(x) for x in lseq]
    return sequence_similarity_mat_numba(typed_a)


# Verify that both implementations give the same result.
# Create a test dataset
lseq = [''.join(np.random.choice(list("ATGC"), 500)) for x in range(100)]
print(
    "Do both implementation give the same result?",
    np.allclose(
        sequence_similarity_mat(lseq), interface_numba_sequence_similarity(lseq)
    )
)
# Another possibility to check that both implementations give the same result
# is to use a small test dataset.
test_lseq = ["AAAGC", "ATAGG", "TTACC"]
print("Native implementation:\n", sequence_similarity_mat(test_lseq))
print("Numba implementation:\n", interface_numba_sequence_similarity(test_lseq))


# Benchmark the 2 implementations.
time_python = %timeit -n 10 -r 3 -o sequence_similarity_mat(lseq)             # ~300 ms
time_numba = %timeit -n 10 -r 3 -o interface_numba_sequence_similarity(lseq)  # ~500 ms
print(f"Speedup factor: {(time_python.average / time_numba.average):.2f}")
# well, in this case, using numba actually makes the code slower...
# sometimes numba is not able to work its magic.
