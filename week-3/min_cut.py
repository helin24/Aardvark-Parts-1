import random
import copy

def min_cut(graph):
    return

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
            single_min = self.single_min_cut()
            print "single min is %s" % (single_min)
            min_so_far = min(min_so_far, single_min)
        return min_so_far

    def single_min_cut(self):
        assoc_arr = copy.deepcopy(self.assoc_arr)

        while len(assoc_arr) > 2:
            current_pair = random.choice(self.all_edges(assoc_arr))
#            print current_pair
            merged_edges = assoc_arr[current_pair[0]]

            merged_edges.extend(assoc_arr[current_pair[1]])
            external_edges = []
            for edge in merged_edges:
                if edge != current_pair[0] and edge != current_pair[1]:
                    external_edges.append(edge)
            
            combined_nodes = []
            combined_nodes.extend(list(current_pair[0]))
            combined_nodes.extend(list(current_pair[1]))
            new_node = tuple(combined_nodes)
            assoc_arr[new_node] = external_edges
   
            for edge in set(external_edges):
                for i in range(0, len(assoc_arr[edge])):
                    if assoc_arr[edge][i] in [current_pair[0], current_pair[1]]:
                        assoc_arr[edge][i] = new_node

            assoc_arr.pop(current_pair[0], None)
            assoc_arr.pop(current_pair[1], None)

#            print assoc_arr

        return len(assoc_arr[new_node])
           
    def num_edges(self):
        total = 0
        for node in self.assoc_arr:
            total += len(self.assoc_arr[node])
        return total

    def all_edges(self, assoc_arr):
        edges = []
        for value in assoc_arr:
            for partner in assoc_arr[value]:
                edges.append([value, partner])
#        print "there are currently %s edges" % (len(edges))
        return list(edges)


# answer to problem given in kargerMinCut.txt is 17

graph = Graph('kargerMinCut.txt')
print graph.min_cut(20)

