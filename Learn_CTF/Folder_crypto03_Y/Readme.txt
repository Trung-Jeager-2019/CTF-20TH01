RSA Math

N = p*q
p = N // q
q = N //p

r = (q-1)*(p-1)

d = gmpy2.divm(1,e,r)
e = gmpy2.divm(1,d,r)

ct = gmpy2.powmod(pt,e,N)
pt = gmpy2.powmod(ct,d,N)


