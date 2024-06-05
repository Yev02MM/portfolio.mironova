import tkinter as tk
from tkinter import ttk
import sqlite3
import locale

def show_definition(event):
    # Get the selected word from the listbox
    selected_word = word_listbox.get(word_listbox.curselection())

    # Retrieve the corresponding definition from the database
    conn = sqlite3.connect('phraseologies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT definition FROM dictionary WHERE word=?", (selected_word,))
    definition = cursor.fetchone()[0]
    conn.close()

    # Display the definition in the text widget
    definition_text.delete('1.0', tk.END)
    definition_text.insert(tk.END, definition)

def search_words():
    # Clear the listbox
    word_listbox.delete(0, tk.END)

    # Get the search term
    search_term = search_entry.get()

    # Retrieve the matching words from the database
    conn = sqlite3.connect('phraseologies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM dictionary WHERE word LIKE ?", ('%' + search_term + '%',))
    words = cursor.fetchall()
    conn.close()

    # Add the matching words to the listbox
    for word in words:
        word_listbox.insert(tk.END, word[0])

def sort_words():
    current_sort = sort_alpha_button['text']
    if current_sort == "Sort A-Z":
        sorted_words = sorted(words, key=lambda x: ukrainian_sort_key(x[0]))
        sort_alpha_button['text'] = "Sort Z-A"
    else:
        sorted_words = sorted(words, key=lambda x: ukrainian_sort_key(x[0]), reverse=True)
        sort_alpha_button['text'] = "Sort A-Z"
    word_listbox.delete(0, tk.END)
    for word in sorted_words:
        word_listbox.insert(tk.END, word[0])

def ukrainian_sort_key(word):
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    return [alphabet.index(c.upper()) for c in word if c.upper() in alphabet]

def retrieve_words():
    word_listbox.delete(0, tk.END)
    words.clear()
    definitions.clear()
    conn = sqlite3.connect('phraseologies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT word, definition FROM dictionary")
    rows = cursor.fetchall()
    for row in rows:
        word = row[0]
        definition = row[1]
        words.append((word, definition))
        definitions.append(definition)
        word_listbox.insert(tk.END, word)
    conn.close()

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

# Create the main window
root = tk.Tk()
root.title("Dictionary")

# Create a search entry
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=0, sticky=tk.EW)

# Create a search button
search_button = ttk.Button(root, text="Search", command=search_words)
search_button.grid(row=0, column=1, sticky=tk.W)

# Create a listbox to display the words
word_listbox = tk.Listbox(root, width=0)  # Set width to 0 to adjust dynamically
word_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

# Create a scrollbar for the listbox
scrollbar = ttk.Scrollbar(root)
scrollbar.grid(row=1, column=2, sticky=tk.NS)
word_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=word_listbox.yview)

# Create a text widget to display the definitions
definition_text = tk.Text(root)
definition_text.grid(row=0, column=3, rowspan=2, sticky=tk.NSEW)

# Configure column and row weights
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, minsize=40)

# Create a button to retrieve words
retrieve_button = ttk.Button(root, text="Retrieve Words", command=retrieve_words)
retrieve_button.grid(row=3, column=0, sticky=tk.W)

# Create a button to sort the words in alphabetical order
sort_alpha_button = ttk.Button(root, text="Sort A-Z", command=sort_words)
sort_alpha_button.grid(row=3, column=1, sticky=tk.W)

# Initialize lists to store words and definitions
words = []
definitions = []


# Retrieve words from the database initially
retrieve_words()

# Connect to the database
conn = sqlite3.connect('phraseologies.db')
cursor = conn.cursor()

# Retrieve all the words from the database
cursor.execute("SELECT word FROM dictionary")
words = cursor.fetchall()

# Determine the width based on the length of the longest word
word_width = max(len(word[0]) for word in words)
word_listbox.config(width=word_width)

# Add the words to the listbox
for word in words:
    word_listbox.insert(tk.END, word[0])


# Close the database connection
conn.close()

# Bind the event handler to the listbox selection
word_listbox.bind('<<ListboxSelect>>', show_definition)

# Start the Tkinter event loop
root.mainloop()
