from Crypto import Util, Random


def generate_random_prime(bits):
    return Util.number.getPrime(bits, randfunc=Random.get_random_bytes)


def find_primitive_root(p):
    # find ϕ(p)
    phi = p - 1

    # divisors of ϕ(p)
    phi_div = [k for k in range(2, phi) if phi % k == 0]

    # iterate through all numbers g∈[1,p], and for each number, to check if it is primitive root.
    for g in range(1, p):
        r = True
        for d in phi_div:
            if g**d % p == 1:
                r = False
                break
        if r == True:
            return g

    return False


def square_and_multiply(n, e):
    """
        @para:
            n : exponent base.
            e : the expoxant.

        function square and multiplication:
            it use to compute n to the power of e.
    """
    # list of bytes of n:
    binary = [int(k) for k in bin(e).split('0b')[1]]

    # First One lists Number
    binary = binary[1:]
    p = n

    for b in binary:
        # Zero calls for Square
        if b == 0:
            p = p**2

        # else : b==1 , One calls for Square + Multiply
        else:
            p = (p**2)*n

    return p
