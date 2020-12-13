from tkinter import *
from tkinter import ttk

root = Tk()
root.title("SGPA Calculator")
root.state('normal')
root.geometry("600x400+100+100")

TopTitle = ttk.Label(root, text='DIU SGPA Calculator',
                     font=("Helvetica", 25)).grid(columnspan=5)


# Asking for Total Number of Courses
askCourseNo = ttk.Label(root, text='Number of Course:').grid(columnspan=5)


# Input Box for Total Number of Course
courseNo = ttk.Entry(root)
courseNo.grid(columnspan=5)

# Button for generating required input boxes
start = ttk.Button(root, text='Start')
start.grid(columnspan=5)

# Array for storing CGPA & Credit
cgpaInput = []
creditInput = []


# Button for Calculate
Result = ttk.Button(root, text='See Result')


# Method for generating required input boxes


def createTextInput():
    no = int(courseNo.get())
    
    for i in range(no):
        ttk.Label(root, text='\nGPA for Course:').grid(columnspan=1)

        cgpaInput.append(ttk.Spinbox(root, from_=0, to=4))
        cgpaInput[i].grid(columnspan=5, column=0)
        row = cgpaInput[i].grid_info()['row'] + 1

        ttk.Label(root, text='\nCredit for Course:\n\n').grid()
        credit = IntVar()
        ttk.Radiobutton(root, text="1", value=1,
                        variable=credit).grid(row=row, column=1)
        ttk.Radiobutton(root, text="2", value=2,
                        variable=credit).grid(row=row, column=2)
        ttk.Radiobutton(root, text="3", value=3,
                        variable=credit).grid(row=row, column=3)
        creditInput.append(credit)

    Result.grid()


start.config(command=createTextInput)

def calculateCGPA():
    no = int(courseNo.get())


    cgpa = 0
    credit = 0

    for i in range(no):
        cgpa += float(cgpaInput[i].get()) * int(creditInput[i].get())
        credit += int(creditInput[i].get())

    output = round(cgpa / credit, 2)

    if (output == 0.00):
        resultType = "Fail"
    elif (output <= 2.00):
        resultType = "Pass"
    elif (output <= 2.25):
        resultType = "Below Average"
    elif (output <= 2.50):
        resultType = "Average"
    elif (output <= 2.75):
        resultType = "Above Average"
    elif (output <= 3.00):
        resultType = "Satisfactory"
    elif (output <= 3.25):
        resultType = "Good"
    elif (output <= 3.50):
        resultType = "Very Good"
    elif (output <= 3.75):
        resultType = "Excellent"
    elif (output <= 3.75):
        resultType = "Excellent"
    elif (output <= 4.00):
        resultType = "Outstanding"
    else:
        resultType = "Invalid"


    Comment = "Your SGPA is " + str(output) + " (" + resultType + ")"
    Output = ttk.Label(root, text="", font=("Helvetica", 30),)
    Output.config(text=Comment)
    Output.grid(columnspan=5)

Result.config(command=calculateCGPA)


root.mainloop()
