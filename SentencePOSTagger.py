import nltk
from nltk.tokenize import RegexpTokenizer
from TokenizeWithoutPunctuation import TokenizeWithoutPunctuation

class SentencePOSTagger:
    def sentence_pos_tagger(str):
        tokenizeString = TokenizeWithoutPunctuation.tokenize_without_punctuation(str)
        return nltk.pos_tag(tokenizeString)