import re
import operator

# Thanks StackOverflow: http://stackoverflow.com/questions/1740726/python-turn-string-into-operator
ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '==': operator.eq,
       '!=': operator.ne,
       '<': operator.lt,
       '<=': operator.le,
       '>': operator.gt,
       '>=': operator.ge,
       'abs': operator.abs,
       '^': operator.pow
       }

#class struct a bit overkill for this, can use dict[varname]=domain if this is all it needs
class MakeVar:
    def __init__(self,n,d=[1,2,3,4]):
        self.name = n
        self.domain = d

# create a constraint for KenKen specific to number of vars involved
class Constraint:
    def __init__(self,vs,op,a):
        self.nvars = len(vs)
        self.vlist = vs
        self.op = op
        if ( 1 == self.nvars ):
            self.fn = lambda x: x == eval(a)
        elif (2 == self.nvars ):
            self.fn = lambda x,y: ops[op](x,y) == eval(a)
        elif (3 == self.nvars ):
            self.fn = lambda x,y,z: ops[op](ops[op](x,y),z) == eval(a)
        else:
            print('num vars not right')

def readKenKen():

    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open('testKenKen.txt').readlines()

    # start a dictionary of variables and a list of constraints
    vars = {}
    Cons = []

    # see https://docs.python.org/3/howto/regex.html
    # check that input is good (testing only the first line). remove all white space first
    r = re.compile('\d+([[]\w+,\W+(,\w+)+[]],*)*')

    testLine = 2 # test this line in file
    l = lines[testLine]
    l=re.sub('[ ]','',l)
    if not r.match(l): return

    # size of puzzle is first number on the line
    n = eval(re.findall('^\d+',l)[0])
    print('size ',n)

    # create a list of constraints (as strings).
    # order is [answer,operator,var+], which can have 1,2, or 3 vars
    # I think I should be able to use 1 regex to capture all as above in match, but couldn't get it working
    cs = []
    c1 = re.findall('[[]\w+,\W+,\w+[]]',l)
    c2 = re.findall('[[]\w+,\W+,\w+,\w+[]]',l)
    c3 = re.findall('[[]\w+,\W+,\w+,\w+,\w+[]]',l)
    cs = c1+c2+c3
    print('cs ',cs)
    print("This is c1")
    print(c1)
    print("This is c2")
    print(c2)
    print("This is c3")
    print(c3)
    # for each of the constraints
    def customCopy(nestedList):
        returnList = []
        for i in nestedList:
            returnList.append(i[:])
        print('returnList', returnList)
        print('returnList[0]', returnList[0])

        return returnList
    returnCS = customCopy(cs)

    copyList = []
    for copy in returnCS:
        copy=re.sub('[[\] ]','',copy)
        copy=re.split(',',copy)
        copyList.append(copy)
        print('copy', copy)
    print('copy[0]', copy[1])
    print('copyList', copyList)
    print('copyList[0][2]', copyList[4][1])

    for c in cs:
        # remove white space and brackets, then split constraint into answer,op,var
        c=re.sub('[[\] ]','',c)
        c=re.split(',',c)
        #print('csfsd ',str(c))
        print('c ',c)
        # makeVars if not already in existence
        for v in c[2:len(c)]:
            #print('v ',v)
            if v not in vars:
                vars[v] = MakeVar(v)
    print('c[0]', c[0])



    #additional processing
    for v in range(1,len(c)):
        c[v] = str(c[v])

        op = c[1]
        answer = c[0]

        # make a constraint
        Cons.append(Constraint( c[2:len(c)], op, answer ))

    #for k in vars:
    #    print(k)

    #test the results for line 0
    if ( testLine == 0 ):
        # 2 var constraint
        c = Cons[0]
        print(c.vlist)
        v1, v2 = vars[c.vlist[0]], vars[c.vlist[1]]
        print(v1.name,'=',v1.domain[3],' ',v2.name,'=',v2.domain[0])
        print('op ', c.fn(v1.domain[3],v2.domain[0]))

        # 3 var constraint
        c = Cons[5]
        v1, v2, v3 = vars[c.vlist[0]], vars[c.vlist[1]], vars[c.vlist[2]]
        print(v1.name,' ',v2.name,' ',v3.name)
        print('op ', c.fn(v1.domain[0],v2.domain[3],v3.domain[1]))
    return copyList

