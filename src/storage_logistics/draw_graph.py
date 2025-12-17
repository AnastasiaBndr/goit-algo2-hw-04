import matplotlib.pyplot as plt
import networkx as nx
from src.storage_logistics.split_row import split_row


def draw_graph(edges):
    G = nx.DiGraph()

    G.add_weighted_edges_from(edges)
    
    shops = [n for n in G.nodes if n.startswith("Shop")]
    storages = [n for n in G.nodes if n.startswith("Storage")]
    terminals = [n for n in G.nodes if n.startswith("Terminal")]

    pos = {}

    pos.update(split_row(shops, y_top=2, y_bottom=-2))
    pos.update(split_row(storages, y_top=1, y_bottom=-1, x_shift=len(shops)//4))
    for i, node in enumerate(terminals):
        pos[node] = (i * 3, 0)

    color_map = [
        "lightgreen" if n.startswith("Shop")
        else "orange" if n.startswith("Storage")
        else "skyblue"
        for n in G.nodes
    ]

    plt.figure(figsize=(20, 10))
    nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=1500,
            font_size=8, font_weight="bold", arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
