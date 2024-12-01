
input = open("input1.txt", "r")
wholeTable = input.read()

oneLine = wholeTable.replace("   ", " ")
oneLine = " ".join(oneLine.splitlines())

numbers = oneLine.split()

desired_array = [int(numeric_string) for numeric_string in numbers]

switchArray = True
firstCollumn = []
secondCollumn = []
for x in desired_array:
    if switchArray == True:
        firstCollumn.append(x)
        switchArray = False
    else:
        secondCollumn.append(x)
        switchArray = True

allDifs = []
myIndex = 0        
for x in firstCollumn:
    difXY = x - secondCollumn[myIndex]
    allDifs.append(difXY)
    myIndex += 1

totalDif = 0
for x in allDifs:
    totalDif = totalDif + x
    
print(totalDif)
