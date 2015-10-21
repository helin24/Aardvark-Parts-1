class DirectedGraph:
    def __init__(self, txt_file):
        self.assoc_arr = {}
        self.reverse_arr = {}
        f = open(txt_file)

        for line in f:
            pass

        origin, dest, nl = line.split(' ')
        origin, dest = int(origin), int(dest)

        for num in range(1, origin + 1):
            self.assoc_arr[num] = {'dest': set(), 'explored': False, 'finished': False}
            self.reverse_arr[num] = {'dest': set(), 'explored': False, 'finished': False}


        f = open(txt_file)
        for line in f:
            origin, dest, nl = line.split(' ')
            origin, dest = int(origin), int(dest)

            self.assoc_arr[origin]['dest'].add(dest)
            self.reverse_arr[dest]['dest'].add(origin)


    def scc(self):
        print "starting scc"

        search = self.reverse_arr.keys()
        ordering = []

        while search:
            current_vertex = search.pop()
            # print "searching %s" % (current_vertex)

            if self.reverse_arr[current_vertex]['finished']:
                continue

            self.reverse_arr[current_vertex]['explored'] = True

            finished = True
            add_to_search = []

            for dest in self.reverse_arr[current_vertex]['dest']:
                if not self.reverse_arr[dest]['explored']:
                    finished = False
                    add_to_search.append(dest)

            if finished:
                ordering.append(current_vertex)
                self.reverse_arr[current_vertex]['finished'] = True
                # print "%s finished in reverse_arr" % (current_vertex)
            else:
                search.append(current_vertex)

            search.extend(add_to_search)

            length = len(ordering)
            if length % 1000 == 0:
                print "ordering has %s elements" % length

        print "starting grouping"

        groups = []
        current_group = []
        total_count = 0

        while ordering:
            search = [ordering.pop()]
            # print "searching %s" % (current_vertex)


            while search:
                current_vertex = search.pop()

                if self.assoc_arr[current_vertex]['finished']:
                    continue

                self.assoc_arr[current_vertex]['explored'] = True

                finished = True
                add_to_search = []

                for dest in self.assoc_arr[current_vertex]['dest']:
                    if not self.assoc_arr[dest]['explored']:
                        finished = False
                        add_to_search.append(dest)
                if finished:
                    self.assoc_arr[current_vertex]['finished'] = True
                    current_group.append(current_vertex)
                    # print "%s finished" % (current_vertex)
                else:
                    search.append(current_vertex)

                search.extend(add_to_search)

            # # for seeing components of each group
            # if current_group:
            #     groups.append(current_group)
            # current_group = []
            # return groups

            # for getting count of elements in group
            if current_group:
                groups.append(len(current_group))
                total_count += len(current_group)
                print "adding group currently %s elements grouped" % (total_count)
            current_group = []

        groups.sort()
        return groups[len(groups) - 5:]

# dg = DirectedGraph('SmallSCC.txt')
dg = DirectedGraph('SCC.txt')
print dg.scc()