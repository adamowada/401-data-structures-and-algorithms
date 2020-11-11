class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source in self.graph.keys():
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]
        if destination in self.graph.keys():
            self.graph[destination].append(source)
        else:
            self.graph[destination] = [source]

    def test_print(self):
        print(self.graph)

    def breadth_first(self, source):
        traversal = ''
        q = [source]
        travelled = []
        while q:
            temp = q.pop(0)
            travelled.append(temp)
            if str(temp) not in traversal:
                traversal = traversal + str(temp) + ', '
            for i in self.graph[temp]:
                if i not in travelled:
                    q.append(i)
        print(traversal)
        return traversal