# memoria
A simple GUI to generate flashcards for memorizing Italian vocabulary, grammar and phrases. Entries are added on a per chapter basis as I work through the Italian textbooks and workbooks of _New Italian Espresso_ and _Nuovo Espresso_, as well as the grammar books _Italian Grammar in Practice_, _English Grammar for Students of Italian_, and _Pocket Italian Grammar_. 

`gui.py` produces a GUI with which you choose: 
- a book to draw entries from,
- whether the entries drawn should belong to vocabulary, grammar or phrases, and
- in which language to display the entries on the flashcards (English or Italian)

A grid of flashcards is then generated. Clicking on a flashcard shows its English/Italian counterpart (or in the case of grammar, the relevant forms).
- For vocabulary, clicking the flashcard a second time opens the [WordReference](https://www.wordreference.com/iten/) website with a search for the word to obtain its dictionary entry.
- For verb conjugation, clicking on the flashcard a second time opens the [Virgilio](https://sapere.virgilio.it/parole/coniuga-verbi/) website with a search for the verb to obtain its conjugations in all tenses.
- For other grammar or phrases, clicking on the flashcard a second time opens google translate with the Italian version of the entry, so that you can hear it spoken by clicking on the speaker icon there.
