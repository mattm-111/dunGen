

class Room():
    def __init__(self, roomID, type, xCoord, yCoord, conPoint, conID):
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
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.conPoint = conPoint
        self.conID = conID


    def genType():
        pass

    def genConnections():
        pass

    def __str__(self):
        return f"Room {self.roomID}, type = {self.type}"
    





