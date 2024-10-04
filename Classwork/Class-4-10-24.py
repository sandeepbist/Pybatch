#write a function that takes one input parameter n and calculates a = n * 10,for all values between 0 to n
import time
n = 100
ns = [12341234,1245123,12412314,1241241]
def eva(n):
    for i in range(0,n):
        a = i * 10

# Estimate execution time of this function 

def wrapper(fun,*args,**kwargs): 
    def wrapped(*args,**kwargs):    
        starter = time.time()

        fun(n)

        ended = time.time()

        print(f"Execution time is {starter} and {ended}")
    wrapped(*args,**kwargs)
    return wrapped

# for n in ns:
#     wrapper(eva,n)    

wrapped_fn = wrapper(eva,n)
wrapped_fn(n)