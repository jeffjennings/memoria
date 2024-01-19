import webbrowser

def translate(entry, source_dict):
    """Get the translation of 'entry' (either English to Italian or vice versa) 
    from the dictionary 'source_dict'"""

    return source_dict[entry]


def look_up_entry(entry, source_dict, reference_type, entry_language='italian'):
    """Depending on 'reference_type', look up online the definition of an Italian 
    word or phrase 'entry', its conjugation, or show the Italian form (that we 
    provide) on google translate to hear it spoken"""

    if reference_type == 'define':
        link = f"https://www.wordreference.com/iten/{entry}"
    elif reference_type == 'conjugate': 
        link = f"https://sapere.virgilio.it/parole/coniuga-verbi/{entry}"
    else:
        link = "https://translate.google.com/?sl=it&tl=en&text="

        # for web address, must replace whitespace in 'entry'
        entry_no_spaces = entry.replace(" ", "%20")

        if entry_language == 'english':
            # don't want to call google translate on an english word/phrase, 
            # as its translation may differ from our stored one
            entry_no_spaces = translate(entry_no_spaces, source_dict)
            
        link += f"{entry_no_spaces}%0A&op=translate"

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
        