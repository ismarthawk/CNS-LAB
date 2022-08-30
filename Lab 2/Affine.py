from math import gcd



def getInverse(num) : 
    if gcd(num, 26) != 1 :
        return float('-inf')
    for i in range(1,26) : 
        if (num * i) % 26 == 1 : return i
    return float('-inf')


class Affine : 
    def encrypt(self, plain, key) :
        a, b = key
        aInv = getInverse(a)
        if aInv == float('-inf') : return 'Invalid a value in key'
        res = ''
        for char in plain : 
            num = ord(char) - 97
            newNum = ((a * num) + b) % 26
            res += chr(newNum + 97)
        return res.upper()
        
        
    def decrypt(self, cipher, key) :
        a, b = key
        aInv = getInverse(a)
        if aInv == float('-inf') : return 'Invalid a value in key'
        res = ''
        cipher = cipher.lower()
        for char in cipher : 
            num = ord(char) - 97
            k = (num - b + 26) % 26
            newNum = (k * aInv) % 26
            res += chr(newNum + 97)
        return res


if __name__ == "__main__" : 
    plain = 'affine'
    key = (17, 20)
    print(Affine().encrypt(plain, key))
    print(Affine().decrypt('UBBAHK', key))
