import math
def gcdcheck(a,b):
    if math.gcd(a,b)==1:
        return True
    return False
  
  
  

def multiplicativeinverse(a,n):
    for i in range(1,n):
        if(((a%n)*(i%n))%n==1):
            return i
    return -1


  
  def decryptattack(plaintext,ciphertext):
    for a in range(1,26,1):
        for b in range(26):
            if gcdcheck(a,b):
                temp=""
            a1=multiplicativeinverse(a,26)
            for i in ciphertext:
                c=ord(i)-97
                k=(c-b)%26
                if k<0:
                    k=((c-b)%26+26)%26
                p=(k*a1)%26    
                temp+=chr(p+97)
            if temp == plaintext:
                return a,b
              
 

decryptattack("pq","if")

