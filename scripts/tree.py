categories = [
    {"id": 1, "name": "Eletrônicos", "parentId": None},
    {"id": 2, "name": "Celulares", "parentId": 1},
    {"id": 3, "name": "TVs", "parentId": 1},
    {"id": 4, "name": "Roupas", "parentId": None},
    {"id": 5, "name": "Camisetas", "parentId": 4},
    {"id": 6, "name": "Android", "parentId": 2},
    {"id": 7, "name": "Samsung", "parentId": 6},
]

def build_tree(tree):
    roots = []
    id_to_node = {}
    # 1. Map all nodes
    for category in tree:
        node = {
            "id": category["id"],
            "name": category["name"],
            "children": []
        }
        id_to_node[category["id"]] = node
    # 2. conect to its parent or add to the roots
    for category in tree:
        node = id_to_node[category["id"]]
        if category["parentId"] is None:
            roots.append(node)
        else:
            parent = id_to_node.get(category["parentId"])
            parent["children"].append(node)
    
    return roots
    
# DFS 
def print_paths_from_root(tree, path = []):
    for node in tree:
        path.append(node["name"])
        if len(node["children"]) > 0:
            print_paths_from_root(node["children"], path)
        else:
            print(" > ".join(path))
        path.pop()

tree = build_tree(categories)
print_paths_from_root(tree)

def find_deep(tree, depth = 0):
    max_depth = depth

    for node in tree:
        if len(node["children"]) > 0:
            result = find_deep(node["children"], max_depth + 1)
            max_depth = max(max_depth, result)
        
    return max_depth

def find_deep_iter(tree):
    max_depth = 0
    stack = [(node, 1) for node in tree]

    while stack:
        node, node_depth = stack.pop()
        max_depth = max(max_depth, node_depth)
        for child in node["children"]:
            stack.append((child, node_depth + 1))
    return max_depth

deep = find_deep_iter(tree)
print("[ ITERATIVE ] The graph has max deep " + str(deep))
deep = find_deep(tree)
print("[ RECURSION ] The graph has max deep " + str(deep))


# BFS 
def basic_bfs_implementation():
    queue = deque([(1, node) for node in tree])

    while queue:
        level, node = queue.popleft()

        for child in node["children"]:
            queue.append((level + 1, child))

# 1. Level order traversal: Print the nodes level by level of the tree.
import heapq

def print_level_orders(graph):
    current_depth = 1
    queue = [(current_depth, node["id"], node) for node in graph]
    heapq.heapify(queue)
    categories = []

    while queue:
        node_depth, _, node = heapq.heappop(queue)

        if node_depth != current_depth:
            print("Nível " + str(current_depth) + ": " + ", ".join(categories))
            current_depth = node_depth
            categories = []

        categories.append(node["name"])

        for child in node["children"]:
            heapq.heappush(queue, (node_depth + 1, child["id"], child))

    print("Nível " + str(current_depth) + ": " + ", ".join(categories))

print_level_orders(tree)

# 2. Find a Node with a Specific Name
# Requirements: Return the full path to it, e.g.: Electronics > Cell Phones > Android > Samsung.
from collections import deque

def find_by_name(graph, name):
    queue = deque([(node, node["name"]) for node in graph])

    while queue:
        node, path = queue.popleft()
        if node["name"] == name:
            return path
        for child in node["children"]:
            queue.append((child, path + " > " + child["name"]))
    return "Not found"

path = find_by_name(tree, "Samsung")
print(path)

# 3. Count Nodes by Level
# Count how many nodes there are at each level of the tree.

def count_nodes_by_level(tree):
    queue = deque([(1, node) for node in tree])
    node_by_levels = {}

    while queue:
        level, node = queue.popleft()
        node_by_levels[level] = node_by_levels.get(level, 0) + 1

        for child in node["children"]:
            queue.append((level + 1, child))

    # print
    for level in node_by_levels.keys():
        print(str(level) + ": " + str(node_by_levels[level]))

count_nodes_by_level(tree)