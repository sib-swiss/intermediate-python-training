%%cython --annotate

# Here, instead of typing python string as `str``, we convert them to unicode
# first, according to recommendation from cython docs:
# https://cython.readthedocs.io/en/latest/src/tutorial/strings.html
# This should let us pass them as C character array (char*) to our function,
# to make it purer C.

import numpy as np
cimport numpy as np
cimport cython
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t


@cython.boundscheck(False) # Turn off bounds-checking for entire function
@cython.wraparound(False)  # Turn off negative index wrapping for entire function
cdef DTYPE_t compute_sequence_similarity_cython2( char* seqA  , char* seqB):
    """compute similarity between 2 sequence as the fraction of position where they have the same value"""
    cdef int l = len(seqA)
    cdef DTYPE_t similar = 0
    for i in range(l):
        if seqA[i] == seqB[i]:
            similar += 1
    return similar/l

@cython.boundscheck(False) # Turn off bounds-checking for entire function
@cython.wraparound(False)  # Turn off negative index wrapping for entire function
def compute_sequence_similarity_mat_cython2( Lseq ):
    # Here, typing a Lseq as a list of string is quite tedious, so I did not do it
    
    cdef int l = len(Lseq)
    cdef DTYPE_t[:, ::1] sim = np.empty((l, l), dtype=DTYPE)
    Lseq_unicode = [ x.encode('UTF-8') for x in Lseq ]

    for i in range(l):  # Enumerate does not translate well into C with cython. use range instead
        for j in range(l):
            sim[i,j] = compute_sequence_similarity_cython2( Lseq_unicode[i] , Lseq_unicode[j]  )

    return sim


# Toy dataset.
testLseq=["AAA","ATA","TTA"]
print("native implementation")
print( compute_sequence_similarity_mat( testLseq ) )
print("cython implementation")
print( np.array( compute_sequence_similarity_mat_cython2( testLseq ) )) # we have to cast the memory back to an array

# Now we time:
%timeit -n 3 -r 7 _=np.array( compute_sequence_similarity_mat_cython2(lseq) )
# from 270ms to 12.7ms -> x21 speedup!
