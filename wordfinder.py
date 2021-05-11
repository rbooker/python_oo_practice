"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
	"""A class that accepts as an argument a path to a file that contains words, one per line.
	Generates a list, stored in an attribute, words, of all the words contained in the file."""

	def __init__(self, path):
		"""Instantiate a new instance of the WordFinder class from an argument, 'path', to a file containing words, one per line"""
		self.file_path = path
		self.words = self.read_words()
		print(f"{len(self.words)} words read")


	def read_words(self):
		"""Reads the words from the provided file into a list"""
		file = open(self.file_path, "r")
		wordlist = []
		for line in file:
			wordlist.append(line[:-1])
		file.close()
		return wordlist

	def random(self):
		"""Returns a randomly selected word from the words list using random.choice()"""
		return choice(self.words)

class SpecialWordFinder(WordFinder):
	"""A subclass of WordFinder that also accepts as arguments files that contain blank lines or commented lines (i.e. lines that start with '#')"""
	def __init__ (self, path):
		"""Instantiate a new instance of the SpecialWordFinder class from an argument, 'path', to a file containing words, one per line
			Weeds out blank lines or lines starting with '#'"""
		super().__init__(path)
		self.words = [word for word in self.words if len(word) != 0 and word[0] != "#"]