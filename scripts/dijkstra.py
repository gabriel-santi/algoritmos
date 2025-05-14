# Set up graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {} 
graph["a"]["end"] = 1


graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}


# Set up costs
costs = {}
costs["a"] = 6 
costs["b"] = 2 
costs["end"] = float("inf") 

# Set up parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processedNodes = []

# Dijsktra's algorithm
def findCheapestNode(nodes):
    cheapestNode = None
    cheapestValue = float("inf")
    for node in nodes:
        if nodes[node] < cheapestValue and node not in processedNodes:
            cheapestNode = node
            cheapestValue = nodes[node]

    return cheapestNode


def processNode(node):
    # Check the neighbors and compare the new cost(using the actual node) with the value stored in costs
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processedNodes.append(node)

def findCheapestPath():
    end = "end"
    start = "start"
    path = []

    current = end
    while current is not start:
        path.insert(0, parents[current]) 
        current = parents[current]
    
    return path

def dijkstra():
    node = findCheapestNode(costs)
    while node is not None:
        processNode(node)
        node = findCheapestNode(costs)
        
    return findCheapestPath()

print(dijkstra())