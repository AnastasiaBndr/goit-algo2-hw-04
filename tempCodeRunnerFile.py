def prefix_tree():
    trie = Homework()
    words = ["doing", "drawing", "challenging", "banana", "band", "swimming", "ball", "bat", "charging"]

    for index, word in enumerate(words):
        trie.put(word, index)
    
    print(trie.count_words_with_suffix("ing"))