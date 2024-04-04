from pyeda.inter import * # pip install pyeda

def getBDDs():
    u = exprvars('u', 32)
    v = exprvars('v', 32)
    even = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    prime = set([3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

    #bdd's constructed from definition in 2.
    
    # "For all 0 ≤ i, j ≤ 31, there is an edge from node i to node j iff (i + 3)%32 = j%32 or (i + 8)%32 = j%32"
    rr_bdd = expr2bdd(expr(u[(u + 3) % 32] | u[(u + 8) % 32] for u in u), u, v) 
    even_bdd = expr2bdd(expr(u in even for u in u), u)
    prime_bdd = expr2bdd(expr(u in prime for u in u), u)
    return rr_bdd, even_bdd, prime_bdd

def testGetBDDs(rr_bdd, even_bdd, prime_bdd):
    assert rr_bdd(27, 3)  # True
    assert not rr_bdd(16, 20) # False
    assert even_bdd(14)   # True
    assert not even_bdd(13)   # False
    assert prime_bdd(7)   # True
    assert not prime_bdd(2)   # False
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
    rr_bdd, even_bdd, prime_bdd = getBDDs()
    testGetBDDs(rr_bdd, even_bdd, prime_bdd)
    rrtwo = rr2()
    testrr2(rrtwo)
    rr2stars = rr2star()
    print(rr2stars)
    return

if __name__ == '__main__':
    main()

