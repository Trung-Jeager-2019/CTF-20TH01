from Crypto.PublicKey import RSA
import gmpy2

def int2Text(number, size):
    text = "".join([chr((number >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

N = 70736025239265239976315088690174594021646654881626421461009089480870633400973
C = 29846947519214575162497413725060412546119233216851184246267357770082463030225
p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163
r=(p-1)*(q-1)
e = 3
d = gmpy2.divm(1, e, r)

rsa = RSA.construct((N,e,d,p,q))
pt = rsa.decrypt(C)

print (pt)  # returns 6872557977505747778161182217242712228364873860070580111494526546045
print (int2Text(pt,100)) #returns ABCTF{th1s_was_h4rd_in_1980}