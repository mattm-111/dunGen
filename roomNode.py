import random
import secrets

class Room():
    def __init__(self, roomID):
        ## xCoord, yCoord, top=None, bottom=None, left=None, right=None):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.dru = None
        self.drd = None
        self.dlu = None
        self.dld = None
        self.roomID = roomID
        self.type = type
        self.xCoord = None
        self.yCoord = None
        self.conPoint = None
        self.conID = None


        


    def genType(self, maxDepth):
        if self.roomID == 0:
            return "start"
        elif self.roomID == maxDepth -1:
            return "boss"
        else:
        
            rNumber = secrets.randbelow(8)
            match rNumber:
                case 0:
                    return "dmChoice"
                case 1:
                    return "encounter"
                case 2:
                    return "miniboss"
                case 3:
                    return "gathering"
                case 4: 
                    return "shop"
                case 5:
                    return "loot"
                case 6:
                    return "rest"
                case 7:
                    return "puzzle"
                case _:
                    return "dmChoice"
            

    def setType(self, number):
        match number:
            case 1:
                return "encounter"
            case 2:
                return "miniboss"
            case 3:
                return "boss"
            case 4: 
                return "shop"
            case 5:
                return "loot"
            case 6:
                return "rest"
            case 7:
                return "puzzle"
            case 8:
                return "dmChoice"
            case 9:
                return "gathering"
            case _:
                return "dmChoice"

    
    def distrobutionGen(self, numberOfRooms, maxDepth):
        ternarySect = (maxDepth - 2) // 3
        firstTernary = ternarySect + 1
        secondTernary = firstTernary + ternarySect
        thirdTernary = secondTernary + ternarySect
        strayRooms = (numberOfRooms - maxDepth) - (int(.25 * (numberOfRooms - maxDepth)) + int(.25 * (numberOfRooms - maxDepth)) + int(.5 * (numberOfRooms - maxDepth)))

        print (f"""\napprox split = {ternarySect} low pop at 25% each, high pop 50%, \n
               first low pop ternary = {1} - > {firstTernary - 1}..... 25% of (total rooms - max depth) is {int(.25 * (numberOfRooms - maxDepth))}\n
               second ternary high pop = {firstTernary} -> {secondTernary}....50% of total rooms - max depth is {int(.5 * (numberOfRooms - maxDepth))}\n
               final ternary low pop = {secondTernary + 1} - > {maxDepth - 2}..... 25% of (total rooms - max depth) is {int(.25 * (numberOfRooms - maxDepth))}\n
                stray rooms = {strayRooms}\n
                """)



    def setCoords(self, maxDepth):
        if self.roomID == 0:
            self.xCoord = 0
            self.yCoord = 0
        elif self.roomID == int(maxDepth) - 1:
            self.xCoord = int(maxDepth) - 1
            self.yCoord = 0
        elif self.roomID < maxDepth:
            self.xCoord = self.roomID
            self.yCoord = 0
        else:
            self.xCoord = 99
            self.yCoord = 99


    def __str__(self):
        return f"Room {self.roomID}, type = {self.type}, xCoord = {self.xCoord}, yCoord = {self.yCoord}"
    





