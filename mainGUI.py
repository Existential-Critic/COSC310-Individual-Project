#Import all needed classes from the other files
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList
from BotSentimentResponse import BotSentimentResponse
from SpellingMistakes import SpellingMistakes
#import's spacy data to significantly speed up the program
from SentencePOSTagger import SentencePOSTagger
import spacy_universal_sentence_encoder
#Import tkinter to create the GUI
import tkinter as tk

databaseInList = DatabaseToList.database_to_list()
nlp = spacy_universal_sentence_encoder.load_model('en_use_md')

class mainGUI:
    def __init__(self):
        #Create the window we will be working with
        self.window = tk.Tk()
        
        # used to to store topic database questions
        self.questionsAsked = []
        
        #Set the title of the window
        self.window.title("Helperbot 9000 Chat")

        #Give extra space on the far left side so it is centered
        self.window.grid_columnconfigure(0, weight=1)

        #Create global variable for state of conversation
        self.conState = 0

        #Create a global variable for length of text lines
        self.textLineLen = 0

        #Create the message log to hold all our said messages
        self.messageLog = []

        #Create two frames: main frame, to contain the chat log, and the type frame for entering new messages
        self.mainFrame = tk.Frame(width=1250,height=400,relief=tk.GROOVE,borderwidth=5,bg="white")
        self.typeFrame = tk.Frame(width=1000,height=50,relief=tk.GROOVE,borderwidth=5,bg="white")
        self.mainFrame.grid(row=0,column=0)
        self.typeFrame.grid(row=1,column=0)

        #Create textbox in mainframe
        self.mainBox = tk.Text(self.mainFrame,bg="white",width=152)
        self.mainBox.configure(state='disabled')
        self.mainBox.grid(row=0)

        #Create a scrollbar widget and set its command to the text widget
        self.scrollbar = tk.Scrollbar(self.mainFrame,orient='vertical',command=self.mainBox.yview)
        #Communicate back to the scrollbar
        self.mainBox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(row=0,column=1,sticky='ns')

        #Set the left and right configurations for the text
        self.mainBox.tag_configure('left',justify='left')
        self.mainBox.tag_configure('right',justify='right')
        self.mainBox.tag_configure('blue',foreground='blue')

        # # Set the main frame to not change shape automatically
        self.mainFrame.grid_propagate(False)

        #Create the entry widget for the user to enter in their responses
        self.typeEntry = tk.Entry(master=self.typeFrame,width=100,highlightbackground="black",highlightthickness=1)

        #Put 5 pixels between the entry line and the submission button to make space
        self.typeEntry.grid(pady=5)

        #Create a button labelled "Submit Response" for the user to press after writing their response
        self.submitButton = tk.Button(master=self.typeFrame,text="Submit Response",bg="black",fg="white")

        #Create a button to close the window
        self.exitButton = tk.Button(text="Exit Window",bg="black",fg="white")

        #Create a bind on the button for when it is clicked
        self.submitButton.bind("<Button-1>",self.handle_click)
        self.submitButton.grid()

        #Create a bind on the exit button for when it is clicked
        self.exitButton.bind("<Button-1>",self.closeWindow)

        #Call update to begin recursion
        self.update()

        #Begin the conversation between bot and user
        self.messageLog.append([GreetMessage.greetMessage(),"bot"])

        #Create the window loop
        self.window.mainloop()

    #Create a function to save what is typed into the submission bar
    def handle_click(self,event):
        if self.conState == 0:
            userInput = self.typeEntry.get()
            self.messageLog.append([userInput,"user"])
            self.typeEntry.delete(0,tk.END)
            spelledCorrect, wordSpelledIncorrect = SpellingMistakes.spelling_mistakes(userInput)
            if(not userInput.replace(' ','').isalpha()):
                self.messageLog.append(["Please try again, remember to use only letters.","bot"])
            elif(len(userInput.split()) != 1):
                self.messageLog.append(["Please try again, remember to only use one word for the greeting.","bot"])
            elif(not spelledCorrect):
                self.messageLog.append(["Please try again, there were spelling mistakes.","bot"])
                self.messageLog.append([f"The misspelled word(s) was: {wordSpelledIncorrect}","bot"])
            else:
                self.messageLog.append([GettingStarted.gettingStarted(),"bot"])
                self.conState = 1
        elif self.conState == 1:
            userInputSentence = self.typeEntry.get()
            self.messageLog.append([userInputSentence,"user"])
            self.typeEntry.delete(0,tk.END)
            spelledCorrect, wordSpelledIncorrect = SpellingMistakes.spelling_mistakes(userInputSentence)
            if((not userInputSentence.replace(' ','').isalpha())):
                self.messageLog.append(["Please try again, remember to use only letters.","bot"])
            elif (len(userInputSentence) == 0):
                self.messageLog.append(["Nothing was entered, please try again. Remember to use only letters.","bot"])
            elif (not spelledCorrect):
                self.messageLog.append(["Please try again, there were spelling mistakes.","bot"])
                self.messageLog.append([f"The misspelled word(s) was: {wordSpelledIncorrect}","bot"])
            elif(len(userInputSentence.split())<=1):
                self.messageLog.append([GoodbyeMessage.goodbyeMessage(),"bot"])
                self.typeFrame.destroy()
                self.exitButton.grid()
            else:
                botAnswer,correctnessValue,spaCyUsedInBotRespons = BotRespons.bot_respons(userInputSentence,databaseInList,nlp)
                if (spaCyUsedInBotRespons and (correctnessValue <= 0.8)):
                    self.messageLog.append(["I am sorry, I cannot understand that sentence. Could you say it a little more simply please?","bot"])
                elif ((not spaCyUsedInBotRespons) and (correctnessValue > 1 or correctnessValue <= (1/2))):
                    self.messageLog.append(["I am sorry, I cannot understand that sentence. Could you say it a little more simply please?","bot"])
                else:
                    if "?" in botAnswer:
                        self.messageLog.append([f"{botAnswer}","bot"])
                    else:
                        question, self.questionsAsked = BotSentimentResponse.bot_sentiment_response(userInputSentence, self.questionsAsked)
                        print(f"Bot: {botAnswer} {question}")
                        self.messageLog.append([f"{botAnswer} {question}","bot"])
                print(f"spaCy Used: {spaCyUsedInBotRespons}")
                print(f"POS tags: {SentencePOSTagger.sentence_pos_tagger(userInputSentence)}")
                print(f"Highest Value: {correctnessValue}")
                print(f"Questions Asked: {self.questionsAsked}")
                correctnessValue = 0

    #Function to close the window
    def closeWindow(self,event):
        self.window.destroy()

    #Function to update the chat log as it is written in
    def update(self):
        #Enable the textbox
        self.mainBox.configure(state='normal')
        #Go through each message in the message log and orient it left or right depending on which user said it
        for x in range(len(self.messageLog)):
            if x < self.textLineLen:
                pass
            elif self.messageLog[x][1] == "bot":
                self.mainBox.insert(tk.END,self.messageLog[x][0]+"\n",('left'))
                self.textLineLen += 1
                #Autoscroll to bottom
                self.mainBox.see("end")
            else:
                self.mainBox.insert(tk.END,self.messageLog[x][0]+"\n",('right','blue'))
                self.textLineLen += 1
                #Autoscroll to bottom
                self.mainBox.see("end")
        #Disable the textbox
        self.mainBox.configure(state='disabled')
        #Call the update again after 100ms
        self.window.after(100,self.update)

mainGUI()