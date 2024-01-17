# memoria
A simple GUI to replicate flashcards for memorizing Italian vocabulary, grammar (especially conjugation/declension) and phrases. Entries are added on a per chapter basis as I work through the Italian textbooks and workbooks of _New Italian Espresso_ and _Nuovo Espresso_, as well as the grammar books _Italian Grammar in Practice_, _English Grammar for Students of Italian_, and _Pocket Italian Grammar_. 

`gui.py` produces a GUI that first asks the user to choose: 
- a book and one or more (or random) chapters to draw from,
- whether to draw vocabulary, grammar or phrases, and
- in which language to draw these (Italian or English)

A grid of flashcards is then generated. Clicking on a flashcard shows its English/Italian counterpart (or in the case of grammar, the relevant forms).
- For vocabulary, clicking the flashcard a second time opens the [WordReference](https://www.wordreference.com/iten/) website with a search for the word to obtain its dictionary entry.
- For verb conjugation, clicking on the flashcard a second time opens the [Virgilio](https://sapere.virgilio.it/parole/coniuga-verbi/) website with a search for the verb to obtain its conjugations in all tenses.
- For other grammar or phrases, clicking on the flashcard a second time has no effect.
