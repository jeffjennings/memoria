import os
import sys
import webbrowser
import memoria
memoria_path = os.path.dirname(memoria.__file__)
sys.path.append(os.path.join(memoria_path, f"dictionaries/en_it"))

colors = ['#C70039', '#FF5733', '#17BF14', '#FFC300']

def get_dictionary(book, card_type):
    """Load the selected dictionary"""

    if book == "nie_a0_a1pt5":
        from nie_a0_a1pt5 import vocab, grammar, phrases
        
    if card_type == 'Vocabulary':
        return vocab
    elif card_type == 'Grammar':
        return grammar
    else:
        return phrases
    
def translate(entry, source_dict):
    """Get the translation of 'entry' (either English to Italian or vice versa) 
    from the dictionary 'source_dict'"""

    return source_dict[entry]


def look_up_entry(entry, source_dict, reference_type, entry_language='Italian'):
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

        if entry_language == 'English':
            # don't want to call google translate on an English word/phrase, 
            # as its translation may differ from our stored one
            entry_no_spaces = translate(entry_no_spaces, source_dict)
            
        link += f"{entry_no_spaces}%0A&op=translate"

    webbrowser.open(link, new=2)


def update_card(card, entry, source_dict, entry_language='English'):
    """For a button flashcard, update the card with the translation of 
    'entry' on first click; open a hyperlink on second click"""

    translation = translate(entry, source_dict)

    if entry_language == 'English':
        en_entry = entry
        it_entry = translation
    else:
        it_entry = entry
        en_entry = translation

    if card['underline'] == 0:
        if en_entry.startswith('to '):
            reference_type = 'conjugate'
        elif " " in entry:
            reference_type = 'hear'
        else:
            reference_type = 'define'

        look_up_entry(it_entry, source_dict, reference_type, entry_language='Italian')

    else:
        new_text = f"{card['text']}\n\n{translation}"
        # update button color once it's clicked
        card.config(text=new_text, fg=colors[2], underline=0)
        