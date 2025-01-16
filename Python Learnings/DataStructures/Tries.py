class Node:
    def __init__(self):
        self.children = {}
        self.is_complete_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_complete_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_complete_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

class WordDictionary():
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_complete_word = True
        return self.print(word)
        

    def print(self, word):
        curr, strng = self.root, []

        for ch in word:
            if ch not in curr.children:
                return strng.append('')
            strng.append(ch)
            curr = curr.children[ch]
        return ''.join(strng)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for el in word:
            if el == '.':
                continue
            elif el not in curr.children:
                return False
            else:
                curr = curr.children[el]
        if word[-1] == '.':
            return True
        else:
            return curr.is_complete_word


word = 'apple'
prefix = 'app'

trie = Trie()
wd = WordDictionary()

# print(trie.insert(prefix))
# print(trie.search('ap'))
# print(trie.startsWith(prefix))

print(wd.addWord(word))
print(wd.search('app.e'))
#print(wd.search(prefix))
