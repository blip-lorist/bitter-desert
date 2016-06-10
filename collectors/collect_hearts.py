from nltk.corpus import wordnet as wn
from textstat.textstat import textstat

# Find a specific synset of "body" 
body = wn._synset_from_pos_and_offset('n',5216365) 

# Keep searching for part_meronyms until there are no more
def collect_parts_recursive(body, collection):
    parts = body.part_meronyms()

    for part in parts:
        collection.append(part)
        collect_parts_recursive(part, collection)

    return collection

all_parts = collect_parts_recursive(body, [])

# Collect heart replacements
hearts = []
for part in all_parts:
    heart = part.name().split('.')[0]
    heart = heart.replace("_", " ")
    syllables = round(textstat.syllable_count(heart))
    if syllables == 1.0:
        print heart

