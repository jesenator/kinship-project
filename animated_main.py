import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

def random_color():
    """Generate a random color in hexadecimal format."""
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def create_kinship_graph():
    # Create a new graph
    G = nx.Graph()

    # Adding nodes for various beings
    beings = [f"Being {i}" for i in range(1, 30)]
    more_kin = ["Me", "You", "Humans", "Hens", "Cows", "Shrimp", "Pigs",
                "Dogs", "Cats", "Turtles", "Elephants", "Whales", "Dolphins",
                "Octopuses", "Horses", "Sheep", "Goats",
                "Family", "Friends", "Jumbos", "Bostonians",
                "Ukrainians", "Russians", "Israelis", "Palestinians",
                "Americans", "Africans", "Germans",
                "Jews", "Christians", "Muslims", "Buddhists",
                "Sentient AI", "Digital minds",
                "Future AI", "Future humans", "Future nonhumans",
                "Chimpanzees", "Orangutans", "Gorillas",
                "Squids", "Lobsters", "Bats", "Rats",
                "Bees", "Jellyfish", "Neanderthals", "Denisovans",
                "Extraterrestrials", "Bioengineered beings",
                "Other beings capable of experienceing pleasure and pain"]

    # Adding nodes and edges
    all_kin = beings + more_kin
    for k in all_kin:
        G.add_node(k, size=5, color=random_color())
        for person in all_kin:
            if k != person:
                G.add_edge(k, person)

    # Prepare layout
    pos = nx.spring_layout(G)  # Initial layout
    fig, ax = plt.subplots(figsize=(10, 8))

    def update(frame):
        # Update node positions
        for node in pos:
            move_val = 0.05
            pos[node] += np.random.rand(2) * move_val - move_val / 2

        ax.clear()
        node_sizes = [G.nodes[node]['size']*20 for node in G.nodes]
        node_colors = [G.nodes[node]['color'] for node in G.nodes]

        # Draw the updated graph
        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=1, ax=ax)
        nx.draw_networkx_edges(G, pos, alpha=0.05, width=0.5, ax=ax)
        labels = {node: node for node in more_kin}
        nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='black', ax=ax)
        ax.set_title("Kinship Network Animation")
        ax.axis('off')  # Hide axes

    # Create and start the animation
    ani = FuncAnimation(fig, update, frames=100, interval=1, repeat=True)
    plt.show()

# Generate and display the animated personal kinship graph
create_kinship_graph()