def readCrypt():

    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open('testCrypt.txt').readlines()
    testLine = 4 # test this line in file
    l = lines[testLine]
    #remove white space
    l=re.sub('[ ]','',l)
    print('l ',l)

    # determine operator and remove, find "answer"
    op = re.findall('^\W',l)
    print('op ',op)
    l = re.sub('^\W,','',l)
    answer = re.findall('=\w+',l)
    answer = re.sub('=','',answer[0])
    print('l ',l,'answer ',answer)

    # start a dictionary of variables and a list of constraints
    Cons = []

    vars = []
    # separate values
    words = re.findall('\w+',l)
    for w in words:
        letters = re.findall('\w',w)
        for letter in letters:
            if letter not in vars: vars.append(letter)
    print('vars ',vars)

def readFutoshiki():

    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open('testFutoshiki.txt').readlines()
    testLine = 0 # test this line in file
    l = lines[testLine]
    #remove white space
    l = re.sub('[ ]','',l)
    print('l ',l)

    # size of puzzle is first number on the line
    n = eval(re.findall('^\d+',l)[0])
    l = re.sub('^\d+','',l)
    print('size ',n)

    # find all "x Op y"
    cs=re.findall('\w+\W+\w+',l)
    print('c ',cs)

    # for each, separate apart the variables, operator, and values
    for c in cs:
        # these are x < y OR x > y
        if re.findall('\w+\d+<\w+\d+',c) or re.findall('\w+\d+>\w+\d+',c):
            lvar = re.findall('^\w+\d+',c)[0]
            rvar = re.findall('\w+\d+$',c)[0]
            op = re.findall('\W',c)[0]
            #convert inequalities to lambda fn
            fn = lambda x,y: ops[op](x,y)
            print('lvar,op,rvar,fn(3,4)',lvar,op,rvar,fn(3,4))
        else:
            # find x = value
            if re.findall('\w+\d+=\d+',c):
                var = re.findall('^\w+\d+',c)[0]
                value = re.findall('\d+$',c)[0]
            # find value = x
            elif re.findall('\d+=\w+\d+',c):
                var = re.findall('\w+\d+$',c)[0]
                value = re.findall('^\d+$',c)[0]
            # conver equalities to lambda fn
            fn = lambda x: x == eval(value)

            #test results with a print
            print('var,val,fn(1) ',var,'==',value,fn(1))

def readCrossMath():

    # I was assuming operators applied in order as listed on puzzle, but
    # probably supposed to follow op precedence. If so, this isn't quite right.

    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open('testCrossMath.txt').readlines()
    testLine = 0 # test this line in file
    l = lines[testLine]
    #remove white space
    l=re.sub('[ ]','',l)
    print('l ',l)

    # split into the different constraints
    cs=re.split(',',l)
    print('cs ',cs)

    # for each constraint, extract vars and create lambda
    for c in cs:
        # extract what the equation equates to
        answer = re.findall('=\d+',c)
        answer = re.sub('=','',answer[0])
        c = re.sub('=\d+','',c)

        groupRight = False
        # check for parantheses for precedence
        if re.search('\)',c):
            if ( re.search('\)',c).start() == len(c)-2 ):
                groupRight = True
                c = re.sub('\(','',c)
                c = re.sub('\)','',c)

        # extract the 2 operators and the 3 vars, create the function
        op2 = re.findall('\W',c)
        var3 = re.findall('\w+\d+',c)

        print('c ',c)
        if groupRight:
            fn = lambda x,y,z : ops[op2[0]](x,ops[op2[1]](y,z)) == eval(answer)
        else:
            fn = lambda x,y,z : ops[op2[1]](ops[op2[0]](x,y),z) == eval(answer)

        # test the results with a print
        print('op var answer fn(16,16,4)',op2,' ',var3,' ',answer,' ',fn(16,16,4))

if __name__ == "__main__":
    readKenKen()
    #readCrypt()
    #readFutoshiki()
    #readCrossMath()
