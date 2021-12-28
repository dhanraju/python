'''Multi threading priority queue.'''
#!/usr/bin/python

import Queue
import threading
import time

EXITFLAG = 0

class MyThread(threading.Thread):
    '''Thread class.'''
    def __init__(self, t_id, name, que):
        threading.Thread.__init__(self)
        self.t_id = t_id
        self.name = name
        self.que = que
    def run(self):
        '''Run method.'''
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

def process_data(thread_name, que):
    '''Process data.'''
    while not EXITFLAG:
        QUEUELOCK.acquire()
        if not WORKQUEUE.empty():
            data = que.get()
            QUEUELOCK.release()
            print("%s processing %s" % (thread_name, data))
        else:
            QUEUELOCK.release()
        time.sleep(1)


if __name__ == '__main__':
    THREADLIST = ["Thread-1", "Thread-2", "Thread-3"]
    NAMELIST = ["One", "Two", "Three", "Four", "Five"]
    QUEUELOCK = threading.Lock()
    WORKQUEUE = Queue.Queue(10)
    THREADS = []
    THREAD_ID = 1

    # Create new THREADS
    for t_name in THREADLIST:
        thread = MyThread(THREAD_ID, t_name, WORKQUEUE)
        thread.start()
        THREADS.append(thread)
        THREAD_ID += 1

    # Fill the queue
    QUEUELOCK.acquire()
    for word in NAMELIST:
        WORKQUEUE.put(word)
    QUEUELOCK.release()

    # Wait for queue to empty
    while not WORKQUEUE.empty():
        pass

    # Notify THREADS it's time to exit
    EXITFLAG = 1

    # Wait for all THREADS to complete
    for t in THREADS:
        t.join()
    print("Exiting Main Thread")

#pylint: disable=pointless-string-statement
'''
OUPUT:
$ python multi_th_priority_queue.py
Starting Thread-1
Starting Thread-2
Starting Thread-3
Thread-3 processing One
Thread-1 processing Two
Thread-2 processing Three
Thread-3 processing Four
Thread-2 processing Five
Exiting Thread-1
Exiting Thread-3
Exiting Thread-2
Exiting Main Thread
'''
