from roomNode import Room
from nodeMap import NodeMap
from functions import genTypeList, genNodesManType, genNodesRandType

import random
import matplotlib.pyplot

from functions import *

def main():
    print("Hello from dunGen!")
    numberOfRooms = int(input("How many rooms in your dungeon?  "))
    maxDepth = int(input("How deep do you want the dungeon?  "))
    typeQ = input("Would you like to specify the occurence of certian rooms? (y/n)  ")
    
    if typeQ == "y" or typeQ == "yes":
        encounterList = genTypeList(numberOfRooms)
        myMap = genNodesManType(numberOfRooms, encounterList)

        # myMap = NodeMap()
        # for i in range (0, numberOfRooms):
        #     node = Room(i)
        #     if i == 0:
        #         node.setType(98)
        #     elif i == (numberOfRooms - 1):
        #         node.setType(99)
        #     else:
        #         print(f"i = {i}, list lenghth = {len(encounterList)}")
        #         node.type = node.setType(encounterList.pop())
        #     myMap.addNode(node)
    else:
        myMap = genNodesRandType(numberOfRooms)
        # myMap = NodeMap()
        # for i in range (0,numberOfRooms):
        #     node = Room(i)
        #     node.type = node.genType(numberOfRooms)
        #     myMap.addNode(node)
    

    # for key, value in myMap.nodeDict.items():
    #     print(f"{key} -> {value}")
    myMap.calcDistro(numberOfRooms, maxDepth)
    
   
    myMap.plotNodes(numberOfRooms, maxDepth)

    for node in myMap.nodeList:
        print (node)    

    print (myMap.roomCoordList)
    #myMap.graphNodes()

    

        

    









if __name__ == "__main__":
    main()
