from collections import Counter, defaultdict
import re

# Define a simple Trie for prefix search
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.words.add(word)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.words

# Stop words to ignore
stop_words = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'to', 'of', 'for', 'with'}

def preprocess_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in stop_words]

class TextAnalyzer:
    def __init__(self, text):
        self.words = preprocess_text(text)
        self.freq = Counter(self.words)
        self.trie = Trie()
        for word in self.freq:
            self.trie.insert(word)

    def query_top_words(self, prefix, top_n):
        matching_words = self.trie.search_prefix(prefix.lower())
        sorted_words = sorted(matching_words, key=lambda w: (-self.freq[w], w))
        return sorted_words[:top_n]

# Example usage
text = """
The theory transformed theoretical physics and astronomy during the 20th century,
 superseding a 200-year-old theory of mechanics created primarily by Isaac Newton.
 It introduced concepts including 4-dimensional spacetime as a unified entity of space and time, 
 relativity of simultaneity, kinematic and gravitational time dilation, and length contraction. 
 In the field of physics, relativity improved the science of elementary particles and their fundamental interactions, 
 along with ushering in the nuclear age. With relativity, cosmology and astrophysics predicted extraordinary astronomical phenomena such as neutron stars,
 black holes, and gravitational waves.
"""

analyzer = TextAnalyzer(text)
print(analyzer.query_top_words('th', 3))  # top 3 words starting with 'th'
