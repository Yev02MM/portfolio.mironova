import tkinter as tk
from tkinter import ttk

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App!!")

        # Button
        self.button = tk.Button(root, text="Do not click here:)", command=self.on_button_click)
        self.button.pack()

        # Label
        self.label = tk.Label(root, text="Mironova Evhenia", font=("Arial", 16), fg="blue", bg="yellow",  width=30)
        self.label.pack()

        # Entry (Single-line text box)
        self.entry = tk.Entry(root, font=("Showcard Gothic", 20), fg="green", bg="white",  width=50)
        self.entry.insert(0, "Hi, my name is Mironova Evhenia")
        self.entry.pack()

        # Text (Multi-line text box)
        self.text = tk.Text(root, font=("Papyrus", 23, "bold"), fg="purple", bg="coral", height=4, width=30)
        self.text.insert(tk.END, "Mironova Evhenia")
        self.text.pack()

        # ComboBox
        self.combobox = ttk.Combobox(root, values=["Evhenia", "Zhenya", "Jecka))"], font=("Veranda", 10))
        self.combobox.set("Select nickname")
        self.combobox.pack()

        # CheckBox
        self.checkbox = tk.Checkbutton(root, text="Mironova Evhenia", font=("Arial", 10), fg="brown", bg="white")
        self.checkbox.pack()

        # RadioButton
        self.radio_button = tk.Radiobutton(root, text="also Mironova Evhenia!!", font=("Arial", 10), fg="orange", bg="white")
        self.radio_button.pack()

        self.radio_button = tk.Radiobutton(root, text="oops, also Evhenia!", font=("Veranda", 10), fg="coral", bg="yellow")
        self.radio_button.pack()

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
