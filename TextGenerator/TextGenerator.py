import random
# Depth parameter:
    # Takes list of words
    # Scans for word count and depth


def storeWords(wordSoup, depth): # Create dictionary based on word soup
    wordDict = dict()
    for x in range(0, len(wordSoup)-depth):
        wordDict.setdefault(wordSoup[x], [])
        chunk = ""
        for y in range(1, depth+1):
            chunk += wordSoup[x + y] + " "
        wordDict[wordSoup[x]].append(chunk)
    return wordDict

def createString(wordDict, wordCount, depth): # Create string based on dictionary
    newText = random.choice(list(wordSoup)) + " " # Starts string with random element from dict
    for x in range(0,wordCount-1):
        for y in range(0, depth):
            newText += random.choice(wordDict[newText.split()[-1]]) # Takes most recent word from newText, checks dict, appends value of that word
    return newText

# DRIVER CODE
file1 = open("Goats.txt", encoding ="utf-8")
wordSoup = file1.read().lower()
for char in '“”0123456789…’‘':
    wordSoup = wordSoup.replace(char, '')
wordSoup = wordSoup.split() # Reads file, converts to string, lowercases then splits into list of words
wordCount = int(input("How many words do you want? "))  # Scans for integer input
depth = int(input("Depth value (default depth is 1) "))
wordDict = storeWords(wordSoup, depth)
print(createString(wordDict, wordCount, depth) + ".")
# print(wordDict)
