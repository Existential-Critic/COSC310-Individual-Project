import nltk
from nltk.tokenize import RegexpTokenizer


class TokenizeWithoutPunctuation:
    def tokenize_without_punctuation(str):
        tokenizer = RegexpTokenizer(r'\w+')
        list = tokenizer.tokenize(str)
        return list