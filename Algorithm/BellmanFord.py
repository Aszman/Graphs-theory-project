import json


class Algorithm:
    # Necessary data
    start_node = 0
    end_node = 0

    nodes = set()
    edges = []

    result = dict()

    # Get data for algorithm
    def __init__(self, file):
        json_file = open(file)
        x = json.load(json_file)

        self.start_node, self.end_node = x[0]
        self.edges = x[1:]

        json_file.close()

        for edge in self.edges:
            if edge[0] not in self.nodes:
                self.nodes.add(edge[0])

            if edge[1] not in self.nodes:
                self.nodes.add(edge[1])

        for node in self.nodes:
            self.result[node] = (float('inf'), -1)

        self.result[self.start_node] = (0, -1)

    # Calculate weights and paths to all nodes
    def relax(self):
        for _ in range(len(self.nodes) - 1):
            changed = False
            for edge in self.edges:
                if self.result[edge[0]][0] + edge[2] < self.result[edge[1]][0]:
                    changed = True
                    self.result[edge[1]] = (self.result[edge[0]][0] + edge[2], edge[0])
            if not changed:
                break

    # Check if conditions are satisfied
    def isSatisfied(self):
        for edge in self.edges:
            if self.result[edge[1]][0] > self.result[edge[0]][0] + edge[2]:
                return False
        return True

    # Print results
    # if end_node is not equal any node, print overall result
    # otherwise, print weight and path to this node
    def print(self):
        resultFile = open("results.txt", 'w')

        if alg.isSatisfied():
            if self.end_node in self.nodes:
                text = "Start node: " + str(self.start_node) + "\n"
                text += "End node: " + str(self.end_node) + "\n"
                text += "Weight: " + str(self.result[self.end_node][0])

                print(text)
                resultFile.write(text+"\n")

                curr_node = self.end_node
                way = str(curr_node)

                while self.result[curr_node][1] != -1:
                    way = str(self.result[curr_node][1]) + " -> " + way
                    curr_node = self.result[curr_node][1]

                text = "Way to this node: " + str(way)
                print(text)
                resultFile.write(text)

            else:
                print("End node: weight, predecessor ")
                resultFile.write("End node: weight, predecessor\n")

                for node, (weight, predecessor) in sorted(self.result.items()):
                    if self.start_node == node:
                        text = str(node) + ": " + str(weight) + ", " + "START"
                    else:
                        text = str(node) + ": " + str(weight) + ", " + str(predecessor)
                    print(text)
                    resultFile.write(text+"\n")

        else:
            print("Graph has negative cycle, can't use Bellman-Ford algorithm correctly")
            resultFile.write("Graph has negative cycle, can't use Bellman-Ford algorithm correctly")

alg = Algorithm("data.json")

alg.relax()

alg.print()
