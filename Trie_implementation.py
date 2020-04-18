class TrieNode:
    def __init__(self,char,isTerminal=False):
        self.char=char
        self.isTerminal=isTerminal
        self.children=dict()

class Trie:
    def __init__(self):
        self.root=TrieNode(None)
    
    def addword(self,word):
        #if len(word)==0 :
        #   pass
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode(char)
            node=node.children[char]
        node.isTerminal=True
    
    def searchword(self,word):
        node=self.root
        for char in word:
            if char in node.children:
                node=node.children[char]
            else:
                return False
        return node.isTerminal
"""
obj=Trie()

obj.addword("hey")
obj.addword("nope")
obj.addword("hi")
obj.addword("hello")

obj.addword("no")
obj.addword("yes")

print(obj.searchword("hello"))
print(obj.searchword("why"))
print(obj.searchword("hi"))
print(obj.searchword("hell"))
obj.searchword("kyun")
"""


