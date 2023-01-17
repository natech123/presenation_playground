import threading
import time

def thread_function(name):
    print("Thread %s: starting", name)
    time.sleep(2)
    print("Thread %s: finishing", name)

if __name__ == "__main__":

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
