'''Non synchronous threads.'''
#!/usr/bin/python

import threading
import time

EXITFLAG = 0

class MyThread(threading.Thread):
    '''My thread.'''
    def __init__(self, t_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = t_id
        self.name = name
        self.counter = counter
    def run(self):
        '''Run Thread.'''
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

def print_time(thread_name, counter, delay):
    '''Pring time.'''
    while counter:
        if EXITFLAG:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    # Create new threads
    THREAD1 = MyThread(1, "Thread-1", 1)
    THREAD2 = MyThread(2, "Thread-2", 2)

    # Start new Threads
    THREAD1.start()
    THREAD2.start()

    print("Exiting Main Thread")

#pylint: disable=pointless-string-statement
'''
OUTPUT:
$ python nonsync_threads.py
Starting Thread-1
Starting Thread-2
 Exiting Main Thread
Thread-1: Mon Sep 18 17:11:59 2017
 Thread-2: Mon Sep 18 17:11:59 2017
Exiting Thread-1
Thread-2: Mon Sep 18 17:12:04 2017
Exiting Thread-2
'''
