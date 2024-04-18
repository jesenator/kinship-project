import networkx as nx
import matplotlib.pyplot as plt
import random

def random_color():
    """Generate a random color in hexadecimal format."""
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def create_kinship_graph():
    # Create a new graph
    G = nx.Graph()

    # Adding nodes for various beings
    beings = [f"Being {i}" for i in range(1, 100)] 
    more_kin = ["Me", "You", "Humans",
                "Hens", "Cows", "Shrimp", "Pigs",
                "Dogs", "Cats", "Turtles", "Elephants", "Whales", "Dolphins",
                "Octopuses", "Horses", "Sheep", "Goats",
                "Family", "Friends",
                "Jumbos", "Bostonians"
                "Ukrainians", "Russians", "Israelis", "Palestinians",
                "Americans", "Africans", "Germans",
                "Jews", "Christians", "Muslims",
                "Sentient AI", "Digital minds", 
                "Future AI", "Future humans", "Future nonhumans",

                "Chimpanzees", "Orangutans", "Gorillas",  # Other primates
                "Squids", "Lobsters",  # Additional sea creatures
                "Bats", "Rats",  # Other mammals and common research animals
                "Bees",  # Insects with complex social structures and behaviors
                "Jellyfish",  # Other beings with simple nervous systems but capable of responses
                "Neanderthals", "Denisovans",  # Extinct human relatives
                "Extraterrestrial beings",  # Hypothetical beings from other planets
                "Bioengineered beings"  # Theoretical future beings created through genetic engineering
                ]

    # Adding nodes and edges
    all_kin = beings + more_kin
    for k in all_kin:
        G.add_node(k, size=5, color=random_color())
        for person in all_kin:
            if k != person:
                G.add_edge(k, person)

    # Drawing the graph
    pos = nx.spring_layout(G)  # random layout
    print(pos)
    node_size = 20
    sizes = [G.nodes[node]['size']*node_size for node in G.nodes]
    colors = [G.nodes[node]['color'] for node in G.nodes]

    # Draw nodes with full opacity and edges with reduced opacity
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=colors, alpha=1)  # Nodes opaque
    nx.draw_networkx_edges(G, pos, alpha=0.05, width=0.5)  # Edges less opaque
    labels = {node: node for node in more_kin}
    nx.draw_networkx_labels(G, pos, labels, font_size=15, font_color='black')
    plt.show()

# Generate and display the expanded personal kinship graph with "Me" among other additional kin
create_kinship_graph()
