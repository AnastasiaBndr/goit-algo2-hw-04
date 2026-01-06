import numpy as np
from src.storage_logistics.edmonds_karp import edmonds_karp
from src.storage_logistics.draw_graph import draw_graph
from src.storage_logistics.get_terminal_to_shop_flow import get_terminal_to_shop_flow
from src.trie.homework import Homework

def edges():
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
    storages = sorted({t for t, _, _ in edges if t.startswith("Storage")})

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

    karp_result = edmonds_karp(
        capacity, node_index['SuperSource'], node_index['SuperSink'])
    flow_matrix = karp_result[1]
    table=get_terminal_to_shop_flow(flow_matrix, node_index,
                              terminals, shops, storages)
    print("Термінал\tМагазин\tФактичний Потік")


    for t in terminals:
        for s in shops:
            print(f"{t}\t{s}\t{int(table[t][s])}")

    draw_graph(edges)

def prefix_tree():
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat


def main():
    edges()
    try:
        prefix_tree()
        print("✅ Усі тести пройдено")
    except AssertionError:
        print("❌ Тест не пройшов")


if __name__ == "__main__":
    main()
