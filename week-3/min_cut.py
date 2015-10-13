import random
import copy
import time

class Graph:
    def __init__(self, filename):
        txt = open(filename)
        self.assoc_arr = {}
        for line in txt:
            values = line.split("\t")
            self.assoc_arr[values[0]] = values[1 : len(values) - 1]

    def min_cut(self, repetitions):
        min_so_far = self.num_edges()
        for i in range(repetitions):
            single_min = self.cut()
            print "single min is %s" % (single_min)
            min_so_far = min(min_so_far, single_min)
        return min_so_far

    def cut(self):
        assoc_arr = copy.deepcopy(self.assoc_arr)

        while len(assoc_arr) > 2:
            node_one, node_two = random.choice(self.all_edges(assoc_arr))
            # this should be improved because getting a list of all edges is time consuming
            # could modify to just choosing a random vertex and then a random edge - but then this would lower probability of getting min cut because vertices with fewer edges have equal probability of being merged?

            # this runs faster but not truly random
            # node_one = random.choice(assoc_arr.keys())
            # node_two = random.choice(assoc_arr[node_one])

            assoc_arr[node_one].extend(assoc_arr[node_two])
            assoc_arr[node_one] = [edge for edge in assoc_arr[node_one] if edge != node_one and edge != node_two]
   
            for edge in set(assoc_arr[node_one]):
                for i in range(0, len(assoc_arr[edge])):
                    if assoc_arr[edge][i] == node_two:
                        assoc_arr[edge][i] = node_one

            assoc_arr.pop(node_two, None)

        return len(assoc_arr[node_one])
           
    def num_edges(self):
        total = 0
        for node in self.assoc_arr:
            total += len(self.assoc_arr[node])
        return total

    def all_edges(self, assoc_arr):
        edges = []
        for value in assoc_arr:
            for partner in assoc_arr[value]:
                edges.append((value, partner))
        return list(edges)


# answer to problem given in kargerMinCut.txt is 17

graph = Graph('kargerMinCut.txt')
start_time = time.time()
print graph.min_cut(100)
print "---- %s  ---- " % (time.time() - start_time)

