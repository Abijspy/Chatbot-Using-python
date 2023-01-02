from future.moves import tkinter
import tkinter as tk
from tkinter import ttk,messagebox

window = tk.Tk()

window.title("Covid-19 ChatBot")
window.minsize(600,400)

label1 = ttk.Label(window, text = "This is Static GUI part of chatbot.\nThis is Covid health tips provider.\n            Enter Your Name:", font = "Times 15").grid(column = 0, row = 0)
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 30, textvariable = name).grid(column = 0, row = 1)

label2 = ttk.Label(window, text = " Enter Your Age:", font = "Times 15").grid(column = 0, row = 2)
age = tk.Variable()
ageEntered = ttk.Entry(window, width = 20, textvariable = age).grid(column = 0, row = 3)

label3 = ttk.Label(window, text = "Select your symptom and click ", font = "Times 15").grid(column = 0, row = 5)

cmb = ttk.Combobox(window, width="25", values=("1)Dry Cough","2)Fever","3)Tiredness", "4)Soar thoart", "5)Difficulty in Breathing" , "6)Chest Pain or Pressure" , "7)Loss of speech or movement"))
#cmb = Combobox

class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = tk.StringVar() # create variable for table
        ttk.Combobox.__init__(self, parent)#  init widget
        self.config(textvariable = self.current_table, state = "readonly",)
        self.current(0) # index of values for current table
        self.place(x = 30, y = 50, anchor = "w") # place drop down box

def checkcmbo():

    if cmb.get() == "1)Dry Cough":
        messagebox.showinfo("icine may also help.Vitamin -B Complex Tablets,Vitamin-C Chewing Tablets(TUSQ).\nIf you are facing more than 2 symptoms,consult your Doctor & Get tested for COVID-19.")

    elif cmb.get() == "2)Fever":
        messagebox.showinfo("Health Tips", "\nGive yourself a sponge bath with lukewarm water.Medications such as paracetamol and ibuprofen may help to ease discomfort.\nIf you are facing more than 2 symptoms,consult your Doctor & Get tested for COVID-19.")

    elif cmb.get() == "3)Tiredness":
        messagebox.showinfo("Health Tips", "Eat a balanced diet.\nGet regular exercise.\nDrink more water.\nTry to sleep on time.Try to take fresh fruit juices.\nIf you are facing more than 2 symptoms,consult your Doctor & Get tested for COVID-19.")

    elif cmb.get() == "4)Soar thoart":
        messagebox.showinfo("Health Tips", "Gargling with warm salt water can help soothe a sore throat.\nYou can also drink turmeric milk before going to bed.\nIf you are facing more than 2 symptoms,consult your Doctor & Get tested for COVID-19.")

    elif cmb.get() == "5)Difficulty in Breathing" :
        messagebox.showwarning("Emergency","\nSeek immediate medical attention.\nCall 108")

    elif cmb.get() == "6)Chest Pain or Pressure" :
        messagebox.showwarning("Emergency","\nSeek immediate medical attention.\nCall 108")

    elif cmb.get() == "7)Loss of speech or movement" :
        messagebox.showwarning("Emergency","\nSeek immediate medical attention.\nCall 108")

    elif cmb.get() == "":
        messagebox.showinfo("Important Message", "Please select your symptoms")




cmb.place(relx="0.1",rely="0.4")

btn = ttk.Button(window, text="Click Here",command=checkcmbo)
btn.place(relx="0.4",rely="0.4")



window.mainloop()




