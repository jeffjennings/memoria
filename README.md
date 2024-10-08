<p align="center">
   <img width = "300" src="https://github.com/jeffjennings/memoria/blob/main/logo.jpg?raw=true"/>
 </p>

<p align="center">
A simple GUI to generate flashcards for memorizing vocabulary, grammar and phrases of a foreign language.
</p>

<p align="center">
  <!-- current release -->
  <a href="https://github.com/jeffjennings/memoria/releases">
      <img src="https://img.shields.io/github/release/jeffjennings/memoria/all.svg">
  </a>

  <!-- current version on pypi -->
  <a href="https://pypi.python.org/pypi/memoria-gui">
      <img src="https://img.shields.io/pypi/v/memoria-gui.svg">

</p>

Install
-------
`pip install memoria-gui`

Using _memoria_
---------------
`python gui.py` from the terminal produces a GUI with which you choose: 
- a book to draw flashcard entries from,
- which chapter(s) in the book to draw from,
- which type of entry to draw (vocabulary among nouns, adjectives, verbs; vocabulary among adverbs, conjunctions, prepositions, pronouns; grammar; phrases; or randomly generated phrases), and
- in which language to display the entries on the flashcards (English or the foreign language).

Grids of flashcards are then generated, spanning all the entries of the chosen type from the chosen source, with the order optionally randomized. Clicking on a flashcard once shows its English/foreign language counterpart (or in the case of grammar, the relevant forms). Clicking on it again links to its translation online (for Italian, this uses [WordReference](https://www.wordreference.com/iten/)).

_memoria_ is currently tailored to Italian, but it's easy to drop in another language (it might eventually support Ancient Greek and Latin) - just add new [dictionaries](https://github.com/jeffjennings/memoria/tree/main/memoria/dictionaries) with the English and foreign language counterparts, following the data structure [here](https://github.com/jeffjennings/memoria/blob/main/memoria/dictionaries/en_it/nie_a0_a1pt5.py).

Resources for learning Italian
------------------------------
If you're interested in learning Italian, these are the books I'm using (and the source of flashcard entries in the code). Together I think they should provide a good teaching of [CEFR levels](https://www.coe.int/en/web/common-european-framework-reference-languages/table-1-cefr-3.3-common-reference-levels-global-scale) A1 - C2 of the language (i.e., from beginner to fluent), including a strong understanding of the grammar:
   * _New Italian Espresso - Beginner and Pre-intermediate_ (CEFR levels A0 - A1.5) and _Intermediate and Advanced_ (CEFR levels A1.5 - B1) - including the companion workbooks
   * _Nuovo Espresso 4, 5, 6_ (CEFR levels B2, C1, C2) - these books are only in Italian and are a continuation of _New Italian Espresso_
   * _Italian Grammar in Practice_ (CEFR levels A1 - B2) - a large set of practice exercises, made by the same publisher of _New Italian Espresso_ and _Nuovo Espresso_
   * _English Grammar for Students of Italian_ - a quick read to recall the structure of English and a helpful comparison to differences in Italian
   * _Pocket Italian Grammar_ - succinct overview of Italian grammar

Background
----------
I wrote this package to have an efficient way to memorize large sets of Italian words and phrases. I've only been using Mac OS, so GUI formatting might be off on Linux or Windows. If you want to use and/or customize the code for your own language and you'd like some help, or if you have any suggestions, feel free to open an issue.

_memoria_ is Latin (and Italian!) for 'memory, remembrance'. Hence the Latin phrase 'In memoriam' and the English derivatives 'memorial' and 'memoir'.

The logo is a Roman mosaic showing μνημοσύνη (Mnemosyne), the Greek Titan of memory and mother of the nine Muses. μνήμη	is Greek for 'memory, remembrance' and is the origin of the English derivative 'mnemonic'.
