import tkinter as tk
from tkinter import font, Tk, ttk

from memoria.vocab import * 
from memoria.grammar import *
from memoria.phrases import *
from memoria.helper_funcs import update_card

source_dict = nie_c1_v # temporary
book = chapter = card_type = 0 # temporary

def selection_gui():
    books = ["New Italian Espresso: A0 - A1.5", 
            "New Italian Espresso: A1.5 - B1",
            "Nuovo Espresso: B2",
            "Nuovo Espresso: C1",
            "Nuovo Espresso: C2",
            "Italian Grammar in Practice",
            "English Grammar for Students of Italian",
            "Pocket Italian Grammar",
            ]
    
    types = ["word", "grammar", "phrase"]

    root = Tk()
    root.geometry("850x250")
    root.title("Book and flashcard type selection")
    base_font = font.Font(family='Lato', size=16, weight='bold')

    # book to draw flashcards from
    chosen_book = tk.StringVar(root)
    chosen_book.set(books[0])

    book_dropdown = ttk.Combobox(root, 
                                state='readonly', 
                                textvariable=chosen_book, 
                                values=books,
                                width=40,
                                font=base_font,
                                )
    book_lab = tk.Label(root, text="Book:", fg='#C70039', font=base_font)
    book_dropdown.grid(row=0, column=1, padx=10, pady=10)
    book_lab.grid(row=0, column=0, padx=10, pady=10)

    # flashcard type (vocab, grammar, phrase)
    chosen_type = tk.StringVar(root)
    chosen_type.set(types[0])

    type_dropdown = ttk.Combobox(root, 
                                state='readonly', 
                                textvariable=chosen_type,
                                values=types,
                                width=40,
                                font=base_font,
                                )
    type_lab = tk.Label(root, text="Entry type:", fg='#FF5733', font=base_font)
    type_dropdown.grid(row=1, column=1, padx=10, pady=10)
    type_lab.grid(row=1, column=0, padx=10, pady=10)

    selection_button = tk.Button(
        root,
        text="Generate flashcards",
        command=flashcard_gui(chosen_book.get(), chosen_type.get()),
        font=base_font,
        bg='#FFC300',
        fg="#303030", # text color
        activebackground="#303030",
        activeforeground="#FFC300", # text color when moused over    
        width=40, # fix button width
        height=2,
    )
    selection_button.grid(row=2, column=1, padx=10, pady=10)

    # return root
    root.mainloop()

def flashcard_gui(book, card_type):
    root = tk.Toplevel()
    root.geometry("2385x1600")
    root.configure(bg='#494949')
    root.title("Flashcards")
    base_font = font.Font(family='Lato', size=22, weight='bold')

    cards = []
    counter = 0 

    nrow = ncol = 5

    for ii in range(nrow):
        # vary button size with window size
        root.columnconfigure(ii, weight=1, minsize=150)
        root.rowconfigure(ii, weight=1, minsize=100)

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
                font=base_font,
                bg='#3393FF',
                fg="#494949", # text color
                activebackground="#38C5E8",
                activeforeground="#494949", # text color when moused over
            )
            
            flashcard.grid(row=ii, column=jj, sticky='nsew', padx=10, pady=10)

            cards.append(flashcard)

            counter += 1

selection_gui()
# root = selection_gui()
# root.mainloop()