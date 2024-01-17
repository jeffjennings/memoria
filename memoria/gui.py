import tkinter as tk
from tkinter import font
import webbrowser

root = tk.Tk()
root.geometry("2385x1600")
root.configure(bg='#494949')
root.title(f"Chapter(s) 1")

# button text
text_font = font.Font(family='Lato', size=22, weight='bold')

def translate(word, source_dict):
    """Get the translation of 'word' from the dictionary 'source_dict'"""
    translation = source_dict[word]

    return translation


def look_up_word(word, reference_type):
    if reference_type in ['define', 'conjugate']:
        if reference_type == 'define':
            link = f"https://www.wordreference.com/iten/{word}"
        else: 
            link = f"https://sapere.virgilio.it/parole/coniuga-verbi/{word}"

        webbrowser.open(link, new=2)

    else:
        pass


def update_card(card, word, source_dict, reference_type):
    """For a button flashcard, update the card the word's translation on first click, or open a hyperlink on second click"""
    if card['underline'] == 0:
        look_up_word(word, reference_type)
    else:
        translation = translate(word, source_dict)

        new_text = f"{card['text']}\n\n{translation}"
        # update button color once it's clicked
        card.config(text=new_text, bg='#900C3F', fg='#EEEEEE', underline=0)
        


cards = []
counter = 0 

# create 5x5 grid of flashcards
for ii in range(5):
    # vary button size with window size
    root.columnconfigure(ii, weight=1, minsize=150)
    root.rowconfigure(ii, weight=1, minsize=100)

    for jj in range(5):
        try:
            word = list(source_dict)[counter]
        except IndexError:
            break

        flashcard = tk.Button(
            master=root,
            text=f"\n {word}",
            command=lambda idx=counter: update_card(cards[idx], 
                                                    list(source_dict)[idx], 
                                                    source_dict, 
                                                    reference_type,
                                                    ),
            anchor='n', # text alignment
            font=text_font,
            bg='#3393FF',
            fg="#494949", # text color
            activebackground="#38C5E8",
            activeforeground="#494949", # text color when moused over
            width=16, # fix button width
            height=6,
        )
        
        flashcard.grid(row=ii, column=jj, sticky='nsew', padx=5, pady=5)

        cards.append(flashcard)

        counter += 1

root.mainloop()