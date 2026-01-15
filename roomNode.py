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


        


    def genType(self, numberOfRooms):
        if self.roomID == 0:
            return "start"
        elif self.roomID == numberOfRooms - 1:
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

    
    # def distrobutionGen(self, numberOfRooms, maxDepth):
    #     ternarySect = (maxDepth - 2) // 3
    #     firstTernary = ternarySect + 1
    #     secondTernary = firstTernary + ternarySect
    #     thirdTernary = secondTernary + ternarySect
    #     fillSect = numberOfRooms - maxDepth
    #     lowPop = int(.25 * fillSect)
    #     highPop = int(.5 * fillSect)
    #     strayRooms = fillSect - (2 * lowPop + highPop)

    #     print (f"""\napprox split = {ternarySect} low pop at 25% each, high pop 50%, \n
    #            first low pop ternary = {1} - > {firstTernary - 1}..... 25% of (total rooms - max depth) is {lowPop}\n
    #            second ternary high pop = {firstTernary} -> {secondTernary}....50% of total rooms - max depth is {highPop}\n
    #            final ternary low pop = {secondTernary + 1} - > {maxDepth - 2}..... 25% of (total rooms - max depth) is {lowPop}\n
    #             stray rooms = {strayRooms}\n
    #             """)
    #     distroDict = {"tern1Start": 1,
    #                   "tern1End": firstTernary - 1,
    #                   "tern2Start": firstTernary,
    #                   "tern2End": secondTernary,
    #                   "tern3Start": secondTernary + 1,
    #                   "tern3End": maxDepth -2,
    #                   "lowPop": lowPop,
    #                   "highPop": highPop,
    #                   "strayRooms": strayRooms}
    #     return distroDict



    # def setCoords(self, maxDepth):
    #     if self.roomID == 0:
    #         self.xCoord = 0
    #         self.yCoord = 0
    #     elif self.roomID == int(maxDepth) - 1:
    #         self.xCoord = int(maxDepth) - 1
    #         self.yCoord = 0
    #     elif self.roomID < maxDepth:
    #         self.xCoord = self.roomID
    #         self.yCoord = 0
    #     else:
    #         self.xCoord = 99
    #         self.yCoord = 99


    def __str__(self):
        return f"Room {self.roomID}, type = {self.type}, xCoord = {self.xCoord}, yCoord = {self.yCoord}"
    





