import random
from typing import Iterator
import numpy as np
from viterabot.controller.generator.iGenerator import iGenerator

class GeneratorLero(iGenerator):
    def __init__(self, filename) -> None:
        self.filename = filename
        self._openFile()
        self.pairs = self._makePairs()
        self._dictGenerator()

    def _openFile(self) -> None:
        self.book = open(self.filename, encoding='utf8').read()
        self.corpus = self.book.split()

    def _makePairs(self) -> Iterator[str]:
        for i in range(len(self.corpus)-1):
            yield (self.corpus[i], self.corpus[i+1])
    
    def _dictGenerator(self):
        self.wordDict = {}
        for word1, word2 in self.pairs:
            if word1 in self.wordDict.keys():
                self.wordDict[word1].append(word2)
            else:
                self.wordDict[word1] = [word2]

    def _firstWord(self):
        firstWord = np.random.choice(self.corpus)

        while firstWord.islower():
            firstWord = np.random.choice(self.corpus)
        return firstWord

    def generateText(self) -> str:
        numbersWords = random.choice( range(8, 30) )
        text = [self._firstWord()]

        for i in range(numbersWords):
            text.append(np.random.choice(self.wordDict[text[-1]]))

        return "".join(text)
    