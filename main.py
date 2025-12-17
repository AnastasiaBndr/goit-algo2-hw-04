import numpy as np
from src.storage_logistics.edmonds_karp import edmonds_karp
from src.storage_logistics.draw_graph import draw_graph


def main():
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
    terminals = sorted({t for t, _, _ in edges if t.startswith("Terminal")})
    shops = sorted(
        {t for _, t, _ in edges if t.startswith("Shop")},
        key=lambda x: (x.split()[0], int(x.split()[1])))

    nodes = ["SuperSource"]+terminals +\
        sorted({u for u, _, _ in edges if u.startswith("Storage")}, key=lambda x: (x.split()[0], int(x.split()[1]))) +\
        shops+["SuperSink"]

    node_index = {node: i for i, node in enumerate(nodes)}

    capacity = np.zeros((len(nodes), len(nodes)), dtype=int)
    for u, v, w in edges:
        capacity[node_index[u]][node_index[v]] = w

    for t in terminals:
        capacity[node_index["SuperSource"]][node_index[t]] = 10**9

    for s in shops:
        capacity[node_index[s]][node_index["SuperSink"]] = 10**9

    max_flow=edmonds_karp(capacity, node_index['SuperSource'],node_index['SuperSink'])
    print(f'Max_flow={max_flow}')

    draw_graph(edges)


if __name__ == "__main__":
    main()
