import os

class Inspector(object):
    def __init__(self):
        self.file = None
        self.total_words = 0
        self.total_sentences = 0
        self.total_syllables = 0

    def read(self, p):
        if (os.path.isfile(p)):
            self.file = open(p)
            print("Opened the file.")
            return self.file
        else:
            print("This is not a valid file path or file.")

    def eval(self):
        sentences = self.file.read().split('.')
        sentences[:] = [x for x in sentences if x != '']
        self.total_sentences = len(sentences)
        print("Number of sentences: " + str(self.total_sentences))
        print(sentences)
        for sentence in sentences:
            words = sentence.split(' ')
            words[:] = [x for x in words if x != '']
            self.total_words += len(words)
            for word in words:
                self.count_syllables(word)
        print("word count is: " + str(self.total_words))
        print("syllable count is: " + str(self.total_syllables))

    def count_syllables(self, w):
        word = w
        if word.endswith('e'):
            if word.endswith("le") and not self.isvowel(word[-3]):
                print("passed")
                pass
            else:
                print("stripped e from " + word)
                word = word.rstrip('e')
                print(word)
        hasvowel = False
        for letter in word:
            if hasvowel and self.isvowel(letter):
                print("stripped " + letter + " from word.")
                word = word.replace(letter, '', 1)
                print(word)
                hasvowel = False
            elif self.isvowel(letter):
                hasvowel = True
            else:
                hasvowel = False
        #syl = 0
        for letter in word:
            if self.isvowel(letter):
                self.total_syllables += 1


    def isvowel(self, l):
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or l == 'y':
            return True
        else:
            return False