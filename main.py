from roomNode import Room
from nodeMap import NodeMap

def main():
    print("Hello from dunGen!")
    numberOfRooms = int(input("How many rooms in your dungeon? "))
    myMap = NodeMap()
    for i in range (0, numberOfRooms):
        node = Room(i)
        myMap.addNode(node)
        
    for key, value in myMap.nodeDict.items():
        print(f"{key} -> {value}")
    

        

    









if __name__ == "__main__":
    main()
