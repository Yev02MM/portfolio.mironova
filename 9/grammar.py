#lectures 10-11

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

my_dict = {
    "ja": "pjevam",
    "ti": "pjevaš",
    "on/ona/ono": "pjeva",
    "mi": "pjevamo",
    "vi": "pjevate",
    "oni/one/ona": "pjevaju"
}


main = Tk()
main.geometry("1200x850")
main.title("Міронова Євгенія")

tabs = ttk.Notebook(main)
tab1 = ttk.Frame(tabs, width=1200, height=800)
tab2 = ttk.Frame(tabs, width=1200, height=800)
tabs.add(tab1, text='Загальна інформація')
tabs.add(tab2, text='Тести')
tabs.grid()

#tab1
label_name = Label(tab1, font=("Arial",18), text = "Іменники, прикметники, займенники та числівники змінюються за відмінками. Дієслово має розвинену систему дієвідміни: чотири ряди простих та складних форм минулого часу, два ряди форм майбутнього часу. Інфінітив може заміняти конструкція зі сполучника «da» і форми теперішнього часу. Наприклад, кореневим прикметником до слова “красивий” є “lijep-“, і ви можете створювати такі форми, як “lijepa” (жіночий, називний) або “lijepim” (чоловічий/середній, інструментальний), використовуючи різні закінчення.")
label_name.configure(wraplength=900)
label_name.place(relx=0.5, rely=0.5, anchor=CENTER)

#ttab2
#радіокнопочки
def create_rb(options,var):
    buttons = []
    for i, option in enumerate(options):
        button = Radiobutton(tab2, text=option, variable=var, value=i)
        button.pack()
        buttons.append(button)
    return buttons

random_key = random.choice(list(my_dict))
question_text = f'Поставте слово pjevati в особу {random_key} теперішнього часу'
question_label = Label(tab2, text=question_text, font=('Arial', 13))
question_label.pack()

options = list(my_dict.values())
correct_answear = my_dict[random_key]
options.remove(correct_answear)

incorrect_options = set()
while len(incorrect_options) < 3:
    incorrect_option = random.choice(options)
    if incorrect_option != correct_answear:
        incorrect_options.add(incorrect_option)

options = list(incorrect_options)
options.append(correct_answear)
random.shuffle(options)
var1 = StringVar()
create_rb(options, var1)

#кнопочка відповісти
button = Button(tab2)
button.configure(text="Відповісти")
button.configure(font=("Arial", 18))

def show_result():
    selected = var1.get()
    if options[int(selected)] == correct_answear:
        showinfo(title="Результат", message="Правильна відповідь!")
    else:
        showinfo(title="Результат", message=f"Невірно. Правильна відповідь {correct_answear} ")

button.configure(command = show_result)
button.pack()


main.mainloop()
