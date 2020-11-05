# using __name__ and __main__

print("this is mod_1 name --> " + __name__)

def main():
    return "from mod_1 function"

    # pass     # keyword pass helps you pass without an error

# syntax if __name__  == "__main__":

if __name__ == "__main__":  # this checks if the code runs from current file
    main()