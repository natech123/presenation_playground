import numpy as np
import time
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

num_jobs = cpu_count()

# increase matrix size to simulate more data (Increase paralellism possibilities...)
# increase indivudual scalar values to increase cpu_bound (fibonacci) difficulty
# a = np.ones((1000,5)) * 20

# def fibonacci_of(n:int) -> int:
#     if n in {0, 1}:
#         return n
#     res = fibonacci_of(n - 1) + fibonacci_of(n - 2)
#     return res

# def element_wise_cpu_bound_compute(x: float) -> int:
#     return fibonacci_of(int(x))

# def transform(a: np.ndarray) -> np.ndarray:
#     res = np.array([element_wise_cpu_bound_compute(el) for el in a.flatten()]).reshape(a.shape)
#     return res

a = np.random.randint(0,20, 100_000_000, dtype="int64")


def random_calc(n:int) -> int:
    return n * (n-1)





if __name__ == '__main__':
    print("Starting single processing...")
    start = time.perf_counter()
    res = np.array(list(map(random_calc, tqdm(a))))
    end = time.perf_counter()
    original_time = end-start
    print(f"Done in {original_time} seconds \n")

    print("Starting multi processing...")
    start = time.perf_counter()
    with Pool(num_jobs) as p:
        a_split = np.array_split(a, num_jobs, axis=0)
        res_list = p.map(random_calc, a_split)
        res_multi = np.concatenate(res_list, axis=0)
    end = time.perf_counter()
    multi_time = end-start
    print(f"✅ Done in {multi_time} seconds using {num_jobs} processes")
    print(f"Multiprocessing with {num_jobs} cores is {original_time/multi_time} times faster!!!")

    assert np.allclose(res, res_multi)
