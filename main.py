from pyeda.inter import * # pip install pyeda

#main issue to solve, get a bdd not a bddConstant

def edge_exists(bdd, i, j):
    u = bddvar('u', i)
    v = bddvar('v', j)
    restricted_bdd = bdd.restrict({u: 1, v: 1})
    return restricted_bdd.is_one()

def count_bdd_nodes(bdd):
    return len(bdd.support)

def initializeBDDs():
    u = [bddvar('u', i) for i in range(32)]
    v = [bddvar('v', i) for i in range(32)]

    R = range(0, 32)
    G = [(i, j) for i in R for j in R if (i+3) % 32 == j % 32 or (i+7) % 32 == j % 32]
    edge_bdds = [u[i] & v[j] for i, j in G]
    rr_bdd = And(*edge_bdds)
    print(type(rr_bdd))
    print(edge_exists(rr_bdd, 16, 20))

    even = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    even_expr = Or([u[i] for i in even])
    even_bdd = expr2bdd(even_expr)

    prime = set([3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    prime_expr = Or([u[i] for i in prime])
    prime_bdd = expr2bdd(prime_expr)

    return rr_bdd, even_bdd, prime_bdd, u, v

def main():
    rr_bdd, even_bdd, prime_bdd, u, v = initializeBDDs()
    print(edge_exists(rr_bdd, u, v, 16, 20))  # Prints True if edge (16, 20) exists, False otherwise
    print(count_bdd_nodes(rr_bdd))  # Prints the number of nodes in rr_bdd
    return
if __name__ == '__main__':
    main()

