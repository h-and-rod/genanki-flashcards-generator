import genanki
import random

novo_deck = genanki.Deck(
    deck_id=random.randrange(1 << 30, 1 << 31),
    name='Nome do deck')

cards = [
  ("Frente card 1", "Verso card 1"),
  ("Frente card 2", "Verso card 2"),
  ("Frente card 3", "Verso card 3"),
  ("Frente card 4", "Verso card 4"),
  ("Frente card 5", "Verso card 5"),
  ("Frente card 6", "Verso card 6"),
  ("Frente card 7", "Verso card 7"),
  ("Frente card 8", "Verso card 8"),
]

for frente, verso in cards:
    nota = genanki.Note(
        model=genanki.BASIC_MODEL,
        fields=[frente, verso],
    )
    novo_deck.add_note(nota)


genanki.Package(novo_deck).write_to_file('novoDeck.apkg')