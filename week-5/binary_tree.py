import math

class BinaryTree:
    def __init__(self, alist=[]):
        self.rep = []
        for number in alist:
            self.insert(number)
        # can augment to have size metric on each node


    def __str__(self):
        pointer = 1
        size = len(self.rep)
        string = ""
        levels = math.ceil(math.log(size, 2))
        max_width = (2**(levels) + 1) * 5

        while pointer <= size:
            level = math.floor(math.log(pointer, 2))
            remaining = 2** level
            step = ' ' * int(max_width / (remaining + 1))

            while remaining and pointer <= size:
                string += step + str(self.rep[pointer - 1])
                pointer += 1
                remaining -= 1

            string += "\n\n"

        return string


    def min(self):
        index = 0
        min_num = None
        
        while index < len(self.rep) and self.rep[index] != None:
            min_num = self.rep[index]
            index = 2 * index + 1

        return min_num


    def max(self):
        index = 0
        max_num = None

        while index < len(self.rep) and self.rep[index] != None:
            max_num = self.rep[index]
            index = 2 * (index + 1)

        return max_num


    def predecessor(self, sub):
        pass

    def successor(self, sub):
        pass

    def insert(self, number):
        index = 0

        if len(self.rep) == 0:
            self.rep.append(number)
            return index
        
        while index < len(self.rep) and self.rep[index]:
            if self.rep[index] >= number:
                index = 2 * index + 1
            else:
                index = 2 * (index + 1)

        if index > len(self.rep):
            self.rep.extend([None] * (index - len(self.rep)))
            self.rep.append(number)
        elif index == len(self.rep):
            self.rep.append(number)
        else:
            self.rep[index] = number

        return index


    def delete(self, number):
        pass

    def select(self, rank):
        pass

    def rank(self, value):
        pass


t = BinaryTree([5,2,7,3,4])
print t
t.insert(8)
print t
t.insert(6)
print t
print t.min()
t.insert(0)
print t.min()
print t.max()
