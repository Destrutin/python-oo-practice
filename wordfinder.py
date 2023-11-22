"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, filepath):
        file = open(filepath, "r")
        self.words = [line.strip() for line in file]
        print (f'{len(self.words)} words read')
        file.close()

    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Special Word Finder: filters blank spaces and comments."""

    def __init__(self, filepath):
        super().__init__(filepath)

        # filtered = []
        # for line in self.words:
        #     stripped = line.strip()
        #     if stripped and not stripped.startswith('#'):
        #         filtered = filtered + [stripped]
        # self.words = filtered
        # 
        # Started like this ^ but was able to look up how to make it comprehensive

        self.words = [line.strip() for line in self.words if line.strip() and not line.strip().startswith('#')]
