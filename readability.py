from readability.Inspector import Inspector

if __name__ == "__main__":
    inspect = Inspector()
    #  Mac users: /Users/user_name/Documents/file
    inspect.read(input("File path? \n"))