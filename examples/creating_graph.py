import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Singapore", "San Francisco"),
    ("San Francisco", "Tokyo"),
    ("Riga", "Copenhagen"),
    ("Copenhagen", "Singapore"),
    ("Singapore", "Tokyo"),
    ("Riga", "San Francisco"),
    ("San Francisco", "Singapore"),
])

pos = {
    "Singapore": (1, 1),
    "San Francisco": (2, 1),
    "Tokyo": (3, 2),
    "Riga": (0, 0),
    "Copenhagen": (1, 0),
}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
plt.show()
