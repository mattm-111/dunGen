import random
from nodeMap import NodeMap
from roomNode import Room



def genTypeList(numberOfRooms):
    print("""
        
        The next numbers entered do not need to add up to 100%
        They are applied in a way to weight outcomes relative to other options during type generation.
        For example choosing '3' for all options will have the same result as choosing '1' for all options
        After all the math is done any quotient remainders will be set as 'DM Choice'
        There are three options total.  Combat, puzzle, and safe room.\n""")
    combatOpt = int(input("on a scale of 0(none) to 5(high) how often would you like combat encounters?  "))
    puzzleOpt = int(input("on a scale of 0(none) to 5(high) how often would you like puzzle encounters?  "))
    safeOpt = int(input("on a scale of 0(none) to 5(high) how often would you like safe room encounters?  "))
    relTotal = combatOpt+ puzzleOpt + safeOpt
    combatRooms = int((numberOfRooms - 2)*(combatOpt/relTotal))
    puzzleRooms = int((numberOfRooms - 2)*(puzzleOpt/relTotal))
    safeRooms = int((numberOfRooms - 2)*(safeOpt/relTotal))
    qRemainder = (numberOfRooms - 2) - (combatRooms + puzzleRooms + safeRooms)
    print(f"combat = {combatRooms}, puzzle = {puzzleRooms}, safe = {safeRooms}, remainder = {qRemainder} ")
    
    encounterList = []
    for i in range (1,combatRooms + 1):
        encounterList.append(random.randint(1,2))
    for i in range (1, puzzleRooms + 1):
        encounterList.append(4)
    for i in range (1, safeRooms + 1):
        encounterList.append(random.randint(5,8))
    for i in range (1,qRemainder + 1):
        encounterList.append(9)
    for i in range (1, 10):
        random.shuffle(encounterList)
    print(encounterList)
    devV = input("dev pause here")
    return encounterList

 


def genNodesManType(numberOfRooms, encounterList):
    myMap = NodeMap()
    for i in range (0, numberOfRooms):
        node = Room(i)
        if i == 0:
            node.type = node.setType(98)
        elif i == (numberOfRooms - 1):
            node.type = node.setType(99)
        else:
            print(f"i = {i}, list lenghth = {len(encounterList)}")
            node.type = node.setType(encounterList.pop())
        myMap.addNode(node)
    return myMap

def genNodesRandType(numberOfRooms):
    myMap = NodeMap()
    for i in range (0,numberOfRooms):
        node = Room(i)
        node.type = node.genType(numberOfRooms)
        myMap.addNode(node)
    return myMap














# def distrobutionGen(numberOfRooms, maxDepth):
#     ternarySect = (maxDepth - 2) // 3
#     firstTernary = ternarySect + 1
#     secondTernary = firstTernary + ternarySect
#     thirdTernary = secondTernary + ternarySect
#     fillSect = numberOfRooms - maxDepth
#     lowPop = int(.25 * fillSect)
#     highPop = int(.5 * fillSect)
#     strayRooms = fillSect - (2 * lowPop + highPop)

#     # print (f"""\napprox split = {ternarySect} low pop at 25% each, high pop 50%, \n
#     #         first low pop ternary = {1} - > {firstTernary - 1}..... 25% of (total rooms - max depth) is {lowPop}\n
#     #         second ternary high pop = {firstTernary} -> {secondTernary}....50% of total rooms - max depth is {highPop}\n
#     #         final ternary low pop = {secondTernary + 1} - > {maxDepth - 2}..... 25% of (total rooms - max depth) is {lowPop}\n
#     #         stray rooms = {strayRooms}\n
#     #         """)
#     distroDict = {"tern1Start": 1,
#                     "tern1End": firstTernary - 1,
#                     "tern2Start": firstTernary,
#                     "tern2End": secondTernary,
#                     "tern3Start": secondTernary + 1,
#                     "tern3End": maxDepth -2,
#                     "lowPop": lowPop,
#                     "highPop": highPop,
#                     "strayRooms": strayRooms}
#     return distroDict
