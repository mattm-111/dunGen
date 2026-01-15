from roomNode import Room

class NodeMap():
    def __init__(self):
        
        self.nodeDict = {}


    def addNode(self, node):
        
        self.nodeDict[node.roomID] = node


