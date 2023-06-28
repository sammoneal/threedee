def powers_of_two(start=1,end=None):
    forever = end is None
    pow = start
    while forever or (pow<end):
        yield 2**pow
        pow += 1