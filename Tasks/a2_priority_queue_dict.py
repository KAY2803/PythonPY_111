"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from Tasks.a1_my_queue import Queue


class PriorityQueue:
    def __init__(self):
        self.__priority_queue = {
            0: Queue(),
            1: Queue(),
            2: Queue(),
            3: Queue(),
            4: Queue(),
            5: Queue(),
            6: Queue(),
            7: Queue(),
            8: Queue(),
            9: Queue(),
            10: Queue()
          }

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """

        self.__priority_queue[priority].enqueue(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.__priority_queue:
            return None
        else:
            for i in range(11):
                if self.__priority_queue[i]:
                    return self.__priority_queue[i].dequeue()

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not self.__priority_queue:
            return None
        else:
            if self.__priority_queue.get(priority, None):
                return self.__priority_queue[priority].peek(ind)

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__priority_queue.clear()
        return None

    def print_(self):
        for k, v in self.__priority_queue.items():
            print(f'{k}: {v}')


priority_queue = PriorityQueue()
priority_queue.enqueue(3)
priority_queue.enqueue(4)
priority_queue.enqueue(6)
priority_queue.enqueue(5, 5)
priority_queue.enqueue(7, 5)
priority_queue.print_()
print(priority_queue.peek(1, 0))
