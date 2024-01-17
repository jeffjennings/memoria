import tkinter as tk
from tkinter import font
import webbrowser

root = tk.Tk()
root.geometry("2400x1600")
root.configure(bg='#494949')
root.title(f"Chapter(s) 1")

text_font = font.Font(family='Lato', size=36, weight='bold')


def look_up_word(word, reference_type):
    if reference_type in ['define', 'conjugate']:
        if reference_type == 'define':
            link = f"https://www.wordreference.com/iten/{word}"
        else: 
            link = f"https://sapere.virgilio.it/parole/coniuga-verbi/{word}"

        webbrowser.open(link, new=2)

    else:
        pass


cards = []
counter = 0 

for ii in range(3):
    root.columnconfigure(ii, weight=1, minsize=150)
    root.rowconfigure(ii, weight=1, minsize=100)

    for jj in range(3):
        word = 'blah'

        flashcard = tk.Button(
            master=root,
            text=f"\n {word}",
            command=lambda idx=counter: translate(cards[idx]),
            anchor='n', # text alignment
            font=text_font,
            bg='#3393FF',
            fg="#494949", # text color
            activebackground="#38C5E8",
            activeforeground="#494949", # text color when moused over
        )
        
        flashcard.grid(row=ii, column=jj, sticky='nsew', padx=5, pady=5)

        cards.append(flashcard)

        counter += 1

root.mainloop()