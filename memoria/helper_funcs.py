import webbrowser

def translate(entry, source_dict):
    """Get the translation of 'entry' (either English to Italian or vice versa) 
    from the dictionary 'source_dict'"""

    return source_dict[entry]


def look_up_word(word, reference_type):
    if reference_type in ['define', 'conjugate']:
        if reference_type == 'define':
            link = f"https://www.wordreference.com/iten/{word}"
        else: 
            link = f"https://sapere.virgilio.it/parole/coniuga-verbi/{word}"

        webbrowser.open(link, new=2)

    else:
        pass

def update_card(card, word, source_dict):
    """For a button flashcard, update the card the word's translation on first click, or open a hyperlink on second click"""
    translation = translate(word, source_dict)

    if card['underline'] == 0:
        if word.startswith('to ') or translation.startswith('to '):
            reference_type = 'conjugate'
        else:
            reference_type = 'define'

        look_up_word(word, reference_type)

    else:
        new_text = f"{card['text']}\n\n{translation}"
        # update button color once it's clicked
        card.config(text=new_text, bg='#900C3F', fg='#EEEEEE', underline=0)
        