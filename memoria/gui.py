from math import ceil
import tkinter as tk
from tkinter import font, Tk
import random 
# random.seed(47)

from memoria.inputs import books, card_types, languages, supported_languages
from memoria.helper_funcs import get_dictionary, update_card, colors

def base_gui(supported_languages):
    """Create a GUI with the option to select a language to study"""
    root = Tk()
    base_font = font.Font(family='Lato', size=16, weight='bold')
    root.geometry("2400x2400")
    root.title("Flashcard selection")

    base_language = tk.StringVar(root, value="")
    
    base_lang_dropdown = tk.OptionMenu(root, 
                                  base_language, 
                                  *list(supported_languages), 
                                  command= selection_gui(books, 
                                                         card_types, 
                                                         languages, 
                                                         base_font)
                                )
    base_lang_dropdown.grid(row=0, column=1, padx=10, pady=10)
    base_lang_dropdown.config(font=base_font, fg=colors[5], width=30)

    base_lang_lab = tk.Label(root, text="Language to study:", fg=colors[5], font=base_font)
    base_lang_lab.grid(row=0, column=0, padx=10, pady=10)

    root.mainloop()


def selection_gui(books, card_types, languages, base_font):
    """Create a GUI with options to select a book from which to 
    generate a given type of flaschards in a given language"""
    win0 = tk.Toplevel()
    base_font = font.Font(family='Lato', size=16, weight='bold')
    win0.geometry("2400x2400")
    win0.title("Flashcard selection")

    # book to draw flashcards from
    chosen_book = tk.StringVar(win0, value=list(books)[0])
    
    book_dropdown = tk.OptionMenu(win0, chosen_book, *list(books))
    book_dropdown.grid(row=1, column=1, padx=10, pady=10)
    book_dropdown.config(font=base_font, fg=colors[0], width=30)

    book_lab = tk.Label(win0, text="Book:", fg=colors[0], font=base_font)
    book_lab.grid(row=1, column=0, padx=10, pady=10)

    # chapters in book to draw flashcard entries from 
    chosen_chap = tk.StringVar(win0, value='all')

    chap_entry = tk.Entry(win0, textvariable=chosen_chap)
    chap_entry.config(font=base_font, fg=colors[1], width=30)

    chap_lab = tk.Label(win0, 
                        text="Chapters\n('all' or comma-separated, e.g. '1, 2'):", 
                        fg=colors[1], 
                        font=base_font,
                        )
    chap_entry.grid(row=2, column=1, padx=10, pady=10)
    chap_lab.grid(row=2, column=0, padx=10, pady=10)

    # flashcard type (vocab, grammar, phrases)
    chosen_type = tk.StringVar(win0, value=card_types[0])

    type_dropdown = tk.OptionMenu(win0, chosen_type, *card_types)
    type_dropdown.config(font=base_font, fg=colors[2], width=30)    
    type_dropdown.grid(row=3, column=1, padx=10, pady=10)    

    type_lab = tk.Label(win0, text="Entry type:", fg=colors[2], font=base_font)
    type_lab.grid(row=3, column=0, padx=10, pady=10)    

    # flashcard language
    chosen_language = tk.StringVar(win0, value=languages[0])

    lang_dropdown = tk.OptionMenu(win0, chosen_language, *languages)
    lang_dropdown.config(font=base_font, fg=colors[4], width=30)
    lang_dropdown.grid(row=4, column=1, padx=10, pady=10)

    lang_lab = tk.Label(win0, text="Show flashcards in:", fg=colors[4], font=base_font)
    lang_lab.grid(row=4, column=0, padx=10, pady=10)   
    
    selection_button = tk.Button(
        win0,
        text="Generate flashcards",
        command=lambda: flashcard_gui(chosen_book.get(),
                                      chosen_chap.get(),
                                      chosen_type.get(), 
                                      chosen_language.get()),
        font=base_font,
        width=30, # fix button width
        height=2,
    )
    selection_button.config(
        fg=colors[3], # text color
        activeforeground=colors[4], # text color when selected
        )
    selection_button.grid(row=5, column=1, padx=10, pady=10)

    return win0


def flashcard_gui(book, chapter, card_type, card_language, nxy=5):
    """Create interactive GUIs displaying all available flashcards of
      from 'book' of 'card_type' in 'card_language', with each GUI 
      displaying flashcards in an nxy x nxy grid"""
    
    # load dictionary from selected book and chapter(s)
    book_module = books[book]
    source_dict = get_dictionary(book_module, chapter, card_type)

    # get all dictionary entries
    if card_language == 'English':
        all_entry = list(source_dict)
    else:
        all_entry = list(source_dict.values())
    nentry = len(all_entry)
    # randomize order (in-place)
    random.shuffle(all_entry)

    windows = []    
    cards = []
    counter = 0 

    for nn in range(int(ceil(nentry / nxy ** 2))):
        win = tk.Toplevel()
        windows.append(win)
        base_font = font.Font(family='Lato', size=16, weight='bold')
        win.geometry("2400x2400")

        # correctly display the index of the final entry
        max_entries = min(nentry, counter + nxy ** 2)
        # indices of the current entries
        current_idx = f"{card_type} {counter + 1} - {max_entries} of {nentry}"
        win.title(current_idx)

        # loop over rows
        for ii in range(nxy):
            # vary button size with window size
            win.columnconfigure(ii, weight=1, minsize=150)
            win.rowconfigure(ii, weight=1, minsize=150)

            # loop over columns
            for jj in range(nxy):
                try:
                    entry = all_entry[counter]
                except IndexError:
                    break

                flashcard = tk.Button(
                    win,
                    text=f"\n {entry}",
                    command=lambda idx=counter: update_card(cards[idx], 
                                                            all_entry[idx], 
                                                            source_dict,
                                                            card_language
                                                            ),
                    anchor='n', # align text to top of grid cell
                )
                flashcard.config(font=base_font, fg=colors[1])
                flashcard.grid(row=ii, column=jj, sticky='nsew', padx=4, pady=4)

                cards.append(flashcard)

                counter += 1
        
    return windows

if __name__ == '__main__':
    base_gui(supported_languages)