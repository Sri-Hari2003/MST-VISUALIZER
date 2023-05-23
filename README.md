# MST-VISUALIZER
The program can serve as an educational tool for teaching graph theory concepts. By visualizing graphs and their minimum spanning trees, students can better understand the fundamental properties and algorithms of graphs. It provides a hands-on experience and facilitates learning through interactive visualization.
It imports the necessary libraries: networkx, matplotlib.pyplot, and random. It also imports the minimum_spanning_tree function from networkx.algorithms.tree module.
It defines a function called generate_random_graph that generates an undirected random graph with a given number of nodes.
It prompts the user for a choice between inputting a graph (choice '1') or generating a random graph (choice '2').
If the user chooses to input a graph (choice '1'), it prompts for the number of nodes and weight between each pair of nodes, and constructs the graph accordingly.
If the user chooses to generate a random graph (choice '2'), it prompts for the number of nodes for the random graph and calls the generate_random_graph function to create the graph.
It uses the spring_layout function from NetworkX to generate positions for the nodes of the graph.
It visualizes the generated graph using nx.draw and nx.draw_networkx_edge_labels functions from NetworkX, and displays it using plt.show() from Matplotlib.
It finds the minimum spanning tree (MST) of the generated graph using the minimum_spanning_tree function.
It visualizes the MST using the same process as step 7.
It displays the graph and MST in ASCII table format by iterating over the edges of the graph and MST and printing the corresponding nodes and weights.
