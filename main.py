from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    try:
        enc = base64.urlsafe_b64decode(enc).decode()  # Hata düzeltilmiş hali
    except:
        messagebox.showinfo("Hata", "Şifre çözme başarısız. Lütfen doğru şifreyi girin.")
        return ""

    dec = []
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def decrypt_notes():
    message_encrypted = tk1_text.get("1.0", END).strip()
    master_secret = tk2_entry.get().strip()

    if not message_encrypted or not master_secret:
        messagebox.showinfo("Hata", "Eksik giriş yaptınız.")
        return

    decrypted_message = decode(master_secret, message_encrypted)

    if decrypted_message:
        tk1_text.delete("1.0", END)  # Mesaj kutusunu temizleme
        tk1_text.insert("1.0", decrypted_message)  # Çözülen metni ekleme

def save_and_note():
    title = tk1_entry.get().strip()
    mesaj = tk1_text.get("1.0", END).strip()
    sifre = tk2_entry.get().strip()

    if not title or not mesaj or not sifre:
        messagebox.showinfo("Uyarı", "Başlık, mesaj veya şifre boş bırakılamaz.")
        return

    massage_encrypted = encode(sifre, mesaj)

    try:
        with open("mysecret.txt", "a", encoding="utf-8") as data_file:
            data_file.write(f"\n{title}\n{massage_encrypted}\n")
        messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya kaydedilirken hata oluştu: {e}")

    tk1_text.delete("1.0", END)
    tk1_entry.delete(0, END)
    tk2_entry.delete(0, END)

# Arayüz
ekran1 = Tk()
ekran1.minsize(350, 600)
ekran1.title("Gizli Notlar Yaz")
FONT = ("Verdana", 9, "normal")
FONT1 = ("Verdana", 7, "normal")

# Resim yükleme
try:
    orijinal_resim = Image.open("img.png")
    kucuk_resim = orijinal_resim.resize((210, 165))
    resim = ImageTk.PhotoImage(kucuk_resim)
    resim_lbl = Label(ekran1, image=resim)
    resim_lbl.place(x=65, y=15)
except:
    pass  # Eğer resim bulunamazsa hata vermesin

# Etiketler
Label(ekran1, text="Mesaj için Başlık Belirle", font=FONT).place(x=107, y=190)
Label(ekran1, text="Gizli mesajı yaz", font=FONT).place(x=127, y=240)
Label(ekran1, text="Gizli Mesaj için şifre belirle", font=FONT).place(x=93, y=467)

# Giriş alanları
tk1_entry = Entry(width=39)
tk1_entry.place(x=52, y=218)

tk1_text = Text(width=29, height=12)
tk1_text.place(x=52, y=260)

tk2_entry = Entry(width=39, show="*")  # Şifre girişini gizle
tk2_entry.place(x=52, y=490)

# Butonlar
Button(ekran1, text="Kaydet ve Şifrele", pady=1, padx=10, font=FONT1, command=save_and_note).place(x=118, y=517)
Button(ekran1, text="Şifresini Çöz", pady=1, padx=7, font=FONT1, command=decrypt_notes).place(x=134, y=548)

ekran1.mainloop()
