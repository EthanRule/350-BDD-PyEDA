from pyeda.inter import * # pip install pyeda
import IPython

R = range(0, 32)
G = [(i, j) for i in R for j in R if (i+3) % 32 == j % 32 or (i+8) % 32 == j % 32]
even = [i for i in R if i % 2 == 0]
prime = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
print(G)

a1 = exprvars('a', 32)
a2 = exprvars('a', 32)
RR = Or(*[And(a1[i], a2[j]) for i, j in G])
EVEN = Or(*[a1[i] for i in even])
PRIME = Or(*[a1[i] for i in prime])

RR = expr2bdd(RR)
EVEN = expr2bdd(EVEN)
PRIME = expr2bdd(PRIME)
print(sorted(RR.support))

#GraphViz
dot = PRIME.to_dot()
with open("graph.dot", "w") as fd:
    fd.write(dot)

a1_bdd = [expr2bdd(a) for a in a1]
a2_bdd = [expr2bdd(a) for a in a2]

print("RR Test1:", RR.restrict({a1_bdd[27]: 1, a2_bdd[3]: 1}) == expr2bdd(expr("1")))   # True
print("RR Test2:", RR.restrict({a1_bdd[16]: 1, a2_bdd[20]: 1}) == expr2bdd(expr("1")))  # False
print("EVEN Test1:", EVEN.restrict({a1_bdd[14]: 1}) == expr2bdd(expr("1")))             # True
print("EVEN Test2:", EVEN.restrict({a1_bdd[13]: 1}) == expr2bdd(expr("1")))             # False
print("PRIME Test1:", PRIME.restrict({a1_bdd[7]: 1}) == expr2bdd(expr("1")))            # True
print("PRIME Test2:", PRIME.restrict({a1_bdd[2]: 1}) == expr2bdd(expr("1")))            # False


# Replace the variable names in RR
RR2 = RR.compose({a1_bdd[i]: a2_bdd[i] for i in range(len(a1_bdd))})

# Test cases
print("RR2 Test1:", RR2.restrict({a2_bdd[27]: 1, a2_bdd[3]: 1}) == expr2bdd(expr("1")))   # True
print("RR2 Test2:", RR2.restrict({a2_bdd[16]: 1, a2_bdd[20]: 1}) == expr2bdd(expr("1")))  # False