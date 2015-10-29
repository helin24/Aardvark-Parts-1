from heap import Heap

def maintain_median(alist):
  m = MedianMaintainer()

  for num in alist:
    print "adding %s" % (num)
    print "new median is %s" % (m.add(num))

class MedianMaintainer:
  def __init__(self):
    self.big_heap = Heap()
    self.small_heap = Heap()
    self.median = None

  def add(self, value):
    if value >= self.median:
      self.big_heap.insert(value)
    else:
      self.small_heap.insert(value * -1)

    self.balance()
    self.update_median()

    return self.median

  def balance(self):
    big_size = len(self.big_heap)
    small_size = len(self.small_heap)
    if big_size > small_size + 1:
      big_min = self.big_heap.get_min()
      self.small_heap.insert(big_min * -1)
    elif big_size < small_size:
      small_max = self.small_heap.get_min()
      self.big_heap.insert(small_max * -1)

    return self

  def update_median(self):
    print self.big_heap
    print self.small_heap
    if len(self.big_heap) > len(self.small_heap):
      self.median = self.big_heap.get_min_without_removing()
    else:
      self.median = (self.big_heap.get_min_without_removing() - self.small_heap.get_min_without_removing()) / 2.0

    return self.median

  
maintain_median([4,5,6,7,8,9,10])
