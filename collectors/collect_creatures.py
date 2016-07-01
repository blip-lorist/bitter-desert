from nltk.corpus import wordnet as wn
from textstat.textstat import textstat

"""
Run with `python collect_creatures.py > unfiltered_creatures.txt`
"""
synorg = wn.synsets('organism', 'n')

for organism in synorg[0].hyponyms():
    for hypo in organism.hyponyms():
        for noun in hypo.lemmas():
            syllables = round(textstat.syllable_count(noun.name())) 
            if syllables == 2.0:
                creature = noun.name().replace("_"," ")
                print creature


