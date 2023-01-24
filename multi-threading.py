import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(1)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    start=time.perf_counter()
    for i in range(10):
        thread_function(i)
    end=time.perf_counter()
    print(f"✅ Done in {end-start} seconds")

    start=time.perf_counter()
    print("Main    : before creating thread")
    jobs=[]
    for i in range(10):
        jobs.append(threading.Thread(target=thread_function, args=[(i,)]))

    print("Main    : before running thread")
    [x.start() for x in jobs]

    print("Main    : wait for the thread to finish")
    [x.join() for x in jobs]

    print("Main    : all done")
    end=time.perf_counter()
    print(f"✅ Done in {end-start} seconds")
