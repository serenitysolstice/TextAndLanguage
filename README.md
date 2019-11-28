# TextAndLanguage
Text and language simplifier. Early development. Though this is a public project, in no way does this mean the system is ready for use by anyone other than a developer interested in working on the project.


Current development focuses on ranking the complexity of words, using a combination of the frequency with which they appear in works of literature (to avoid accidentally ranking specialist industry related terms and the like) and the number of syllables in a word:

Complexity = num syllables / frequency

The project makes heavy use of the NLTK to break down words, to define words and to find synonyms, which is the basis of word substitution.
