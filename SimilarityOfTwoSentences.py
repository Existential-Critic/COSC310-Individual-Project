from turtle import pos
from SentencePOSTagger import SentencePOSTagger
from SynonymRecognition import SynonymRecognition

from DatabaseToList import DatabaseToList

class SimilarityOfTwoSentences:
    def sentence_similarity(userIn, prompt):
        # A speical case where nothing is inputed
        if len(userIn) == 0 and len(prompt) == 0:
            return round(1.0000, 3)
        
        # splits the user's input sentence to compare
        userSplit = userIn.split()
        
        # splits a database sentence to compare
        promptSplit = prompt.split()
        
        #  used to count the number of sentence_similarities
        count = 0

        # get the POS tags of the user's input sentence
        posPrompt = SentencePOSTagger.sentence_pos_tagger(prompt)
        
        correctValue = 0
        
        if (len(userSplit) <= len(promptSplit)):
            i=0
            while(i < len(userSplit)):
                # call SynonymRecognition and store the list of synonym into synonym
                synonym = SynonymRecognition.synonym_recognition(posPrompt[i][0], posPrompt[i][1])
                # Determines if a word in the input string matches an answer in our database
                # or whether the userSplit[i] matches any word from synonym
                if(userSplit[i] == promptSplit[i] or userSplit[i] in synonym):
                    count+=1
                i+=1
            # in case prompt is inputed nothing
            if len(promptSplit) == 0:
                correctValue = 0.0
            else:
                correctValue = count / len(promptSplit)
        else:
            i=0
            while(i < len(promptSplit)):
                # call SynonymRecognition and store the list of synonym into synonym
                synonym = SynonymRecognition.synonym_recognition(posPrompt[i][0], posPrompt[i][1])
                # Determines if a word in the input string matches an answer in our database
                # or whether the userSplit[i] matches any word from synonym
                if((userSplit[i] == promptSplit[i]) or (userSplit[i] in synonym)): #determines if a word in the input string matches an answer in our database
                    count+=1
                i+=1
            # in case prompt is inputed nothing
            if len(promptSplit) == 0:
                correctValue = 0.0
            else:
                correctValue = count / len(promptSplit)

        return round(correctValue, 3)