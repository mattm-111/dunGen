from roomNode import Room
import random
import matplotlib



class NodeMap():
    def __init__(self):
        
        self.nodeList = []
        
    


    def addNode(self, node):
        
        self.nodeList.append(node)

    def calcDistro(self, numberOfRooms, maxDepth):
        ternarySect = (maxDepth - 2) // 3
        firstTernary = ternarySect + 1
        secondTernary = firstTernary + ternarySect
        thirdTernary = secondTernary + ternarySect
        fillSect = numberOfRooms - 2
        self.lowPop = int(.25 * fillSect)
        self.highPop = int(.5 * fillSect)
        self.strayRooms = fillSect - (2 * self.lowPop + self.highPop)
        self.tern1Start = 1
        self.tern1End = firstTernary - 1
        self.tern2Start = firstTernary
        self.tern2End = secondTernary
        self.tern3Start = secondTernary + 1
        self.tern3End = maxDepth - 2
        # self.distroDict = {"tern1Start": 1,
        #     "tern1End": firstTernary - 1,
        #     "tern2Start": firstTernary,
        #     "tern2End": secondTernary,
        #     "tern3Start": secondTernary + 1,
        #     "tern3End": maxDepth -2,
        #     "lowPop": lowPop,
        #     "highPop": highPop,
        #     "strayRooms": strayRooms
        #     }

       # print(f"sect size = {ternarySect},  first tern = {self.tern1End}, second tern = {self.tern2End}, third tern end {self.tern3End}, low pop = {self.lowPop}, high pop = {self.highPop}, stray = {self.strayRooms}")

        
    def plotNodes(self, numberOfRooms, maxDepth):
        usedCoords = []
        counter = 0
        highMaxY = int(self.highPop / 2)
        lowMaxy = int(self.highPop / 3)
        print(f"low maxy = {lowMaxy},  lowpop = {self.lowPop}, highpop = {self.highPop}")
        for node in self.nodeList:
            if node.roomID == 0:
                node.xCoord = 0
                node.yCoord = 0
                usedCoords.append([0,0])
            elif node.roomID == (numberOfRooms - 1):
                node.xCoord = (maxDepth - 1)
                node.yCoord = 0
                usedCoords.append([node.xCoord, node.yCoord])

            else:
                if node.roomID <= self.lowPop:
                    while 1:
                        tempX = random.randint(1,self.tern1End)
                        tempY = random.randint(0,lowMaxy)
                        if [tempX, tempY] not in usedCoords:
                            node.xCoord = tempX
                            node.yCoord = tempY
                            usedCoords.append([tempX, tempY])
                            break
                            

                elif node.roomID > self.lowPop and node.roomID <= (self.lowPop + self.highPop + self.strayRooms):
                    while 1:
                        tempX = random.randint(self.tern2Start,self.tern2End)
                        tempY = random.randint(0,highMaxY)                    
                        if [tempX, tempY] not in usedCoords:
                            node.xCoord = tempX
                            node.yCoord = tempY
                            usedCoords.append([tempX, tempY])
                            break

                elif node.roomID > self.tern2End and node.roomID < (numberOfRooms - 1):
                    while 1:
                        tempX = random.randint(self.tern3Start,self.tern3End)
                        tempY = random.randint(0,lowMaxy)
                        if [tempX, tempY] not in usedCoords:
                            node.xCoord = tempX
                            node.yCoord = tempY
                            usedCoords.append([tempX, tempY])
                            break
        for i in range(0, numberOfRooms):
            usedCoords[i].append(i)
        
        print (usedCoords)
        self.roomCoordList = usedCoords



    def graphNodes(self):
        matplotlib.use('TkAgg')
        
        x_coords = [row[0] for row in self.roomCoordList]
        y_coords = [row[1] for row in self.roomCoordList]
        node_ids = [row[2] for row in self.roomCoordList]
        matplotlib.pyplot.scatter(x_coords, y_coords, color='red')
        for i, label in enumerate(node_ids):
            matplotlib.pyplot.annotate(
                label,                      # The text to display
                (x_coords[i], y_coords[i]), # The point (x, y) to label
                textcoords="offset points", # How to position the text
                xytext=(0, 10),             # Distance from text to point (x, y)
                ha='center'                 # Horizontal alignment
            )

        matplotlib.pyplot.xlabel('X Coord')
        matplotlib.pyplot.ylabel('Y Coord')
        matplotlib.pyplot.title('Dungeon Map')
        #matplotlib.pyplot.grid(True)
        #pyp.savefig('labeled_nodes.png')
        matplotlib.pyplot.show()



        

            
           



                       





