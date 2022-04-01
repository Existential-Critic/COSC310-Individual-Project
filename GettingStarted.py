from random import randint

class GettingStarted:
    def gettingStarted():
        starterMessages = [] 
        starterMessages.append("How are you feeling?")
        starterMessages.append("What is bothering you?")
        starterMessages.append("How can I help you?")
        starterMessages.append("What do you feel is wrong?")
        randomMessage = randint(0,3)
        return starterMessages[randomMessage]