# MST Visualizer

MST Visualizer is a Python script that allows users to input a graph or generate a random graph, visualize the graph using NetworkX and Matplotlib, find its Minimum Spanning Tree (MST), and display both the graph and MST in ASCII table format.

## Features

- Input a custom graph or generate a random one.
- Visualize the graph and its Minimum Spanning Tree.
- Display graph and MST details in an ASCII table.

## Prerequisites

Before running this script, make sure you have the following dependencies installed:

- Python 3.x
- NetworkX
- Matplotlib

You can install these dependencies using `pip`:

```bash
pip install networkx matplotlib
```

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone [<repository-url>]
cd MST-Visualizer
```

2. Run the script:

```bash
python mst_visualizer.py
```

Follow the on-screen prompts to input a custom graph or generate a random one. The script will then visualize the graph and its Minimum Spanning Tree.

## Usage

- Choose whether to input a custom graph (choice '1') or generate a random graph (choice '2').
- If you choose to input a custom graph:
  - Enter the number of nodes.
  - Enter the weights between each pair of nodes.
- If you choose to generate a random graph:
  - Enter the number of nodes for the random graph.

The script will display the graph and its Minimum Spanning Tree using graphical visualization and also provide an ASCII table with node connections and weights.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This project uses the NetworkX and Matplotlib libraries.
```
