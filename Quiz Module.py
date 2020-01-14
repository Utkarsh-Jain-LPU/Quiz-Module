from tkinter import messagebox
from tkinter import *
import tkinter
import sqlite3

marks = {"E1": "", "E2": "", "E3": "", "E4": "", "E5": "", "E6": "", "E7": "", "E8": "", "E9": "", "E10": ""}
marks1 = {"M1": "", "M2": "", "M3": "", "M4": "", "M5": "", "M6": "", "M7": "", "M8": "", "M9": "", "M10": ""}
marks2 = {"H1": "", "H2": "", "H3": "", "H4": "", "H5": "", "H6": "", "H7": "", "H8": "", "H9": "", "H10": ""}
answer = ""
text = ""
count = 0


def check():
    data = Name.get()
    data1 = Reg.get()
    data2 = Sec.get()
    data3 = var.get()
    verify = data1.isdigit()
    if data == "":
        messagebox.showwarning("Warning...!!", "Name field must not be Empty.")
    elif data1 == "":
        messagebox.showwarning("Warning...!!", "Registration No. field must not be Empty.")
    elif verify == False:
        messagebox.showerror("Error...!!", "Registration Number must be in digits.")
    elif len(data1) != 8:
        messagebox.showerror("Error...!!", "Registration Number must be of 8 digits.")
    elif data2 == "":
        messagebox.showwarning("Warning...!!", "Section field must not be Empty.")
    elif data3 == 0:
        messagebox.showwarning("Warning...!!", "You have not selected any Category.")
    else:
        messagebox.showinfo("Greeting", "Welcome \"" + data + "\"")
        selection()


def selection():
    global text
    data = var.get()
    if data == 1:
        text = "Easy"
        obj = Easy1()
        Home.withdraw()
    elif data == 2:
        text = "Medium"
        obj = Med1()
        Home.withdraw()
    else:
        text = "Hard"
        obj = Hard1()
        Home.withdraw()


