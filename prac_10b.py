import mysql.connector
from tkinter import *

running = True
root=Tk()
root.geometry('750x600')
root.title("Dictionaries")
root.configure(background='#FBF6EB')
#Entry widget object
textin=StringVar()
closecheck = StringVar()

con = mysql.connector.connect(
host="localhost",
user="root",
password="",
database ="tk_projectdb2"
)

cursor = con.cursor()

ent=Entry(root,width=20,font=('none 18 bold'),textvar=textin,bg='white')
ent.place(x=680,y=100,anchor=E)  

output=Text(root,width=40,height=8,font=('Time 20 bold'),fg="black")
output.place(x=105,y=220)

def clk():
    word = ent.get() 
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
    results = cursor.fetchall()
    
    def translate(w):
        w = w.lower()
        if w in results:
            return results[w]
        elif w.upper() in results:
            return results[w.upper()]
        elif w.title() in results:
            return results[w.title()]
        else:
            return ("The word doesnt exists, please double check it.")
    if results:
        for result in results:
            textin = result[1]
            output.insert(0.0,textin)
    else:
        put = translate(word)
        if output == list:
            for item in output:  
                textin = item
                output.insert(0.0,textin)
        else:
            textin = output
            output.insert(0.0,textin)
         
def clr():
     textin.set("")
     output.delete('1.0', END)

label1 = Label(root, text="Ḋi̇̇стi̇̇ỏɴẫяӯ",width=10,bg='#FBF6EB',font=("bold", 20))
label1.place(x=295,y=10)

label2 = Label(root, text="Enter word",width=10,bg='#FBF6EB',font=("bold", 20))
label2.place(x=300,y=100,anchor=E)

but1=Button(root,text='Submit',command=clk,width=10,bg='brown',fg='white',font=('bold'))
but1.place(x=360,y=160,anchor=E)

but2=Button(root,text='Clear',command=clr,width=10,bg='brown',fg='white',font=('bold'))
but2.place(x=520,y=160,anchor=E)

label3=Label(root,text='Results',bg='#FBF6EB',font=('non 18 bold'))
label3.place(x=10,y=185)

but3=Button(root,text='Exit',command=exit,width=10,bg='brown',fg='white',font=('bold'))
but3.place(x=320,y=510)

root.mainloop()
