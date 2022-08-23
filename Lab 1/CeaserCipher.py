class CeaserCipher : 
    def encrypt(self, message, key) : 
        res = ''
        for char in message : 
            num = ord(char) - 97
            # print(num)
            num += key
            num = num % 26
            newKey = 97 + num
            # print(char, newKey)
            res += chr(newKey)
        return res.upper()
        
    def decrypt(self, message, key) : 
        message = message.lower() 
        res = ''
        for char in message : 
            num = ord(char) - 97
            num -= key 
            num = ((26 + num) % 26) + 97
            
            res += chr(num)
        # print(res)
        return res 


if __name__ == "__main__" : 
    message  = 'damodar'
    key = 2
    print(CeaserCipher().encrypt(message, 2))
    print(CeaserCipher().decrypt('FCOQFCT', 2))
