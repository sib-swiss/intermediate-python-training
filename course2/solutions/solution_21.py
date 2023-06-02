import numpy as np

# Native python version.
def integrate_f_native(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        x = a + i * dx
        s += x ** 2 - x
    return s * dx


# Numpy optimized version.
def integrate_f_numpy(a, b, N):
    dx = (b - a) / N
    X = np.arange(a, b, dx)  # Generate all points.
    
    # Now we can just use the vectorized operations:
    return (X**2 - X).sum() * dx

# Always check that you get (almost) the same result between the old and
# new version of the code.
print(integrate_f_native(0,2,100) ,'<->', integrate_f_numpy(0, 2, 100))

# Benchmark the native vs. numpy implementation.
print("Native python: ", end="")
native_time = %timeit -n 10 -r 3 -o integrate_f_native(0, 2, 1_000_000)

print("Numpy        : ", end="")
numpy_time = %timeit -n 10 -r 3 -o integrate_f_numpy (0, 2, 1_000_000)
print("Speed-up factor: {:.2f}".format(native_time.average / numpy_time.average))
