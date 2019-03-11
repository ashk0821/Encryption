e_dict = {}  # Global Variable; Encryption dictionary
d_dict = {}  # Global Variable; Decryption dictionary

# Loads a cipher from a specified file (Text file that has a list of letters followed by the encryption of the letters)
def load_cipher_file(file_name):

    cipher_file = open(file_name, "r")
    for line in cipher_file:
        temp = line.split("\t")
        x = temp[0].strip()
        y = temp[1].strip()
        e_dict[x] = y
        d_dict[y] = x

# Takes a message and encrypts/decrypts it and returns the altered message
def encrypt_or_decrypt_message(dictionary, msg):
    s = ""
    for i in msg.upper():
        d = dictionary.get(i, i)
        s += d
        s = s.strip("\n")
    return s

# Handles the user interaction in the program, asks what cipher to load, prints menu.
def main():
    file_name = input("Enter the filename of the cipher to use.")
    load_cipher_file(file_name)
    user = input("E- Encrypt a message \nD- Decrypt a message \nL- Load new cipher key \nQ- Quit")
    while user != "Q":
        if user == "Q":
            break
        elif user == "E":
            msg = input("What is the secret message?")
            p = encrypt_or_decrypt_message(e_dict, msg)
            print(p)
        elif user == "D":
            msg = input("What is the secret message?")
            p = encrypt_or_decrypt_message(d_dict, msg)
            print(p)
        elif user == "L":
            file_name = input("Enter the name of the new cipher you would like to use.")
            load_cipher_file(file_name)
        else:
            print("Invalid")
        user = input("E- Encrypt a message \nD- Decrypt a message \nL- Load new cipher key \nQ- Quit")

    print("Goodbye!")


main()
