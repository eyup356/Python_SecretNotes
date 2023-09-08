from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cryptocode

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
def button1_clicked():
    secret = text.get("1.0", END)
    masterkey = entry1.get()
    if not secret.strip() or not masterkey.strip():
        messagebox.showinfo(title="WARNING !!!", message="Not empty encrypted string or master, please input any value")
        return
    else:
        decrypted_secret = cryptocode.decrypt(secret, masterkey)
        text.delete("1.0", END)
        text.insert(END, decrypted_secret)
def button_clicked():
    title = entry.get()
    secret = text.get("1.0", END)
    if not title.strip() or not secret.strip():
        messagebox.showinfo(title="WARNING !!!", message="Not empty title or secret please input any value")
    else:
        masterkey = entry1.get()
        encoded_text = cryptocode.encrypt(secret, masterkey)
        with open('secret.txt', 'a') as file:
            file.write(title + '\n')
            file.write(encoded_text + '\n')
        messagebox.showinfo(title="RECORD", message="Your secret notes added")
        text.delete("1.0", END)
        entry1.delete(0, END)
        entry.delete(0,END)
button = Button(text="Save & Encrypt", command=button_clicked)
button.config()
button.pack()
spacer2 = Label(window, text="", height=1)
spacer2.pack()
button1 = Button(text="Decrypt", command=button1_clicked)
button1.config()
button1.pack()
window.mainloop()