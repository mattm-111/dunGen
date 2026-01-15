from roomNode import Room
import random

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
                usedCoords.append([0,maxDepth - 1])

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




        

            
           



                       





