import json

class Algorithm:

    #Necessary data
    start_node = 0
    end_node = 0

    nodes = set()
    edges = []

    result = dict()

    #Get data for algorithm
    def __init__(self, file):
        json_file = open(file)
        x = json.load(json_file)

        self.start_node, self.end_node =x[0]
        self.edges = x[1:]

        for edge in self.edges:
            if edge[0] not in self.nodes:
                self.nodes.add(edge[0])

            if edge[1] not in self.nodes:
                self.nodes.add(edge[1])

        for node in self.nodes:
            self.result[node] = (float('inf'), -1)

        self.result[self.start_node] = (0, -1)

    #Calcule wages and paths to all nodes
    def relax(self):
        for _ in range(len(self.nodes)-1):
            changed = False
            for edge in self.edges:
                if self.result[edge[0]][0] + edge[2] < self.result[edge[1]][0]:
                    changed = True
                    self.result[edge[1]] = (self.result[edge[0]][0] + edge[2], edge[0])
            if(changed == False):
                break

    #Check if conditions are satisfied
    def isSatisfied(self):
        for edge in self.edges:
            if self.result[edge[1]][0] > self.result[edge[0]][0] + edge[2]:
                return False
        return True

    #Print results
    #if end_node is not equal any node, print overall result
    #otherwise, print wage and path to this node
    def print(self):
        if self.end_node in self.nodes:
            print("Start node:", self.start_node)
            print("End node:", self.end_node)
            print("Wage:", self.result[self.end_node][0])

            curr_node = self.end_node
            way = str(curr_node)
            while self.result[curr_node][1] != -1:
                way = str(self.result[curr_node][1])+" -> "+way
                curr_node = self.result[curr_node][1]
            print("Way to this node:", way)

        else:
            print("End node: wage, predecessor ")
            for node, (wage, predecessor) in sorted(self.result.items()):
                print(str(node)+":", str(wage)+",", predecessor)

alg = Algorithm("data.json")
alg.relax()

if alg.isSatisfied():
    alg.print()
else:
    print("Graph has negative cycle, can't use Bellman-Ford algorithm correctly")
