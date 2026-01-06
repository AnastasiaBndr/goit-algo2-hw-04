from src.trie.trie import Trie
from src.trie.trienode import TrieNode


class Homework(Trie):
    def __init__(self) -> None:
        super().__init__()
        self._suffix_trie = Trie()
        self._suffix_ready=False
    
    def has_prefix(self, prefix)->bool:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(
                f"Illegal argument for put: prefix = {prefix} must be a non-empty string")

        return len(self.keys_with_prefix(prefix)) > 0

    def _build_suffix_trie(self):
        for word in self.keys():
            self._suffix_trie.put(word[::-1],True)

        self._suffix_ready=True


    def count_words_with_suffix(self,suffix)->int:
        if not isinstance(suffix, str) or not suffix:
            raise TypeError(
                f"Illegal argument for put: suffix = {suffix} must be a non-empty string")

        if not self._suffix_ready:
            self._build_suffix_trie()

        reverced_pattern = suffix[::-1]
        return len(self._suffix_trie.keys_with_prefix(reverced_pattern))
        