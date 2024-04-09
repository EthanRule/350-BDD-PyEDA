from functools import reduce
from pyeda.inter import * # pip install pyeda
from pyeda.boolalg.bdd import Or
import IPython

R = range(0, 32)
# Convert numbers to 5-bit binary strings
R_bin = [format(i, '05b') for i in R]

G = [(i, j) for i in R_bin for j in R_bin if (int(i, 2)+3) % 32 == int(j, 2) % 32 or (int(i, 2)+8) % 32 == int(j, 2) % 32]
even = [i for i in R_bin if int(i, 2) % 2 == 0]
prime = {'00011', '00101', '00111', '01011', '01101', '10001', '10011', '10111', '11101', '11111'}
#print(G)

x = bddvars('x', 5)
y = bddvars('y', 5)
edges = None
firstEdge = 0
RRtest1 = 0
RRtest2 = 0
for tuple in G:
    i, j = tuple
    i = str(i)
    j = str(j)
    node1 = None
    node2 = None
    if i[0] == '1':
        node1 = x[0]
    elif i[0] == '0':
        node1 = ~x[0]
    if j[0] == '1':
        node2 = y[0]
    elif j[0] == '0':
        node2 = ~y[0]

    for index in range(1, len(i)):
        if i[index] == '1':
            node1 &= x[index]
        elif i[index] == '0':
            node1 &= ~x[index]
    for index in range(1, len(i)):
        if j[index] == '1':
            node2 &= y[index]
        elif j[index] == '0':
            node2 &= ~y[index]
    edge = node1 & node2
    #Test RR(27, 3)
    if edge == x[0] & x[1] & ~x[2] & x[3] & x[4] & ~y[0] & ~y[1] & ~y[2] & y[3] & y[4]:
        RRtest1 += 1
    #Test RR(16, 20)
    if edge == x[0] & ~x[1] & ~x[2] & ~x[3] & ~x[4] & y[0] & y[1] & ~y[2] & y[3] & ~y[4]:
        RRtest2 += 1

    if firstEdge == 0:
        edges = edge
        firstEdge += 1
    else:
        edges |= edge
RR = edges
if RRtest1 == 1:
    print("Test RR(27, 3): true, PASSED")
else:
    print("Test RR(27, 3): true, FAILED")
if not RRtest2:
    print("Test RR(16, 20): false, PASSED")
else:
    print("Test RR(16, 20): true, FAILED")

# EVEN (yy1 ... yy5) & PRIME (xx1 ... xx5)
firstEven = 0
evenNodes = None
for item in even:
    i = str(item)
    node = None
    if i[0] == '1':
        node = y[0]
    elif i[0] == '0':
        node = ~y[0]
    for index in range(len(i[1:5])):
        if i[index] == '1':
            node &= y[index]
        elif i[index] == '0':
            node &= ~y[index]
    if firstEven == 0:
        evenNodes = node
        firstEven += 1
    else:
        evenNodes |= edge
EVEN = evenNodes

firstPrime = 0
primeNodes = None
for item in prime:
    i = str(item)
    node = None
    if i[0] == '1':
        node = x[0]
    elif i[0] == '0':
        node = ~x[0]
    for index in range(len(i[1:5])):
        if i[index] == '1':
            node &= x[index]
        elif i[index] == '0':
            node &= ~x[index]
    if firstPrime == 0:
        primeNodes = node
        firstPrime += 1
    else:
        primeNodes |= edge
PRIME = primeNodes
RR = expr2bdd(RR)

#GraphViz
# dot = edge.to_dot()
# with open("graph.dot", "w") as fd:
#     fd.write(dot)

# a2 = [exprvar('a2', i) for i in range(32)]

# # Represent each edge as an And operation between the two nodes
# edges = [And(a1[int(i, 2)], a2[int(j, 2)]) for i, j in G]

# # Represent the entire graph as an Or operation between all the edges
# RR = Or(*edges)

# print(RR)
# print(type(RR))
# RR = expr2bdd(RR)
# print(type(RR))