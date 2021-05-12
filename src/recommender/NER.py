import spacy
#from spacy import displacy
from collections import Counter
#from spacy.cli import download
import re
from collections import Counter
#import matplotlib.pyplot as plt
#import wikipedia
import json

# print(download('en_core_web_trf'))

nlp = spacy.load("en_core_web_trf")

actors = []
with open("../scraper/data.json", 'r', encoding="utf-8") as file:
    data = json.load(file)["data"]
    # print(data[:2])
    text = [obj[6] for obj in data]
    # This could easily be done with NLTK as well, sent_tokenizer would be more appropriate.
    # print(text)

NER = nlp("\n".join(text[:int(len(text) / 10)]))

# # Manual
# synonym = {
#     "Luke Skywalker": ["Luke", "Skywalker", "Jedi", "Behind luke", "LUKE"],
#     "Han Solo": ["HAN", "Solo", "INT. MILLENNIUM FALCON - COCKPIT", "Captain Solo", "Han Solo"],
#     "Leia Organa": ["LEIA", "Leia", "Princess Leia"],
#     "C3PO": ["THREEPIO", "Threepio", "See-Threepio"],
#     "R2D2": ["Artoo", "Artoo-Detoo"],
#     "Lando Calrissian": ["LANDO", "Lando Calrissian"],
#     "Darth Vader": ["VADER", "INT. VADER'S STAR DESTROYER - BRIDGE", "Darth Vader", "Vader"],
#     "Grandmaster Yoda": ["YODA", "CREATURE", "Creature", "Yoda"],
#     "Chewbacca": ["Chewie", "Chewbacca", "Wookiee"],
#     "Obi-Wan Kenobi": ["Ben", "BEN", "Obi-Wan", "Ben Kenobi"]
# }
# items = [x.text for x in NER.ents if x.label_ == "PERSON"]

# actorObj = Counter((actors)).most_common(15)
# NERObj = Counter(items).most_common(35)
# final = {}

# # NEL


# def completeDict():
#     completeDict = actorObj+NERObj
#     for key, val in completeDict:
#         for synKey in synonym:
#             if key in synonym.get(synKey):
#                 final[synKey] = val if final.get(
#                     synKey, 0) == 0 else val + final[synKey]


# completeDict()

# final = dict(sorted(final.items(), key=lambda item: item[1]))
# sentences = [str(x) for x in NER.sents]

# plt.bar(final.keys(), final.values())
# plt.show()
#displacy.serve(NER, style="ent")
