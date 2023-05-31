%%cython --annotate 
# put that at the cell's top

# Here we will use the cython tricks we have already seen.
# mostly typing 
# python string can simply be typed 'str' for simplicity .

import numpy as np
cimport numpy as np
cimport cython
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

cdef DTYPE_t compute_sequence_similarity_cython( str seqA  , str seqB):
    """compute similarity between 2 sequence as the fraction of position where they have the same value"""
    cdef int l = len(seqA)
    cdef DTYPE_t similar = 0
    for i in range(l):
        if seqA[i] == seqB[i]:
            similar += 1
    return similar/l

def compute_sequence_similarity_mat_cython( Lseq ):
    # Here, typing a Lseq as a list of string is quite tedious, so I did not do it
    
    cdef int l = len(Lseq)
    cdef DTYPE_t[:, ::1] sim = np.empty((l, l), dtype=DTYPE)
    
    for i in range(l):  # Enumerate does not translate well into C with cython. use range instead
        for j in range(l):
            sim[i,j] = compute_sequence_similarity_cython( Lseq[i] , Lseq[j] )
    return sim


# Toy dataset
testLseq=["AAA","ATA","TTA"]
print("native implementation")
print( compute_sequence_similarity_mat( testLseq ) )
print("cython implementation")
print( np.array( compute_sequence_similarity_mat_cython( testLseq ) )) # we have to cast the memory back to an array

# Now we time:
%timeit -n 3 -r 7 _=np.array( compute_sequence_similarity_mat_cython(lseq) )
# from 270ms to 24ms -> x11 speedup!
