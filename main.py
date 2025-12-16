import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from storage_logistics.split_row import split_row


def main():
    G = nx.DiGraph()

    edges = [
        ("Terminal 1", "Storage 1", 25),
        ("Terminal 1", "Storage 2", 20),
        ("Terminal 1", "Storage 3", 15),

        ("Terminal 2", "Storage 3", 15),
        ("Terminal 2", "Storage 4", 30),
        ("Terminal 2", "Storage 2", 10),

        ("Storage 1", "Shop 1", 15),
        ("Storage 1", "Shop 2", 10),
        ("Storage 1", "Shop 3", 20),

        ("Storage 2", "Shop 4", 15),
        ("Storage 2", "Shop 5", 10),
        ("Storage 2", "Shop 6", 25),

        ("Storage 3", "Shop 7", 20),
        ("Storage 3", "Shop 8", 15),
        ("Storage 3", "Shop 9", 10),

        ("Storage 4", "Shop 10", 20),
        ("Storage 4", "Shop 11", 10),
        ("Storage 4", "Shop 12", 15),
        ("Storage 4", "Shop 13", 5),
        ("Storage 4", "Shop 14", 10),
    ]
    G.add_weighted_edges_from(edges)

    nodes=sorted({u for u,v,_ in edges}|{v for u,v,_ in edges})
    node_index={node:i for i,node in enumerate(nodes)}
    print(node_index)
    capacity=np.zeros((len(nodes),len(nodes)), dtype=int)
    for u,v,w in edges:
        i=node_index[u]
        j=node_index[v]
        capacity[i][j]=w

    print(capacity)

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


if __name__ == "__main__":
    main()
