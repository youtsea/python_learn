import heapq


class PriorityQueue(object):
    """docstring for PriorityQueue"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if len(self._queue) == 0:
            return None
        return heapq.heappop(self._queue)[-1]


class Item(object):
    """docstring for Item"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item(%s)' % self.name


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print q.pop()
print q.pop()
print q.pop()
print q.pop()
print q.pop()
