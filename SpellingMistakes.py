from nltk.corpus import stopwords
from nltk.corpus import brown

class SpellingMistakes:
    def spelling_mistakes(userInput):
        userInputLowerCaseSplit = userInput.lower().split()
        userInputLowerCaseSplitOrginialSize = userInput.split() 
        #stop words are words like the, they and then
        stopWords = set(stopwords.words('english'))
        # gets a list of words
        wordList = brown.words()
        spelledCorrect = []
        wordSpelledIncorrect = []
        # gose through each word and checks if it is in stopsWords or wordList, if it is, then 
        # will set spelledCorrect to True 
        for i in range(len(userInputLowerCaseSplit)):
            if (userInputLowerCaseSplit[i] in stopWords) or (userInputLowerCaseSplit[i] in wordList):
                spelledCorrect.append(True)
            else:
                spelledCorrect.append(False)
                wordSpelledIncorrect.append(userInputLowerCaseSplitOrginialSize[i])
        print(spelledCorrect)
        if False in spelledCorrect:
            return False, wordSpelledIncorrect
        else:
            return True, wordSpelledIncorrect