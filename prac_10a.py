import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="collage"
)
mycursor = mydb.cursor()

root = Tk()
root.geometry('750x600')
root.title("Registration Form")

f_name=StringVar()
address=StringVar()

def database():
      name1=f_name.get()
      addre=address.get()
      
      mycursor.execute('INSERT INTO customers (name,address) VALUES(%s, %s)',(name1,addre))
      messagebox.showinfo("success", "You have Registration Successfully")
      
      mydb.commit()

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=250,y=10)

label = Label(root, text="Name",width=15,anchor=W,font=("bold", 10))
label.place(x=80,y=80)
entry_0 = Entry(root,textvar=f_name,width=40)
entry_0.place(x=280,y=80,)

label_1 = Label(root, text="Address",width=15,anchor=W,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root,textvar=address,width=40)
entry_1.place(x=280,y=130)

def display():
      mycursor.execute("SELECT name,address FROM customers")
      catch = mycursor.fetchall()
      for item in catch:
            textin = item
            output.insert(END,textin)
            output.insert(END,"\n")
            messagebox.showinfo("success", "Data Successfully Fetched")
def clr():
     output.delete('1.0', END)
    
output=Text(root,width=40,height=8,font=('Time 20 bold'),fg="black")
output.place(x=75,y=220)


Button(root, text='Submit',width=15,bg='brown',fg='white',command=database).place(x=312,y=180)
Button(root, text='Display',width=10,bg='brown',fg='white',command=display).place(x=275,y=500)
Button(root,text='Clear',command=clr,width=10,bg='brown',fg='white').place(x=400,y=500)

root.mainloop()
