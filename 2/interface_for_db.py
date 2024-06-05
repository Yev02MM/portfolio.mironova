from tkinter import *
from tkinter import ttk
import sqlite3

#проєкт
main = Tk()
main.geometry("600x600")
n=main.title("Міронова Євгенія, ПЛ, 2 група, ЛР 2")

#БД
label_result = Label(main, font=("Veranda, 16"))
label_result.configure(bg="lightgray")
label_result.place(x=250, y=50)

conn = sqlite3.connect(r"C:\Users\Lenovo\Downloads\pol_lab02.s3db")
curs = conn.cursor()
curs.execute("SELECT sgN from tnoun WHERE sgN LIKE 'P%'")
result = curs.fetchone()[0]
label_result.configure(text=result)

#таблиця
for i in range(13):
    for j in range(3):
        e = Entry(main, width=9, font=('Arail',11))
        e.insert(0, " ")
        e.grid(row=i, column=j)

def get_n_nouns():
    conn = sqlite3.connect(r"C:\Users\Lenovo\Downloads\pol_lab02.s3db")
    curs = conn.cursor()
    curs.execute("SELECT id, sgN, sgL from tnoun LIMIT 13")
    noun_list1 = []

    for i in range(13):
        noun_list1.append(curs.fetchone())
        for j in range(3):
            e = Entry(main, width=9, font=('Colibri',11))
            e.insert(0, noun_list1[i][j])
            e.grid(row=i, column=j)

#комбобокс
cb_nouns = ttk.Combobox(main, font=("Papyrus"))

def combobox():
    conn = sqlite3.connect(r"C:\Users\Lenovo\Downloads\pol_lab02.s3db")
    curs = conn.cursor()
    curs.execute("SELECT sgN from tnoun WHERE sgN LIKE 'P%'")
    noun_list = curs.fetchall()
    cb_nouns.configure(values=noun_list)

cb_nouns.place(y=300)

#кнопка
button = Button(main)
button.configure(text="Кнопка")
button.configure(font=("Comic Sans MS", 11))

button.configure(command=lambda:[get_n_nouns(),combobox()])
button.place(x=250, y=0)

main.mainloop()
