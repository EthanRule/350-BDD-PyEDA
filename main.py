from pyeda.inter import * # pip install pyeda

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getBDDs():
    u = exprvars('u', 32)
    v = exprvars('v', 32)
    even = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    prime = set([3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

    #bdd's constructed from definition in 2.
    
    # "For all 0 ≤ i, j ≤ 31, there is an edge from node i to node j iff (i + 3)%32 = j%32 or (i + 8)%32 = j%32"
    rr_bdd = expr2bdd(expr(u[i] ^ v[i] for i in range(32)))
    print("rr_bdd generated")
    even_bdd = expr2bdd(expr(u[i] for i in range(32) if i % 2 == 0))
    print("even_bdd generated")
    prime_bdd = expr2bdd(expr(u[i] for i in range(32) if is_prime(i)))
    print("prime_bdd generated")
    return rr_bdd, even_bdd, prime_bdd, u, v

def testGetBDDs(rr_bdd, even_bdd, prime_bdd, u, v):
    assert rr_bdd.restrict({u[27]: True, v[3]: True}) == BDDConstant(True)  # True
    assert rr_bdd.restrict({u[16]: True, v[20]: True}) == BDDConstant(False) # False
    assert even_bdd.restrict({u[14]: True})   # True
    assert not even_bdd.restrict({u[13]: True})   # False
    assert prime_bdd.restrict({u[7]: True})   # True
    assert not prime_bdd.restrict({u[2]: True})   # False
    print("getBDDs() PASSED!")

def rr2(rr_bdd):
    rr2 = rr_bdd.compose(rr_bdd)
    return rr2

def testrr2(rr_bdd):
    rr2_bdd = rr2(rr_bdd)
    assert rr2_bdd(27, 6)  # True
    assert not rr2_bdd(27, 9) # False
    print("rr2() PASSED!")

def rr2star(rr_bdd):
    rr2star = rr2.smoothing('u', 'v')
    return rr2star

def main():
    rr_bdd, even_bdd, prime_bdd, u, v = getBDDs()
    testGetBDDs(rr_bdd, even_bdd, prime_bdd, u, v)
    #rrtwo = rr2()
    #testrr2(rrtwo)
    #rr2stars = rr2star()
    #print(rr2stars)
    return

if __name__ == '__main__':
    main()

