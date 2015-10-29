import math

class Heap:
    def __init__(self, alist=[]):
        self.heap = []
        for num in alist:
            self.insert(num)
            

    def __str__(self):
        pointer = 1
        size = len(self.heap)
        string = ""
        if size == 0:
            return string
        levels = math.ceil(math.log(size, 2)) # max index of level
        max_width = (2**(levels) + 1) * 5
        
        while pointer <= size:
            level = math.floor(math.log(pointer, 2))
            remaining = 2**level
            step = ' ' * int(max_width / (remaining + 1))

            while remaining and pointer <= size:
                string += step + str(self.heap[pointer - 1])
                pointer += 1
                remaining -= 1

            string += "\n\n"

        return string

    
    def __len__(self):
        return len(self.heap)
    

    def insert(self, number):
        self.heap.append(number)
        index = len(self.heap) - 1

        if index == 0:
            return self

        parent = self.heap[(index - 1) / 2]
        while number < parent and index > 0:
            self.heap[index] = parent
            index = (index - 1) / 2
            self.heap[index] = number
            parent = self.heap[(index - 1) / 2]

        return self


    def get_min_without_removing(self):
        return self.heap[0]


    def get_min(self):
        removed = self.heap[0]

        sub = self.heap.pop()
        index = 0

        if len(self.heap) == 1:
            self.heap[index] = sub

        while len(self.heap) > index * 2 + 1:
            left = self.heap[index * 2 + 1]
            right = self.heap[(index + 1) * 2] if len(self.heap) > (index + 1) * 2 else None

            if right:
                if sub > left or sub > right:
                    if left <= right:
                        self.heap[index] = left
                        index = index * 2 + 1
                        self.heap[index] = sub
                    else:
                        self.heap[index] = right
                        index = (index + 1) * 2
                        self.heap[index] = sub
            else:
                if sub >= left:
                    self.heap[index] = left
                    self.heap[index * 2 + 1] = sub
                    break
            print index

        return removed


# h = Heap([1,5,8,2, 3, 1, 4])
# print h
# h.insert(0)
# print h
# print h.get_min()
# print h
