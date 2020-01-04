import spellchecker

def get_file():
    valid = True
    while valid:
        try:
            fileName = input("Enter the name of the file to read:\n")
            f = open(fileName, "r")
            valid = False
            return f
        except:
            print("Could not open file.")
            
def checker(file):
    counter = 1
    passed = 0
    failed = 0
    allWords = 0
    for line in file:
        for x in line.split():
            allWords += 1
            if SP.check(x) == True:
                passed += 1
                continue
            else:
                failed += 1
                print("Possible Spelling Error on line", counter, ":", x)
        counter += 1
    passing = "{:,}".format(passed)
    failed = "{:,}".format(failed)
    failedPercent = round(((passed/allWords)*100), 2)
    print(passing, "words passed spell checker.")
    print(failed, "words failed spell checker.")
    print(str(round(((passed/allWords)*100), 2)) + "% of the words passed.")
         
if __name__ == "__main__":
    SP = spellchecker.spellchecker("english_words.txt")
    print("Welcome to Text File Spellchecker.")
    files = get_file()
    checker(files)
    
    files.close()
    
    
        
    