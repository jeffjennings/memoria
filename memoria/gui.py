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
root.title(f"Chapter(s) 1")

reference_type = 'word'
source_dict = {
    'pillow':'cuscino',
    'blanket':'coperta',
    'she is':'è',
    'bed':'letto',
    'book':'libro',
    'window':'finestra',
    'door':'porta',
    'chair':'sedia',
    'table':'tavolo',
    'zpillow':'cuscino',
    'zblanket':'coperta',
    'zshe is':'è',
    'zbed':'letto',
    'zbook':'libro',
    'zwindow':'finestra',
    'zdoor':'porta',
    'zchair':'sedia',
    'ztable':'tavolo',
    'ypillow':'cuscino',
    'yblanket':'coperta',
    'yshe is':'è',
    'ybed':'letto',
    'ybook':'libro',
    'ywindow':'finestra',
    'ydoor':'porta',
    'ychair':'sedia',
    'ytable':'tavolo',        
}

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