# problem Link: https://www.geeksforgeeks.org/sorting-queue-without-extra-space/


from queue import Queue
import sys


def find_min_index(qe, sorted_index):
    min_index = -1
    min_value = sys.maxsize
    for i in range(qe.qsize()):
        cur = qe.queue[0]
        qe.get()

        if cur <= min_value and i <= sorted_index:
            min_index = i
            min_value = cur
        qe.put(cur)
    return min_index


def insert_min_to_rear(qe, min_index):
    min_value = None
    for i in range(qe.qsize()):
        cur = qe.queue[0]
        qe.get()

        if i != min_index:
            qe.put(cur)
        else:
            min_value = cur
    qe.put(min_value)


def sort_queue(qe):
    for i in range(q.qsize()):
        min_index = find_min_index(q, q.qsize()-1-i)
        insert_min_to_rear(q, min_index)


q = Queue(4)
q.put(30)
q.put(11)
q.put(15)
q.put(4)

sort_queue(q)

for j in range(q.qsize()):
    print(q.queue[0], end=" ")
    q.get()

