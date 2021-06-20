from tkinter import *
from PyDictionary import PyDictionary
dic = PyDictionary()
root = Tk()

root.geometry("400x400")
def dict():
    meaning.config(text=dic.meaning(word.get())['Noun'][0])
    synonym.config(text=dic.synonym(word.get()))
    antonym.config(text=dic.antonym(word.get()))
Label( root, text="Dictionary", font=("Arial 20 bold"), fg="Green").pack(pady=10)

frame= Frame(root)
Label(frame, text="TYPE WORD", font=("Arial 15 bold")),pack(side=LEFT)
word= Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font=("Arial 10 bold")),pack(side=LEFT)
meaning = Label(frame1, text="",font=("Arial 10"))
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(root)
Label(frame2, text="Synonym:- ", font=("Arial 10 bold")),pack(side=LEFT)
synonym = Label(frame2, text="",font=("Arial 10"))
synonym.pack()
frame2.pack(pady=10)

frame3 = Frame(root)
Label(frame3, text="Antonym:- ", font=("Arial 10 bold")),pack(side=LEFT)
antonym = Label(frame3, text="",font=("Arial 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="SUBMIT", font=("Arial 15 bold"), command=dic).pack()

root.mainloop()