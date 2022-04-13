import re
#Stores information about a word in this structure. Has the ability to print out
#the information about the word, as well as getting important data about the word as well
class DataEntry:
    #creates the new object that stores information
    def __init__(self, word, pronounciation, type, definition):
        self.word = word
        self.pronounciation = pronounciation
        self.type = type
        self.definition = definition
    
    #prints all of the information about the word in an easy to read format
    def printData(self):
        print("word:" + self.word)
        print("pronounciation:" + self.pronounciation)
        print("type:" + self.type)
        print("definition:" + self.definition)

    #gets the definition of the word
    def getDefinition(self):
        return self.definition

    #gets the pronounciation of the word
    def getPronounciation(self):
        return self.pronounciation

    #gets the type of the word
    def getType(self):
        return self.type
    #gets the word in the new custom language
    def getWord(self):
        return self.word

#loads the internal database(array) with all of the words in the new language
#as well as the information about that word
def loadDatabase(fileName):
    listData = []
    with open(fileName) as file:
        fileLines = file.readlines()
        for x in fileLines:
            arr = x.split(',')
            entry = DataEntry(arr[0], arr[1], arr[2], arr[3])
            listData.append(entry)    
    return listData

#checks to see if the entry passed in matches the english definition
#done by splitting the definition into a list and checks each one
def findCustom(entry, english):
    x = entry.getDefinition()
    y = re.split(", |; |\n", x)
    for i in y:
        if(i == english):
            return True

    return False
    

#checks to see if the entry passed in matches the word from the custom language
def findEnglish(entry, custom):
    x = entry.getWord()
    if(x == custom):
        return True
    return False    

#tells the program if the user wants to continue running
isLeaving = False

#beginning of the program. Reads in a file name and loads the array with entries
print("What file do you want to load?\n")
filename = input()
listDict = loadDatabase(filename)

#main loop of the program. Requests a word from the user and will find the word if it exists
#if it does, it will print all the data about that word. If not, will tell the user
#the word was not found
while(isLeaving == False):
    print("What word do you want to find?")
    word = input()

    #checks to see if the user wants to exit
    if(word != "exit"):
        found = False
        #runs through every word in the list of entries and tries to find a match
        for i in listDict:
            if(findEnglish(i, word) == True):
                i.printData()
                found = True
            elif(findCustom(i, word) == True):
                i.printData()
                found = True

        #if the data is not found, program will tell the user it couldn't find that words
        if(found == False):
         print("Error. That word cannot be found!")
    else:
        isLeaving = True
#Prints goodby if the user is exiting the program
print("goodby!")