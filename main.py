from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)

mylabel=Label(text="Your height (m):  ", font=('Arial', 30, "normal"))
mylabel.pack()

heightentry= Entry()
heightentry.pack()

mylabel1= Label(text="Your weight (kg):  ", font=('Arial', 30, "normal"))
mylabel1.pack()

weightentry= Entry()
weightentry.pack()




def calculate():
    try:
        height= float(heightentry.get())
        weight= float(weightentry.get())
        bmi= weight/(height**2)
        if bmi < 18.5:
            label_sonuc.config(text="You are Underweight")
        elif 18.5 <= bmi <= 24.9:
            label_sonuc.config(text="You are Normal weight")
        else:
            label_sonuc.config(text="You are Overweight")
    except ValueError:
        label_sonuc.config(text="Invalid input!")



mybutton= Button(window, text="Calculate", command=calculate)
mybutton.pack()

label_sonuc = Label(window, text="The answer: ")
label_sonuc.pack()


window.mainloop()