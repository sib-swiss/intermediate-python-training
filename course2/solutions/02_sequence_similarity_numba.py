from numba import jit

@jit(nopython=True)
def compute_sequence_similarity_numba(seqA  ,seqB):
    """compute similarity between 2 sequence as the fraction of position where they have the same value"""

    l = len(seqA)
    similar = 0
    for i in range(l):
        if seqA[i] == seqB[i]:
            similar += 1
    return similar/l

@jit(nopython=True)
def compute_sequence_similarity_Mat_numba(Lseq):
    # compute similarity between all sequence pair
    sim = np.zeros( ( len(Lseq),len(Lseq) ) )
    for i,s1 in enumerate(Lseq):
        for j,s2 in enumerate(Lseq):
            sim[i,j] = compute_sequence_similarity_numba( s1 , s2 )
    return sim


## if you run this function directly, you will get a warning of future deprecation pointing toward 
## this webpage: https://numba.readthedocs.io/en/stable/reference/deprecation.html#deprecation-of-reflection-for-list-and-set-types
## I followed the recommendation there to do a interfacing function
from numba.typed import List
def interface_numba_sequence_similarity( Lseq ):
    Lseq_typed = List()
    [Lseq_typed.append(x) for x in Lseq]
    return compute_sequence_similarity_Mat_numba(Lseq_typed)


#toy dataset
testLseq=["AAA","ATA","TTA"]
print("native implementation")
print( compute_sequence_similarity_Mat( testLseq ) )
print("numba implementation")
print( interface_numba_sequence_similarity( testLseq ) )

## now we time:
%timeit -n 3 -r 7 _=interface_numba_sequence_similarity(Lseq)
## well, it is actually slower... (~600ms, vs ~270ms for the native)
## sometimes numba is not able to work its magic
