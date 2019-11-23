import wordRelationships
from nltk.corpus import wordnet as wn


def getNetName(net, num):
    '''
    Gets the synset name of an object - useful for other wordnet methods
    THIS METHOD WORKS AS INTENDED

    :param net:
    :param num:
    :return:
    '''
    netName = net[num].name()
    return netName


def getWordName(net, num):
    '''
    Gets the core word of the synset - useful for external checking and substitution
    THIS METHOD WORKS AS INTENDED

    :param net:
    :param num:
    :return:
    '''
    lemma = net[num].lemmas()
    word = lemma[0].name()
    return word


def getDefinition(net, num):
    '''
    Gets the definition of a word - useful where user wants to understand what a word means.
    THIS FUNCTION WORKS AS INTENDED
    :param net:
    :param num:
    :return:
    '''
    definition = net[num].definition()
    return definition


def checkWordInDictionary(word):
    '''
    Checks that a word is in the dictionary.
    THIS FUNCTION WORKS AS INTENDED
    :param word:
    :return:
    '''
    with open("words.txt", "r") as file:
        dictionary = file.read().splitlines()
        for w in dictionary:
            if w[0] == word[0]:
                if word == w:
                    return True
                else:
                    continue
            else:
                continue


def getSynonyms(word):
    '''
    Returns synonyms of a given word in a list
    THIS FUNCTION WORKS AS INTENDED
    :param word:
    :return: synonyms
    '''
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


def getAntonyms(word):
    '''
    Returns antonyms of a given word in a list
    THIS FUNCTION WORKS AS INTENDED
    :param word:
    :return: antonyms
    '''
    antonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return antonyms

w = input("Enter word: ")
b = checkWordInDictionary(w)
if b == True:
    print("Word is in dictionary")
else:
    print("Word not found")
net = wn.synsets(w)
if len(net) > 1:
    print(net)
    num = int(input("Which element of the list are you interested in?"))
else:
    num = 0

print(getDefinition(net, num))

synonyms = getSynonyms(w)
antonyms = getAntonyms(w)
print(synonyms)
print(antonyms)


