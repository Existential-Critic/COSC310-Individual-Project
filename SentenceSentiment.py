from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentenceSentinment:
    def sentence_sentiment(sentence):
        sentiment_analyzer = SentimentIntensityAnalyzer()
        compoundScore = sentiment_analyzer.polarity_scores(sentence)['compound']
        subjectivity = ""
        if compoundScore > 0:
            subjectivity = "Positive"
        elif compoundScore < 0:
            subjectivity = "Negative"
        else:
            subjectivity = "Neutral"
        return compoundScore,subjectivity