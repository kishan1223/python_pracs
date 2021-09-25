from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector

con = mysql.connector.connect(
host="localhost",
user="root",
password="",
database ="tk_projectdb"
)

cursor=con.cursor()

def submit():
    name = e_name.get();
    phone = e_phone.get();
    gender = e_gender.get();
    uid = e_uid.get();
    if(name=="" or phone=="" or gender=="" or uid==""):
           MessageBox.showinfo("Insert Status", "All Field Required")
    else:
           cursor.execute('INSERT INTO student (uname,phone,gender,uuid) VALUES(%s, %s, %s, %s)',(name,phone,gender,uid))
           cursor.execute("commit");
           MessageBox.showinfo("Submit Status", "Submitted Successfully");

def update():
    name = e_name.get();
    phone = e_phone.get();
    gender = e_gender.get();
    uid = e_uid.get();
    if(name=="" or phone=="" or gender=="" or uid==""):
           MessageBox.showinfo("Insert Status", "All Field Required")
    else:
           cursor.execute("SELECT * FROM student WHERE phone = '%s'" %(phone))
           catch1 = cursor.fetchone()
           print(catch1)
           if catch1 == None:
                  MessageBox.showerror("error","some error encountered")
           else:
                  cursor.execute("UPDATE student set uname = '%s',phone = '%s',gender = '%s',uuid = '%s'WHERE phone = '%s'" %(name,phone,gender,uid,phone))
                  cursor.execute("commit");
                  MessageBox.showinfo("Submit Status", "Record Updated Successfully");

def delete():
       phone = e_phone.get();
       cursor.execute("SELECT * FROM student WHERE phone = '%s'" %(phone))
       catch2 = cursor.fetchone()
       print(catch2)
       if catch2 == None:
              MessageBox.showerror("error","some error encountered")
       else:
              cursor.execute("DELETE FROM student WHERE phone = '%s'" %phone)
              cursor.execute("commit");
              MessageBox.showinfo("Submit Status", "Data deleted Successfully");

root = Tk()
root.geometry("400x300");
root.title("Student Details");

name = Label(root, text='Enter Name',font=('bold',10))
name.place(x=20, y=30)                                      
e_name = Entry()
e_name.place(x=150, y=30)


phone = Label(root, text='Enter phone',font=('bold',10))
phone.place(x=20, y=60)
e_phone = Entry()
e_phone.place(x=150, y=60)


gender = Label(root, text='Enter Gender',font=('bold',10))
gender.place(x=20, y=90)
e_gender = Entry()
e_gender.place(x=150, y=90)


uid = Label(root, text='Enter Uid',font=('bold',10))
uid.place(x=20, y=120)
e_uid = Entry()
e_uid.place(x=150, y=120)

submit = Button(root, text="submit", font=("italic", 10),bg="green", command=submit)
submit.place(x=20, y= 170)

delete = Button(root, text="delete", font=("italic", 10),bg="red", command=delete)
delete.place(x=80, y= 170)

update = Button(root, text="update", font=("italic", 10),bg="blue", command=update)
update.place(x=130, y= 170)

root.mainloop() 


