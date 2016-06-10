from nltk.corpus import wordnet as wn
from textstat.textstat import textstat
from pattern.en import conjugate, PRESENT, PARTICIPLE 
from language_filter import filtered_wordlist

# Collect present participle (ending in 'ing') of single-syllable verbs
verbs = list(wn.all_synsets('v'))
squattings = []

for item in verbs:
    for verb in item.lemmas():
        syllables = round(textstat.syllable_count(verb.name()))
        if syllables == 1.0:
            squat = verb.name().replace("_", " ")
            squatting = conjugate(squat, PRESENT+PARTICIPLE)
            print squatting.encode('utf8')
            


