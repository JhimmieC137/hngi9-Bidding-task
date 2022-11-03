from cryptography.fernet import Fernet

key = Fernet.generate_key()   #generates new keys for hashing
f = Fernet(key)



def encryption(payload):
    ciphertext = f.encrypt(payload)  #payload variable is hashed 
    return ciphertext
