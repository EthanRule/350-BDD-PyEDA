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
z = bddvars('z', 5)
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
evenTest1 = 0
evenTest2 = 0
for item in even:
    i = str(item)
    node = None
    if i[0] == '1':
        node = y[0]
    elif i[0] == '0':
        node = ~y[0]
    for index in range(1, len(i)):
        if i[index] == '1':
            node &= y[index]
        elif i[index] == '0':
            node &= ~y[index]
    if node == ~y[0] & y[1] & y[2] & y[3] & ~y[4]:
        evenTest1 += 1
    if node == ~y[0] & y[1] & y[2] & ~y[3] & y[4]:
        evenTest2 += 1
    if firstEven == 0:
        evenNodes = node
        firstEven += 1
    else:
        evenNodes |= node
EVEN = evenNodes
if evenTest1 == 1:
    print("Test EVEN(14): true, PASSED")
else:
    print("Test EVEN(14): false, FAILED")
if not evenTest2:
    print("Test EVEN(13): false, PASSED")
else:
    print("Test EVEN(13): true, FAILED")

firstPrime = 0
primeNodes = None
primeTest1 = 0
primeTest2 = 0
for item in prime:
    i = str(item)
    node = None
    if i[0] == '1':
        node = x[0]
    elif i[0] == '0':
        node = ~x[0]
    for index in range(1, len(i)):
        if i[index] == '1':
            node &= x[index]
        elif i[index] == '0':
            node &= ~x[index]
    if node == ~x[0] & ~x[1] & x[2] & x[3] & x[4]:
        primeTest1 += 1
    if node == ~x[0] & ~x[1] & ~x[2] & x[3] & ~x[4]:
        primeTest2 += 1
    if firstPrime == 0:
        primeNodes = node
        firstPrime += 1
    else:
        primeNodes |= node
PRIME = primeNodes
if primeTest1 == 1:
    print("Test PRIME(7): true, PASSED")
else:
    print("Test PRIME(7): false, FAILED")
if not primeTest2:
    print("Test PRIME(2): false, PASSED")
else:
    print("Test PRIME(2): true, FAILED")

#RR2 2 step reachability
mapping_y_to_z = {y[i]: z[i] for i in range(len(y))}
banana = RR.compose(mapping_y_to_z)
mapping_x_to_z = {x[i]: z[i] for i in range(len(x))}
apple = RR.compose(mapping_x_to_z)
RR2 = (banana & apple).smoothing(z)

#test
rr2Test1 = {x[0]: 1, x[1]: 1, x[2]: 0, x[3]: 1, x[4]: 1, y[0]: 0, y[1]: 0, y[2]: 1, y[3]: 1, y[4]: 0}
rr2Test2 = {x[0]: 1, x[1]: 1, x[2]: 0, x[3]: 1, x[4]: 1, y[0]: 0, y[1]: 1, y[2]: 0, y[3]: 0, y[4]: 1}
rr2Test1 = RR2.restrict(rr2Test1)
rr2Test2 = RR2.restrict(rr2Test2)
if rr2Test1.is_one():
    print("Test RR2(27, 6): true, PASSED")
else:
    print("Test RR2(27, 6): false, FAILED")
if rr2Test2.is_zero():
    print("Test RR2(27, 9): false, PASSED")
else:
    print("Test RR2(27, 9): true, FAILED")

#RR2*
RR2_star = RR2
prev = None
while RR2_star is not prev:
    prev = RR2_star
    mapping_z_to_y = {z[i]: y[i] for i in range(len(z))}
    RR2_star = (RR2_star & RR2_star.compose(mapping_z_to_y)).smoothing(z)

#u = x, v = y
#PRIME (xx1 ... xx5)
#EVEN (yy1 ... yy5)
#RR2_star (xx1 ... xx5 ; yy1 ... yy5)
#A -> B == (~A) V B

banana = (EVEN & RR2_star)
apple = banana.smoothing(y)
result = ~(((~PRIME) | apple).smoothing(x)) #in lecture said this should be a BDDConstant which means it must be 0 or 1
if expr2truthtable(result):
    print("∀u. (PRIME(u) → ∃v. (EVEN(v) ∧ RR2star(u, v))) Truth Value: True")
else:
    print("∀u. (PRIME(u) → ∃v. (EVEN(v) ∧ RR2star(u, v))) Truth Value: False")