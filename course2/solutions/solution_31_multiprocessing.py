# In this exercise, the idea is to split the data in as many chunks as there
# are processes.
# NB : this is not necessarily the most efficient solution, but it does work.

import multiprocessing as mp

def get_data_parts(N,nb_processes):
    # Data is composed of as many sub-lists as there are processes.
    data = [ [] for i in range(nb_processes)]

    for i in range(N):    
        data[ i%(nb_processes) ].append( i )
        
        ## Here, the trick is that we use the % operator.
        ## For instance for 2 processes:
        ## * If i is 3, then i%2 == 1 -> goes to sublist 1.
        ## * If i is 4, then i%2 == 0 -> goes to sublist 0.
    return data

# Let's test it out: say we have 10 points, and 2 processes.
N = 10
nb_processes = 2
data_parts = get_data_parts(N, nb_processes)
print(data_parts)

# Then the task is to apply `f2` to a set of points:
def f2(i , a, dx):
    x = a + i * dx
    return x ** 2 - x

def task(data , a , dx):
    s = 0
    for d in data:
        s += f2(d , a , dx )
    return s*dx

#let's work outside the function and focus on the main loop:
a = 0
b = 2
N = 100#2 * 10**7
dx = (b - a) / N

data_parts = get_data_parts(N, 2)

# Test it on our test data.
S1 , S2 = task(data_parts[0],a,dx), task(data_parts[1],a,dx)
print("data parts results:",S1 , S2)
# of course at the end you want to sum
print("final result:", S1+S2)

# Now, to be applied with map, we will make a specific version of the task with a and dx fixed

task_specific = lambda data : task(data , a , dx)

print("no multiprocessing")
%time list(map(task_specific, data_parts))

# With 1 process it should take ~ 4 seconds.
for NP in [1,2,4,8]:
    print(NP)
    with mp.Pool(NP) as pool:
        data_parts = get_data_parts(N, NP)
        %time  pool.map(task_specific, data_parts)
