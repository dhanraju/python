"""Printing tasks queue problem.

Printing tasks to the shared printer in the computer science laboratory.
Scenario: On any average day about 10 students are working in the lab at any
given hour. These students typically print up to twice during that time, and
the length of these tasks ranges from 1 to 20 pages. The printer in the lab is
older, capable of processing 10 pages per minute of draft quality. The printer
could be switched to give better quality, but then it would produce only five
pages per minute. The slower printing speed could make student wait too long.
What page rate should be used?

Calculation:
If 10 students lab and each prints twice, then there are 20 print tasks per
hour on average. So, the time it takes to finish a task is calculated as:
20tasks/hr -> 20tasks/3600secs -> 1task/180secs

So, for every second the chance that a print task occurs between 1 and 180.
"""
import random
from queue import Queue


class Printer:
    """Tracks whether it has a current task.
    
    If it does, then it is busy and the amount of time needed can be computed
    from the number of pages in the task.
    """
    def __init__(self, ppm):
        """Initialize the pages per minute setting."""
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """Decrements the internal timer.
        
        And also sets the printer to idle if the task is completed.
        """
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        """Checks the current task is running or not."""
        if self.current_task is not None:
            return True
        return False

    def start_next(self, new_task):
        """Starts new task."""
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    """Represents a single task.
    
    When the task is created, a random number generator will provide a length
    from 1 to 20 pages.

    Each task need to keep a timestamp to be used for computing wait time. This
    timestamp will represent the time that the task was created and place in the printer queue.
    """
    def __init__(self, time):
        """Generate a random number between 1 and 21 for the given task."""
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        """Gets the time stamp of the given task."""
        return self.timestamp

    def get_pages(self):
        """Gets the number of pages performed by the task."""
        return self.pages

    def wait_time(self, current_time):
        """Calculates the wait time.
        
        i.e., the amount of time spent in the queue before printing begins.
        """
        return current_time - self.timestamp


def new_print_task():
    """Decides whether a new priting task has been created or not."""
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False


def simulation(num_seconds, pages_per_minute):
    """Set the total time and the pages per mintue for the printer."""
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    # For each second, check new task is created or not. If so, add it to the
    # queue with current_second as the timestamp. Then, check the printer is
    # not busy and the new task is waiting in the print queue. If so, remove
    # the next task from the print queue and assign it to the printer. Now,
    # append the waiting time for the next task to a list for later processing.
    for current_second in range(num_seconds):
        # Check if the new task is created or not.
        if new_print_task():
            # Add it to the queue with current_second as the timestamp.
            task = Task(current_second)
            print_queue.enqueue(task)
        # Check if the printer is not busy and a task is waiting.
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            # Remove the next task from the print queue and assign it to printer
            next_task = print_queue.dequeue()
            # Append the waiting time for the next task to a list for later
            # processing.
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()

    # Compute the average waiting time from the list of waiting times generated.
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining." % (
        average_wait, print_queue.size()
    ))


if __name__ == '__main__':
    # Send print requests from 10 students and number of pages per minute.
    for i in range(10):
        simulation(3600, 5)
