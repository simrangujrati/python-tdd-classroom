class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if (character=='a' or character=='A' or character=='e' or character=='E' or character=='i' or character=='I' or character=='o' or character=='O' or character=='u' or character=='U'):
            return True
        return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest_word = ''

        for word in list(sentence.split()):
            if len(word) > len(longest_word):
                longest_word=word
        return longest_word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        return [len(x) for x in text.split()]