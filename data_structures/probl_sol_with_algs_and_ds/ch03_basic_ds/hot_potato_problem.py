"""Hot potato problem.

Let's consider the children's game Hot Potato. In this game, children line up
in a circle and pass an item from neighbour to neighbour as fast as they can.
At a certain point in the game, the action is stopped and the child who has the
item (the potato) is removed from the circle. Play continues until only one
child is left.
"""

from queue import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()
    # Add list of name in to the queue.
    for name in name_list:
        sim_queue.enqueue(name)
    # Until only one name is left, pass the item from one name to the other.
    while sim_queue.size() > 1:
        # Run through the names in the queue until reaches the number.
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        # Remove the name after the number of iterations.
        sim_queue.dequeue()
    # Return the last name.
    return sim_queue.dequeue()


if __name__ == '__main__':
    names_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    number = 7
    print(hot_potato(names_list, number))
