from nltk.corpus import wordnet as wn
from textstat.textstat import textstat

"""
Run with `python collect_naked.py > unfiltered_naked.txt`
"""

adjectives = list(wn.all_synsets('a')) + list(wn.all_synsets('s'))
nakeds = []

# Collect all two-syllable adjectives
for item in adjectives:
    for adj in item.lemmas():
        syllables = round(textstat.syllable_count(adj.name()))
        if syllables == 2.0:
            naked = adj.name().replace("_", " ")
            nakeds.append(naked)

# Uniques only
nakeds = set(nakeds)


for naked in nakeds:
    print naked.encode('utf8')
