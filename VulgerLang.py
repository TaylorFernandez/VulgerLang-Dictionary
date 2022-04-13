import pygame as pg

class DataEntry:
    def __init__(self, word, pronounciation, type, definition):
        self.word = word
        self.pronounciation = pronounciation
        self.type = type
        self.definition = definition
    
    def printData(self):
        print("word:" + self.word)
        print("pronounciation:" + self.pronounciation)
        print("type:" + self.type)
        print("definition:" + self.definition)

    def getDefinition(self):
        return self.definition

    def getWord(self):
        return self.word

x = DataEntry("test", "howIsayIt", "verb", "What it means")

def loadDatabase(fileName):
    listData = []
    with open(fileName) as file:
        fileLines = file.readlines()
        for x in fileLines:
            arr = x.split(',')
            entry = DataEntry(arr[0], arr[1], arr[2], arr[3])
            listData.append(entry)    
    return listData

def findCustom(entry, english):
    x = entry.getDefinition()
    y = x.split(';')
    for i in y:
        if(i == english):
            return True
    return False

def findEnglsih(entry, custom):
    x = entry.getWord()
    if(x == custom):
        return True
    return False

def newWindow(width, height):
    screen = pg.display.set_mode((width,height))
    return screen
    
            
isLeaving = False
screen = newWindow(100,100)
print("What file do you want to load?\n")
filename = input()
listDict = loadDatabase(filename)

while(isLeaving == False):
    print("What word do you want to find?\n")
    word = input()
    if(word != "exit"):
        found = False
        for i in listDict:
            if(findEnglsih(i, word) == True or findCustom(i,word) == True):
                i.printData()
                found = True

        if(found == False):
         print("Error. That word cannot be found!")

    else:
        isLeaving = True

print("goodby!")
        
    


