import tkinter as tk
from tkinter import font, Tk, ttk

from memoria.dictionaries import * 
from memoria.helper_funcs import update_card

source_dict = nie_c1_v # temporary
book = chapter = card_type = 0 # temporary

books = ["New Italian Espresso: A0 - A1.5", 
         "New Italian Espresso: A1.5 - B1",
         "Nuovo Espresso: B2",
         "Nuovo Espresso: C1",
         "Nuovo Espresso: C2",
         "Italian Grammar in Practice",
         "English Grammar for Students of Italian",
         "Pocket Italian Grammar",
         ]

root = Tk()
root.geometry("2385x1600")
root.configure(bg='#494949')
root.title("Flashcards")

# button text
text_font = font.Font(family='Lato', size=22, weight='bold')

chosen_book = tk.StringVar(root)
chosen_book.set(books[0])

book_dropdown = ttk.Combobox(root, state='readonly', textvariable=chosen_book, values=books)
lab = tk.Label(root, text="Book:", fg='blue')
book_dropdown.grid(row=0, column=4)
lab.grid(row=0, column=4)

def make_flashcards(book, chapter, card_type):
    cards = []
    counter = 0 

    nrow = ncol = 5

    for ii in range(nrow):
        # vary button size with window size
        # root.columnconfigure(ii, weight=1, minsize=150)
        # root.rowconfigure(ii, weight=1, minsize=100)

        for jj in range(ncol):
            try:
                word = list(source_dict)[counter]
            except IndexError:
                break

            flashcard = tk.Button(
                root,
                text=f"\n {word}",
                command=lambda idx=counter: update_card(cards[idx], 
                                                        list(source_dict)[idx], 
                                                        source_dict, 
                                                        ),
                anchor='n', # text alignment
                font=text_font,
                bg='#3393FF',
                fg="#494949", # text color
                activebackground="#38C5E8",
                activeforeground="#494949", # text color when moused over
                width=20, # fix button width
                height=6,
            )
            
            flashcard.grid(row=ii, column=jj, sticky='nsew', padx=10, pady=10)

            cards.append(flashcard)

            counter += 1

make_flashcards(book, chapter, card_type)

root.mainloop()