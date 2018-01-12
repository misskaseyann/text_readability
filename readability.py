from readability.Inspector import Inspector

if __name__ == "__main__":
    inspect = Inspector()
    #  Mac users: /Users/user_name/Documents/file
    inspect.eval(inspect.read(input("File path? \n")))
    stats = inspect.stats()
    print("Total words: " + str(stats[0]) + ". Total sentences: " + str(stats[1]) + ". Total syllables: " +
          str(stats[2]) + ".")
    print(inspect.school_level(inspect.reading_ease()))