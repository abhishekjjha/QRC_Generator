# import modules

from tkinter import *
import os
import qrcode
from PIL import Image, ImageTk
import pymsgbox as pymsg
from resizeimage import resizeimage


class Login:

    # Designing Main(first) window
    def __init__(self, root):
        self.root = root
        self.root.title("Account Login")
        self.root.geometry("1300x680+30+10")
        self.root.resizable(False, False)
        try:
            root.wm_iconbitmap('images/login.ico')
        except:
            pass

        self.bg = ImageTk.PhotoImage(file="images/Login_bg.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_btn_main = Button(self.root,text="Login", height="1", width="8", font=("times new roman", 17, "bold"),
                bg="black", fg="green", cursor="hand2", command=self.login).place(x=430, y=220)

        register_btn_main = Button(self.root,text="Register", height="1", width="8", font=("times new roman", 17, "bold"),
                fg="green", bg="black", cursor="hand2", command= self.register).place(x=430, y=270)


    # Designing window for registration
    def register(self):

        self.register_screen = self.root
        self.register_screen.title("Register")
        self.register_screen.bg = ImageTk.PhotoImage(file="images/Login_bg.jpg")
        self.register_screen.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.username = StringVar()
        self.password = StringVar()

        Label(self.register_screen, text="Please enter details below:",
              bg="black", fg="white").place(x=460, y=180)
        username_label = Label(self.register_screen, text="Username *", bg="black", fg="white")
        username_label.place(x=430, y=220)
        self.username_entry = Entry(self.register_screen, textvariable=self.username)
        self.username_entry.place(x=510, y=220)
        password_label = Label(self.register_screen, text="Password *", bg="black", fg="white")
        password_label.place(x=430, y=250)
        self.password_entry = Entry(self.register_screen, textvariable=self.password, show='*')
        self.password_entry.place(x=510, y=250)
        Button(self.register_screen, text="Register", width=6, height=1, bg="green", fg= "white",
               command=self.register_user, cursor="hand2", font=("times new roman", 11, "bold")).place(x=510, y=280)
        Button(self.register_screen, text="Cancel", width=5, height=1, cursor="hand2", bg="green", fg="white",
               font=("times new roman", 11, "bold"), command=self.cancel).place(x=585, y=280)

    # Implementing event on register button

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        if str(os.path.exists(self.username.get())) == 'True' :
            pymsg.alert("User already exists", "Error!", timeout=1000)
        else:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            pymsg.alert("Registration Success", "Info")



    # Designing window for login

    def login(self):

        login_screen = self.root
        login_screen.title("Login")
        login_screen.bg = ImageTk.PhotoImage(file="images/Login_bg.jpg")
        login_screen.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(login_screen, text="Please enter details below to login", bg="black", fg="white").place(x=490, y=180)
        Label(login_screen, text="Username * ", bg= "black", fg="white").place(x=460, y=210)
        self.username_login_entry = Entry(login_screen, textvariable=self.username_verify)
        self.username_login_entry.place(x=530, y=210)
        Label(login_screen, text="Password * ", bg= "black", fg="white").place(x=460, y=240)
        self.password_login_entry = Entry(login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.place(x=530, y=240)
        Button(login_screen, text="Login", width=5, height=1, cursor="hand2", bg= "green", fg="white",
                font=("times new roman", 11, "bold"), command= self.login_verify).place(x=530, y=270)
        Button(login_screen, text="Cancel", width=5, height=1, cursor="hand2", bg="green", fg="white",
               font=("times new roman", 11, "bold"), command=self.cancel).place(x=600, y=270)

    # Implementing events on login button

    def login_verify(self):

        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()

            else:
                pymsg.alert("Invalid Password", "Error!", timeout=1000)
        else:
            pymsg.alert("Invalid Username", "Error!", timeout=1000)

    # Defining Login cancel button

    def cancel(self):
        root= self.root
        Login.__init__(self, root)



    # Designing popup for login success

    def login_sucess(self):
        self.root.destroy()
        QR_Code_Gen(self)


class QR_Code_Gen:

    # GUI Design QR code generator
    def __init__(self, root):
        root = Tk()
        self.root = root
        root.title('QR Code Generator | Developed by Abhishek Jha')
        root.geometry("1240x600+30+30")
        root.resizable(False, False)

        try:
            root.wm_iconbitmap('images/qrc.ico')
        except:
            pass

        appName = Label(root, text='QR Code Generator', fg='white', bg="black",
                        font=('times new roman', 27, 'bold'))
        appName.pack(side=TOP, fill=BOTH)
        copyright_symbol = u"\u00A9"
        copyri8 = Label(root, text='App developed by: Abhishek Jha %s 2020-2021' % (copyright_symbol),
                        fg='red3', bg="black", font=('arial', 10, 'bold'))
        copyri8.pack(side=TOP, fill=BOTH)


        # Entry Window
        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        emp_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_frame.place(x=50, y=115, width=550, height=400)

        emp_title = Label(emp_frame, text="Employee Details", font=('goudy old style', 25),bg="black",
                          fg="White").place(x=0, y=0, relwidth=1)
        emp_id = Label(emp_frame, text="Emp. Id :", font=('impact', 10), bg="white" ).place(x=25, y=65)
        name = Label(emp_frame, text="Name :", font=('impact', 10), bg="white").place(x=25, y=100)
        department = Label(emp_frame, text="Department :", font=('impact', 10), bg="white").place(x=25, y=135)
        designation = Label(emp_frame, text="Designation :", font=('impact', 10), bg="white").place(x=25, y=170)

        emp_id_entry = Entry(emp_frame, fg='blue', bd=1, width=55, bg="#ced5e0",textvariable= self.var_emp_id).place(x=115, y=65)
        name_entry = Entry(emp_frame, fg='blue', bd=1, width=55, bg="#ced5e0", textvariable= self.var_name).place(x=115, y=100)
        department_entry = Entry(emp_frame, fg='blue', bd=1, width=55, bg="#ced5e0", textvariable= self.var_department).place(x=115, y=135)
        designation_entry = Entry(emp_frame, fg='blue', bd=1, width=55, bg="#ced5e0", textvariable= self.var_designation).place(x=115, y=170)

        getQRCode = Button(emp_frame, text='Generate QR Code', bg='green', fg='white', activebackground='blue',
                           width=25, activeforeground='yellow', command=self.QRCode).place(x=115, y=205)

        reset_btn = Button(emp_frame, text='Reset', bg='lightgrey', fg="red",
                          width=15, command=self.reset).place(x=335, y=205)
        self.msg= "QR Code generated sucessfully!!!"
        self.lbl_msg = Label(emp_frame, text=self.msg, font=('times new roman', 21),bg="white", fg='green')
        self.lbl_msg.place(x=1, y=245, relwidth=1)

        # QR Output
        qr_out = Label(self.root,bd=2, relief=RIDGE, bg="white")
        qr_out.place(x=630, y=115, width=550, height=400)
        emp_qr = Label(qr_out, text="Employee QR output", font=('goudy old style', 25), bg="black",
                          fg="White").place(x=0, y=0, relwidth=1)
        self.qr_code = Label(qr_out, text="No QR code\navilable now.", image='', font=("times new roman", 32, "bold"),
                        bg="#87ceeb", fg="black", bd=1, relief= RIDGE)
        self.qr_code.place(x=105, y=60, width=320, height=320)

    # QR Code generator
    def reset(self):
        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')


    def QRCode(self):
        if self.var_emp_id.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
            self.msg='All fields are mandatory!!!'
            self.lbl_msg.config(text=self.msg, fg='red')

        elif str(os.path.exists("Emp_QR/Emp_id_"+self.var_emp_id.get()+'.png')) == 'True':
            pymsg.alert("Employee ID already exists.", "Error!", timeout=1000)

        else:
            qr_data = (f"Emp. ID : {self.var_emp_id.get()}\n Name : {self.var_name.get()}\n Department : {self.var_department.get()}\n Designation : {self.var_designation.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [350, 350])
            qr_code.save("Emp_QR/Emp_id_"+self.var_emp_id.get()+'.png')

            #QR Output configuration

            self.im = ImageTk.PhotoImage(file="Emp_QR/Emp_id_"+self.var_emp_id.get()+'.png')
            self.qr_code.config(image=self.im)

            self.msg = 'QR Code generated sucessfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')






root = Tk()
obj= Login(root)
root.mainloop()
