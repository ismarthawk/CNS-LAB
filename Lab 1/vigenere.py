class Vigenere : 
    def encrypt(self, plain, key) : 
        s = ''
        while len(s) < len(plain) :
            s += key 
        res = ''
        for ind, char in enumerate(plain) :
            k = ord(s[ind]) - 97
            num = ord(char) - 97
            newNum = (num + k) % 26
            res += chr(newNum + 97)
        return res.upper()
        
        
    def decrypt(self, cipher, key) : 
        s = ''
        cipher = cipher.lower()
        while len(s) < len(cipher) : 
            s += key
        res = ''
        for ind, char in enumerate(cipher) : 
            k = ord(s[ind]) - 97
            num = ord(char) - 97
            newNum = (num - k + 26) % 26
            res += chr(newNum + 97)
        return res



if __name__ == "__main__" : 
    print(Vigenere().encrypt('damodar','estate'))
    print(Vigenere().decrypt('HSFOWEV','estate'))
