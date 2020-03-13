import random

import math

def is_prime(n):	
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if (n % i == 0):
			return False
	return True	

def gcd(a, b):
	while (a % b != 0):
		c = b
		b = a % b
		a = c
	return b

def multiplicative_inverse(e, phi):
	a = phi
	b = e
	c = a%b
	d = a//b
	i = 0
	mass = []
	while True:
		mass.append([])
		mass[i].append(a)
		mass[i].append(b)
		mass[i].append(c)
		mass[i].append(d)
		buf = b
		b = a % b
		a = buf
		c = a%b
		d = a//b
		i += 1
		if (a % b == 0):
			mass.append([])
			mass[i].append(a)
			mass[i].append(b)
			mass[i].append(c)
			mass[i].append(d)
			break
	x = mass[i][2]
	y = mass[i][1]
	
	while ((i - 1) >= 0):
		buf = x
		x = y
		y = buf - y * mass[i - 1][3]
		i -= 1

	return y%phi

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

print('Input p:')
p = int(input())
print('Input q:')
q = int(input())
print (generate_keypair(p, q))

def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))