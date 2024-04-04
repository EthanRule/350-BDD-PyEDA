#Practice Code
    # int(True)
    # # 1
    # int('0')
    # # 0

    # #Creating Variable Instances
    # a, b, c, d = map(exprvar, 'abcd')
    # a.name, b.name, c.name, d.name
    # print(a.name, b.name, c.name, d.name)

    # #Indexing Variables
    # x_0 = exprvar('x', 0)
    # x_1 = exprvar('x', 1)
    # print(x_0, x_1)

    # X = exprvars('x', 8)
    # print(X)
    # print(X[2:5])

    # #Multi Dementional Indexing
    # Y = exprvars('y', 4, 4)
    # print(Y)

    # #Points in Boolean Space
    #     #two coin flips
    # x = exprvar('x')
    # y = exprvar('y')
    # two_flips = list(iter_points([x, y]))
    # print(two_flips)
    #     #three coin flips
    # x, y, z = map(exprvar, 'xyz')
    # three_flips = list(iter_points([x, y, z]))
    # print(three_flips)

    # #Boolean Functions
    # X = exprvars('x', 3)
    # f = truthtable(X, "00000001")
    # print(f)
    # f = truthtable2expr(f)
    # print(f)
    
    # #majority wins
    # f = truthtable(X, "00010111")
    # print(f)
    # f = truthtable2expr(f)
    # print(f)

    # #PyEDA Variable/Function Base Classes
    
    # #Boolean Variables
    # # do NOT instantiate a Variable directly. Instead, 
    # # use one of the concrete implementations: pyeda.boolalg.bdd.bddvar() 
    # # pyeda.boolalg.expr.exprvar(), pyeda.boolalg.table.ttvar().

    # #Boolean Functions
    # #https://pyeda.readthedocs.io/en/latest/boolalg.html#boolean-functions

    # #BDD's - https://pyeda.readthedocs.io/en/latest/bdd.html

    # #Constructing BDD's
    # print("Constructing BDD's")
    # # 1. Convert an expression
    # f = expr("a & b | a & c | b & c")
    # print(f)
    # f = expr2bdd(f)
    # print(f)
    # # 2. User operators on existing BDDs
    # a, b, c = map(bddvar, 'abc')
    # print(type(a))
    # isinsta = isinstance(a, BinaryDecisionDiagram)
    # print(isinsta)