# from _typeshed import Self
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3
import datetime


class ChatBot:
    def __init__(self, root):
        self.root=root


        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()


        # def wishMe():
        #     hour = int(datetime.datetime.now().hour)
        #     if hour >=0 and hour<12:
        #         speak("Good Morning!")

        #     elif hour >=12 and hour<18:
        #         speak("Good Afternoon!")

        #     else:
        #         speak("Good Evening!")

        #     speak("I am Sirra Sir. Please tell me how may i help you")


        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        self.root.title("ChatBot")
        # self.root.geometry("730x640+0+0")
        self.root.geometry("{}x{}+0+0".format(w,h))


        self.root.bind('<Return>', self.enter_func)


                # #*****************BACKGROUND IMAGE*******************

        self.img=Image.open(r"bg.psd")
        self.img=self.img.resize((1500,1000),Image.ANTIALIAS) 
        self.photo4=ImageTk.PhotoImage(self.img)   
        self.img_l1=Label(self.root, image=self.photo4)  
        # self.img_l1.place(x=0,y=h/4.4,width=w,height=1100)
        self.img_l1.place(x=0,y=0,width=w,height=h) 



        main_frame = Frame(self.root, bd=2, bg="grey", width=615)
        main_frame.pack(pady=20)
        # main_frame = Frame(self.root, bd=4, pady=10, bg="powder blue", width=610)
        # main_frame.pack()


        



        img_chat = Image.open("coverimg.jpg")
        img_chat = img_chat.resize((200, 70), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=15, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg, text='How Can I Help You?', font=("arial", 39, 'bold'), fg='#00264d', bg='white')
        Title_label.pack(side=TOP, pady=5)

        #*****************FOR SCROLL BAR AND TEXT AREA***************
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()



        #**************second frame**************
        btn_frame = Frame(self.root, bd=4, bg="white", width=730)
        btn_frame.pack(pady=0)


        label_1 = Label(btn_frame, text="Type Something", font=("arial", 14, 'bold'), fg='#00264d', bg='white' )
        label_1.grid(row=0, column=0, padx=25, sticky="w")


        #***********ENTRY BOX***************
        self.entry=StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=("arial", 14, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky="w")

        #***********FOR SEND BUTTON *************
        self.send = Button(btn_frame, text="Send>>", command=self.send ,font=("arial", 14, 'bold'), width=8, bg="#00264d")
        self.send.grid(row=0, column=2, padx=5, sticky="w")

        #***********FOR CLEAR BUTTON *************
        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=("arial", 14, 'bold'), width=8, bg="#00264d")
        self.clear.grid(row=1, column=0, padx=5, sticky="w")

        self.msg=''
        self.label_11 = Label(btn_frame, text=self.msg, font=("arial", 14, 'bold'), fg='#00264d', bg='white' )
        self.label_11.grid(row=1, column=1, padx=5, sticky="w")


        



#*************************FUNCTION DECLARATION*******************

    #FOR USING THE ENTER BUTTON WITH SEND BOTTON
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    #FOR CLEARING ALL DATA
    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    


    def send(self):
        send = '\t\t\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END, '\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg = "Please enter some input"
            self.label_11.config(text=self.msg, fg='red')

        else:
            self.msg=''
            self.label_11.config(text=self.msg, fg='red')

#**************CONVERSATION B/W US****************

        if (self.entry.get()=='hello'):
            pyttsx3.speak(self.text.insert(END, '\n\n'+'Bot: Hi!'))

        elif (self.entry.get()=='hi'):
            self.text.insert(END, '\n\n'+'Bot: Hello!')

        elif (self.entry.get()== 'how are you'):
            self.text.insert(END, '\n\n'+ "Bot: I'm Fine, Thanks!" )

        elif (self.entry.get()=='what is your name'):
            self.text.insert(END, '\n\n'+ "Bot: My Name is Bot" )

        elif (self.entry.get()=='who are you'):
            self.text.insert(END, '\n\n'+ "Bot: I'm Your Bot")

        elif (self.entry.get()=='who created you'):
            self.text.insert(END, '\n\n'+ "Bot: Respected sir Atul!")

        elif (self.entry.get()=='i love you'):
            self.text.insert(END, '\n\n'+'Bot: I Love You Too!')
 
        elif (self.entry.get()=='what is the chatbot'):
            self.text.insert(END, '\n\n'+'Bot: A chatbot is an artificial intelligence (AI) software that can simulate a conversation (or a chat) with a user in natural language through messaging applications, websites, mobile apps or through the telephone. \n')

        elif (self.entry.get()=='what is machine learning'):
            self.text.insert(END, '\n\n'+'Bot: Machine learning is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. \n')
        
        elif (self.entry.get()=='what is ml'):
            self.text.insert(END, '\n\n'+'Bot: Machine learning is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. \n')

        
        elif (self.entry.get()=='what is ML'):
            self.text.insert(END, '\n\n'+'Bot: Machine learning is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. \n')

        
        elif (self.entry.get()=='what is AI'):
            self.text.insert(END, '\n\n'+'Bot: Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. \n')

        
        elif (self.entry.get()=='what is artificial intelligence'):
            self.text.insert(END, '\n\n'+'Bot: Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. \n')

        #main help ****************

        elif (self.entry.get()=='how can i login'):
            self.text.insert(END, '\n\n'+'Bot: Enter the Email> Enter the password> Tap login \n')

        
        elif (self.entry.get()=='how can i registration'):
            self.text.insert(END, '\n\n'+'Bot: Tap on the Register button> Create New Account> Submit \n')

        
        elif (self.entry.get()=='how can i register'):
            self.text.insert(END, '\n\n'+'Bot: Tap on the Register button> Create New Account> Submit \n')


        
        

    

        else:
            self.text.insert(END, '\n\n'+ "Bot: Sorry, I didn't get this. Please check the Spelling or You can contect us via Email: facial2attendance@gmail.com")





if __name__=='__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
    

