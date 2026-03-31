import random
from coinor.blimpy import LinkedList

import random

class PriorityQueue:
    '''This is a minimal priority queue'''    
    def __init__(self, priority = 'min'):
        self.KEY = 0
        self.PRIORITY = 1
        if priority == 'max':
            def compare(x, y):
                return x > y
            def compare_eq(x, y):
                return x >= y
        else:
            def compare(x, y):
                return x <= y
            def compare_eq(x, y):
                return x <= y
        self.compare = compare
        self.compare_eq = compare_eq
        self.Q = LinkedList()
        
    def isEmpty(self):
        return len(self.Q) == 0
                
    def pop(self, key = None):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        if self.isEmpty():
            raise KeyError('pop from an empty priority queue')
        if key == None:
            min_index = 0
            min_priority = self.Q[min_index][self.PRIORITY]
            for i in range(len(self.Q)):
                if self.Q[i][self.PRIORITY] < min_priority:
                    min_priority = self.Q[i][self.PRIORITY]
                    min_index = i
        else:
            for i in range(len(self.Q)):
                if self.Q[i][self.PRIORITY] == key:
                    min_index = i
        pop_key = self.Q[min_index][self.KEY]
        del self.Q[min_index]
        return pop_key       
            
    def peek(self):
        if self.isEmpty():
            raise KeyError('pop from an empty priority queue')
        min_index = 0
        min_priority = self.Q[min_index][self.PRIORITY]
        for i in range(len(self.Q)):
            if self.Q[i][self.PRIORITY] < min_priority:
                min_priority = self.Q[i][self.PRIORITY]
                min_index = i
        return self.Q[min_index][self.KEY]

    def get_priority(self, key):
        for i in range(len(self.Q)):
            if self.Q[i][self.KEY] == key:
                return self.Q[i][self.PRIORITY]
        raise KeyError("Key not found")

    def set_priority(self, key, priority):
        for i in range(len(self.Q)):
            if self.Q[i][self.KEY] == key:
                self.Q[i] = (key, priority)
                break

    def push(self, key, priority = 0):
        'Add to the heap or update the priority of an existing task'
        for i in range(len(self.Q)):
            if self.Q[i][self.KEY] == key:
                self.Q[i] = (key,priority)
                return
        self.Q.append((key, priority))

    def remove(self, key):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        for i in range(len(self.Q)):
            if self.Q[i][self.KEY] == key:
                del self.Q[i]
                break

    def __contains__(self, key):
        for i in range(len(self.Q)):
            if self.Q[i][self.KEY] == key:
                return True
        return False
    
def test_linked_list():
    random.seed(0)
    M = 100
    N = 1000
    aList = [int(random.random()*N) for i in range(M)]
    Q = PriorityQueue()
    for key in aList:
        Q.push(key, key)
    for i in range(M//2):
        Q.remove(aList[i])
    key = Q.pop()
    while not Q.isEmpty():
        oldkey = key
        key = Q.pop()
        assert(Q.compare_eq(oldkey, key))


def test_append_search():
    random.seed(0)
    o = LinkedList()
    for i in range(100):
        o.append(int(random.random()*1000))
    assert(238 in o)
    assert(10000 not in o)


