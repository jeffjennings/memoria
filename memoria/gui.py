import sys
import os
import tkinter as tk
from tkinter import font, Tk

from memoria.inputs import books, card_types, languages
from memoria.helper_funcs import update_card, colors
import memoria
memoria_path = os.path.dirname(memoria.__file__)

def get_dictionary(book, card_type):
    """Load the selected dictionary"""

    sys.path.append(os.path.join(memoria_path, f"dictionaries/en_it/{book}"))
    if card_type == 'Vocabulary':
        import vocab
        return vocab.vocab
    elif card_type == 'Grammar':
        import grammar 
        return grammar.grammar
    else:
        import phrases
        return phrases.phrases


def selection_gui(books, card_types, languages):
    """Create a GUI with options to select a book from which to 
    generate a given type of flaschards in a given language"""
    root = Tk()
    base_font = font.Font(family='Lato', size=16, weight='bold')
    # root.geometry("850x250")
    root.geometry("2400x2400")
    # root.configure(bg='#494949')
    root.title("Book and flashcard type selection")

    # book to draw flashcards from
    chosen_book = tk.StringVar(root, value=list(books)[0])
    
    book_dropdown = tk.OptionMenu(root, 
                                chosen_book, 
                                *list(books),
                                )
    book_dropdown.grid(row=0, column=1, padx=10, pady=10)
    book_lab.grid(row=0, column=0, padx=10, pady=10)

    # flashcard type (vocab, grammar, phrases)
    chosen_type = tk.StringVar(root, value=card_types[0])

    type_dropdown = tk.OptionMenu(root, 
                                chosen_type,
                                *card_types,
                                )

    # flashcard language
    chosen_language = tk.StringVar(root, value=languages[0])

    type_dropdown = tk.OptionMenu(root, 
                                chosen_language,
                                *languages,
                                )
    type_dropdown.grid(row=2, column=1, padx=10, pady=10)    
    # folder name for book dictionaries
    book_module = books[chosen_book.get()]
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