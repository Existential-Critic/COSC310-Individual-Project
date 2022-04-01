from DatabaseTopicPrompt import DatabaseTopicPrompt

class BotTopicQuestionAsked:
    def bot_topic_question_asked(botTopicList):
        databasePrompt,databaseTopicLength = DatabaseTopicPrompt.database_topic_prompt()
        if len(botTopicList) >= databaseTopicLength:
            botTopicList = []
            botTopicList.append(databasePrompt)
            return databasePrompt, botTopicList
        else:
            while databasePrompt in botTopicList:
                databasePrompt,databaseTopicLength = DatabaseTopicPrompt.database_topic_prompt()
            botTopicList.append(databasePrompt)
            return databasePrompt, botTopicList