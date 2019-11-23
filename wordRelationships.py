def makeGraph(keys, values):
    '''
    Builds a graph from a list of keys and list of values. The graph is a dictionary, the
    values are the difficulty rating of a given word.

    :param keys: Words in the English Language
    :param values: Difficulty of the word to understand
    :return graph: Returns the dictionary
    '''
    graph = dict(zip(keys, values))
    return graph


def findBest(word, graph):
    '''
    Determines the best synonym for a word based on the word's value

    :param word: the word that is to be swapped
    :param graph: a dictionary of words and their relationships to the target word
    :return b: the best word
    '''
    i = 0
    for word in graph:
        if i == 0:  # if word is first in the dictionary
            b = word
            i = 1
        elif graph[b] > graph[word]:
            b = word
    return b


translationWord = "principle"
words = ["foundation", "assumption", "convention", "rule"]
weights = [8, 5, 2, 2]

graph = makeGraph(words, weights)

print(translationWord)
print("The best possible match we have found is: ")

bestWord = findBest(translationWord, graph)
print(bestWord)

