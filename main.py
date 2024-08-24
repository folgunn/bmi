from tkinter import *



def bmi_button():
    userInput= bmi_entry.get()
    userInput2= bmi_entry_2.get()
    bmi_result= float(userInput)/(float(userInput2)/100)**2
    if bmi_result <=18.5:
        result_label.config(text="Your bmi is : underwight")
    elif bmi_result <=24.9:
        result_label.config(text="Your bmi is : healty weight")
    elif bmi_result <=29.9:
        result_label.config(text="Your bmi is : overweight")
    elif bmi_result>= 30:
        result_label.config(text= "Your bmi is : obesity")

bmi_screen= Tk()
bmi_screen.title("welcome to bmi canculater")
bmi_screen.minsize(width=300, height=150)




bmi_label= Label(text="Enter your Weight(kg)")
bmi_label.pack()

bmi_entry= Entry()
bmi_entry.pack()

bmi_label_2= Label(text="Enter your height(cm)")
bmi_label_2.pack()

bmi_entry_2=Entry()
bmi_entry_2.pack()


my_button= Button(bmi_screen,text="calculate", command=bmi_button)
my_button.pack()



result_label=Label(bmi_screen,text="")
result_label.pack()





bmi_screen.mainloop()
