import argparse
import os

# Encryption function
def encryption(plain_text , key):
    ciphertext = ""
    for letter in plain_text:
        tmp = (ord(letter) + key) % 256
        ciphertext += chr(tmp)

    return ciphertext

# Decryption function
def decryption(ciphertext , key):
    plain_text = ""
    for letter in ciphertext:
        tmp = (ord(letter) - key) % 256
        plain_text += chr(tmp)

    return plain_text

# Cheking if the user's directory input is valid
def is_valid_file_dir(path):
    if not os.path.isfile(path):
        print("Error: File does not exist.")
        return False
    elif not path.lower().endswith(".txt"):
        print("Error: Invalid file format. Only .txt files are supported.")
        return False
    else:
        return True

# Check if its is a valid key
def is_valid_key(k):
    k = int(k)
    if k >=0 :
        return True
    else :
        print("Error: Key must be a positive integer.")
        return False

# Get the text from the txt file
def read_file(path):
    opened_file = open(path, 'rt',encoding='utf-8')
    text = opened_file.read()
    return text

# Encrypt the text in the file function
def encrypt_file(path,key):
    text = read_file(path)
    ciphertext = encryption(text,key)
    opened_file = open('ciphertext.txt', 'w' ,encoding='utf-8')
    opened_file.write(ciphertext)
    opened_file.close()
    print("Encryption successful. The ciphertext is in ciphertext.txt .")

# Decrypt the text in the file function
def decrypt_file(path,key):
    text = read_file(path)
    plaintext = decryption(text,key)
    opened_file = open('plaintext.txt', 'w' ,encoding='utf-8')
    opened_file.write(plaintext)
    opened_file.close()
    print("Decryption successful. The plaintext is in plaintext.txt .")

# Preparing the parser
def prs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory" ,required=True, help="Specify the file directory that you want to Encrypt/Decrypt , it must be .txt file type ")
    parser.add_argument("-o","--option" , required=True,help="Choose ['e','E'] for Encrypting the file or ['d','D'] for Decrypting the file")
    parser.add_argument("-k","--key" , required=True,help="The encryption/decryption key")
    
    args = parser.parse_args()
    return args

# Our main function
def caesar(arg):
    file_path = str(arg.directory)
    option = str(arg.option).lower()
    key = int(arg.key)

    if option == 'e':
        if is_valid_file_dir(file_path) and is_valid_key(key):
            encrypt_file(file_path, key)
    elif option == 'd':
        if is_valid_file_dir(file_path) and is_valid_key(key):
            decrypt_file(file_path, key)
    else:
        print("Error: Invalid option. Use 'e' for encryption or 'd' for decryption.")

    

if __name__ == "__main__":
    args = prs()
    caesar(args)
    
    
