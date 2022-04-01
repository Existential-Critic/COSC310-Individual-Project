import unittest
from SimilarityOfTwoSentences import SimilarityOfTwoSentences

class TestSimilarityOfTwoSentences(unittest.TestCase):
    # case where the two inputs are ""
    def test_nothing(self):
        result = SimilarityOfTwoSentences.sentence_similarity("", "")
        self.assertEquals(result, 1.0)
    
    # case where the user input is ""
    def test_no_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity("", "I like candy")
        self.assertEquals(result, 0.0)
    
    # case where the database input is ""
    def test_no_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I like cats", "")
        self.assertEquals(result, 0.0)
    
    # case where both inputs are " "
    def test_two_space(self):
        result = SimilarityOfTwoSentences.sentence_similarity(" ", " ")
        self.assertEquals(result, 0.0)
    
    # case where the database input is " "
    def test_space_in_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("", " ")
        self.assertEquals(result, 0.0)   
    
    # case where the user input is " "
    def test_space_in_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity(" ", "")
        self.assertEquals(result, 0.0)   
    
    # case of testing the synonym integration 
    def test_like_synonym(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I like cats", "I desire cats")
        self.assertEquals(result, 0.667)
    
    # case of testing the synonym integration 
    def test_want_and_feline_synonym(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I want cats", "I desire cats")
        self.assertEquals(result, 1.0)

    # case of testing the pos tagging influence on synonyms   
    def test_change_in_pos_tag(self):
        result = SimilarityOfTwoSentences.sentence_similarity("My want feline", "I desire cats")
        self.assertEquals(result, 0.333)
    
    # case where there is a space at the end of user input
    def test_space_at_the_end_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity("My like feline ", "My desire cats")
        self.assertEquals(result, 0.333)

    # case where there is a space at the end of database input
    def test_space_at_the_end_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("My like feline", "My desire cats ")
        self.assertEquals(result, 0.333)
    
    # case where there is a space at the start of user input
    def test_space_at_the_start_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity(" My like feline ", "My desire cats")
        self.assertEquals(result, 0.333)

    # case where there is a space at the start of database input
    def test_space_at_the_start_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("My like feline", " My desire cats")
        self.assertEquals(result, 0.333)
    
    # case where user input is bigger than database input
    def test_input_bigger(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I always wanted candy", "I want candy")
        self.assertEquals(result, 0.333)
    
    # case where user input is bigger than database input with synonym integration 
    def test_input_bigger_synonym_test(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I always wanted candy as well", "I perpetually want candy")
        self.assertEquals(result, 0.75)
    
    # case where there is a space at the start of user input
    def test_input_bigger_space_at_the_start_of_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity(" I always wanted candy as well", "I perpetually want candy")
        self.assertEquals(result, 0.75)
    
    # case where there is a space at the start of database input
    def test_input_bigger_space_at_the_start_of_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I always wanted candy as well", " I perpetually want candy")
        self.assertEquals(result, 0.75)
    
    # case where there is a space at the end of user input
    def test_input_bigger_space_at_the_end_of_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I always wanted candy as well ", "I perpetually want candy")
        self.assertEquals(result, 0.75)
    
    # case where there is a space at the end of database input
    def test_input_bigger_space_at_the_end_of_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I always wanted candy as well", "I perpetually want candy ")
        self.assertEquals(result, 0.75)
    
    # case where database input is is bigger 
    def test_database_bigger(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I want friends", "I want friends a lot")
        self.assertEquals(result, 0.6)

    # case where database input is is bigger with synonym test
    def test_database_bigger_synonym_test(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I desire friends", "I want friends a lot")
        self.assertEquals(result, 0.6)

    # case where database input is is bigger with space at the start of user input
    def test_database_bigger_space_at_the_start_of_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity(" I desire friends", "I want friends a lot")
        self.assertEquals(result, 0.6)

    # case where database input is is bigger with space at the start of database input
    def test_database_bigger_space_at_the_start_of_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I desire friends", " I want friends a lot")
        self.assertEquals(result, 0.6)
    
    # case where database input is is bigger with space at the end of user input
    def test_database_bigger_space_at_the_end_of_user_input(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I desire friends ", "I want friends a lot")
        self.assertEquals(result, 0.6)

    # case where database input is is bigger with space at the end of database input
    def test_database_bigger_space_at_the_end_of_database_prompt(self):
        result = SimilarityOfTwoSentences.sentence_similarity("I desire friends", "I want friends a lot ")
        self.assertEquals(result, 0.6)

# allows the running of the unit test via the pulgin Run code
if __name__ == '__main__':
    unittest.main()