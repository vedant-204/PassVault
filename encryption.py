from cryptography.fernet import Fernet
import os
import pickle

def generate_key(filename):
    curr_d4 = os.getcwd()
    key = Fernet.generate_key()
    f = open(curr_d4 + "\\data_file\\" + filename + ".log", "wb")
    pickle.dump(key,f)
    f.close()

def encrypt_message(message,filename):
    curr_d5 = os.getcwd()
    f = open(curr_d5 + "\\data_file\\" + filename + ".log", "rb")
    try:
        while True:
            x = pickle.load(f)
    except EOFError:
        f.close()
    key = x
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message