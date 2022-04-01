import unittest
from BotSentimentResponse import BotSentimentResponse

class TestBotSentimentResponse(unittest.TestCase):
    # case where there is an empty list with the input sentence being negative
    def test_empty_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", [])
        self.assertEquals(len(result[1]), 1)
    
    # case where there is an list of size 1 with the input sentence being negative
    def test_size_one_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", [""])
        self.assertEquals(len(result[1]), 2)

    # case where there is an list of size 2 with the input sentence being negative
    def test_size_two_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["",""])
        self.assertEquals(len(result[1]), 3)
    
    # case where there is an list of size 3 with the input sentence being negative
    def test_size_three_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["","",""])
        self.assertEquals(len(result[1]), 4)

    # case where there is an list of size 4 with the input sentence being negative
    def test_size_four_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["","","",""])
        self.assertEquals(len(result[1]), 5)

    # case where there is an list of size 5 with the input sentence being negative
    def test_size_five_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["","","","",""])
        self.assertEquals(len(result[1]), 6)

    # case where there is an list of size 6 with the input sentence being negative
    def test_size_six_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["","","","","",""])
        self.assertEquals(len(result[1]), 1)

    # case where there is an list of size 7 with the input sentence being negative
    # why? because there are only 6 topic database questions
    def test_size_seven_list_with_negative_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel sad", ["","","","","","",""])
        self.assertEquals(len(result[1]), 1)

    # case where there is an empty list with the input sentence being postive
    def test_empty_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", [])
        self.assertEquals(len(result[1]), 0)
    
    # case where there is an list of size 1 with the input sentence being postive
    def test_size_one_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", [""])
        self.assertEquals(len(result[1]), 1)

    # case where there is an list of size 2 with the input sentence being postive
    def test_size_two_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["",""])
        self.assertEquals(len(result[1]), 2)

    # case where there is an list of size 3 with the input sentence being postive
    def test_size_three_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["","",""])
        self.assertEquals(len(result[1]), 3)

    # case where there is an list of size 4 with the input sentence being postive
    def test_size_four_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["","","",""])
        self.assertEquals(len(result[1]), 4)

    # case where there is an list of size 5 with the input sentence being postive
    def test_size_five_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["","","","",""])
        self.assertEquals(len(result[1]), 5)

    # case where there is an list of size 6 with the input sentence being postive
    def test_size_six_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["","","","","",""])
        self.assertEquals(len(result[1]), 6)

    # case where there is an list of size 7 with the input sentence being postive
    # why? because there are only 6 topic database questions
    def test_size_seven_list_with_postive_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("I feel happy", ["","","","","","",""])
        self.assertEquals(len(result[1]), 7)
    
    # case where there is an list of size 7 with the input sentence being ""
    # why? because there are only 6 topic database questions
    def test_size_seven_list_with_nothing_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("", ["","","","","","",""])
        self.assertEquals(len(result[1]), 1)

    # case where there is an list that is empty with the input sentence being ""
    def test_empty_list_list_with_nothing_sentiment(self):
        result = BotSentimentResponse.bot_sentiment_response("", [])
        self.assertEquals(len(result[1]), 1)

if __name__ == '__main__':
    unittest.main()