'''
def generate_key_iv(masterkey):
    key = masterkey.encode().rjust(32)
    iv = get_random_bytes(16)
    return key, iv


def button_clicked():
    title = entry.get()
    secret = text.get("1.0", END)

    if not title.strip() or not secret.strip():
        messagebox.showinfo(title="WARNING !!!", message="Not empty title or secret please input any value")
    else:
        masterkey = entry1.get()
        key, iv = generate_key_iv(masterkey)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        secret = secret.encode()
        secret = secret + b' ' * (16 - len(secret) % 16)
        encrypted_bytes = cipher.encrypt(secret)
        encrypted_string = base64.b64encode(encrypted_bytes).decode()

        with open('secret.txt', 'a') as file:
            file.write(title + '\n')
            file.write(encrypted_string + '\n')

        messagebox.showinfo(title="RECORD", message="Your secret notes added")


def decrypt_text(masterkey, encrypted_text):
    key, iv = generate_key_iv(masterkey)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_bytes = base64.b64decode(encrypted_text.encode())
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_string = decrypted_bytes.rstrip(b' ')

    return decrypted_string.decode()




'''