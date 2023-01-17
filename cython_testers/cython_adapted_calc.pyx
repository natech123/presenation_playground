
import numpy as np

def cython_calculation() -> None:
    cdef long a = np.random.randint(0,100)
    cdef long b = np.random.randint(0,100)
#   for run in range(n_runs):
    cdef long c = 0
    for run in range(100_000_000):
        c += (a*b)




# if __name__ == "__main__":
#   print("Start Calculation...")
#   start = time.perf_counter()
#   cython_calculation()
#   end = time.perf_counter()
#   print(f"Calculation took {end-start} seconds")
