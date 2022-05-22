import numpy as np
import hashlib

def hash384(chaine):
    hash_object = hashlib.sha384(chaine)
    hex_dig = hash_object.hexdigest()
    return(hex_dig)

def f(n):
    sum = 0
    for k in range(0, n):
        sum+=(4/9)**(k)
    a_float = (np.sqrt(3)/4) * (1 + sum) * np.cos(5*n)
    return "{:.8f}".format(a_float)

print("Valeur pour n = 5 > ", f(5))
print("Hash correspondant > ", hash384(b"HACKDAY{"+bytes(str(f(5)), 'utf-8')+b"}"))

for i in range(0, 65536):
    word = b"HACKDAY{"+bytes(str(f(i)), 'utf-8')+b"}"
    hash = hash384(word)
    if hash == "f757157d00bb06567dcefc5fe84e00490f3f646874cc1d898e87051d6c60ced9e40da917101af97fe4926ed432c12ac0":
        print("Le drapeau est > {}, obtenu pour n = {}".format(word, i))
