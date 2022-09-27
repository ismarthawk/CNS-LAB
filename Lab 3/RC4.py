

cipher_text = []


def encryption(key,plain_text,n):    
    S = [i for i in range(0, 2**n)]
    key_list = [key[i:i + n] for i in range(0, len(key), n)] 
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2) 
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)
    print("Plain text ( in array form ): ", pt) 
    diff = int(len(S)-len(key_list))
    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])
    print("Key list : ", key_list)
        
 
    print("KSA iterations : ")
    KSA(S,key_list)
    print(" ")
     
    key_stream = []
    print("PGRA iterations : ")
    print(" ")
    PGRA(key_stream,S)
    
    XOR(cipher_text,key_stream,pt)
 
    encrypted_to_bits = ""
    for i in cipher_text:
        encrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
    print("Cipher text : ", encrypted_to_bits)
    
    

def KSA(S,key_list):
        j = 0
        N = len(S)         
        for i in range(0, N):           
            j = (j + S[i]+key_list[i]) % N             
            S[i], S[j] = S[j], S[i]
            print(i, " ", end ="")             
            print(S)
        initial_permutation_array = S
        print(" ")
        print("The initial permutation array is : ",initial_permutation_array)


        
        

def XOR(cipher_text,key_stream,pt):
        for i in range(len(pt)):
            c = key_stream[i] ^ pt[i]
            cipher_text.append(c)

def PGRA(key_stream,S):
        N = len(S)
        i = j = 0
        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N             
            S[i], S[j] = S[j], S[i]
            print(k, " ", end ="")
            print(S)
            t = (S[i]+S[j]) % N
            key_stream.append(S[t])
        print("Key stream : ", key_stream)
        print(" ")
        


plain_text = "001010010010"
key = "101001000001"
n = 3 




encryption(key,plain_text,n)

def decryption(cipher_text):
    S = [i for i in range(0, 2**n)]
    key_list = [key[i:i + n] for i in range(0, len(key), n)]
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)
    diff = int(len(S)-len(key_list))
    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])
    KSA(S,key_list)
 
    key_stream = []
    print("PGRA iterations : ")
    PGRA(key_stream,S)
 
    original_text = []
    XOR(original_text,key_stream,cipher_text)
 
    decrypted_to_bits = ""
    for i in original_text:
        decrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
 
    print("Decrypted text : ",decrypted_to_bits)
  
  

decryption(cipher_text)


