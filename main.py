import random
from sympy import mod_inverse
from sympy import nextprime

# SSS Algo
def encrypt_with_SSS(prime=nextprime(10**96)):
    print("\nIndicate how many shares you want to produce in TOTAL")
    num_shares = int(input())
    print("\nIndicate how many of the total amount of shares you will need to reconstruct your secret")
    threshold = int(input())
    print("\nInput the complete number you wish to split in shares")
    secret = int(input())
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(threshold - 1)]
    # Generate shares pairs as (x, P(x))
    shares = []
    for i in range(1, num_shares + 1):
        x = i
        y = sum((coeff * pow(x, exp, prime)) % prime for exp, coeff in enumerate(coefficients)) % prime
        shares.append((x, y))
    return shares

def reconstruct_secret(shares, prime=nextprime(10**96)):
    # Reconstruct the initial value using Lagrange interpolation
    def lagrange_interpolate(x, x_s, y_s, prime):
        total = 0
        for i in range(len(x_s)):
            xi, yi = x_s[i], y_s[i]
            li = 1
            for j in range(len(x_s)):
                if i != j:
                    xj = x_s[j]
                    li *= (x - xj) * mod_inverse(xi - xj, prime)
                    li %= prime
            total += yi * li
            total %= prime
        return total

    x_s, y_s = zip(*shares)
    return lagrange_interpolate(0, x_s, y_s, prime)

def words_to_number():
    print("Input the number of words to encode: ")
    n = int(input())

    encoded = ""
    for i in range(n):
        not_valid_word = True
        while (not_valid_word):
            print("\nType word {}:".format(i+1))
            inword = input()
            try:
                index = str(words.index(inword)).zfill(4)
            except Exception:
                print("\nWord not found, re-enter the word {}".format(i+1))
            else:
                encoded += index
                not_valid_word = False

    return encoded


with open("english.txt", 'r') as file:
    words = file.read().split('\n')[:-1]
while(True):
    print ("Select desired action")
    print("1 - Convert words to encryptable numbers")
    print("2 - Convert encryptable number to shares using SSS")
    print("3 - Recover original phrase from shares")
    selection = int(input())

    if (selection == 1):
        encoded = words_to_number()
        print("\nNumber encoding the words ready to encrypt with SSS:")
        print(encoded)

    elif(selection == 2):
        sss_shares = encrypt_with_SSS()
        print("Save this shares as pairs, both number of each pair are important for recovering the secret")
        print(sss_shares)
        
    elif(selection == 3):
        print("Indicate how many shares you need to recover your secret")
        n_shares = int(input())
        shares = []
        for i in range(n_shares):
            print("\nShare N.", i+1)
            print("Input the first share component (i.e. the index of the share)")
            index = int(input())
            print("Input the second component of the share (i.e. the large number)")
            number = int(input())
            shares.append((index, number))
        secret = reconstruct_secret(shares=shares[:4])
        secret_str = str(secret)
        secret_reconstructed = '0'*((4- (len(secret_str)%4)) if (len(secret_str)%4)>0 else 0)
        secret_reconstructed += secret_str
        print("\nOriginal Phrase is: ")
        for i in range(int(len(secret_reconstructed)/4)):
            print(words[int(secret_reconstructed[(i*4):(i*4+4)])])
        print()
