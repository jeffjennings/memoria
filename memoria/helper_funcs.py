import os
import sys
import webbrowser
import random
import memoria
from memoria.inputs import languages, person, tense, colors

memoria_path = os.path.dirname(memoria.__file__)
sys.path.append(os.path.join(memoria_path, f"dictionaries/en_it"))

def get_dictionary(book, chapter, card_type):
    """Load the selected dictionary"""
    if book == "nie_a0_a1pt5":
        if card_type in [
            "Vocab: nouns, adjectives, verbs", 
            "Vocab: adverbs, conjunctions, prepositions, pronouns",
            "Randomly generated conjugations",
            "Randomly generated adjective + noun"]:
            from nie_a0_a1pt5 import vocab as chosen_dict
        elif card_type == "Grammar":
            from nie_a0_a1pt5 import grammar as chosen_dict
        else:
            from nie_a0_a1pt5 import phrases as chosen_dict

    all_entries = {}
    if chapter != "all":
        chapter = chapter.split(",")
        selected_chapters = {}
        for cc in chapter:
            selected_chapters[cc] = chosen_dict['ch' + cc]
        chosen_dict = selected_chapters

    for chap in chosen_dict:
        if card_type == "Vocab: nouns, adjectives, verbs":                    
            for vv in ["nouns", "adjectives", "verbs"]:
                # merge dictionaries
                all_entries = {**all_entries, **chosen_dict[chap][vv]}

        elif card_type == "Vocab: adverbs, conjunctions, prepositions, pronouns":            
            for vv in ["adverbs", "conjunctions", "prepositions", "pronouns"]:
                all_entries = {**all_entries, **chosen_dict[chap][vv]}
                
        elif card_type == "Randomly generated conjugations":
            for ii in range(50):
                # _for is foreign language
                rp_eng, rp_for = random.choice(list(person.items()))
                rt_eng, rt_for = random.choice(list(tense.items()))
                rv_eng, rv_for = random.choice(list(chosen_dict[chap]['verbs'].items()))

                # remove "to " from English
                phrase_eng = f"{rp_eng} {rv_eng[3:]}\n({rt_eng})"
                phrase_for = f"{rp_for} {rv_for}\n({rt_for})"
                all_entries[phrase_eng] = phrase_for

        elif card_type == "Randomly generated adjective + noun":
            for ii in range(50):
                ra_eng, ra_for = random.choice(list(chosen_dict[chap]['adjectives'].items()))
                rn_eng, rn_for = random.choice(list(chosen_dict[chap]['nouns'].items()))
                phrase_eng = f"{ra_eng} {rn_eng}"
                phrase_for = f"{ra_for} {rn_for}"
                all_entries[phrase_eng] = phrase_for

        else:
            all_entries = {**all_entries, **chosen_dict[chap]}

    return all_entries


def translate(entry, source_dict, entry_language="English"):
    """Get the translation of 'entry' (either English to foreign language
    or vice versa) from the dictionary 'source_dict'"""

    if entry_language == "English":
        translation = source_dict[entry]
    else:
        translation = [i for i in source_dict if source_dict[i] == entry][0]

    return translation


def look_up_entry(entry, source_dict, entry_language="Italian"):
    """Look up the definition of a foreign language word online."""

    if entry_language == "Italian":
        link = f"https://www.wordreference.com/iten/{entry}"

    webbrowser.open(link, new=2)


def update_card(card, entry, source_dict, entry_language="English"):
    """For a button flashcard, update the card with the translation of
    'entry' on first click; open a hyperlink on second click."""

    translation = translate(entry, source_dict, entry_language)

    if entry_language == "English":
        foreign_entry = translation
    else:
        foreign_entry = entry

    if card["underline"] == 0:
        if "Italian" in languages:
            look_up_entry(
                foreign_entry,
                source_dict,
                entry_language="Italian",
            )

    else:
        new_text = f"{card['text']}\n\n{translation}"
        # update button color once it's clicked
        card.config(text=new_text, fg=colors[6], underline=0)
