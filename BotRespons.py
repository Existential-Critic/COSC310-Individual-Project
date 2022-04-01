from SimilarityOfTwoSentences import SimilarityOfTwoSentences
from spaCySentenceSimilarity import spaCySentenceSimilarity

class BotRespons:
    def bot_respons(userInput, databasePrompts, nlp):
        databaseList = databasePrompts
        botReply = ""
        bestMatch = 0
        for i in range(len(databaseList)):
            correctValue = SimilarityOfTwoSentences.sentence_similarity(userInput,databaseList[i][0])  #calls our similarities function to see the value of matched words
            #statement ensures that the best matched string and words matched values are updated if greater match is found
            if correctValue > bestMatch:
                botReply = databaseList[i][1]     
                bestMatch = correctValue    
        
        spaCyUsed = False
        
        if bestMatch < (4/5):
            botReply, bestMatch = spaCySentenceSimilarity.spaCy_sentence_similarity(userInput, databasePrompts, nlp)
            spaCyUsed = True
        
        return botReply, bestMatch, spaCyUsed