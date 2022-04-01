from random import randint

class GreetMessage:
    def greetMessage():
        greetMessages = []
        greetMessages.append("Hello")
        greetMessages.append("Howdy")
        greetMessages.append("Hi")
        greetMessages.append("Greetings")
        randomMessage = randint(0,3)
        return greetMessages[randomMessage]