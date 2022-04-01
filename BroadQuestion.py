from random import randint

class BroadQuestion:
    def broad_question():
        diffQuestions = []
        diffQuestions.append("What else are you feeling?")
        diffQuestions.append("What else is keeping you down?")
        diffQuestions.append("Would you like talk about anything else?")
        diffQuestions.append("What else would you like to talk about?")
        diffQuestions.append("Is there anything else that is keeping you down?")
        diffQuestions.append("Is there anything else I can help you with?")
        diffQuestions.append("What else is on your mind?")
        diffQuestions.append("How else can I help you?")
        diffQuestions.append("Is there anything else you are feeling?")
        diffQuestions.append("What else would you like to talk about?")
        diffQuestions.append("What else do you feel?")
        diffQuestions.append("Is there anything else on your mind?")
        diffQuestions.append("Anything else you forgot to mention? ")
        selectRand = randint(0,12)
        return diffQuestions[selectRand]