class Easy1(Tk):
    def __init__(self):
        self.easy1 = Tk()
        self.easy1.title("Question Bank")
        self.easy1.geometry("450x500+535+125")

        Label(self.easy1, text="Easy Questions - ( 1/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy1, text="Let, ABC = ( 'Apple','Banana','Cherry','Guava' ). \n "
                               "Then, What is the value of print ( ABC [2] ) ?", font="Helvetica 12 bold",
              bg="light grey", fg="chocolate", bd="3").place(x="40", y="70")

        Label(self.easy1, text="1) Banana", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy1, text="2) Apple", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy1, text="3) Cherry", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy1, text="4) Guava", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy1, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy1, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy1, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee1).place(x="165", y="380")

        Button(self.easy1, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne2).place(x="230", y="380")

        Button(self.easy1, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee1():
        marks["E1"] = answer.get()
        if marks["E1"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E1"]) == 1 or int(marks["E1"]) == 2 or int(marks["E1"]) == 3 or int(marks["E1"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callne2(self):
        self.easy1.withdraw()
        obj = Easy2()


class Easy2(Tk):
    def __init__(self):
        self.easy2 = Tk()
        self.easy2.title("Question Bank")
        self.easy2.geometry("450x500+535+125")

        Label(self.easy2, text="Easy Questions - ( 2/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy2, text="Which keyword is used for functions ?", font="Helvetica 12 bold", bg="light grey",
              fg="chocolate", bd="3").place(x="60", y="80")

        Label(self.easy2, text="1) Fun", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy2, text="2) Def", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy2, text="3) Function", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy2, text="4) Define", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy2, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy2, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy2, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe1).place(x="137", y="380")

        Button(self.easy2, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee2).place(x="197", y="380")

        Button(self.easy2, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne3).place(x="260", y="380")

        Button(self.easy2, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee2():
        marks["E2"] = answer.get()
        if marks["E2"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E2"]) == 1 or int(marks["E2"]) == 2 or int(marks["E2"]) == 3 or int(marks["E2"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe1(self):
        self.easy2.withdraw()
        obj = Easy1()

    def callne3(self):
        self.easy2.withdraw()
        obj = Easy3()


class Easy3(Tk):
    def __init__(self):
        self.easy3 = Tk()
        self.easy3.title("Question Bank")
        self.easy3.geometry("450x500+535+125")

        Label(self.easy3, text="Easy Questions - ( 3/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy3, text="Which of the following enclose the input parameters \n ""and arguments of a function ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="20", y="70")

        Label(self.easy3, text="1) Parenthesis", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy3, text="2) Brackets", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy3, text="3) Curly Braces", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy3, text="4) Quotation Mark", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy3, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy3, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy3, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe2).place(x="137", y="380")

        Button(self.easy3, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee3).place(x="197", y="380")

        Button(self.easy3, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne4).place(x="260", y="380")

        Button(self.easy3, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee3():
        marks["E3"] = answer.get()
        if marks["E3"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E3"]) == 1 or int(marks["E3"]) == 2 or int(marks["E3"]) == 3 or int(marks["E3"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe2(self):
        self.easy3.withdraw()
        obj = Easy2()

    def callne4(self):
        self.easy3.withdraw()
        obj = Easy4()


class Easy4(Tk):
    def __init__(self):
        self.easy4 = Tk()
        self.easy4.title("Question Bank")
        self.easy4.geometry("450x500+535+125")

        Label(self.easy4, text="Easy Questions - ( 4/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy4, text="Which of the following items are present in the \n function header ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="40", y="70")

        Label(self.easy4, text="1) Function Name", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy4, text="2) Function List", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy4, text="3) Return Value", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy4, text="4) Both A and B", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy4, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy4, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy4, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe3).place(x="137", y="380")

        Button(self.easy4, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee4).place(x="197", y="380")

        Button(self.easy4, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne5).place(x="260", y="380")

        Button(self.easy4, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee4():
        marks["E4"] = answer.get()
        if marks["E4"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E4"]) == 1 or int(marks["E4"]) == 2 or int(marks["E4"]) == 3 or int(marks["E4"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe3(self):
        self.easy4.withdraw()
        obj = Easy3()

    def callne5(self):
        self.easy4.withdraw()
        obj = Easy5()


class Easy5(Tk):
    def __init__(self):
        self.easy5 = Tk()
        self.easy5.title("Question Bank")
        self.easy5.geometry("450x500+535+125")

        Label(self.easy5, text="Easy Questions - ( 5/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy5, text="How many Keyword argument can be passed to a \n ""function in a single function call ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="30", y="70")

        Label(self.easy5, text="1) Zero", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy5, text="2) One", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy5, text="3) Zero or more", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy5, text="4) One or more", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy5, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy5, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy5, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe4).place(x="137", y="380")

        Button(self.easy5, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee5).place(x="197", y="380")

        Button(self.easy5, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne6).place(x="260", y="380")

        Button(self.easy5, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee5():
        marks["E5"] = answer.get()
        if marks["E5"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E5"]) == 1 or int(marks["E5"]) == 2 or int(marks["E5"]) == 3 or int(marks["E5"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe4(self):
        self.easy5.withdraw()
        obj = Easy4()

    def callne6(self):
        self.easy5.withdraw()
        obj = Easy6()


class Easy6(Tk):
    def __init__(self):
        self.easy6 = Tk()
        self.easy6.title("Question Bank")
        self.easy6.geometry("450x500+535+125")

        Label(self.easy6, text="Easy Questions - ( 6/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy6, text="What is the Output : d = { 'John' : 40, 'Peter' : 45 }. \n d [ 'John' ] = ??",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="35", y="70")

        Label(self.easy6, text="1) 45", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy6, text="2) 40", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy6, text="3) Peter", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy6, text="4) John", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy6, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy6, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy6, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe5).place(x="137", y="380")

        Button(self.easy6, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee6).place(x="197", y="380")

        Button(self.easy6, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne7).place(x="260", y="380")

        Button(self.easy6, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee6():
        marks["E6"] = answer.get()
        if marks["E6"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E6"]) == 1 or int(marks["E6"]) == 2 or int(marks["E6"]) == 3 or int(marks["E6"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe5(self):
        self.easy6.withdraw()
        obj = Easy5()

    def callne7(self):
        self.easy6.withdraw()
        obj = Easy7()


class Easy7(Tk):
    def __init__(self):
        self.easy7 = Tk()
        self.easy7.title("Question Bank")
        self.easy7.geometry("450x500+535+125")

        Label(self.easy7, text="Easy Questions - ( 7/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy7, text="Which of the following Statement given below \n is/are true ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="40", y="70")

        Label(self.easy7, text="1) Tuple have Structure and List have Order", font="Helvetica 12 bold")\
            .place(x="40", y="140")

        Label(self.easy7, text="2) Tuple are immutable and List are mutable", font="Helvetica 12 bold")\
            .place(x="40", y="180")

        Label(self.easy7, text="3) None of these", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy7, text="4) Both A and B", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy7, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy7, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy7, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe6).place(x="137", y="380")

        Button(self.easy7, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee7).place(x="197", y="380")

        Button(self.easy7, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne8).place(x="260", y="380")

        Button(self.easy7, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee7():
        marks["E7"] = answer.get()
        if marks["E7"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E7"]) == 1 or int(marks["E7"]) == 2 or int(marks["E7"]) == 3 or int(marks["E7"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe6(self):
        self.easy7.withdraw()
        obj = Easy6()

    def callne8(self):
        self.easy7.withdraw()
        obj = Easy8()


class Easy8(Tk):
    def __init__(self):
        self.easy8 = Tk()
        self.easy8.title("Question Bank")
        self.easy8.geometry("450x500+535+125")

        Label(self.easy8, text="Easy Questions - ( 8/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy8, text="Suppose List1 = [ 3, 5, 25, 1, 3 ]. What is the Value \n of min ( List1 ) ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="30", y="70")

        Label(self.easy8, text="1) 5", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy8, text="2) 25", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy8, text="3) 1", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy8, text="4) 3", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy8, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy8, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy8, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe7).place(x="137", y="380")

        Button(self.easy8, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee8).place(x="197", y="380")

        Button(self.easy8, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne9).place(x="260", y="380")

        Button(self.easy8, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee8():
        marks["E8"] = answer.get()
        if marks["E8"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E8"]) == 1 or int(marks["E8"]) == 2 or int(marks["E8"]) == 3 or int(marks["E8"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe7(self):
        self.easy8.withdraw()
        obj = Easy7()

    def callne9(self):
        self.easy8.withdraw()
        obj = Easy9()


class Easy9(Tk):
    def __init__(self):
        self.easy9 = Tk()
        self.easy9.title("Question Bank")
        self.easy9.geometry("450x500+535+125")

        Label(self.easy9, text="Easy Questions - ( 9/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy9, text="What is the data type of the Value ( 1 ) ?", font="Helvetica 12 bold", bg="light grey",
              fg="chocolate", bd="3").place(x="65", y="80")

        Label(self.easy9, text="1) List", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy9, text="2) Tuple", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy9, text="3) Integer", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy9, text="4) Both B and C", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy9, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy9, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy9, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe8).place(x="137", y="380")

        Button(self.easy9, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee9).place(x="197", y="380")

        Button(self.easy9, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne10).place(x="260", y="380")

        Button(self.easy9, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee9():
        marks["E9"] = answer.get()
        if marks["E9"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E9"]) == 1 or int(marks["E9"]) == 2 or int(marks["E9"]) == 3 or int(marks["E9"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe8(self):
        self.easy9.withdraw()
        obj = Easy8()

    def callne10(self):
        self.easy9.withdraw()
        obj = Easy10()


class Easy10(Tk):
    def __init__(self):
        self.easy10 = Tk()
        self.easy10.title("Question Bank")
        self.easy10.geometry("450x500+535+125")

        Label(self.easy10, text="Easy Questions - ( 10/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy10, text="Def factor ( n ) : , if ( n == 0 ): return 1 \n else return _______________",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="65", y="70")

        Label(self.easy10, text="1) n * factor ( n-1 )", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy10, text="2) n", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy10, text="3) n * ( n-1 )", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy10, text="4) None of these", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy10, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy10, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy10, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe9).place(x="165", y="380")

        Button(self.easy10, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee10).place(x="230", y="380")

        Button(self.easy10, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=caleasymarks).place(x="180", y="430")

    @staticmethod
    def savee10():
        marks["E10"] = answer.get()
        if marks["E10"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks["E10"]) == 1 or int(marks["E10"]) == 2 or int(marks["E10"]) == 3 or int(marks["E10"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe9(self):
        self.easy10.withdraw()
        obj = Easy9()


def caleasymarks():
    global count
    name = Name.get()
    reg = Reg.get()
    sec = Sec.get()
    if marks["E1"] == '3':
        count = count+1
    if marks["E2"] == '2':
        count = count+1
    if marks["E3"] == '1':
        count = count+1
    if marks["E4"] == '4':
        count = count+1
    if marks["E5"] == '3':
        count = count+1
    if marks["E6"] == '2':
        count = count+1
    if marks["E7"] == '4':
        count = count+1
    if marks["E8"] == '3':
        count = count+1
    if marks["E9"] == '3':
        count = count+1
    if marks["E10"] == '1':
        count = count+1
    messagebox.showinfo("Result...", "You got "+str(count)+" marks out of 10. ( "+str(count)+"/10 )")
    con = sqlite3.connect("Utkarsh_Jain.db")
    c = con.cursor()
    c.execute("insert into Marks values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, reg, sec, text, marks["E1"],
                                                                          marks["E2"], marks["E3"], marks["E4"],
                                                                          marks["E5"], marks["E6"], marks["E7"],
                                                                          marks["E8"], marks["E9"], marks["E10"],
                                                                          count))
    c.close()
    con.commit()


class Med1(Tk):
    def __init__(self):
        self.med1 = Tk()
        self.med1.title("Question Bank")
        self.med1.geometry("450x500+535+125")

        Label(self.med1, text="Medium Questions - ( 1/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.med1, text="Which function overloads the + operator ?", font="Helvetica 12 bold",
              bg="light grey", fg="chocolate", bd="3").place(x="50", y="80")

        Label(self.med1, text="1)  __add__()", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.med1, text="2)  __plus__()", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.med1, text="3)  __sum__()", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.med1, text="4)  None of these", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.med1, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.med1, bd="3")
        answer.place(x="190", y="325")

        Button(self.med1, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savem1).place(x="165", y="380")

        Button(self.med1, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callnm2).place(x="230", y="380")

        Button(self.med1, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savem1():
        marks1["M1"] = answer.get()
        if marks1["M1"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M1"]) == 1 or int(marks1["M1"]) == 2 or int(marks1["M1"]) == 3 or int(marks1["M1"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callnm2(self):
        self.med1.withdraw()
        obj = Med2()


class Med2(Tk):
    def __init__(self):
        self.med2 = Tk()
        self.med2.title("Question Bank")
        self.med2.geometry("450x500+535+125")

        Label(self.med2, text="Medium Questions - ( 2/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.med2, text="Which operator is overloaded by __invert__( ) ?", font="Helvetica 12 bold",
              bg="light grey", fg="chocolate", bd="3").place(x="40", y="80")

        Label(self.med2, text="1)   !", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.med2, text="2)   ~", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.med2, text="3)   ^", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.med2, text="4)   -", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.med2, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.med2, bd="3")
        answer.place(x="190", y="325")

        Button(self.med2, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpm1).place(x="137", y="380")

        Button(self.med2, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savem2).place(x="197", y="380")

        Button(self.med2, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callnm3).place(x="260", y="380")

        Button(self.med2, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savem2():
        marks1["M2"] = answer.get()
        if marks1["M2"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M2"]) == 1 or int(marks1["M2"]) == 2 or int(marks1["M2"]) == 3 or int(marks1["M2"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpm1(self):
        self.med2.withdraw()
        obj = Med1()

    def callnm3(self):
        self.med2.withdraw()
        obj = Med3()


class Med3(Tk):
    def __init__(self):
        self.med3 = Tk()
        self.med3.title("Question Bank")
        self.med3.geometry("450x500+535+125")

        Label(self.med3, text="Medium Questions - ( 3/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.med3, text="Which of the following is false about protected class \n member ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="20", y="70")

        Label(self.med3, text="1) They begin with _", font="Helvetica 12 bold").place(x="30", y="140")

        Label(self.med3, text="2) They can be accessed by subclasses", font="Helvetica 12 bold").place(x="30", y="180")

        Label(self.med3, text="3) They can be accessed by name mangling method", font="Helvetica 12 bold")\
            .place(x="30", y="220")

        Label(self.med3, text="4) They can be accessed within a class", font="Helvetica 12 bold").place(x="30", y="260")

        Label(self.med3, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.med3, bd="3")
        answer.place(x="190", y="325")

        Button(self.med3, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpm2).place(x="137", y="380")

        Button(self.med3, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savem3).place(x="197", y="380")

        Button(self.med3, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callnm4).place(x="260", y="380")

        Button(self.med3, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savem3():
        marks1["M3"] = answer.get()
        if marks1["M3"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M3"]) == 1 or int(marks1["M3"]) == 2 or int(marks1["M3"]) == 3 or int(marks1["M3"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpm2(self):
        self.med3.withdraw()
        obj = Med2()

    def callnm4(self):
        self.med3.withdraw()
        obj = Med4()


class Med4(Tk):
    def __init__(self):
        self.easy4 = Tk()
        self.easy4.title("Question Bank")
        self.easy4.geometry("450x500+535+125")

        Label(self.easy4, text="Medium Questions - ( 4/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy4, text="The readlines() method returns ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="70", y="80")

        Label(self.easy4, text="1) String", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy4, text="2) A List of lines", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy4, text="3) A next line from file pointer", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy4, text="4) A single text line", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy4, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy4, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy4, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe3).place(x="137", y="380")

        Button(self.easy4, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee4).place(x="197", y="380")

        Button(self.easy4, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne5).place(x="260", y="380")

        Button(self.easy4, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee4():
        marks1["M4"] = answer.get()
        if marks1["M4"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M4"]) == 1 or int(marks1["M4"]) == 2 or int(marks1["M4"]) == 3 or int(marks1["M4"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe3(self):
        self.easy4.withdraw()
        obj = Med3()

    def callne5(self):
        self.easy4.withdraw()
        obj = Med5()


class Med5(Tk):
    def __init__(self):
        self.easy5 = Tk()
        self.easy5.title("Question Bank")
        self.easy5.geometry("450x500+535+125")

        Label(self.easy5, text="Medium Questions - ( 5/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy5, text="What is the output of the following :- \n all ( [ 2,4,0,6 ] )",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="70", y="70")

        Label(self.easy5, text="1) Error", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy5, text="2) True", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy5, text="3) False", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy5, text="4) Zero", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy5, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy5, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy5, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe4).place(x="137", y="380")

        Button(self.easy5, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee5).place(x="197", y="380")

        Button(self.easy5, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne6).place(x="260", y="380")

        Button(self.easy5, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee5():
        marks1["M5"] = answer.get()
        if marks1["M5"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M5"]) == 1 or int(marks1["M5"]) == 2 or int(marks1["M5"]) == 3 or int(marks1["M5"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe4(self):
        self.easy5.withdraw()
        obj = Med4()

    def callne6(self):
        self.easy5.withdraw()
        obj = Med6()


class Med6(Tk):
    def __init__(self):
        self.easy6 = Tk()
        self.easy6.title("Question Bank")
        self.easy6.geometry("450x500+535+125")

        Label(self.easy6, text="Medium Questions - ( 6/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy6, text="Which function is used to check whether first \n string is present in another "
                               "string or not ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="50", y="70")

        Label(self.easy6, text="1) issubset()", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy6, text="2) issuperset()", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy6, text="3) ispresent()", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy6, text="4) isset()", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy6, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy6, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy6, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe5).place(x="137", y="380")

        Button(self.easy6, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee6).place(x="197", y="380")

        Button(self.easy6, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne7).place(x="260", y="380")

        Button(self.easy6, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee6():
        marks1["M6"] = answer.get()
        if marks1["M6"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M6"]) == 1 or int(marks1["M6"]) == 2 or int(marks1["M6"]) == 3 or int(marks1["M6"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe5(self):
        self.easy6.withdraw()
        obj = Med5()

    def callne7(self):
        self.easy6.withdraw()
        obj = Med7()


class Med7(Tk):
    def __init__(self):
        self.easy7 = Tk()
        self.easy7.title("Question Bank")
        self.easy7.geometry("450x500+535+125")

        Label(self.easy7, text="Medium Questions - ( 7/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy7, text="Which of the following is a feature of DocString ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="40", y="80")

        Label(self.easy7, text="1) Provided a way for Documentation", font="Helvetica 12 bold")\
            .place(x="30", y="140")

        Label(self.easy7, text="2) All function should have a DocString", font="Helvetica 12 bold")\
            .place(x="30", y="180")

        Label(self.easy7, text="3) DocStrings can be accessed by _doc_ attribute", font="Helvetica 12 bold")\
            .place(x="30", y="220")

        Label(self.easy7, text="4) All of the above mentioned", font="Helvetica 12 bold").place(x="30", y="260")

        Label(self.easy7, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy7, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy7, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe6).place(x="137", y="380")

        Button(self.easy7, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee7).place(x="197", y="380")

        Button(self.easy7, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne8).place(x="260", y="380")

        Button(self.easy7, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee7():
        marks1["M7"] = answer.get()
        if marks1["M7"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M7"]) == 1 or int(marks1["M7"]) == 2 or int(marks1["M7"]) == 3 or int(marks1["M7"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe6(self):
        self.easy7.withdraw()
        obj = Med6()

    def callne8(self):
        self.easy7.withdraw()
        obj = Med8()


class Med8(Tk):
    def __init__(self):
        self.easy8 = Tk()
        self.easy8.title("Question Bank")
        self.easy8.geometry("450x500+535+125")

        Label(self.easy8, text="Medium Questions - ( 8/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy8, text="Which of the following function help us to randomize \n items of a List ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="20", y="70")

        Label(self.easy8, text="1) seed", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy8, text="2) randomize", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy8, text="3) shuffle", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy8, text="4) uniform", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy8, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy8, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy8, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe7).place(x="137", y="380")

        Button(self.easy8, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee8).place(x="197", y="380")

        Button(self.easy8, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne9).place(x="260", y="380")

        Button(self.easy8, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee8():
        marks1["M8"] = answer.get()
        if marks1["M8"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M8"]) == 1 or int(marks1["M8"]) == 2 or int(marks1["M8"]) == 3 or int(marks1["M8"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe7(self):
        self.easy8.withdraw()
        obj = Med7()

    def callne9(self):
        self.easy8.withdraw()
        obj = Med9()


class Med9(Tk):
    def __init__(self):
        self.easy9 = Tk()
        self.easy9.title("Question Bank")
        self.easy9.geometry("450x500+535+125")

        Label(self.easy9, text="Medium Questions - ( 9/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy9, text="Which of the following have the highest precedence \n in the expression ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="25", y="70")

        Label(self.easy9, text="1) Exponential", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy9, text="2) Division", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy9, text="3) Modulus", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy9, text="4) Parenthesis", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy9, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy9, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy9, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe8).place(x="137", y="380")

        Button(self.easy9, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee9).place(x="197", y="380")

        Button(self.easy9, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne10).place(x="260", y="380")

        Button(self.easy9, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee9():
        marks1["M9"] = answer.get()
        if marks1["M9"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M9"]) == 1 or int(marks1["M9"]) == 2 or int(marks1["M9"]) == 3 or int(marks1["M9"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe8(self):
        self.easy9.withdraw()
        obj = Med8()

    def callne10(self):
        self.easy9.withdraw()
        obj = Med10()


class Med10(Tk):
    def __init__(self):
        self.easy10 = Tk()
        self.easy10.title("Question Bank")
        self.easy10.geometry("450x500+535+125")

        Label(self.easy10, text="Medium Questions - ( 10/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy10, text="In Tower of Hanoi, how many steps are needed for \n 4 disks ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="25", y="70")

        Label(self.easy10, text="1) 5", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy10, text="2) 10", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy10, text="3) 15", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy10, text="4) 20", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy10, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy10, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy10, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe9).place(x="165", y="380")

        Button(self.easy10, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee10).place(x="230", y="380")

        Button(self.easy10, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calmedmarks).place(x="180", y="430")

    @staticmethod
    def savee10():
        marks1["M10"] = answer.get()
        if marks1["M10"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks1["M10"]) == 1 or int(marks1["M10"]) == 2 or int(marks1["M10"]) == 3 or int(marks1["M10"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe9(self):
        self.easy10.withdraw()
        obj = Med9()


def calmedmarks():
    global count
    name = Name.get()
    reg = Reg.get()
    sec = Sec.get()
    if marks1["M1"] == '1':
        count = count+1
    if marks1["M2"] == '2':
        count = count+1
    if marks1["M3"] == '3':
        count = count+1
    if marks1["M4"] == '2':
        count = count+1
    if marks1["M5"] == '3':
        count = count+1
    if marks1["M6"] == '2':
        count = count+1
    if marks1["M7"] == '4':
        count = count+1
    if marks1["M8"] == '3':
        count = count+1
    if marks1["M9"] == '4':
        count = count+1
    if marks1["M10"] == '3':
        count = count+1
    messagebox.showinfo("Result...", "You got "+str(count)+" marks out of 10. ( "+str(count)+"/10 )")
    con = sqlite3.connect("Utkarsh_Jain.db")
    c = con.cursor()
    c.execute("insert into Marks values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, reg, sec, text, marks1["M1"],
                                                                          marks1["M2"], marks1["M3"], marks1["M4"],
                                                                          marks1["M5"], marks1["M6"], marks1["M7"],
                                                                          marks1["M8"], marks1["M9"], marks1["M10"],
                                                                          count))
    c.close()
    con.commit()


class Hard1(Tk):
    def __init__(self):
        self.easy1 = Tk()
        self.easy1.title("Question Bank")
        self.easy1.geometry("450x500+535+125")

        Label(self.easy1, text="Hard Questions - ( 1/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy1, text="Which of the following is Invalid ?", font="Helvetica 12 bold",
              bg="light grey", fg="chocolate", bd="3").place(x="60", y="80")

        Label(self.easy1, text="1)  _str = 1", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy1, text="2)  __str = 1", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy1, text="3)  __str__ = 1", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy1, text="4)  None", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy1, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy1, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy1, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee1).place(x="165", y="380")

        Button(self.easy1, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne2).place(x="230", y="380")

        Button(self.easy1, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee1():
        marks2["H1"] = answer.get()
        if marks2["H1"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H1"]) == 1 or int(marks2["H1"]) == 2 or int(marks2["H1"]) == 3 or int(marks2["H1"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callne2(self):
        self.easy1.withdraw()
        obj = Hard2()


class Hard2(Tk):
    def __init__(self):
        self.easy2 = Tk()
        self.easy2.title("Question Bank")
        self.easy2.geometry("450x500+535+125")

        Label(self.easy2, text="Hard Questions - ( 2/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy2, text="Which of the following is not a Keyword ?", font="Helvetica 12 bold", bg="light grey",
              fg="chocolate", bd="3").place(x="60", y="80")

        Label(self.easy2, text="1) eval", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy2, text="2) pass", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy2, text="3) assert", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy2, text="4) nonlocal", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy2, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy2, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy2, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe1).place(x="137", y="380")

        Button(self.easy2, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee2).place(x="197", y="380")

        Button(self.easy2, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne3).place(x="260", y="380")

        Button(self.easy2, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee2():
        marks2["H2"] = answer.get()
        if marks2["H2"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H2"]) == 1 or int(marks2["H2"]) == 2 or int(marks2["H2"]) == 3 or int(marks2["H2"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe1(self):
        self.easy2.withdraw()
        obj = Hard1()

    def callne3(self):
        self.easy2.withdraw()
        obj = Hard3()


class Hard3(Tk):
    def __init__(self):
        self.easy3 = Tk()
        self.easy3.title("Question Bank")
        self.easy3.geometry("450x500+535+125")

        Label(self.easy3, text="Hard Questions - ( 3/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy3, text="What is the output of the following Code : \n 'The {0} side {1} {2}'"
                               ".format('bright', 'of', 'life')", font="Helvetica 12 bold", bg="light grey",
              fg="chocolate", bd="3").place(x="50", y="70")

        Label(self.easy3, text="1) Error", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy3, text="2) 'The bright side of life'", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy3, text="3) 'The {bright} side {of} {life}'", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy3, text="4) No Output", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy3, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy3, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy3, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe2).place(x="137", y="380")

        Button(self.easy3, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee3).place(x="197", y="380")

        Button(self.easy3, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne4).place(x="260", y="380")

        Button(self.easy3, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee3():
        marks2["H3"] = answer.get()
        if marks2["H3"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H3"]) == 1 or int(marks2["H3"]) == 2 or int(marks2["H3"]) == 3 or int(marks2["H3"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe2(self):
        self.easy3.withdraw()
        obj = Hard2()

    def callne4(self):
        self.easy3.withdraw()
        obj = Hard4()


class Hard4(Tk):
    def __init__(self):
        self.easy4 = Tk()
        self.easy4.title("Question Bank")
        self.easy4.geometry("450x500+535+125")

        Label(self.easy4, text="Hard Questions - ( 4/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy4, text="An exception is",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="40", y="80")

        Label(self.easy4, text="1) A standard module", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy4, text="2) A special function", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy4, text="3) An object", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy4, text="4) A module", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy4, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy4, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy4, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe3).place(x="137", y="380")

        Button(self.easy4, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee4).place(x="197", y="380")

        Button(self.easy4, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne5).place(x="260", y="380")

        Button(self.easy4, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee4():
        marks2["H4"] = answer.get()
        if marks2["H4"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H4"]) == 1 or int(marks2["H4"]) == 2 or int(marks2["H4"]) == 3 or int(marks2["H4"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe3(self):
        self.easy4.withdraw()
        obj = Hard3()

    def callne5(self):
        self.easy4.withdraw()
        obj = Hard5()


class Hard5(Tk):
    def __init__(self):
        self.easy5 = Tk()
        self.easy5.title("Question Bank")
        self.easy5.geometry("450x500+535+125")

        Label(self.easy5, text="Hard Questions - ( 5/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy5, text="What is the output of the following : \n print('abcd'.translate({'a': '1', 'b': '2', "
                               "'c': '3', 'd': '4'}))", font="Helvetica 12 bold", bg="light grey", fg="chocolate",
              bd="3").place(x="30", y="70")

        Label(self.easy5, text="1) abcd", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy5, text="2) 1234", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy5, text="3) Error", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy5, text="4) None", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy5, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy5, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy5, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe4).place(x="137", y="380")

        Button(self.easy5, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee5).place(x="197", y="380")

        Button(self.easy5, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne6).place(x="260", y="380")

        Button(self.easy5, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee5():
        marks2["H5"] = answer.get()
        if marks2["H5"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H5"]) == 1 or int(marks2["H5"]) == 2 or int(marks2["H5"]) == 3 or int(marks2["H5"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe4(self):
        self.easy5.withdraw()
        obj = Hard4()

    def callne6(self):
        self.easy5.withdraw()
        obj = Hard6()


class Hard6(Tk):
    def __init__(self):
        self.easy6 = Tk()
        self.easy6.title("Question Bank")
        self.easy6.geometry("450x500+535+125")

        Label(self.easy6, text="Hard Questions - ( 6/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy6, text="What is the type of sys.argv ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="35", y="80")

        Label(self.easy6, text="1) Set", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy6, text="2) List", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy6, text="3) Tuple", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy6, text="4) String", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy6, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy6, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy6, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe5).place(x="137", y="380")

        Button(self.easy6, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee6).place(x="197", y="380")

        Button(self.easy6, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne7).place(x="260", y="380")

        Button(self.easy6, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee6():
        marks2["H6"] = answer.get()
        if marks2["H6"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H6"]) == 1 or int(marks2["H6"]) == 2 or int(marks2["H6"]) == 3 or int(marks2["H6"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe5(self):
        self.easy6.withdraw()
        obj = Hard5()

    def callne7(self):
        self.easy6.withdraw()
        obj = Hard7()


class Hard7(Tk):
    def __init__(self):
        self.easy7 = Tk()
        self.easy7.title("Question Bank")
        self.easy7.geometry("450x500+535+125")

        Label(self.easy7, text="Hard Questions - ( 7/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy7, text="How many keyword arguments can be passed to a \n function in a single call ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="30", y="70")

        Label(self.easy7, text="1) Zero", font="Helvetica 12 bold")\
            .place(x="40", y="140")

        Label(self.easy7, text="2) One", font="Helvetica 12 bold")\
            .place(x="40", y="180")

        Label(self.easy7, text="3) Zero or more", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy7, text="4) One or more", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy7, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy7, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy7, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe6).place(x="137", y="380")

        Button(self.easy7, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee7).place(x="197", y="380")

        Button(self.easy7, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne8).place(x="260", y="380")

        Button(self.easy7, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee7():
        marks2["H7"] = answer.get()
        if marks2["H7"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H7"]) == 1 or int(marks2["H7"]) == 2 or int(marks2["H7"]) == 3 or int(marks2["H7"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe6(self):
        self.easy7.withdraw()
        obj = Hard6()

    def callne8(self):
        self.easy7.withdraw()
        obj = Hard8()


class Hard8(Tk):
    def __init__(self):
        self.easy8 = Tk()
        self.easy8.title("Question Bank")
        self.easy8.geometry("450x500+535+125")

        Label(self.easy8, text="Hard Questions - ( 8/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy8, text="What is the output of \"hello\"+1+2+3 ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="30", y="80")

        Label(self.easy8, text="1) hello", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy8, text="2) hello123", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy8, text="3) hello6", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy8, text="4) Error", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy8, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy8, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy8, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe7).place(x="137", y="380")

        Button(self.easy8, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee8).place(x="197", y="380")

        Button(self.easy8, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne9).place(x="260", y="380")

        Button(self.easy8, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee8():
        marks2["H8"] = answer.get()
        if marks2["H8"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H8"]) == 1 or int(marks2["H8"]) == 2 or int(marks2["H8"]) == 3 or int(marks2["H8"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe7(self):
        self.easy8.withdraw()
        obj = Hard7()

    def callne9(self):
        self.easy8.withdraw()
        obj = Hard9()


class Hard9(Tk):
    def __init__(self):
        self.easy9 = Tk()
        self.easy9.title("Question Bank")
        self.easy9.geometry("450x500+535+125")

        Label(self.easy9, text="Hard Questions - ( 9/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy9, text="Suppose i = 5 and j = 4, then 1+j is same as ", font="Helvetica 12 bold",
              bg="light grey", fg="chocolate", bd="3").place(x="50", y="80")

        Label(self.easy9, text="1) __add( j )", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy9, text="2) __add__( j )", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy9, text="3) __Add( j )", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy9, text="4) __ADD__( j )", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy9, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy9, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy9, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe8).place(x="137", y="380")

        Button(self.easy9, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee9).place(x="197", y="380")

        Button(self.easy9, text="Next", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callne10).place(x="260", y="380")

        Button(self.easy9, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee9():
        marks2["H9"] = answer.get()
        if marks2["H9"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H9"]) == 1 or int(marks2["H9"]) == 2 or int(marks2["H9"]) == 3 or int(marks2["H9"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe8(self):
        self.easy9.withdraw()
        obj = Hard8()

    def callne10(self):
        self.easy9.withdraw()
        obj = Hard10()


class Hard10(Tk):
    def __init__(self):
        self.easy10 = Tk()
        self.easy10.title("Question Bank")
        self.easy10.geometry("450x500+535+125")

        Label(self.easy10, text="Hard Questions - ( 10/10 )", bg="black", fg="white", height="2", width="450",
              font="Helvetica 12 bold").pack()

        Label(self.easy10, text="What is the output of the code : \n A = [1, 2, 3, 4, 5], print ( A[3: :-1] ) ?",
              font="Helvetica 12 bold", bg="light grey", fg="chocolate", bd="3").place(x="65", y="70")

        Label(self.easy10, text="1) [2, 3, 4, 5]", font="Helvetica 12 bold").place(x="40", y="140")

        Label(self.easy10, text="2) [4, 3, 2, 1]", font="Helvetica 12 bold").place(x="40", y="180")

        Label(self.easy10, text="3) [1, 2, 3, 4]", font="Helvetica 12 bold").place(x="40", y="220")

        Label(self.easy10, text="4) [5, 4, 3, 2]", font="Helvetica 12 bold").place(x="40", y="260")

        Label(self.easy10, text="Answer - ", font="Helvetica 12 bold").place(x="110", y="325")
        global answer
        answer = ""
        answer = Entry(self.easy10, bd="3")
        answer.place(x="190", y="325")

        Button(self.easy10, text="Prev", bd="2", font="Helvetica 12 bold", bg="royal blue", fg="white",
               command=self.callpe9).place(x="165", y="380")

        Button(self.easy10, text="Save", bd="2", font="Helvetica 12 bold", bg="sea green", fg="white",
               command=self.savee10).place(x="230", y="380")

        Button(self.easy10, text="End Quiz", bd="2", font="Helvetica 12 bold", bg="black", fg="white",
               command=calhardmarks).place(x="180", y="430")

    @staticmethod
    def savee10():
        marks2["H10"] = answer.get()
        if marks2["H10"] == "":
            messagebox.showwarning("Warning...!!", "Answer field is Empty.")
        elif int(marks2["H10"]) == 1 or int(marks2["H10"]) == 2 or int(marks2["H10"]) == 3 or int(marks2["H10"]) == 4:
            messagebox.showinfo("Congrats...!!", "Answer Saved Successfully.")
        else:
            messagebox.showwarning("Warning...!!", "Answer must be in Options.")

    def callpe9(self):
        self.easy10.withdraw()
        obj = Hard9()


def calhardmarks():
    global count
    name = Name.get()
    reg = Reg.get()
    sec = Sec.get()
    if marks2["H1"] == '4':
        count = count+1
    if marks2["H2"] == '1':
        count = count+1
    if marks2["H3"] == '1':
        count = count+1
    if marks2["H4"] == '3':
        count = count+1
    if marks2["H5"] == '3':
        count = count+1
    if marks2["H6"] == '2':
        count = count+1
    if marks2["H7"] == '3':
        count = count+1
    if marks2["H8"] == '4':
        count = count+1
    if marks2["H9"] == '2':
        count = count+1
    if marks2["H10"] == '2':
        count = count+1
    messagebox.showinfo("Result...", "You got "+str(count)+" marks out of 10. ( "+str(count)+"/10 )")
    con = sqlite3.connect("Utkarsh_Jain.db")
    c = con.cursor()
    #c.execute("create table Marks(Name varchar(80), Reg_No varchar(80), Section varchar(80), Category varchar(80), Q1 int, Q2 int, Q3 int, Q4 int, Q5 int, Q6 int, Q7 int, Q8 int, Q9 int)")
    c.execute("insert into Marks values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, reg, sec, text, marks2["H1"],
                                                                          marks2["H2"], marks2["H3"], marks2["H4"],
                                                                          marks2["H5"], marks2["H6"], marks2["H7"],
                                                                          marks2["H8"], marks2["H9"], marks2["H10"],
                                                                          count))
    c.close()
    con.commit()


Home = tkinter.Tk()
Home.title("Quiz Game")
Home.geometry("450x500+535+125")

Top_label = Label(Home, text="Quiz", bg="black", fg="white", height="2", width="450", font="Helvetica 12 bold")
Top_label.pack()

label1 = Label(Home, text="Name : ", height="2", font="Helvetica 12 bold")
label1.place(x="160", y="80")
Name = Entry(Home, bd="3")
Name.place(x="235", y="88")

label2 = Label(Home, text="Registration No. : ", height="2", font="Helvetica 12 bold")
label2.place(x="80", y="130")
Reg = Entry(Home, bd="3")
Reg.place(x="235", y="138")

label3 = Label(Home, text="Section : ", height="2", font="Helvetica 12 bold")
label3.place(x="145", y="180")
Sec = Entry(Home, bd="3")
Sec.place(x="235", y="188")

Category = Label(Home, text="<-- Category -->", height="2", font="Helvetica 12 bold")
Category.place(x="160", y="230")

var = IntVar()

Check1 = Checkbutton(Home, text="Easy", font="Helvetica 12 bold", variable=var, onvalue=1, offvalue=0)
Check1.place(x="180", y="290")

Check2 = Checkbutton(Home, text="Medium", font="Helvetica 12 bold", variable=var, onvalue=2, offvalue=0)
Check2.place(x="180", y="320")

Check3 = Checkbutton(Home, text="Hard", font="Helvetica 12 bold", variable=var, onvalue=3, offvalue=0)
Check3.place(x="180", y="350")

Button0 = Button(Home, text="SUBMIT", bd="3", font="Helvetica 12 bold", bg="black", fg="white", command=check)
Button0.place(x="180", y="410")

Req = Label(Home, text="All fields are Compulsary....!!", font="Helvetica 11 bold", fg="red")
Req.place(x="120", y="460")

Home.mainloop()
