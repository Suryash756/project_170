from tkinter import*

root = Tk()
root.title("percentage calculator")
root.geometry("600x600")
mark3 = Label(root)
mark5 = Label(root)
mark10 = Label(root)
class grade3:
    def __init__(self,maths,lang):
        self.language= lang
        self.mathamatics = maths
    def per(self):
        total = self.language+self.mathamatics
        per = (total*100)/200
        mark3["text"] = per
class grade5:
    def __init__(self,maths,lang,social):
        self.language= lang
        self.mathamatics = maths
        self.sst = social
    def per(self):
        total = self.language+self.mathamatics+self.sst
        per = (total*100)/300
        mark5["text"] = per
class grade10:
    def __init__(self,maths,lang,social,sci):
        self.language= lang
        self.mathamatics = maths
        self.sst = social
        self.science = sci
    def per(self):
        total = self.language+self.mathamatics+self.sst+self.science
        per = (total*100)/400
        mark10["text"] = per

obj_3 = grade3(89,91)
btn3= Button(root,text="percentage_checker_grade_3",command =obj_3.per)
btn3.pack()
mark3.pack()

obj_5 = grade5(89,91,97)
btn5= Button(root,text="percentage_checker__grade_5",command =obj_5.per)
btn5.pack()
mark5.pack()

obj_10 = grade10(89,91,97,100)
btn10= Button(root,text="percentage_checker__grade_10",command =obj_10.per)
btn10.pack()
mark10.pack()

root.mainloop()
    