import numpy as np
def integrate_f_numpy(a, b, N):
    dx = (b - a) / N
    X = np.arange(a,b,dx) # Generate all points
    # now we can just use the vectorized operations:
    return ( X**2 - X ).sum() * dx

## always check you get (almost) the same result between the old and new version of the code 
print( integrate_f_native(0,2,100) ,'<->', integrate_f_numpy(0,2,100) )
%timeit -n 3 -r 7 _=integrate_f_native(0,2,1000000)
%timeit -n 3 -r 7 _=integrate_f_numpy (0,2,1000000)
