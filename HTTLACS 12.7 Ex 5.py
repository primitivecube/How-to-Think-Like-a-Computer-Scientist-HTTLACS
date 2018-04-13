# NOTE: This program is not a complete translation solution due to not providing translations on words with
# mid-word punctuation, and not maintaining capitalisation of mid-sentence capital letters. However,
# the answer that HTTLACS provides to this question only functions on exact matches of sub-strings to the
# dictionary keys, and thus has a high rate of failure against any normal sentence, especially when parsing
# punctuation. The program that I provide herein handles a much wider range of cases than the HTTLACS answer.

# Here’s a table of English to Pirate translations
# English	Pirate
# sir	matey
# hotel	fleabag inn
# student	swabbie
# boy	matey
# madam	proud beauty
# professor	foul blaggart
# restaurant	galley
# your	yer
# excuse	arr
# students	swabbies
# are	be
# lawyer	foul blaggart
# the	th’
# restroom	head
# my	me
# hello	avast
# is	be
# man	matey
# Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

sentence = 'Hello students and lawyers, how are the restrooms in the hotel?'

def eng_to_pirate(trans_sentence):
    eng_to_pirate_dict = {"sir":"matey","hotel":"fleabag inn","student":"swabbie","boy":"matey","madam":"proud beauty",
                      "professor":"foul blaggart","restaurant":"galley","your":"yer","excuse":"arr","students":"swabbies",
                      "are":"be","lawyer":"foul blaggard","the":"th'","restroom":"head","my":"me","hello":"avast",
                      "is":"be","man":"matey"}
    for key in eng_to_pirate_dict:
        while key in trans_sentence:
            trans_sentence = trans_sentence.replace(key,eng_to_pirate_dict[key]).lower()
    return trans_sentence.capitalize()

print(eng_to_pirate(sentence))
