from random import randint

class GoodbyeMessage:
    def goodbyeMessage():
        goodbyeMessages = []
        goodbyeMessages.append("Have a good day!")
        goodbyeMessages.append("See you later")
        goodbyeMessages.append("Bye bye.")
        goodbyeMessages.append("Goodbye")
        randomMessage = randint(0,3)
        return goodbyeMessages[randomMessage]