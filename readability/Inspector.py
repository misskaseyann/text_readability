import os

class Inspector(object):
    def __init__(self):
        self.file = None

        #  do nothing

    def read(self, path):
        if (os.path.isfile(path)):
            self.file = open(path)
            print("Opened the file.")
            print(self.file.read())
            return self.file
        else:
            print("This is not a valid file path or file.")

    #  parse text file from token

    #  calculate score
