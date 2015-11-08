import testRead
import ast

def makeBoard(n):
   return [[[range(1, n+1)]]*n]*n

alphabetVals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def makeRows(n):
    rows = []

    for i in range(1,n+1):
        rows.append(alphabetVals[i])
    return rows

def makeCols(n):
    cols = []
    for i in range(1,n+1):
        numString = str(i)
        cols.append(numString)
    return cols


def makeVars(boardSize):
    currRows = makeRows(boardSize)
    currCols = makeCols(boardSize)
    varNames = [ x+y for x in currRows for y in currCols ]
    #for var in varNames:
        #print(var)

#print(randomBoard(6))
#print(makeVars(6))
if __name__ == '__main__':
    variables = testRead.readKenKen()
    constraintList = []
    sickList = []
    #print('dslkfasf', variables)
    #print('variables[0[][0]', variables[0][2])
#    for i in range(0,len(variables)):
 #       constraintList.append(variables[i])

#print()
    #for i in constraintList:
    #    print(i)
    #    localList = ast.literal_eval(i)
    #    localList = [n.strip() for n in localList]
    #    sickList.append(localList)
    #print(sickList)





