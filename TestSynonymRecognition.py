import unittest
from SynonymRecognition import SynonymRecognition

class TestSynonymRecognition(unittest.TestCase):
    # testing noun tag
    def test_NN(self):
        result = SynonymRecognition.synonym_recognition("tree", "NN")
        self.assertIn("tree_diagram", result)
    
    # testing noun plural tag
    def test_NNS(self):
        result = SynonymRecognition.synonym_recognition("desks", "NNS")
        self.assertIn("desk", result)

    # testing adverb singular tag
    def test_RB(self):
        result = SynonymRecognition.synonym_recognition("swiftly", "RB")
        self.assertIn("fleetly", result)

    # testing adverb comapative tag
    def test_RBR(self):
        result = SynonymRecognition.synonym_recognition("harder", "RBR")
        self.assertIn("severely", result)

    # testing adverb, superlative tag
    def test_RBS(self):
        result = SynonymRecognition.synonym_recognition("fastest", "RBS")
        self.assertIn("quickest", result)
    
    # testing adjective tag
    def test_JJ(self):
        result = SynonymRecognition.synonym_recognition("large", "JJ")
        self.assertIn("declamatory", result)

    # testing adjective, comparative tag
    def test_JJR(self):
        result = SynonymRecognition.synonym_recognition("larger", "JJR")
        self.assertIn("enceinte", result)

    # testing adjective, superlative tag
    def test_JJS(self):
        result = SynonymRecognition.synonym_recognition("largest", "JJS")
        self.assertIn("turgid", result)

    # testing verb tag
    def test_VB(self):
        result = SynonymRecognition.synonym_recognition("ask", "VB")
        self.assertIn("postulate", result)
        
    # testing verb gerund tag
    def test_VBG(self):
        result = SynonymRecognition.synonym_recognition("judging", "VBG")
        self.assertIn("approximate", result)

    # testing verb past tense
    def test_VBD(self):
        result = SynonymRecognition.synonym_recognition("pleaded", "VBD")
        self.assertIn("plead", result)

    # testing verb past participle
    def test_VBN(self):
        result = SynonymRecognition.synonym_recognition("reunified", "VBN")
        self.assertIn("reunify", result)

    # testing verb, present tense not 3rd person singular
    def test_VBP(self):
        result = SynonymRecognition.synonym_recognition("wrap", "VBP")
        self.assertIn("enwrap", result)

    # testing verb, present tense with 3rd person singular
    def test_VBZ(self):
        result = SynonymRecognition.synonym_recognition("bases", "VBZ")
        self.assertIn("found", result)

    # testing speical case where the word does not exist
    def test_UH(self):
        result = SynonymRecognition.synonym_recognition("sdf", "UH")
        self.assertTrue(result == [])

    # testing a speical case where the word "" is inputted
    def test_TO(self):
        result = SynonymRecognition.synonym_recognition("", "TO")
        self.assertTrue(result == [])

    # speical case where the tag is ""
    def test_no_tag(self):
        result = SynonymRecognition.synonym_recognition("bases", "")
        self.assertTrue(result == [])

    # speical case where the word is a tag
    def test_WRB(self):
        result = SynonymRecognition.synonym_recognition("WRB", "WRB")
        self.assertTrue(result == [])

    # speical case where the tag is teh word
    def test_word(self):
        result = SynonymRecognition.synonym_recognition("word", "word")
        self.assertTrue(result == [])

    # speical case where the word and tag is ""
    def test_nothing(self):
        result = SynonymRecognition.synonym_recognition("", "")
        self.assertTrue(result == [])

# allows the running of the unit test via the pulgin Run code
if __name__ == '__main__':
    unittest.main()