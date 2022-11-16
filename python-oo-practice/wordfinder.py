"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine to create a word finder

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ['apple', 'banana', 'kiwi']
    True
    """

    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized Word Finder
    >>> swf = SpecialWordFinder('complex.txt')
    3 words read

    >>> swf.random() in ['carrot', 'potato', 'onion']
    True
    """

    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]
