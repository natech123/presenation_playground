import numpy as np
import time
from cython_calc import cython_calculation
from cython_adapted_calc import cython_calculation as cca

def random_heavy_calculation() -> None:
    a = np.random.randint(0,100)
    b = np.random.randint(0,100)
#   for run in range(n_runs):
    c = 0
    for run in range(100_000_000):
        c += (a*b)





if __name__ == "__main__":
    print("Start Calculation...")
    start = time.perf_counter()
    random_heavy_calculation()
    end = time.perf_counter()
    normal_time = end-start
    print(f"Calculation took {normal_time} seconds")

    print("Start Cython Calculation...")
    start = time.perf_counter()
    cython_calculation()
    end = time.perf_counter()
    cython_time = end - start
    print(f"Cython Calculation took {cython_time} seconds")
    print(f"Cython is {normal_time/cython_time} times faster")

    print("Start Adapted Cython Calculation...")
    start = time.perf_counter()
    cca()
    end = time.perf_counter()
    cython_adapted_time = end-start
    print(f"Cython Calculation took {cython_adapted_time} seconds")
    print(f"Cython with pre-defined dtypes is {normal_time/cython_adapted_time} times faster")
