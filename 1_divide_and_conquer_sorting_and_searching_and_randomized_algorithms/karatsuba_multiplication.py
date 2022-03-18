
def decide_cuts(x,y):
    if len(str(x)) == len(str(y)) and len(str(x)) % 2 == 0:
        n = len(str(x))
        half_n = n // 2
        cut_x = half_n
        cut_y = half_n
    elif len(str(x)) == len(str(y)) and len(str(x)) % 2 == 1:
        n = len(str(x))
        half_n = n // 2
        cut_x = half_n + 1
        cut_y = half_n + 1
    elif len(str(x)) > len(str(y)):
        n = len(str(x))
        half_n = n // 2
        cut_x = n - half_n
        cut_y = len(str(y)) - half_n
    else:
        n = len(str(y))
        half_n = n // 2
        cut_x = len(str(x)) - half_n
        cut_y = n - half_n
    return n, half_n, cut_x, cut_y
    

def karatsuba_mult(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    n, half_n, cut_x, cut_y = decide_cuts(x, y)
    a = int(str(x)[:cut_x])
    b = int(str(x)[cut_x:])
    c = int(str(y)[:cut_y])
    d = int(str(y)[cut_y:])
    ac = karatsuba_mult(a, c)
    bd = karatsuba_mult(b, d)
    ad_bc = karatsuba_mult(a+b, c+d) - ac - bd
    return int(str(ac) + '0'*(2*half_n)) + int(str(ad_bc) + '0'*half_n) + bd

if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    r = karatsuba_mult(x, y)
    assert r == x*y
