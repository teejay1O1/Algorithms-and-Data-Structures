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
        for i in range(len(word)):
            prev=node
            node=node.children.get(word[i],TrieNode(word[i]))
            prev.children[word[i]]=node
        node.isTerminal=True
    
    def searchword(self,word):
        node=self.root
        for i in range(len(word)):
            node=node.children.get(word[i])
            if node is None :
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


