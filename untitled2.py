from tkinter import *
import random

root=Tk()
root.title("Totally legit IQ test")
root.geometry("400x400")
root.config(bg="lavender")

label = Label(root, bg="orchid3",fg="white", font=("Times",40))
label.place(relx=0.5,rely=0.4,anchor=CENTER)
label2 = Label(root, bg="lavender", font=("Times",20),text="Score: 0")
label2.place(relx=0.15,rely=0.1,anchor=CENTER)
label3=Label(root,bg="lavender",text="Rules: type 'skip' to skip the question.")
label3.place(relx=0.5,rely=0.2,anchor=CENTER)
label5=Label(root,bg="lavender",text="do not put spaces in between words.")
label5.place(relx=0.5,rely=0.25,anchor=CENTER)
label6=Label(root,bg="lavender",text="Thanks for playing and have fun!")
label6.place(relx=0.5,rely=0.3,anchor=CENTER)
label4=Label(root,bg="lavender",font=("Times",20))
label4.place(relx=0.5,rely=0.55,anchor=CENTER)
entry = Entry(root)
entry.place(relx=0.5,rely=0.65,anchor=CENTER)

class game:
    def __init__(self):
        self._score=0
        self.active=True;
    def updateGame(self):
        if(self.active==True):
            self.text=["orange","red","yellow","green","cyan","blue","purple","navy","forestgreen","skyblue", "wheat", "pink", "white", "black", "lavender","gray","gold","lime","plum","teal","chocolate","brown"]
            self.convience=len(self.text)-1 #this is just here since im lazy
            self.number = random.randint(0,self.convience)
            self.number2 = random.randint(0,self.convience)
            self.number3 = random.randint(0,self.convience)
            label["text"]=self.text[self.number]
            label["fg"]=self.text[self.number2]
            label["bg"]=self.text[self.number3]
            self.questions = ["What is the font color?","What color does it say?","What is the background color?"]
            self.qn = random.randint(0,2)
            label4['text']=self.questions[self.qn]
            self.active=False
            label3["text"]=""
            label5["text"]=""
            label6["text"]=""
            self.y=0.8
        
    def check(self):
        self.ans = entry.get()
        if(self.active==False):
            if(self.qn==0):
                if(self.ans==self.text[self.number2]):
                    self._score+=1
                elif(self.ans=="skip" or self.ans=="Skip"):
                    self._score = self._score
                else:
                    self._score-=1
            elif(self.qn==1):
                if(self.ans==self.text[self.number]):
                    self._score+=1
                elif(self.ans=="skip" or self.ans=="Skip"):
                    self._score = self._score
                else:
                    self._score-=1
            elif(self.qn==2):
                if(self.ans==self.text[self.number3]):
                    self._score+=1
                elif(self.ans=="skip" or self.ans=="Skip"):
                    self._score = self._score
                else:
                    self._score-=1
            label2["text"]="Score: "+str(self._score)
            self.number = random.randint(0,9)
            self.number2 = random.randint(0,9)
            self.number3 = random.randint(0,9)
            label["text"]=self.text[self.number]
            label["fg"]=self.text[self.number2]
            label["bg"]=self.text[self.number3]
            self.qn = random.randint(0,2)
            label4['text']=self.questions[self.qn]
            entry.delete(0,END)
        
gaem = game()
btn=Button(root,text="Start",command=gaem.updateGame, highlightbackground='#E6E6FA')
btn.place(relx=0.65,rely=0.8,anchor=CENTER)
    
btn=Button(root,text="Check",command=gaem.check, highlightbackground='#E6E6FA')
btn.place(relx=0.35,rely=0.8,anchor=CENTER)

root.mainloop()

#This took me 2 hours to code and debug....
