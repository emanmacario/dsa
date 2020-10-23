# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.
# Hints: #22, #56, #63

from enum import Enum

class Animal(Enum):
    DOG = 1
    CAT = 2
    def __str__(self):
        return 'Dog' if self.value == 1 else 'Cat'

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Returns a string representation of the linked list
        s = ''
        tmp = self
        while tmp:
            s += f"{tmp.val}->"
            tmp = tmp.next
        s += 'NULL'
        return s

    @classmethod
    def from_list(cls, vals):
        # Creates a linked list given a list of values
        if not vals:
            return None
        nodes = [ListNode(val) for val in vals]
        for n1, n2 in zip(nodes, nodes[1:] + [None]):
            n1.next = n2
        return nodes[0]


class AnimalQueue:
    """
    A queue data structure for an animal shelter that
    supports enqueueing and dequeueing of both cats
    and dogs, denoted via characters Animal.CAT and Animal.DOG
    respectively 
    """
    def __init__(self):
        self.head = None

    def enqueue(self, animal):
        new = ListNode(animal)
        if not self.head:
            # Insert into empty queue
            self.head = self.tail = new
        else:
            # Add to end of queue
            self.tail.next = new
            self.tail = self.tail.next

    def dequeueAny(self):
        # Empty queue
        if not self.head:
            return None

        # Get head of queue and adjust head and tail pointers
        self.head = self.head.next
        if not self.head:
            self.tail = None

        return self.head.val

    def dequeueAnimal(self, animal):
        prev, curr = None, self.head
        while curr:
            if curr.val == animal:
                if prev is None:
                    # Dequeued node is head
                    self.head = self.head.next
                    # Check if tail is equal to head
                    if self.tail is curr:
                        self.tail = self.head
                else:
                    if self.tail is curr:
                        # Dequeued node is last node in queue
                        self.tail = prev
                        prev.next = None
                    else:
                        # Dequeued node is neither head nor tail
                        prev.next = curr.next         
                
                return curr.val

            prev, curr = curr, curr.next


    def dequeueDog(self):
        self.dequeueAnimal(Animal.DOG)

    def dequeueCat(self):
        self.dequeueAnimal(Animal.CAT)

    @classmethod
    def from_list(cls, animals):
        queue = AnimalQueue()
        for animal in animals:
            queue.enqueue(animal)

        return queue

    def __str__(self):
        return self.head.__str__()



if __name__ == "__main__":
    queue = AnimalQueue.from_list([Animal.CAT, Animal.DOG, Animal.DOG, Animal.CAT, Animal.DOG, Animal.CAT])
    print(queue)
    queue.dequeueDog()
    print(queue)
    queue.dequeueAny()
    print(queue)

