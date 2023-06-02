import numpy as np

# The basic idea of the numpy solution is to have the nucleotide sequences
# as numpy arrays instead of a string.
# By having the sequences in a numpy array, we can then use the ability of
# numpy to compare two arrays on an element-wise basis (seq_A == seq_B),
# which is a lot faster than iterating through the sequences to compare
# the nucleotides one position at a time.
#
# However, this solutions requires the conversion of the sequences from a
# string to a numpy array, which is a costly operation in terms of time. It
# is therefore important to convert all 'str' sequences to numpy arrays once
# before entering the double loop that calls sequence_similarity_numpy() -
# and not inside the loop where we would be converting multiple times the
# same sequence.

def sequence_similarity_numpy(seq_A, seq_B):
    """Compute similarity between 2 sequence as the fraction of
    positions where they have the same value.
    The input arguments must be numpy arrays.
    """
    # Check equality of each individual element with == and
    # then mean() returns the fraction of element with were equal.
    return (seq_A == seq_B).mean()


def sequence_similarity_mat_numpy(lseq):
    """Compute similarity between all sequence pairs."""
    # Create a version of lseq which contains numpy arrays instead of `str`.
    lseq_np = [np.array(list(s)) for s in lseq]
    
    sim_matrix = np.zeros((len(lseq),) * 2)
    for i, s1 in enumerate(lseq_np):
        for j, s2 in enumerate(lseq_np):
            sim_matrix[i, j] = sequence_similarity_numpy(s1, s2)
    return sim_matrix

# Verify that both implementations give the same result.
# Create a test dataset
lseq = [''.join(np.random.choice(list("ATGC"), 500)) for x in range(100)]

print(
    "Do both implementation give the same result?",
    np.allclose(
        sequence_similarity_mat(lseq), sequence_similarity_mat_numpy(lseq)
    )
)
# Another possibility to check that both implementations give the same result
# is to use a small test dataset.
test_lseq = ["AAAGC", "ATAGG", "TTACC"]
print("Native implementation:\n", sequence_similarity_mat(test_lseq))
print("Numpy implementation:\n", sequence_similarity_mat_numpy(test_lseq))


# Benchmark the 2 implementations.
time_python = %timeit -n 10 -r 3 -o sequence_similarity_mat(lseq)        # ~300 ms
time_numpy = %timeit -n 10 -r 3 -o sequence_similarity_mat_numpy(lseq)   # ~75 ms
print(f"Speedup factor: {(time_python.average / time_numpy.average):.2f}")
# from 300 to 75 ms -> x4 speedup!


# Note: we can further optimize the second function by computing only
# once each similarity between 2 sequences. This speeds things-up by
# another factor ~2!
def sequence_similarity_mat_numpy(lseq):
    """Compute similarity between all sequence pairs."""
    # Create a version of lseq which contains numpy arrays instead of `str`.
    lseq_np = [np.array(list(s)) for s in lseq]
    
    sim_matrix = np.zeros((len(lseq),) * 2)   
    for i, s1 in enumerate(lseq_np):
        for j, s2 in enumerate(lseq_np):
            if i <= j:
                sim_matrix[i, j] = sequence_similarity_numpy(s1, s2)
            else:
                sim_matrix[i, j] = sim_matrix[j, i]
    return sim_matrix

# Verify that both implementations give the same result.
print(
    "Do both implementation give the same result?",
    np.allclose(
        sequence_similarity_mat(lseq), sequence_similarity_mat_numpy(lseq)
    )
)

# Benchmark the 2 implementations.
time_python = %timeit -n 10 -r 3 -o sequence_similarity_mat(lseq)        # ~300 ms
time_numpy = %timeit -n 10 -r 3 -o sequence_similarity_mat_numpy(lseq)   # ~75 ms
print(f"Speedup factor: {(time_python.average / time_numpy.average):.2f}")
# from 300 to 40 ms -> x7.5 speedup!