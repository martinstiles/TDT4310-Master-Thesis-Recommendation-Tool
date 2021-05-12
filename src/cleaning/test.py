from nltk import word_tokenize, sent_tokenize

print(word_tokenize(
    "P\u00e5 IDI bruker vi i stor grad profesjonelle verkt\u00f8y i utdanningen, f.eks. VS Code"))

print(sent_tokenize("P\u00e5 IDI bruker vi i stor grad profesjonelle verkt\u00f8y i utdanningen, f.eks. VS Code. Dette er et svært godt verktøy!"))
