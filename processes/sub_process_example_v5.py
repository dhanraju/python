'''This example demonstrates running two processes independently.

Each process runs same method with different sleep time.
Also wait for all the processes to be terminated.
How to run: python sub_process_example_v4.py
'''

import multiprocessing
import time

def singleMethod(sleep_time_secs):
    """Process 1 to run."""
    print("Inside singleMethod with sleep for %d secs." % sleep_time_secs)
    # Just sleep for 5 secs.
    time.sleep(sleep_time_secs)
    print("Sleep time %d secs completed." % sleep_time_secs)

def run_all_processes():
    """Run process 1 and process 2 and track status of all processes."""
    print("Running all processes.")
    print("Start Process 1.")
    proc1 = multiprocessing.Process(target=singleMethod, args=(5,))
    proc1.start()

    print("Start Process 2.")
    proc2 = multiprocessing.Process(target=singleMethod, args=(3,))
    proc2.start()

    print("Check processes status.")
    while proc1.is_alive() or proc2.is_alive():
        # print the status of proc1 and proc2 util both are terminated.
        if proc1.is_alive():
            if proc2.is_alive():
                print("proc1 is alive. proc2 is alive.")
            else:
                print("proc1 is still Alive. proc2 is Terminated!")
        elif proc2.is_alive():
            print("proc1 is Terminated. proc2 is still Alive!")

    print("All processes are terminated.")


if __name__ == '__main__':
    run_all_processes()
    print("All processes Ran.")
