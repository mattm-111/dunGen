from roomNode import Room
from nodeMap import NodeMap

def main():
    print("Hello from dunGen!")
    numberOfRooms = int(input("How many rooms in your dungeon? "))
    maxDepth = int(input("How deep do you want the dungeon? "))
    myMap = NodeMap()
    for i in range (0, numberOfRooms):
        node = Room(i)
        node.setCoords(maxDepth)
        node.type = node.genType(maxDepth)
        myMap.addNode(node)
        
    for key, value in myMap.nodeDict.items():
        print(f"{key} -> {value}")
    myMap.nodeDict[0].distrobutionGen(numberOfRooms, maxDepth)
    

        

    









if __name__ == "__main__":
    main()
