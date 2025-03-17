class Anagram:
    def __init__(self, word):
        """Initialize the Anagram class with a word."""
        self.word = word.lower()  # Store the word in lowercase to handle case-insensitivity

    def match(self, possible_anagrams):
        """Return a list of words from possible_anagrams that are anagrams of self.word."""
        matches = []
        # Convert self.word to sorted list of letters once to avoid repeated computation
        sorted_word = sorted(self.word)
        
        for candidate in possible_anagrams:
            # Check if candidate is an anagram by comparing sorted letters
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)
        
        return matches