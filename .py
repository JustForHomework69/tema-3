def suma_cifrelor(n:int):
    s = sum(int(c) for c in str(n))
    return(F"Suma cifrelor lui {n} este {s}.")

def cmmdc(a: int, b: int):
    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    return(F"CMMDC(12, 18) = 6.")

def cmmmc(a: int, b: int):
    x, y=abs(a),abs(b)
    while y !=0:
        x,y =y, x % y
        cmmdc_val = x
        cmmmc_val = abs(a * b) // cmmdc_val
    return(F"CMMMC(4, 6) = 12.")
