class spaCySentenceSimilarity:
    def spaCy_sentence_similarity(userIn, databaselist, nlp):

        # preps spacy with userIn
        userSentence = nlp(userIn)
        bestMatchScore = 0
        bestSentence = ""
        for i in range(len(databaselist)):
            # preps spacy with current prompt in the database
            databaseSentence = nlp(databaselist[i][0])
            # gets the similarity value
            matchScore = databaseSentence.similarity(userSentence)
            # checks if the similarity value is better than the best value
            if(matchScore > bestMatchScore):
                bestMatchScore = matchScore
                bestSentence = databaselist[i][1]
        return bestSentence, bestMatchScore