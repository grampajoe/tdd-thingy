"""
Cool tools!!!!!
"""
def f(x):
    x += 1
    return reduce(lambda i, j: i * j, xrange(1, x), 1)
