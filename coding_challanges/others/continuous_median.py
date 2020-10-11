from heapq import heappop, heappush


class ContinuousMedian:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.mean = None
    
    def add(self, value):
        self._add_value(value)
        self._balance_heaps()
        self._calc_mean()
        print(self.mean)

    def _add_value(self, value):
        if not self.maxheap:
            heappush(self.maxheap, -value)
        elif not self.minheap:
            heappush(self.minheap, value)
            self._swap_min_and_max_tops_if_necessary()
        elif -self.maxheap[0] < value < self.minheap[0] or value <= -self.maxheap[0]:
            heappush(self.maxheap, -value)
        else:
            heappush(self.minheap, value)

    def _balance_heaps(self):
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) + 1 < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))            

    def _calc_mean(self):
        if len(self.maxheap) == len(self.minheap):
            self.mean = (-self.maxheap[0] + self.minheap[0]) / 2.0
        else:
            self.mean = -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else self.minheap[0]
    
    def _swap_min_and_max_tops_if_necessary(self):
        if -self.maxheap[0] > self.minheap[0]:
            maxtop, mintop = heappop(self.maxheap), heappop(self.minheap)
            heappush(self.maxheap, -mintop)
            heappush(self.minheap, -maxtop)


if __name__ == '__main__':
    cm = ContinuousMedian()
    cm.add(5)
    cm.add(1)
    cm.add(6)
    cm.add(2)
    cm.add(2)
    cm.add(8)
    cm.add(-5)
