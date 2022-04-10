from cryptography.fernet import Fernet
import pickle
import os

def decrypt_message(encrypted_message, filename):
    curr_d5 = os.getcwd()
    f = open(curr_d5 + "\\data_file\\" + filename + ".log", "rb")
    try:
        while True:
            x = pickle.load(f)
    except EOFError:
        f.close()
    key = x
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message)