def countSyllables(word):
    '''
    This code belongs to https://stackoverflow.com/questions/46759492/syllable-count-in-python
    It is not mine.
    However, after near a week of crying and threats I have decided that using this is better.
    Made a single edit to the embedded if statement so it stopped removing every syllable for words that end in "e"
    :param word: string of a single word
    :return: number of syllables in the word
    '''
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
            if word[index] == "e" and index == len(word) - 1:
                count -= 1
    if count == 0:
        count += 1
    return count


def frequencyList(text):
    wordList = []
    countList = []
    for word in text:
        if word not in wordList:
            wordList.append(word)
            countList.append(1)
        else:
            index = wordList.index(word)
            count = countList[index]
            count += 1
            countList[index] = count
    return wordList, countList


def getFrequencyOfWord(word):
    with open("booksForComplexity\wordCountSH.txt", "r") as file:
        text = file.read()
        wordsAndFreq = text.split(" ")




def removePunct(list):
    punct = """,.\/'@;:#~][{])(“*&^%$£!”—‘?><_"""
    for word in list:
        index = list.index(word)
        for letter in word:
            if letter in punct:
                word = word.replace(letter, '')
                list[index] = word
    return list

'''
    Final complexity should be a combination of the number of syllables and the number of times it appears in
        a collection of texts.
    
'''


with open("booksForComplexity/janeAusten.txt", "r", encoding="utf8") as file:
    text = file.read()
wordList = text.split()
wordList = removePunct(wordList)
for word in wordList:
    word = word.lower()
words, count = frequencyList(wordList)
with open("booksForComplexity/wordCountJA.txt", "w", encoding="utf8") as f:
    for word in words:
        index = words.index(word)
        number = count[index]
        f.write(word + ": " + str(number) + "\n")


