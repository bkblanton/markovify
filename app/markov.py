from collections import defaultdict
from random import choice

import re


class Markov:
    START = object()
    STOP = object()
    _last_word = re.compile(r'.*[.!?]+[^,\w]*$')

    def __init__(self, ends_with_sentence=True):
        self.markov = defaultdict(list)
        self.ends_with_sentence = ends_with_sentence

    def add_words(self, words):
        words = iter(words)
        word = self.START
        while True:
            prev = word
            try:
                word = next(words)
                self.markov[prev].append(word)
                if self.ends_with_sentence and self._last_word.match(word):
                    self.markov[word].append(self.STOP)
                    word = self.START
            except StopIteration:
                if prev is not self.START:
                    self.markov[prev].append(self.STOP)
                break

    def add_string(self, string):
        self.add_words(string.strip().split())

    def add_lines(self, lines):
        for line in lines:
            self.add_string(line.strip())

    @classmethod
    def from_string(cls, string, ends_with_sentence=True):
        markov = cls(ends_with_sentence=ends_with_sentence)
        markov.add_string(string)
        return markov

    @classmethod
    def from_lines(cls, lines, ends_with_sentence=True):
        markov = cls(ends_with_sentence=ends_with_sentence)
        markov.add_lines(lines)
        return markov

    def generate(self, n=1):
        for _ in range(n):
            word = self.START
            while word is not self.STOP:
                word = choice(self.markov[word])
                if type(word) is str:
                    yield word.strip()
