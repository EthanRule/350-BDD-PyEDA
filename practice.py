from pyeda.inter import * # pip install pyeda
import IPython

# 1. Convert an expression
f = expr("a & b | a & c | b & c")
print(f)
f = expr2bdd(f)
print(f)

# 2. Use operators on existing BDDs
a, b, c = map(bddvar, 'abc')
print(type(a))

# 3. Use Boolean function methods
print("f.support")
print(f.support)  # Returns the support set of the function
print("f.usupport")
print(f.usupport)
print("f.inputs")
print(f.inputs)  # Returns the support set in name/index order
print("f.top")
print(f.top)  # Returns the first variable in the ordered support set
print("f.degree")
print(f.degree)  # Returns the degree of the function
print("f.cardinality")
print(f.cardinality)  # Returns the cardinality of the relation BN⇒B

# 4. Iterate through all points in the domain
print("f.iter_domain")
for point in f.iter_domain():
    print(point)

print("f.iter_image")
for point in f.iter_image():
    print(point)

# 5. Restrict a subset of support variables to {0,1}
print("f.restrict")
restricted_f = f.restrict({a: 1, b: 0})
print(restricted_f)

# 6. Substitute a subset of support variables with other Boolean functions
print("f.compose")
composed_f = f.compose({a: b & c, b: a | c})
print(composed_f)

# 7. If this function is satisfiable, return a satisfying input point
print("f.satisfy_one")
satisfying_point = f.satisfy_one()
print(satisfying_point)

# 8. Iterate through all satisfying input points
print("f.satisfy_all")
for point in f.satisfy_all():
    print(point)

# 9. Return the cardinality of the set of all satisfying input points
print("f.satisfy_count")
print(f.satisfy_count())

# 10. Iterate through the cofactors of a function over N variables
print("f.iter_cofactors")
for cofactor in f.iter_cofactors([a, b, c]):
    print(cofactor)

# 11. Return a tuple of the cofactors of a function over N variables
print("f.cofactors")
print(f.cofactors([a, b, c]))

# 12. Return the smoothing of a function over a sequence of N variables
print("f.smoothing")
print(f.smoothing([a, b, c]))

# 13. Return the consensus of a function over a sequence of N variables
print("f.consensus")
print(f.consensus([a, b, c]))

# 14. Return the derivative of a function over a sequence of N variables
print("f.derivative")
print(f.derivative([a, b, c]))

# 15. Return whether this function is zero
print("f.is_zero")
print(f.is_zero())

# 16. Return whether this function is one
print("f.is_one")
print(f.is_one())

# Constructing BDD's
    # 1. Convert an expression
print("Coverting an Expression to BDD's")
f = expr("a & b | a & c | b & c")
print(f)
f = expr2bdd(f)
print(f)
    # 2. Use operators on existing BDDs
print("Using Operators on Existing BDDs")
a, b, c = map(bddvar, 'abc')
print(type(a))
isinstance(a, BinaryDecisionDiagram)

a0 = bddvar('a', 0)
print(a0)
b_a_0_1 = bddvar(('a', 'b'), (0, 1))
print(b_a_0_1)

X = bddvars('x', 4, 4)
print(X)

f = a & b | a & c | b & c
print(f)
print("f.restrict({a: 0})")
print(f.restrict({a: 0}))
print("f.restrict({a: 1, b: 0})")
print(f.restrict({a: 1, b: 0}))
print("f.restrict({a: 1, b: 1})")
print(f.restrict({a: 1, b: 1}))
print("f.restrict({a: 0, b: 0, c: 1})")
print(f.restrict({a: 0, b: 0, c: 1}))
print(IPython.paths.get_ipython_dir() + '/extensions')

#GraphViz
print("GraphViz")
a, b, c = map(bddvar, 'abc')
f = a & ~b & ~c | ~a & b & ~c | ~a & ~b & c | a & b & c
f2 = a ^ b ^ c
dot = f.to_dot()
with open('graph.dot', 'w') as fd:
    fd.write(dot)

print("f = f2?", f is f2)

X = bddvars('x', 8)
f1 = X[0] & X[3] | X[1] & X[4] | X[2] & X[5]
Y = bddvars('y', 6)
f1 = f1.compose({X[0]: Y[0], X[1]: Y[2], X[2]: Y[4], X[3]: Y[1], X[4]: Y[3], X[5]: Y[5]})
dot = f1.to_dot()
with open('graph.dot', 'w') as fd:
    fd.write(dot)

# Boolean Expressions
zeroA = expr(0)
zeroB = expr(False)
zeroC = expr("0")
print("zeroA == zeroB == zeroC")
print(zeroA == zeroB == zeroC)

print("Single Index Exprvar")
a42 = exprvar('a', 42)
print(str(a42))

print("Multiple Index Exprvar")
a_1_2_3 = exprvar('a', (1, 2, 3))
print(str(a_1_2_3))

#Complements
a = exprvar('a')
print(~a)
print(type(~a))

a, b, ci = map(exprvar, "a b ci".split())
s = ~a & ~b & ci | ~a & b & ~ci | a & ~b & ~ci | a & b & ci
s = a ^ b ^ ci
co = a & b | a & ci | b & ci
print(expr2truthtable(s))
print(expr2truthtable(co))
co = expr2bdd(co)
dot = co.to_dot()
with open('graph.dot', 'w') as fd:
    fd.write(dot)

s = Or(And(Not('a'), Not('b'), 'ci'), And(Not('a'), 'b', Not('ci')), And('a', Not('b'), Not('ci')), And('a', 'b', 'ci'))
s = Xor('a', 'b', 'ci')
co = Or(And('a', 'b'), And('a', 'ci'), And('b', 'ci'))