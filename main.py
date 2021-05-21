import json

json_file = open("data.json")

x = json.load(json_file)

num_of_nodes, start_node, end_node =x[0]
edges = x[1:]

result = []
for i in range (0, num_of_nodes):
    result.append((float('inf'), -1))

result[start_node] = (0, -1)

for _ in range(num_of_nodes-1):
    changed = False
    for edge in edges:
        if result[edge[0]][0] + edge[2] < result[edge[1]][0]:
            changed = True
            result[edge[1]] = (result[edge[0]][0] + edge[2], edge[0])
    if(changed == False):
        break

if end_node >=0 and end_node < num_of_nodes:
    print("Start node:", start_node)
    print("End node:", end_node)
    print("Wage:", result[end_node][0])

    curr_node = end_node
    way = str(curr_node)
    while result[curr_node][1] != -1:
        way = str(result[curr_node][1])+" -> "+way
        curr_node = result[curr_node][1]
    print("Way to this node:", way)

else:
    print("End node: wage, predecessor ")
    for node in range(num_of_nodes):
        print(str(node)+":", str(result[node][0])+",", result[node][1])


