import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import numpy as np

# Create the graph
G = nx.Graph()
nodes = ["Me", "You", "Humans", "Dogs", "Cats", "Sentient AI"]
G.add_nodes_from(nodes)
G.add_edges_from([(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)])

# Initialize positions using a spring layout
pos = nx.spring_layout(G)

fig, ax = plt.subplots(figsize=(8, 6))

def update(frame):
    ax.clear()  # Clear previous frame before drawing the new one
    
    # Update positions based on previous positions
    for node in pos:
        move_val = 0.05
        pos[node] += np.random.rand(2) * 0.05 - 0.05 / 2 # Adjust node positions slightly

    # Draw the updated graph
    nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color='skyblue', edge_color='gray')
    ax.set_title("Kinship Network Animation")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=200, repeat=True)

plt.show()
