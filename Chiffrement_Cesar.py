alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cesarMoins(c,n):
    for i in range(0,26):
        if c==alpha[i]:
            x=i
            break 
    p=x-n    
    if p<0:
        return alpha[26+p]
    else:
        return alpha[x-n]

def cesarPlus(c,n):
    for i in range(0,26):
        if c==alpha[i]:
            x=i
            break 
    p=x+n    
    if p>25:
        dec=26-x
        deca=n-dec
        return alpha[deca]
    else:
        return alpha[x+n]

def chiffrer(msg,k):
    chainchiffrer = ''
    for i in range(len(msg)):
        chainchiffrer = chainchiffrer + cesarPlus(msg[i],k)
    return chainchiffrer

def dechiffrer(msg,k):
    chaindechiffrer = ''
    for i in range(len(msg)):
        chaindechiffrer = chaindechiffrer + cesarMoins(msg[i],k)
    return chaindechiffrer 

msg=input("entrer le message a chiffrer : ")
k=int(input("entrer la cle de Cesar : "))
cypher = chiffrer(msg,k)
print("le message en claire  :"+msg)
print("le message chiffre  :"+cypher)
print("------------------------------------------")
msg2=input("entrer le message a dechiffrer : ")
k=int(input("entrer la cle de Cesar : "))
msg = dechiffrer(msg2,k)  
print("le message chiffre  :"+msg2)
print("le message dechiffre  :"+msg)

