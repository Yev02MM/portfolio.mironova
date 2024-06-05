from tkinter import *
from tkinter import ttk
import sqlite3

main = Tk()
main.geometry("1200x850")
main.title("Міронова Євгенія, 2 група, лабораторна робота 3")

tabs = ttk.Notebook(main)
tab1 = ttk.Frame(tabs, width=1200, height=800)
tab2 = ttk.Frame(tabs, width=1200, height=800)
tabs.add(tab1, text='Словник')
tabs.add(tab2, text='Про автора')
tabs.grid()


#tab1
#combobox
cb_categories = ttk.Combobox(tab1)
cb_categories.configure(font=("Colibri, 11"), values=["person", "anim","object","food", "abstract"])
cb_categories.place(relx=0.5, rely=0)

#table
conn = sqlite3.connect(r"C:\Users\Lenovo\PycharmProjects\pythonProject\lab3bd.db")
curs = conn.cursor()
curs.execute("SELECT * from vocab Order by croatian")
word_list = []

for i in range(50):
    word_list.append(curs.fetchone())
    for j in range(8):
        e = Entry(tab1, width=11)
        e.insert(0, word_list[i][j])
        e.grid(row=i, column=j)



#таб2
label_name = Label(tab2, font=("Arail", 16, "bold"), text = "Роботу виконала студентка 4 курсу 2 групи "
                                                            "спеціальності Прикладна (комп'ютерна) лінгвістика та англійська мова "
                                                            "Міронова Євгенія ",
                   wraplength=300, justify="center")
label_name.place(relx=0.5, rely=0.5, anchor=CENTER)


main.mainloop()
