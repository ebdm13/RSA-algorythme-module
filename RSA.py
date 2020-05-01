
from random import randint

def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)

def getFactors(n):
    factors = [];
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_p_q(a):
	while True:
		if getFactors(a) == [1, a]:
			return a
			break
		a = randint(100, 999)   

def generator():
	p1,q1 = randint(100, 999), randint(100, 999)
	p,q = get_p_q(p1),get_p_q(q1)
	#p,q = 137, 751
	n = p*q
	pn = (p-1)*(q-1)

	if p > q:
		g = p

	if q > p:
		g = q

	e = g + 1
	while e < pn:
		if pgcd(pn, e) == 1:
			#print("e = ", e)
			break
		e = e + 1

	d = e + 1
	while d < pn:
		if e * d % pn == 1:
			#print("d = ", d)
			break
		d = d + 1
	public_key = e,n
	private_key = d,n
	print("your public key is: ", public_key)
	print("your private key is: ", private_key)

def en_crypt(e, n):
	print("entrer le message à crypter")
	c = input()
	d = []
	for i in c:
		d.append(ord(i))
	v = 0
	crypt_d = []
	while v < len(d):
		crypt_d.append(pow(d[int(v)], e)%n)
		v = v + 1
	print(crypt_d)

def de_crypt(d, n):
	print("Entrer le message à décrypter (s'éparer les nombres par des virgules)")
	cc = input().split(",")
	cc = list(map(int, cc))
	v2 = 0
	d2 = []
	while v2 < len(cc):
		d2.append(pow(cc[int(v2)], d)%n)
		v2 = v2 + 1
	#print(d2)

	j = []
	for i in d2:
		j.append(chr(i))
	j = ''.join(j)
	print(j)
