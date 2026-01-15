import random

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


        


    def genType(self, max):
        if self.roomID == 0:
            return "start"
        elif self.roomID == max -1:
            return "boss"
        else:
        
            rNumber = random.randint(1,8)
            match rNumber:
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
                case 8:
                    return "dmChoice"
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

    
    def treeGen(numberOfRooms, maxDepth):
        pass

    def setCoords(self, max):
        if self.roomID == 0:
            self.xCoord = 0
            self.yCoord = 0
        elif self.roomID == int(max) - 1:
            self.xCoord = int(max) - 1
            self.yCoord = 0
        elif self.roomID < max:
            self.xCoord = self.roomID
            self.yCoord = 0
        else:
            self.xCoord = 99
            self.yCoord = 99


    def __str__(self):
        return f"Room {self.roomID}, type = {self.type}, xCoord = {self.xCoord}, yCoord = {self.yCoord}"
    





