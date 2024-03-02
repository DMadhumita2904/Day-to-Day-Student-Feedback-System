from tkinter import Tk, Frame, Label, Entry, Button, messagebox,PhotoImage,Toplevel,Text,ttk
from PIL import Image, ImageTk
from mysql.connector import connect
from tabulate import tabulate
import sqlite3


fonts = ('Times new Roman', 16, 'bold')

root = Tk()
root.resizable(0,0)
class Home:
    def __init__(self, root):
        self.root = root
        bg1= Image.open("C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/class3.jpg")
        self.background1 = ImageTk.PhotoImage(bg1)
        bg2 = Image.open("C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/class3.jpg")
        self.background2 = ImageTk.PhotoImage(bg2)

        
        

        self.right =Frame(self.root, width = 599, height = 600)
        self.right.place(x = 0, y = 0 )
        self.bg_label1 = Label(self.right, image=self.background1)
        self.bg_label1.place(x=0, y=0, relwidth=1, relheight=1)



        self.logo_image = Image.open('C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/tt.png')
        self.logo_image = self.logo_image.resize((150, 150))  # Adjust size as needed3

        # Convert the logo image to a format compatible with Tkinter
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create a Label widget to display the logo
        self.logo_label = Label(self.right, image=self.logo_photo)
        self.logo_label.place(x=225, y=60)
        
        

        
        self.admin_name = Label(self.right, text='FACULTY ID', width=10, fg='black', font=fonts)
        self.admin_name.place(x=70, y=250)


        self.admin_name_entry = Entry(self.right, width = 18,font = fonts)
        self.admin_name_entry.place(x = 220, y = 250)

        self.admin_pass = Label(self.right, text = 'PASSWORD', width = 10, fg ='black', font = fonts)
        self.admin_pass.place(x = 70, y = 300)
        self.admin_pass_entry = Entry(self.right, width = 18, font = fonts)
        self.admin_pass_entry.place(x = 220, y = 300)

        self.admin_login_btn = Button(self.right, text = 'LOGIN', fg = 'white',bg='green',font = fonts, command = self.admin_login)
        self.admin_login_btn.place(x = 185, y = 370)


        self.left =Frame(self.root, width = 599, height = 600)
        self.left.place(x = 600, y = 0 )
        self.bg_label2 = Label(self.left, image=self.background2)
        self.bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

        self.logo_im = Image.open('C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/stud.png')
        self.logo_im = self.logo_im.resize((150, 150))  # Adjust size as needed

        # Convert the logo image to a format compatible with Tkinter
        self.logo_pho = ImageTk.PhotoImage(self.logo_im)

        # Create a Label widget to display the logo
        self.logo_lab = Label(self.left, image=self.logo_pho)
        self.logo_lab.place(x=225, y=60)

        self.student_name = Label(self.left, text = 'STUDENT ID', fg ='Black', font = fonts,width = 10)
        self.student_name.place(x = 70, y = 250)

        self.student_name_entry = Entry(self.left, width = 18, font = fonts)
        self.student_name_entry.place(x = 220, y = 250)

        self.student_pass = Label(self.left, text = 'PASSWORD', fg ='black', font = fonts, width = 10)
        self.student_pass.place(x = 70, y = 300)
        self.student_pass_entry = Entry(self.left, width = 18, font = fonts)
        self.student_pass_entry.place(x = 220, y = 300)

        self.student_login_btn = Button(self.left, text='LOGIN', fg='white', bg='green', font=fonts, command=self.student_login)
        self.student_login_btn.place(x=185, y=370)

    
    def admin_login(self):
        global admin
        self.a_name = self.admin_name_entry.get()
        self.a_pass = self.admin_pass_entry.get()
        # Connect to the SQLite database
        conn = sqlite3.connect('C:/Users/Naga Sai/OneDrive/Desktop/Project/feed6.db')
        c = conn.cursor()
        # Query the faculty table to check admin credentials
        c.execute("SELECT * FROM faculty WHERE faculty_id = ? AND password = ?", (self.a_name, self.a_pass))
        result = c.fetchone()
        if result:  # If the result is not None, credentials are valid
            self.right.destroy()
            self.left.destroy()
            admin_obj = Admin(root)
            self.middle = Frame(self.root, width=1200, height=600)
            self.middle.place(x=0, y=0)
            bg_imag = Image.open('C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/bg2.png')
            # Optionally, resize the background image to fit the frame
            bg_imag = bg_imag.resize((1200, 600))
                # Convert the background image to a format compatible with Tkinter
            self.bg_phot = ImageTk.PhotoImage(bg_imag)
                # Create a Label widget to display the background image
            self.bg_label1 = Label(self.middle, image=self.bg_phot)
            self.bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
            self.faculty_btn = Button(self.middle, text='VIEW FEEDBACK', font=fonts, command=self.faculty_feed, width=20,height=5)
            self.faculty_btn.place(x=500, y=200)
        else:
            messagebox.showerror('INVALID', 'ID or PASSWORD INCORRECT')
    def faculty_feed(self):
        def display_feedback_aiml_a():
    # Retrieve feedback for the specified subject from the database
            conn = sqlite3.connect('C:/Users/Naga Sai/OneDrive/Desktop/Project/feed6.db')
            c = conn.cursor()
            c.execute("SELECT * FROM feedback WHERE subject = 'SE'")
            feedback_data = c.fetchall()

    # Create a new window to display the feedback in a TreeVie
            '''self.middle3 = Frame(self.root,width = 1200,height = 600)
            self.middle3.place(x = 0,y=0)'''
            self.middle = Toplevel(root)
            self.middle.title("Feedback for SE")
            self.middle.geometry("500x500")
            
            style = ttk.Style()
            style.configure("Treeview.Heading",font=("Times New Roman",20))
            style.configure("Treeview", font=("Times New Roman", 14))
    # Create a TreeView widget
            tree = ttk.Treeview(self.middle, columns=("Feedback"), show="headings")
            tree.heading("Feedback", text="Feedback")

    # Insert feedback data into the TreeView
            for feedback in feedback_data:
                tree.insert("", "end", values=(feedback[2],))

    # Add the TreeView to the window
            tree.pack(expand=True, fill="both")

    # Check if feedback exists for the subject
            if feedback_data:
        # If feedback exists, display the TreeView
                tree.pack(expand=True, fill="both")
            else:
        # If no feedback is available, display a message
                no_feedback_label = Label(self.middle, text="No feedback available for SE", font=fonts)
                no_feedback_label.pack()

    # Close the database connection
            ok_button = Button(self.middle, text="OK",command=self.ok_button_callback,width=10, height=2, bg="green", fg="white")
            ok_button.pack()
            conn.close()
        self.middle = Frame(self.root,width = 1200,height = 600)
        self.middle.place(x = 0,y=0)
        bg_image2 = Image.open('C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/bg2.png')
    # Optionally, resize the background image to fit the frame
        bg_image2 = bg_image2.resize((1200, 600))
    # Convert the background image to a format compatible with Tkinter
        self.bg_photo2 = ImageTk.PhotoImage(bg_image2)
    # Create a Label widget to display the background image
        self.bg_label2 = Label(self.middle, image=self.bg_photo2)
        self.bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

    # Create the AIML_A button
        aiml_a_btn = Button(self.middle, text='AIML_A', font=fonts, width=15, height=2,
                        command=display_feedback_aiml_a)
        aiml_a_btn.place(x=550, y=100)

    # Place other buttons as before
        self.faculty_btn = Button(self.middle, text='AIML_B', font=fonts, width=15, height=2)
        self.faculty_btn.place(x=550, y=200)
        self.faculty_btn = Button(self.middle, text='AIDS_A', font=fonts, width=15, height=2)
        self.faculty_btn.place(x=550, y=300)
        self.faculty_btn = Button(self.middle, text='AIDS_B', font=fonts, width=15, height=2)
        self.faculty_btn.place(x=550, y=400)

    def ok_button_callback(self):
    # This function is called when the "OK" button is clicked
    # Destroy the frame containing the feedback and the "OK" button
        self.middle.destroy()

    
        
        

    def student_login(self):
        global student, studpass
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()
        conn = sqlite3.connect('C:/Users/Naga Sai/OneDrive/Desktop/Project/feed6.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE student_id = ? AND password = ?", (self.b_name,self.b_pass))
        result = c.fetchone()
        if result:
            self.right.destroy()
            self.left.destroy()
            student_obj = Student(root)
            self.middle = Frame(self.root,width = 1200,height = 600)
            self.middle.place(x = 0,y=0)
            bg_image = Image.open('C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/bg2.png')
            # Optionally, resize the background image to fit the frame
            bg_image = bg_image.resize((1200, 600))
                # Convert the background image to a format compatible with Tkinter
            self.bg_photo = ImageTk.PhotoImage(bg_image)
                # Create a Label widget to display the background image
            self.bg_label = Label(self.middle, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.student_btn = Button(self.middle, text = 'PROVIDE FEEDBACK', font = fonts,width=20,height = 5,command = self.stud_feed)
            self.student_btn.place(x = 500, y = 200)
        else:
            messagebox.showerror('INVALID','ID or PASSWORD INCORRECT') 
        from tkinter import PhotoImage
    def stud_feed(self):
    # Destroy the current frame
        self.middle.destroy()
        student_obj1 = Student(root)
    
    # Create a new frame
        self.middle1 = Frame(self.root, width=1200, height=600)
        self.middle1.place(x=0, y=0)
        bg_image = Image.open("C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/sub.png")
        bg_image = bg_image.resize((1200, 600))  # Resize the image to match the frame size

    # Convert the image to PhotoImage format
        bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Create a label to display the background image
        bg_label = Label(self.middle1, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Ensure the image is retained by keeping a reference
        bg_label.image = bg_photo
    
    # Retrieve subjects from the database based on student ID
        conn = sqlite3.connect('C:/Users/Naga Sai/OneDrive/Desktop/Project/feed6.db')
        c = conn.cursor()
        c.execute("SELECT subjects FROM student_subjects WHERE student_id = ?", (self.b_name,))
        subjects_row = c.fetchone()
        if subjects_row:
            subjects = subjects_row[0].split(', ')
        # Create buttons for each subject
            for i, subject in enumerate(subjects):
            # Calculate the x and y coordinates for placing the buttons
                x_coord = 200 + (i % 3) * 300  # Adjust the spacing by changing the values
                y_coord = 200 + (i // 3) * 100  # Adjust the spacing by changing the values
                button = Button(self.middle1, text=subject, font=fonts, width=15, height=2)
                button.place(x=x_coord, y=y_coord)
            # Bind each button to a function that handles the feedback for that subject
                button.bind("<Button-1>", lambda event, subject=subject: self.handle_feedback(event, subject))
                
    def handle_feedback(self, event, subject):
        self.middle1.destroy()
        student_obj2 = Student(root)
        self.middle2 = Frame(self.root, width=1200,height=600)
        self.middle2.place(x=0,y=0)

    # Set background image for the window
        bg_image = Image.open("C:/Users/Naga Sai/OneDrive/Desktop/Project/assests/p1.png")
        bg_image = bg_image.resize((1200, 600))  # Resize image to fit the window
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo
        
        feedback_entry = Text(self.root, wrap="word", width=25, height=8,font=("Times New Roman", 20))  # Smaller textbox size
        feedback_entry.place(x=400, y=100)  # Adjust placement as needed

    # Function to submit feedback
        def submit_feedback_to_db():
            feedback = feedback_entry.get("1.0", "end-1c")  # Retrieve feedback from the text box
            if feedback:
                submit_feedback(subject, feedback)
                messagebox.showinfo("Success", "Feedback submitted successfully!")
                self.middle2.destroy()
            else:
                messagebox.showerror("Error", "Please enter feedback before submitting!")

    # Create a submit button with green color
        submit_button = Button(self.root, text="Submit Feedback",bg="green", fg="white", command=submit_feedback_to_db,font=("Helvetica", 16))
        submit_button.place(x=480, y=400)  # Adjust placement as needed

    # Keep a reference to the background image to prevent it from being garbage collected

# Existing code...
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
def submit_feedback(subject, feedback):
    conn = sqlite3.connect('C:/Users/Naga Sai/OneDrive/Desktop/Project/feed6.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (subject, feedback) VALUES (?, ?)", (subject, feedback))
    conn.commit()
    conn.close()
'''if _name_ == "_main_":
    root = Tk()
    root.resizable(False,False)
    app = MY-APP(root)
    root.mainloop()'''
root.geometry('1200x600+120+80')
root.title('MY-APP')
home = Home(root)
root.mainloop()


