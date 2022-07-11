import numpy as np
## so the trick here is to convert all 'str' sequences to arrays once before we get into the double loop
## once we have done that, we can use the fast vectorized operation:

def compute_sequence_similarity_numpy(seqA  ,seqB):
    """takes 2 numpy array"""
    ## we check equality of each individual element with ==
    # and then mean() returns the fraction of element with were equal
    return (seqA == seqB).mean()


def compute_sequence_similarity_Mat_numpy(Lseq):
    # compute similarity between all sequence pair
    sim = np.zeros( ( len(Lseq),len(Lseq) ) )
    
    # we create a version of Lseq which contains arrays instead of str
    Lseq_np = []
    for seq in Lseq:
        Lseq_np.append( np.array(list(seq)) )
    
    for i,s1 in enumerate(Lseq_np):
        for j,s2 in enumerate(Lseq_np):
            sim[i,j] = compute_sequence_similarity_numpy( s1 , s2 )
    return sim


#toy dataset
testLseq=["AAA","ATA","TTA"]
print("native implementation")
print( compute_sequence_similarity_Mat( testLseq ) )
print("numpy implementation")
print( compute_sequence_similarity_Mat_numpy( testLseq ) )

## now we time:
%timeit -n 3 -r 7 _=compute_sequence_similarity_Mat_numpy(Lseq)
## from 270ms to 102ms -> x2.7 speedup!
