import random
from typing import Iterator
import numpy as np

class GeneratorLero:
    def __init__(self, filename) -> None:
        self._filename = filename
        self._openFile()
        self._pairs = self._makePairs()
        self._dictGenerator()

    def _openFile(self) -> None:
        self._book = open(self._filename, encoding='utf8').read()
        self._corpus = self._book.split()

    def _makePairs(self) -> Iterator[str]:
        for i in range(len(self._corpus)-1):
            yield (self._corpus[i], self._corpus[i+1])
    
    def _dictGenerator(self):
        self._wordDict = {}
        for word1, word2 in self._pairs:
            if word1 in self._wordDict.keys():
                self._wordDict[word1].append(word2)
            else:
                self._wordDict[word1] = [word2]

    def _firstWord(self):
        firstWord = np.random.choice(self._corpus)

        while firstWord.islower():
            firstWord = np.random.choice(self._corpus)
        return firstWord

    def generateText(self) -> str:
        numbersWords = random.choice( range(14, 28) )
        text = [self._firstWord()]

        for i in range(numbersWords):
            text.append(np.random.choice(self._wordDict[text[-1]]))

        return " ".join(text)