



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
