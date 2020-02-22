from tkinter import *

def welcometips():
    welcomert = Tk()
    welcomert.title("Başlarken")
    welcomert.geometry("685x300")
    welcomert.resizable(False,False)
    welcomert.config(bg="#202020")

    brandfont = ('roboto', 30)
    labelfont = ('roboto', 10)

    brandlabel = Label(welcomert,text="Başlarken",bg="#202020",fg="#fff")
    brandlabel.config(font=brandfont)
    brandlabel.pack()
    brandlabel.place(x=10,y=10)

    onetext = Label(welcomert,text="> İlk Önce Asistan'a 'Bilgilerimi Kaydet' yazarak kişisel bilgilerinizi kaydedebilirsiniz.",bg="#202020",fg="#fff")
    onetext.config(font=labelfont)
    onetext.pack()
    onetext.place(x=10,y=70)

    twotext = Label(welcomert,text="> Ardından 'Asistan Bilgilerini Kaydet' yazarak asistana vermek istediğiniz bilgileri kaydedebilirsiniz.",bg="#202020",fg="#fff")
    twotext.config(font=labelfont)
    twotext.pack()
    twotext.place(x=10,y=90)

    thtext = Label(welcomert,text="> Tüm komutları Komutlar.txt dosyasından bulabilirsiniz.",bg="#202020",fg="#fff")
    thtext.config(font=labelfont)
    thtext.pack()
    thtext.place(x=10,y=110)

    auttext = Label(welcomert,text="> https://kilavuzkod.blogspot.com | Enes Kasapoğlu",bg="#202020",fg="#fff")
    auttext.pack()
    auttext.place(x=10,y=280)

    welcomert.mainloop()