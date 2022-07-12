## here the idea would be to split the data in as many chunks as there are processes
## NB : this is not necessarily the most efficient solution, but it does work.


def get_data(N,nb_processes):
    data = [ [] for i in range(nb_processes)] ## data is composed of as may sub-lists as thre are processes

    for i in range(N):    
        data[ i%(nb_processes) ].append( i )
        ## here, my trick is to use the % operator.
        ## for instance for 2 processes
        ## eg, if i is 3, then i%2 == 1 -> goes to sublist 1
        ##     if i is 4, then i%2 == 0 -> goes to sublist 0
    return data

## let's test it out: 
## say we have 10 points, and 2 processes:
N = 10
nb_processes = 2
data = get_data(N,nb_processes)
print( data )

## then the task is to apply `f2` to a set of points:
def f2(i):
    x = a+i*dx
    return x ** 2 - x

def task(data):
    s = 0
    for d in data:
        s+= f2(d)
    return s

## test it on our test data 
print( task( data[0] ) , task( data[1] ) )
#let's work outside the function and focus on the main loop:
a=0
b=2
N=2*10**7
dx = (b - a) / N

print("no multiprocessing")
%time list( map(task, data) )

## with 1 process it should take ~4seconds
for NP in [1,2,4,8]:
    print(NP)
    with mp.Pool(NP) as pool :
        data = get_data( N, NP )
        %time  pool.map(task, data)
