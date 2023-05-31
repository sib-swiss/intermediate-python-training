import numpy as np

# The trick here is to convert all 'str' sequences to arrays once before
# we get into the double loop. Once we have done that, we can use the fast
# vectorized operation.

def compute_sequence_similarity_numpy(seqA  ,seqB):
    """Takes 2 numpy array."""
    
    # We check equality of each individual element with ==
    # and then mean() returns the fraction of element with were equal.
    return (seqA == seqB).mean()


def compute_sequence_similarity_mat_numpy(lseq):
    # Compute similarity between all sequence pairs.
    sim = np.zeros((len(lseq), len(lseq)))
    
    # Create a version of lseq which contains arrays instead of `str`.
    lseq_np = []
    for seq in lseq:
        lseq_np.append(np.array(list(seq)))
    
    for i,s1 in enumerate(lseq_np):
        for j,s2 in enumerate(lseq_np):
            sim[i,j] = compute_sequence_similarity_numpy(s1 , s2)
    return sim


#toy dataset
test_lseq = ["AAA", "ATA", "TTA"]
print("native implementation")
print(compute_sequence_similarity_mat(test_lseq))

print("numpy implementation")
print(compute_sequence_similarity_mat_numpy(test_lseq))

## now we time:
%timeit -n 3 -r 7 _= compute_sequence_similarity_mat_numpy(lseq)
## from 270ms to 102ms -> x2.7 speedup!
