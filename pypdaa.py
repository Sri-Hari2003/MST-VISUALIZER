import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms.tree import minimum_spanning_tree

# Function to generate an undirected random graph
def generate_random_graph(num_nodes):
    G = nx.Graph()
    nodes = range(1, num_nodes + 1)
    G.add_nodes_from(nodes)
    edges = []
    for i in range(1, num_nodes):
        for j in range(i + 1, num_nodes + 1):
            weight = random.randint(1, 10)
            edges.append((i, j, weight))
    G.add_weighted_edges_from(edges)
    return G

# Prompt the user for graph input choice
choice = input("Enter '1' to input a graph or '2' to generate a random graph: ")

if choice == '1':
    # User inputs the graph
    G = nx.Graph()
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = range(1, num_nodes + 1)
    G.add_nodes_from(nodes)
    edges = []
    for i in range(1, num_nodes):
        for j in range(i + 1, num_nodes + 1):
            weight_input = input(f"Enter the weight between node {i} and node {j} (press Enter for 0): ")
            weight = float(weight_input) if weight_input != "" else 0
            if weight != 0:
                edges.append((i, j, weight))
    G.add_weighted_edges_from(edges)
else:
    # Generate a random undirected graph
    num_nodes = int(input("Enter the number of nodes for the random graph: "))
    G = generate_random_graph(num_nodes)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.axis('off')
plt.show()

# Find the minimum spanning tree (MST)
mst = minimum_spanning_tree(G)

# Display the MST
pos_mst = nx.spring_layout(mst)
nx.draw(mst, pos_mst, with_labels=True)
nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=nx.get_edge_attributes(mst, 'weight'))

plt.axis('off')
plt.show()

# Display the graph and MST in ASCII table format
print("Generated Graph:")
for u, v, w in G.edges(data='weight'):
    print(f"Node {u} - Node {v}: {w}")

print("\nMinimum Spanning Tree:")
for u, v, w in mst.edges(data='weight'):
    print(f"Node {u} - Node {v}: {w}")


