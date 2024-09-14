import json
import genanki
import os

# Define a unique model ID and deck ID
MODEL_ID = 2040879827
DECK_ID = 1452536260

# Define the model for the flashcards
my_model = genanki.Model(
    MODEL_ID,
    'Spanish Verb Model',
    fields=[
        {'name': 'Verb'},
        {'name': 'Translation'},
        {'name': 'Definition'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<b>{{Verb}}</b><br><br>What is the English translation?',
            'afmt': '{{FrontSide}}<hr id="answer">{{Translation}}<br><br><i>{{Definition}}</i>',
        },
        {
            'name': 'Card 2',
            'qfmt': '<b>{{Translation}}</b><br><br>What is the Spanish verb?',
            'afmt': '{{FrontSide}}<hr id="answer">{{Verb}}<br><br><i>{{Definition}}</i>',
        },
    ],
    css='''
        .card {
         font-family: Arial;
         font-size: 20px;
         text-align: left;
         color: black;
         background-color: white;
        }
    ''')

# Create the deck
my_deck = genanki.Deck(
    DECK_ID,
    "Verb Definitions for Lisardo's KOFI Method (Spanish)"
)

# Load the JSON data
with open('C:\\Users\\power\\OneDrive\\vscode\\anki-spanish-KOFI\\verbs.json', 'r', encoding='utf-8') as f:
    verbs = json.load(f)

# Iterate over each verb and add a note to the deck
for verb_entry in verbs:
    note = genanki.Note(
        model=my_model,
        fields=[
            verb_entry['verb'],
            verb_entry['translation'],
            verb_entry['definition'],
        ]
    )
    my_deck.add_note(note)

# Define the output file name
output_file = "C:\\Users\\power\\OneDrive\\vscode\\anki-spanish-KOFI\\Verb Definitions for Lisardos KOFI Method (Spanish).apkg"

# Remove the output file if it already exists to avoid duplication
if os.path.exists(output_file):
    os.remove(output_file)

# Generate the .apkg file
genanki.Package(my_deck).write_to_file(output_file)

print(f'Anki deck "{output_file}" has been successfully created.')