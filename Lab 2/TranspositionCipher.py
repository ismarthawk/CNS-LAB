def encryptMessage(key,plaintext):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)
  
  
  

myMessage = input()
myKey=int(input())
ciphertext = encryptMessage(myKey, myMessage)
print(ciphertext)

