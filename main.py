import googletrans
import speech_recognition
import gtts
import playsound
from tkinter import *
from tkinter import ttk,messagebox
import textblob

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c.upper())
    # t1=googletrans.Translator()
    # text_=f"You have selected {c.upper()}"
    # trans_text=t1.translate(text_,src="english",dest=combo1.get())
    # text1.delete(1.0,END)
    # text1.insert(END,trans_text.text)
    # t2=googletrans.Translator()
    # text1_=f"You have selected {c1.upper()}"
    # trans_text1=t1.translate(text1_,src="english",dest=combo2.get())
    # text2.delete(1.0,END)
    # text2.insert(END,trans_text1.text)
    label2.configure(text=c1.upper())
    root.after(200,label_change)

def translate_now():
    print("detecting")
    c=combo1.get()
    c1=combo2.get()
    language=googletrans.LANGUAGES.items()
    for i,j in language:
        if(j==c):
            c=i
        if(j==c1):
            c1=i

    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak now...")
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice,language=c)
        text1.delete(1.0,END)
        text1.insert(END,text)
    

    translator=googletrans.Translator()
    translation=translator.translate(text,dest=c1)
    t1=googletrans.Translator()
    trans_text=t1.translate(text,src=combo1.get(),dest=combo2.get())
    text2.delete(1.0,END)
    text2.insert(END,trans_text.text)
    converted_audio=gtts.gTTS(trans_text.text,lang=c1)
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")

root=Tk()
root.title("Language Translator")
root.geometry("1080x450")

#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=110)

language=googletrans.LANGUAGES
languagev=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languagev,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("english")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2=ttk.Combobox(root,values=languagev,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("english")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate=Button(root,text="Speak Now",font="Roboto 15 bold italic",activebackground="orange",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()

root.configure(bg="white")

root.mainloop()