from tkinter import messagebox
from tkinter import *
from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Anahtar üretme işlemi
def generate_key():
    title = titleEntry.get()
    secret = secretEntry.get("1.0", END)
    master_key = masterEntry.get()

    if title != "" and secret != "" and master_key != "":
        # Başlığın zaten kullanılıp kullanılmadığını kontrol ediyoruz
        if os.path.exists("secrets.txt"):
            with open("secrets.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    if lines[i].strip() == title:
                        messagebox.showinfo("Bilgilendirme", "Bu başlık zaten kullanılıyor.")
                        return

        secret = secret.encode()
        key = base64.urlsafe_b64encode(hashlib.sha256(master_key.encode()).digest())
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(secret)
        with open("secrets.txt", "a") as file:
            file.write(title + "\n" + cipher_text.decode() + "\n" + key.decode() + "\n")
        infoLabel.config(text="Veri sorunsuz bir şekilde şifrelendi.")
    else:
        messagebox.showinfo("Bilgilendirme", "Verilerinizin tamamını giriniz.")

# Şifreli veriyi çözme işlemi
def decrypt_data():
    cipher_text = secretEntry.get("1.0", END).strip().encode()
    master_key = masterEntry.get()

    try:
        if os.path.exists("secrets.txt"):
            with open("secrets.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    if lines[i+1].strip().encode() == cipher_text:
                        key = lines[i+2].strip()
                        if key == base64.urlsafe_b64encode(hashlib.sha256(master_key.encode()).digest()).decode():
                            cipher_suite = Fernet(key.encode())
                            plain_text = cipher_suite.decrypt(cipher_text)
                            secretEntry.delete('1.0', END)
                            secretEntry.insert(END, plain_text.decode())
                            infoLabel.config(text="Veri çözüldü.")
                            return
    except Exception as e:
        messagebox.showinfo("Hata", f"Hata oluştu: {str(e)}")
    else:
        infoLabel.config(text="Verilerinizi kontrol ediniz.")
        messagebox.showinfo("Uyarı", f"Değerleri kontrol ediniz.")

window = Tk()
window.title("My Quiz")
window.geometry("400x700")
window.config(padx=20, pady=20)

titleLabel = Label(window, text="Enter your title")
titleLabel.pack()

titleEntry = Entry()
titleEntry.pack()

secretTitle = Label(text="Enter your secret")
secretTitle.pack()

secretEntry = Text()
secretEntry.pack()

masterTitle = Label(text="Enter master key")
masterTitle.pack()

masterEntry = Entry()
masterEntry.pack()

saveBtn = Button(text="Save & Encrypt", command=generate_key)
saveBtn.pack()

decBtn = Button(text="Decrypt", command=decrypt_data)
decBtn.pack()

infoLabel = Label(text="")
infoLabel.pack()

window.mainloop()
