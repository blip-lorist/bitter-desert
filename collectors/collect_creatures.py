from nltk.corpus import wordnet as wn
from textstat.textstat import textstat
from language_filter import filtered_wordlist

synorg = wn.synsets('organism', 'n')
creatures = []

for organism in synorg[0].hyponyms():
    for hypo in organism.hyponyms():
        for noun in hypo.lemmas():
            syllables = round(textstat.syllable_count(noun.name())) 
            if syllables == 2.0:
                creature = noun.name().replace("_"," ")
                creatures.append(creature)

# Uniques only
creatures = set(creatures)

# Filter out offensive language
filtered_creatures = filtered_wordlist(creatures)

for critter in filtered_creatures:
    print critter.encode('utf8')

