# 'In the Desert' Mad Libs
Experiments with NLTK, syllable analysis, and a Stephen Crane poem

## Example Result
`python crane_bot.py`
>In the birch forest hills  
>I saw a bartender, lithic, beastial  
>Who, setting on the ground  
>Held their brow in their hands  
>And ate of it.  
>
>I said, "Is it good, friend?"  
>It is sour - sour, they answered;  
>"But I like it  
>Because it is sour  
>And because it is my brow"  

## Poem Template
In the NOUN (BIOME)  
I saw a NOUN, ADJECTIVE, bestial,   
Who, VERB (PRESENT PARTICIPLE) upon the ground,   
Held POSSESSIVE PRONOUN NOUN in POSSESSIVE PRONOUN hands,   
And ate of it.   
I said, “Is it good, friend?”   
“It is ADJECTIVE (FLAVOR),” PRONOUN answered;   

“But I like it   
Because it is ADJECTIVE (FLAVOR),   
And because it is my NOUN.”  

## Corpora Collectors
### "Creature" replacements
- Collector searches through WordNet for synonym groups and their hyponyms. 
- Two-syllables only, filtered by textstat library

### "Naked" replacements
- Collects two-syllable adjectives from WordNet

### "Squatting" replacements
- Collects present participle (ending in "ing") of single-syllable verbs using the pattern library, WordNet, and textstat

### "Heart" replacements
- Recursive method that retrieves meronyms of the word "body", as in "the physical structure of a person or animal"
- Searches for single-syllable meronyms. Decided to go with single-syllable to maintain meter somewhat and avoid terms that sounded too medical

### "Bitter" replacements
- I had a difficult time searching for flavor-specific words with NLTK, so I selected a corpus from some food-related website.

### "Desert" replacements 
- Snagged a list from the Minecraft wiki. (It's odd to think about blending the imagery of this poem and Minecraft.)


