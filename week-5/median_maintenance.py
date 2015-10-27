from heap import Heap

def maintain_median(alist):
  m = MedianMaintainer()

  for num in alist:
    print "adding %s" % (num)
    print "new median is %s" % (m.add(num))
    raw_input()

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
    print "big heap size is %s and small heap size is %s" % (big_size, small_size)
    if big_size > small_size + 1:
      print "moving min from big to small"
      big_min = self.big_heap.get_min()
      self.small_heap.insert(big_min * -1)
    elif big_size < small_size:
      print "moving max from small to big"
      small_max = self.small_heap.get_min()
      self.big_heap.insert(small_max * -1)

    return self

  def update_median(self):
    print self.big_heap
    print self.small_heap
    if len(self.big_heap) > len(self.small_heap):
      print "big heap is bigger"
      self.median = self.big_heap.get_min_without_removing()
    else:
      print "small heap is bigger"
      self.median = (self.big_heap.get_min_without_removing() - self.small_heap.get_min_without_removing()) / 2.0

    return self.median

  
maintain_median([5,3,2,1,3,2,1,5,6,7,9])
