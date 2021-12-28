'''Synchronous THREADS.'''
#!/usr/bin/python

import threading
import time

class MyThread(threading.Thread):
    '''My Thread.'''
    def __init__(self, t_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = t_id
        self.name = name
        self.counter = counter
    def run(self):
        '''Run thread.'''
        print("Starting " + self.name)
        # Get lock to synchronize THREADS
        THREADLOCK.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        THREADLOCK.release()

def print_time(thread_name, delay, counter):
    '''Print time.'''
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    THREADLOCK = threading.Lock()
    THREADS = []

    # Create new THREADS
    THREAD1 = MyThread(1, "Thread-1", 1)
    THREAD2 = MyThread(2, "Thread-2", 2)

    # Start new Threads
    THREAD1.start()
    THREAD2.start()

    # Add THREADS to thread list
    THREADS.append(THREAD1)
    THREADS.append(THREAD2)

    # Wait for all THREADS to complete
    for t in THREADS:
        t.join()
    print("Exiting Main Thread")

#pylint: disable=pointless-string-statement
'''
OUTPUT:
$ python sync_THREADS.py Starting Thread-1
 Starting Thread-2
Thread-1: Mon Sep 18 17:13:06 2017
Thread-1: Mon Sep 18 17:13:07 2017
Thread-1: Mon Sep 18 17:13:08 2017
Thread-2: Mon Sep 18 17:13:10 2017
Thread-2: Mon Sep 18 17:13:12 2017
Thread-2: Mon Sep 18 17:13:14 2017
Exiting Main Thread
'''
