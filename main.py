from pyeda.inter import * # pip install pyeda

def initializeBDDs():
    u = [bddvar('u', i) for i in range(32)]
    v = [bddvar('v', i) for i in range(32)]
    even = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    prime = set([3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

    edges = []
    for i in range(32):
        for j in range(32):
            if i != j and ((i + 3) % 32 == j or (i + 8) % 32 == j):
                edge = And(u[i], v[j])
                edges.append(edge)
    rr_bdd = expr2bdd(Or(*edges))

    even_bdd = expr2bdd(Or([u[i] for i in even]))
    prime_bdd = expr2bdd(Or([u[i] for i in prime]))

    return rr_bdd, even_bdd, prime_bdd, u, v

def testInitializeBDDs(rr_bdd, even_bdd, prime_bdd, u, v):
    assert rr_bdd.restrict({u[27]: True, v[3]: True})  # True
    assert not rr_bdd.restrict({u[16]: True, v[20]: True})  # False
    assert even_bdd.restrict({u[14]: True})  # True
    assert not even_bdd.restrict({u[13]: True})  # False
    assert prime_bdd.restrict({u[7]: True})  # True
    assert not prime_bdd.restrict({u[2]: True})  # False
    print("getBDDs() PASSED!")

def main():
    rr_bdd, even_bdd, prime_bdd, u, v = initializeBDDs()
    testInitializeBDDs(rr_bdd, even_bdd, prime_bdd, u, v)
    return
if __name__ == '__main__':
    main()

