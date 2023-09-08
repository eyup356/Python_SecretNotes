from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import Crypto

window = Tk()
window.title("Python Tkinter")
window.minsize(width=400, height=700)
window.config(padx=20, pady=50)

original_image = Image.open("hacker.png")
resized_image = original_image.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)

panel = Label(window, image=img)
panel.config(padx=200, pady=200)
panel.pack()

# label
label = Label(text="Enter Your Title")
label.pack()
label.config(padx=20, pady=20)

entry = Entry(width=20)
entry.pack()

# label
label2 = Label(text="Enter Your Secret")
label2.pack()
label2.config(padx=20, pady=5)

text = Text(width=40)
text.pack()

# label
label3 = Label(text="Enter Master Key")
label3.pack()
label3.config(padx=20, pady=5)

entry1 = Entry(width=20)
entry1.config()
entry1.pack()

spacer = Label(window, text="", height=1)
spacer.pack()


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
        encrypted_bytes = cipher.encrypt(secret)
        encrypted_string = base64.b64encode(encrypted_bytes).decode()

        with open("secret.txt", "a") as file:
            file.write(title + "\n")
            file.write(encrypted_string + "\n")

        messagebox.showinfo(title="RECORD", message="Your secret notes added")


import cryptography


import cryptography


def decrypt_text(masterkey, encrypted_secret):
    key, iv = generate_key_iv(masterkey)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_bytes = base64.b64decode(encrypted_secret.encode())
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # if not cryptography.is_bytes_non_start(decrypted_bytes):
    #     raise UnicodeDecodeError("Invalid UTF-8 byte found")

    decrypted_string = decrypted_bytes.rstrip(b' ').decode('utf-8')

    return decrypted_string






def button1_clicked():
    masterkey = entry1.get()

    encrypted_secret = text.get("1.0", END)
    decrypted_secret = decrypt_text(masterkey, encrypted_secret)
    text.delete("1.0", END)
    text.insert(END, decrypted_secret)


button = Button(text="Save & Encrypt", command=button_clicked)
button.config()
button.pack()

spacer2 = Label(window, text="", height=1)
spacer2.pack()

button1 = Button(text="Decrypt", command=button1_clicked)
button1.config()
button1.pack()

window.mainloop()
