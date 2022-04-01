from BroadQuestion import BroadQuestion
from SentenceSentiment import SentenceSentinment
from BotTopicQuestionAsked import BotTopicQuestionAsked

class BotSentimentResponse:
    def bot_sentiment_response(sentenceString,topicList):
        sentenceSentiment,subjectivity = SentenceSentinment.sentence_sentiment(sentenceString)
        print(f"Sentiment Value: {sentenceSentiment}")
        if sentenceSentiment > 0:
            return BroadQuestion.broad_question(), topicList
        else:
            newSentenceString, topicList = BotTopicQuestionAsked.bot_topic_question_asked(topicList)
            return newSentenceString, topicList