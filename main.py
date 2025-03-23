from tkinter import *
from PIL import Image, ImageTk
# pillowdan image ve ımage tk modüllerini aldık. png formatı olsaydı direkt eklerdik

ekran1 = Tk()
ekran1.minsize(350,600)
ekran1.title("Gizli Notlar Yaz.")
FONT = ("Verdana",9,"normal")
FONT1 = ("Verdana",7,"normal")

#  Resmi yükleme ve boyutunu küçültme
orijinal_resim = Image.open("img.png")  # Resmi değişkene açtık
kucuk_resim = orijinal_resim.resize((170, 165))  # diğer değişken içinde resize ile boyut belirttik Genişlik: 150px, Yükseklik: 100px
resim = ImageTk.PhotoImage(kucuk_resim) #resmi içerisine modül ile ekledik

#  Küçültülen resmi ekleme
resim_lbl = Label(ekran1, image=resim)  # resmi label içine ekledik
resim_lbl.place(x=90, y=15)  # Yeni konumlandırma


"""Grafik YÜZÜ"""
#lbl
tk_lbl = Label(ekran1, text="Mesaj için Başlık Belirle", font=FONT)
tk_lbl.place(x=107, y=190)
tk1_lbl = Label(ekran1, text="Gizli mesajı yaz.", font=FONT)
tk1_lbl.place(x=127, y=240)
tk2_lbl = Label(ekran1, text="Gizli Mesaj için şifre belirle", font=FONT)
tk2_lbl.place(x=93, y=467)

#text
tk1_text = Text(width=29, height=12) # height eni belirliyor
tk1_text.place(x=52, y=260)

#entry
tk1_entry = Entry(width=39)
tk1_entry.place(x=52, y=218)
tk2_entry = Entry(width=39)
tk2_entry.place(x=52, y=490)

#button
tk1_bttn = Button(ekran1, text="Kaydet ve Şifrele", pady=1, padx=10, font=FONT1)
tk1_bttn.place(x=118, y=517)
tk2_bttn = Button(ekran1, text="Şifresini Çöz", pady=1, padx=7, font=FONT1)
tk2_bttn.place(x=134, y=548)


ekran1.mainloop()