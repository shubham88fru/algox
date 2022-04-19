########################################
# Traverse a graph in dfs way and return
# an array containing nodes in the order
# of traversal
########################################
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    #T: O(V+E), S: O(V)
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array