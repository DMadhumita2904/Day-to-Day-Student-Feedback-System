from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
from mysql.connector import connect
from tabulate import tabulate


fonts = ('Courier New', 12, 'bold')
admin = 'SVECW@9504'
password = 'priya'
student = '29'
studpass = 'madhu'
root = Tk()
class Home:
    def __init__(self, root):
        self.root = root
        self.right =Frame(self.root, width = 599, height = 600)
        self.right.place(x = 0, y = 0 )
        self.admin_name = Label(self.right, text = 'FACULTY ID',width = 10, bg = 'steel blue', fg ='white', font = fonts)
        self.admin_name.place(x = 60, y = 200)
        self.admin_name_entry = Entry(self.right, width = 18,font = fonts)
        self.admin_name_entry.place(x = 200, y = 200)

        self.admin_pass = Label(self.right, text = 'PASSWORD', width = 10,bg = 'steel blue', fg ='white', font = fonts)
        self.admin_pass.place(x = 60, y = 250)
        self.admin_pass_entry = Entry(self.right, width = 18, font = fonts)
        self.admin_pass_entry.place(x = 200, y = 250)

        self.admin_login_btn = Button(self.right, text = 'LOGIN', font = fonts, command = self.admin_login)
        self.admin_login_btn.place(x = 175, y = 350)


        self.left =Frame(self.root, width = 599, height = 600,bg = 'pink')
        self.left.place(x = 600, y = 0 )
        self.student_name = Label(self.left, text = 'STUDENT ID', bg = 'steel blue', fg ='white', font = fonts,width = 10)
        self.student_name.place(x = 60, y = 200)
        self.student_name_entry = Entry(self.left, width = 18, font = fonts)
        self.student_name_entry.place(x = 200, y = 200)

        self.student_pass = Label(self.left, text = 'PASSWORD', bg = 'steel blue', fg ='white', font = fonts, width = 10)
        self.student_pass.place(x = 60, y = 250)
        self.student_pass_entry = Entry(self.left, width = 18, font = fonts)
        self.student_pass_entry.place(x = 200, y = 250)

        self.student_login_btn = Button(self.left, text = 'LOGIN', font = fonts, command = self.student_login)
        self.student_login_btn.place(x = 175, y = 350)
    
    def admin_login(self):
        global admin, password
        self.a_name = self.admin_name_entry.get()
        self.a_pass = self.admin_pass_entry.get()
        if self.a_name == admin:
            if self.a_pass == password:
                self.right.destroy()
                self.left.destroy()
                admin_obj = Admin(root)
                self.middle = Frame(self.root,width = 1200,height = 600, bg = 'red')
                self.middle.place(x = 0,y=0)
                self.faculty_btn = Button(self.middle, text = 'VIEW FEEDBACK', font = fonts,command = self.faculty_feed,width = 20,height=5)
                self.faculty_btn.place(x = 500, y = 200)
            else:
                messagebox.showerror('INVALID','PASSWORD INCORRECT')
        else:
                messagebox.showerror('INVALID','ID INVALID')
    def faculty_feed(self):
        self.middle = Frame(self.root,width = 1200,height = 600, bg = 'violet')
        self.middle.place(x = 0,y=0)
        self.faculty_btn = Button(self.middle, text = 'AIML_A', font = fonts,width=15,height = 2,command = self.Stud_remark)
        self.faculty_btn.place(x = 500, y = 150)
        self.faculty_btn = Button(self.middle, text = 'AIML_B', font = fonts,width=15,height = 2,command = self.Stud_remark)
        self.faculty_btn.place(x = 500, y = 200)
        self.faculty_btn = Button(self.middle, text = 'AIDS_A', font = fonts,width=15,height = 2,command = self.Stud_remark)
        self.faculty_btn.place(x = 500, y = 250)
        self.faculty_btn = Button(self.middle, text = 'AIDS_B', font = fonts,width=15,height = 2,command = self.Stud_remark)
        self.faculty_btn.place(x = 500, y = 300)
        

    def student_login(self):
        global student, studpass
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()
        if self.b_name == student:
            if self.b_pass == studpass:
                self.right.destroy()
                self.left.destroy()
                student_obj = Student(root)
                self.middle = Frame(self.root,width = 1200,height = 600, bg = 'green')
                self.middle.place(x = 0,y=0)
                self.student_btn = Button(self.middle, text = 'PROVIDE FEEDBACK', font = fonts,width=20,height = 5,command = self.stud_feed)
                self.student_btn.place(x = 500, y = 200)

            else:
                messagebox.showerror('INVALID','PASSWORD INCORRECT')
        else:
            messagebox.showerror('INVALID','ID INVALID')        
    def stud_feed(self):
        self.middle.destroy()
        stud_obj = Stud(root)
        self.mid = Frame(self.root,width = 1200,height = 600, bg = 'violet')
        self.mid.place(x = 0,y=0)
        self.stud_btn = Button(self.mid, text = 'DBMS', font = fonts,width=15,height = 2,command = self.dbms_feed)
        self.stud_btn.place(x = 500, y = 150)   
        self.stud_btn = Button(self.mid, text = 'JAVA', font = fonts,width=15,height = 2,command = self.java_feed)
        self.stud_btn.place(x = 500, y = 200)
        self.stud_btn = Button(self.mid, text = 'FAI', font = fonts,width=15,height = 2,command = self.fai_feed)
        self.stud_btn.place(x = 500, y = 250) 
        self.stud_btn = Button(self.mid, text = 'DM', font = fonts,width=15,height = 2,command = self.dm_feed)
        self.stud_btn.place(x = 500, y = 300) 
        self.stud_btn = Button(self.mid, text = 'OS', font = fonts,width=15,height = 2,command = self.os_feed)
        self.stud_btn.place(x = 500, y = 350) 
    def dbms_feed(self):
        self.mi= Frame(self.root,width = 1200,height = 600, bg = 'brown')
        self.mi.place(x = 0,y=0)
    def java_feed(self):
        self.ja= Frame(self.root,width = 1200,height = 600, bg = 'orange')
        self.ja.place(x = 0,y=0)
    def fai_feed(self):
        self.fa= Frame(self.root,width = 1200,height = 600, bg = 'indigo')
        self.fa.place(x = 0,y=0)
    def dm_feed(self):
        self.fa= Frame(self.root,width = 1200,height = 600, bg = 'cyan')
        self.fa.place(x = 0,y=0)
    def os_feed(self):
        self.fa= Frame(self.root,width = 1200,height = 600, bg = 'dark sea green')
        self.fa.place(x = 0,y=0)
    def Stud_remark(self):
        conn = connect(
                    host = 'localhost',                    
                    user = 'root',
                    password = '1234',
       
                    database  = 'admin'
        )

        cur = conn.cursor()
        cur.execute('SELECT * from AIML')      
        data = cur.fetchall()
        headers = [column[0] for column in cur.description]
        table = tabulate(data, headers, tablefmt="fancy_grid")
        self.middle = Frame(self.root,width = 1200,height=600,bg = 'yellow')
        self.middle.place(x=0,y=0)
        self.s_feed = Label(self.middle,text = table)
        self.s_feed.place(x = 500,y = 200)
class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title('FACULTY PAGE')
        self.right = Frame(self.root, width = 500, height = 300, bg = 'red')
        self.right.place(x = 0, y = 0)
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title('STUDENT PAGE')
        self.right = Frame(self.root, width = 500, height = 300, bg = 'green')
        self.right.place(x = 0, y = 0)
class Stud:
    def __init__(self, root):
        self.root = root
        self.root.title('STUD PAGE')
        self.right = Frame(self.root, width = 500, height = 300, bg = 'grey')
        self.right.place(x = 0, y = 0)
root.geometry('1200x600+120+80')
root.title('MY-APP')
home = Home(root)
root.mainloop()


