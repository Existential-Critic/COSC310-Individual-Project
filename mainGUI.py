#Import all needed classes from the other files
from sklearn.preprocessing import scale
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList
from BotSentimentResponse import BotSentimentResponse
from SpellingMistakes import SpellingMistakes
from bingTranslate import translate
from flickrImage import topicTag
#import's spacy data to significantly speed up the program
from SentencePOSTagger import SentencePOSTagger
import spacy_universal_sentence_encoder
#Import tkinter to create the GUI
import tkinter as tk
#Import libraries to open images
from PIL import ImageTk,Image
from io import BytesIO
import requests

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

        #Create three frames: main frame, to contain the chat log, type frame for entering new messages, and image frame for holding images
        self.mainFrame = tk.Frame(width=1250,height=400,relief=tk.GROOVE,borderwidth=5,bg="white")
        self.typeFrame = tk.Frame(width=1000,height=50,relief=tk.GROOVE,borderwidth=5,bg="white")
        self.imageFrame = tk.Frame(width=250,height=250,relief=tk.GROOVE,borderwidth=5,bg="white")
        self.mainFrame.grid(row=0,column=0)
        self.typeFrame.grid(row=1,column=0)
        self.imageFrame.grid(row=2,column=0)

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

        #Set the main frame to not change shape automatically
        self.mainFrame.grid_propagate(False)

        #Set the image frame to not change shape automatically
        self.imageFrame.grid_propagate(False)

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
        self.greeting = GreetMessage.greetMessage()
        #Add image to image frame
        self.imageTag = topicTag(self.greeting)
        self.img = ImageTk.PhotoImage(self.createImage(self.imageTag))
        self.imageLabel = tk.Label(self.imageFrame,image=self.img)
        self.imageLabel.grid()
        self.messageLog.append([self.greeting,"bot"])
        #Translate the greetings and append to the message log
        self.translatedGreetings = translate([{'text':self.greeting}])
        for item in self.translatedGreetings:
            self.messageLog.append([item,"bot"])

        #Create the window loop
        self.window.mainloop()

    #Create a function to save what is typed into the submission bar
    def handle_click(self,events):
        if self.conState == 0:
            userInput = self.typeEntry.get()
            self.messageLog.append([userInput,"user"])
            self.typeEntry.delete(0,tk.END)
            spelledCorrect, wordSpelledIncorrect = SpellingMistakes.spelling_mistakes(userInput)
            if(not userInput.replace(' ','').isalpha()):
                onlyLettersMessage = "Please try again, remember to use only letters."
                onlyLettersImageTag = topicTag(onlyLettersMessage)
                onlyLettersImg = ImageTk.PhotoImage(self.createImage(onlyLettersImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=onlyLettersImg)
                self.imageLabel.grid()
                self.messageLog.append([onlyLettersMessage,"bot"])
                translatedOnlyLetterMessage = translate([{'text':onlyLettersMessage}])
                for item in translatedOnlyLetterMessage:
                    self.messageLog.append([item,"bot"])
            elif(len(userInput.split()) != 1):
                oneWordMessage = "Please try again, remember to only use one word for the greeting."
                oneWordImageTag = topicTag(oneWordMessage)
                oneWordImg = ImageTk.PhotoImage(self.createImage(oneWordImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=oneWordImg)
                self.imageLabel.grid()
                self.messageLog.append([oneWordMessage,"bot"])
                translatedOneWordMessage = translate([{'text':oneWordMessage}])
                for item in translatedOneWordMessage:
                    self.messageLog.append([item,"bot"])
            elif(not spelledCorrect):
                spellingMistakesMessage = "Please try again, there were spelling mistakes."
                spellingMistakesImageTag = topicTag(spellingMistakesMessage)
                spellingMistakesImg = ImageTk.PhotoImage(self.createImage(spellingMistakesImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=spellingMistakesImg)
                self.imageLabel.grid()
                misspelledWordsMessage = f"The misspelled word(s) was: {wordSpelledIncorrect}"
                self.messageLog.append([spellingMistakesMessage,"bot"])
                translatedSpellingMistakesMessage = translate([{'text':spellingMistakesMessage}])
                for item in translatedSpellingMistakesMessage:
                    self.messageLog.append([item,"bot"])
                self.messageLog.append([misspelledWordsMessage,"bot"])
                translatedMisspelledWordsMessage = translate([{'text':misspelledWordsMessage}])
                for item in translatedMisspelledWordsMessage:
                    self.messageLog.append([item,"bot"])
            else:
                gettingStartedMessage = GettingStarted.gettingStarted()
                gettingStartedImageTag = topicTag(gettingStartedMessage)
                gettingStartedImg = ImageTk.PhotoImage(self.createImage(gettingStartedImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=gettingStartedImg)
                self.imageLabel.grid()
                self.messageLog.append([gettingStartedMessage,"bot"])
                translatedGettingStartedMessage = translate([{'text':gettingStartedMessage}])
                for item in translatedGettingStartedMessage:
                    self.messageLog.append([item,"bot"])
                self.conState = 1
        elif self.conState == 1:
            userInputSentence = self.typeEntry.get()
            self.messageLog.append([userInputSentence,"user"])
            self.typeEntry.delete(0,tk.END)
            spelledCorrect, wordSpelledIncorrect = SpellingMistakes.spelling_mistakes(userInputSentence)
            if((not userInputSentence.replace(' ','').isalpha())):
                onlyLettersMessage = "Please try again, remember to use only letters."
                onlyLetterImageTag = topicTag(onlyLettersMessage)
                onlyLetterImg = ImageTk.PhotoImage(self.createImage(onlyLetterImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=onlyLetterImg)
                self.imageLabel.grid()
                self.messageLog.append([onlyLettersMessage,"bot"])
                translatedOnlyLetterMessage = translate([{'text':onlyLettersMessage}])
                for item in translatedOnlyLetterMessage:
                    self.messageLog.append([item,"bot"])
            elif (len(userInputSentence) == 0):
                nothingEnteredMessage = "Nothing was entered, please try again. Remember to use only letters."
                nothingEnteredImageTag = topicTag(nothingEnteredMessage)
                nothingEnteredImg = ImageTk.PhotoImage(self.createImage(nothingEnteredImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=nothingEnteredImg)
                self.imageLabel.grid()
                self.messageLog.append([nothingEnteredMessage,"bot"])
                translatedNothingEnteredMessage = translate([{'text':nothingEnteredMessage}])
                for item in translatedNothingEnteredMessage:
                    self.messageLog.append([item,"bot"])
            elif (not spelledCorrect):
                spellingMistakesMessage = "Please try again, there were spelling mistakes."
                spellingMistakesImageTag = topicTag(spellingMistakesMessage)
                spellingMistakesImg = ImageTk.PhotoImage(self.createImage(spellingMistakesImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=spellingMistakesImg)
                self.imageLabel.grid()
                misspelledWordsMessage = f"The misspelled word(s) was: {wordSpelledIncorrect}"
                self.messageLog.append([spellingMistakesMessage,"bot"])
                translatedSpellingMistakesMessage = translate([{'text':spellingMistakesMessage}])
                for item in translatedSpellingMistakesMessage:
                    self.messageLog.append([item,"bot"])
                self.messageLog.append([misspelledWordsMessage,"bot"])
                translatedMisspelledWordsMessage = translate([{'text':misspelledWordsMessage}])
                for item in translatedMisspelledWordsMessage:
                    self.messageLog.append([item,"bot"])
            elif(len(userInputSentence.split())<=1):
                goodbyeMessage = GoodbyeMessage.goodbyeMessage()
                goodbyeImageTag = topicTag(goodbyeMessage)
                goodbyeImg = ImageTk.PhotoImage(self.createImage(goodbyeImageTag))
                for widget in self.imageFrame.winfo_children():
                    widget.destroy()
                self.imageLabel = tk.Label(self.imageFrame,image=goodbyeImg)
                self.imageLabel.grid()
                self.messageLog.append([goodbyeMessage,"bot"])
                translatedGoodbyeMessage = translate([{'text':goodbyeMessage}])
                for item in translatedGoodbyeMessage:
                    self.messageLog.append([item,"bot"])
                self.typeFrame.destroy()
                self.exitButton.grid()
            else:
                botAnswer,correctnessValue,spaCyUsedInBotRespons = BotRespons.bot_respons(userInputSentence,databaseInList,nlp)
                notUnderstandMessage = "I am sorry, I cannot understand that sentence. Could you say it a little more simply please?"
                if (spaCyUsedInBotRespons and (correctnessValue <= 0.8)):
                    notUnderstandImageTag = topicTag(notUnderstandMessage)
                    notUnderstandImg = ImageTk.PhotoImage(self.createImage(notUnderstandImageTag))
                    for widget in self.imageFrame.winfo_children():
                        widget.destroy()
                    self.imageLabel = tk.Label(self.imageFrame,image=notUnderstandImg)
                    self.imageLabel.grid()
                    self.messageLog.append([notUnderstandMessage,"bot"])
                    translatedNotUnderstandMessage = translate([{'text':notUnderstandMessage}])
                    for item in translatedNotUnderstandMessage:
                        self.messageLog.append([item,"bot"])
                elif ((not spaCyUsedInBotRespons) and (correctnessValue > 1 or correctnessValue <= (1/2))):
                    notUnderstandImageTag = topicTag(notUnderstandMessage)
                    notUnderstandImg = ImageTk.PhotoImage(self.createImage(notUnderstandImageTag))
                    for widget in self.imageFrame.winfo_children():
                        widget.destroy()
                    self.imageLabel = tk.Label(self.imageFrame,image=notUnderstandImg)
                    self.imageLabel.grid()
                    self.messageLog.append([notUnderstandMessage,"bot"])
                    translatedNotUnderstandMessage = translate([{'text':notUnderstandMessage}])
                    for item in translatedNotUnderstandMessage:
                        self.messageLog.append([item,"bot"])
                else:
                    if "?" in botAnswer:
                        questionBotMessage = f"{botAnswer}"
                        questionImageTag = topicTag(questionBotMessage)
                        questionImg = ImageTk.PhotoImage(self.createImage(questionImageTag))
                        for widget in self.imageFrame.winfo_children():
                            widget.destroy()
                        self.imageLabel = tk.Label(self.imageFrame,image=questionImg)
                        self.imageLabel.grid()
                        self.messageLog.append([questionBotMessage,"bot"])
                        translatedQuestionBotMessage = translate([{'text':questionBotMessage}])
                        for item in translatedQuestionBotMessage:
                            self.messageLog.append([item,"bot"])
                    else:
                        question, self.questionsAsked = BotSentimentResponse.bot_sentiment_response(userInputSentence, self.questionsAsked)
                        answerQuestionBotMessage = f"{botAnswer} {question}"
                        answerQuestionImageTag = topicTag(answerQuestionBotMessage)
                        answerQuestionImg = ImageTk.PhotoImage(self.createImage(answerQuestionImageTag))
                        for widget in self.imageFrame.winfo_children():
                            widget.destroy()
                        self.imageLabel = tk.Label(self.imageFrame,image=answerQuestionImg)
                        self.imageLabel.grid()
                        self.messageLog.append([answerQuestionBotMessage,"bot"])
                        translatedAnswerQuestionBotMessage = translate([{'text':answerQuestionBotMessage}])
                        for item in translatedAnswerQuestionBotMessage:
                            self.messageLog.append([item,"bot"])
                correctnessValue = 0

    #Function to close the window
    def closeWindow(self,event):
        self.window.destroy()

    #Function to create image
    def createImage(self,url):
        self.imageURL = url
        #Open the image source
        self.response = requests.get(self.imageURL)
        #Save the image source
        self.imageData = self.response.content
        #Turn into a TKImage with proper dimensions
        self.image = Image.open(BytesIO(self.imageData))
        self.properImage = self.image.resize((250,250))
        return self.properImage

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