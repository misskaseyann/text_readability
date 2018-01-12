import os
import re


class Inspector(object):
    """
    Inspects a text file and evaluates a total number of words, sentences, and syllables.
    """
    def __init__(self):
        self.total_words = 0
        self.total_sentences = 0
        self.total_syllables = 0

    @staticmethod
    def read(p):
        if os.path.isfile(p):
            file = open(p, 'r+', encoding='utf-8')
            return file
        else:
            print("This is not a valid file path or file.")

    def eval(self, file):
        sentences = file.read()
        sentences = re.split('[.?!]+', sentences)
        sentences[:] = [x for x in sentences if x != '']
        self.total_sentences = len(sentences)
        for sentence in sentences:
            sentence.strip('\n')
            print(sentence)
            words = sentence.split(' ')
            words[:] = [x for x in words if x != '']
            self.total_words += len(words)
            for word in words:
                self.count_syllables(word)

    def count_syllables(self, w):
        word = w
        if word.endswith('e'):
            if len(word) > 2 and word.endswith("le") and not self.isvowel(word[-3]):
                pass
            else:
                word = word.rstrip('e')
        hasvowel = False
        for letter in word:
            if hasvowel and self.isvowel(letter):
                word = word.replace(letter, '', 1)
                hasvowel = False
            elif self.isvowel(letter):
                hasvowel = True
            else:
                hasvowel = False
        for letter in word:
            if self.isvowel(letter):
                self.total_syllables += 1

    @staticmethod
    def isvowel(letter):
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            return True
        else:
            return False

    def stats(self):
        return self.total_words, self.total_sentences, self.total_syllables

    def reading_ease(self):
        score = 206.835 - 1.015 * (self.total_words / self.total_sentences) - \
                84.6 * (self.total_syllables / self.total_words)
        print("Flesch-Kincaid Reading Ease Score: " + str(score))
        return score

    @staticmethod
    def school_level(score):
        if score >= 90.0:
            return "School level: 5th Grade\nVery easy to read. Easily understood by an average 11-year-old student."
        elif score >= 80.0:
            return "School level: 6th Grade\nEasy to read. Conversational English for consumers."
        elif score >= 70.0:
            return "School level: 7th Grade\nFairly easy to read."
        elif score >= 60.0:
            return "School level: 8th & 9th Grade\nPlain English. Easily understood by 13 to 15-year-old students."
        elif score >= 50.0:
            return "School level: 10th & 12th Grade\nFairly difficult to read."
        elif score >= 30.0:
            return "School level: College\nDifficult to read."
        elif score >= 0.0:
            return "School level: College Graduate\nVery difficult to read. Best understood by university graduates."
        else:
            return "Not a valid score."
