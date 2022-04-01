from pydoc_data.topics import topics
from random import randint

class DatabaseTopicPrompt:
    def database_topic_prompt():
        topicPrompts = []
        topicPrompts.append("Do you have any hobbies?")
        topicPrompts.append("Do you have a boyfriend or girlfriend?")
        topicPrompts.append("Do you have any friends?")
        topicPrompts.append("Do you live with anyone?")
        topicPrompts.append("Do you have any pets?")
        topicPrompts.append("What do you like doing?")
        selectRand = randint(0,5)
        return topicPrompts[selectRand], len(topicPrompts)
