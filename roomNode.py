
import secrets

class Room():
    def __init__(self, roomID):
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
                return "puzzle"
            case 5:
                return "loot"
            case 6:
                return "rest"
            case 7:
                return "gathering"
            case 8:
                return "shop"
            case 9:
                return "DM Choice"
            case 98:
                return "Start"
            case 99:
                return "Boss"
            case _:
                return "dmChoice"


    def __str__(self):
        return f"Room {self.roomID}, type = {self.type}, xCoord = {self.xCoord}, yCoord = {self.yCoord}"
    





