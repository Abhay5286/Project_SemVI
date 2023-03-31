import os
import tkinter
import tkinter.messagebox
from tkinter import *

from tkinter import messagebox
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk

from Train import Train
from attendance import Attendance
from developer import Developer
from face_recog import Face_Recog
from student import Student


def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()


class LoginPage:
    def __init__(self, window):
        self.app = None
        self.window = window
        self.window.geometry('1920x1080')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title(' L O G I N     P A G E ')
        self.window.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\nature-wallpaper-g2760245c8_1920.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=1200, height=800)
        self.lgn_frame.place(x=370, y=120)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=680, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=715, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=650, y=300)

        self.username_entry = Entry(self.lgn_frame, textvariable=self.var_email, highlightthickness=0, relief=FLAT,
                                    bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=680, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=630, y=359)

        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=630, y=332)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=650, y=420)

        self.password_entry = Entry(self.lgn_frame, textvariable=self.var_pass, highlightthickness=0, relief=FLAT,
                                    bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=680, y=456, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=630, y=480)

        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=630, y=454)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=630, y=500)
        self.login = Button(self.lgn_button_label, text='LOGIN', command=self.login, font=("yu gothic ui", 13, "bold"),
                            width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, command=self.forgot_pass, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=710, y=570)

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=630, y=620)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, command=self.register_window, image=self.signup_img,
                                          bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=760, y=620, width=111, height=35)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=940, y=460)

    def destroy_main(self):
        self.root.destroy()

    def register_window(self):
        self.new_window = Toplevel(self.window)
        self.app = Register(self.new_window)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=940, y=460)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=940, y=460)
        self.password_entry.config(show='*')

    def login(self):
        # username = self.username_entry.get()
        # password = self.password_entry.get()
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and Pass=%s", (
                self.var_email.get(),
                self.var_pass.get()
            ))
            row = my_cursor.fetchone()
            open_main = True
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                    self.new_window = Toplevel(self.window)
                    self.app = Face_Recognition_System(self.new_window)
                    if not open_main:
                        return
            conn.commit()
            conn.close()




    def forgot_pass(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error", "Please enter the Email Address to reset the Password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Enter the valid E-Mail")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("440x590+710+180")

                l = Label(self.root2, text="Forgot Password", font=('times new roman', 20, "bold"), bg="black",
                          fg="white")
                l.place(x=0, y=10, relwidth=1)

                select_Q = Label(self.root2, text="Selct Security Question", font=('times new roman', 15, "bold"),
                                 bg="white", fg="black")
                select_Q.place(x=90, y=100)

                self.combo_security_Q = ttk.Combobox(self.root2, textvariable=self.var_securityQ,
                                                     font=('times new roman', 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Birthdate", "Your Favourite Car")
                self.combo_security_Q.place(x=90, y=140, width=250)
                self.combo_security_Q.current(0)

                security_answer = Label(self.root2, text="Security Answer", font=('times new roman', 15, "bold"),
                                        bg="white",
                                        fg="black")
                security_answer.place(x=90, y=200)

                self.txt_s_answer = ttk.Entry(self.root2, textvariable=self.var_securityA,
                                              font=('times new roman', 15, "bold"))
                self.txt_s_answer.place(x=90, y=240, width=250)

                password = Label(self.root2, text="New Password", font=('times new roman', 15, "bold"),
                                 bg="white",
                                 fg="black")
                password.place(x=90, y=300)

                self.txt_password = ttk.Entry(self.root2,
                                              font=('times new roman', 15, "bold"))
                self.txt_password.place(x=90, y=340, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=('times new roman', 15, "bold"),
                             fg="black", bg="#FC2947")
                btn.place(x=180, y=400)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question",parent=self.root2)
        elif self.txt_s_answer.get() == "":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_password.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            qury = ("select * from register where email=%s and SelectQ=%s and SelectA=%s")
            value = (self.var_email.get(), self.combo_security_Q.get(), self.txt_s_answer.get())
            my_cursor.execute(qury, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
            else:
                query = ("update register set Pass=%s where email=%s")
                value = (self.txt_password.get(), self.var_email.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your Password has been reset",parent=self.root2)
                self.root2.destroy()


# =======================================Home Page=========================================================

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recogniton System")
        self.root.wm_iconbitmap(
            "explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        # TOP IMAGE
        img = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\klim-musalimov-rDMacl1FDjw-unsplash.jpg")
        img = img.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1920, height=250)

        # BACKFROUND IMAGE
        img3 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\klim-musalimov-rDMacl1FDjw-unsplash.jpg")
        img3 = img3.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=250, width=1920, height=1080)

        # TITLE
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="BLACK", fg="#be4d25")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # STUDENT BUTTON
        img4 = Image.open(r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-fox-1595391.jpg")
        img4 = img4.resize((260, 240), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor=" hand2 ")
        b1.place(x=190, y=150, width=260, height=240)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="#be4d25", fg="black")
        b1_1.place(x=190, y=390, width=260, height=40)

        # DETECT FACE BUTTON
        img5 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-cottonbro-studio-8090263.jpg")
        img5 = img5.resize((260, 240), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor=" hand2 ", command=self.face_data)
        b2.place(x=590, y=150, width=260, height=240)

        b1_2 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,
                      font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_2.place(x=590, y=390, width=260, height=40)

        # ATTENDANCE FACE BUTTON
        img6 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-pavel-danilyuk-8423046.jpg")
        img6 = img6.resize((260, 240), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, command=self.Attendance_data, cursor=" hand2 ")
        b3.place(x=980, y=150, width=260, height=240)

        b1_3 = Button(bg_img, text="Attedance", cursor="hand2", command=self.Attendance_data,
                      font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_3.place(x=980, y=390, width=260, height=40)

        # TRAIN FACE BUTTON
        img8 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\train.jpg")
        img8 = img8.resize((260, 240), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor=" hand2 ", command=self.Train)
        b5.place(x=190, y=500, width=260, height=240)

        b1_5 = Button(bg_img, text="Train Face Data", cursor="hand2", command=self.Train,
                      font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=190, y=740, width=260, height=40)

        # PHOTOS
        img9 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-pixabay-265946.jpg")
        img9 = img9.resize((260, 240), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img, image=self.photoimg9, cursor=" hand2 ", command=self.opem_img)
        b5.place(x=590, y=500, width=260, height=240)

        b1_5 = Button(bg_img, text="Photos", cursor="hand2", command=self.opem_img,
                      font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=590, y=740, width=260, height=40)

        # DEVELOPER
        img10 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-lukas-574071.jpg")
        img10 = img10.resize((260, 240), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b5 = Button(bg_img, image=self.photoimg10, cursor=" hand2 ", command=self.Developer)
        b5.place(x=980, y=500, width=260, height=240)

        b1_5 = Button(bg_img, text="Developer", cursor="hand2", command=self.Developer,
                      font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=980, y=740, width=260, height=40)

        # EXIT
        img11 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-kelly-3861798.jpg")
        img11 = img11.resize((260, 240), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b5 = Button(bg_img, image=self.photoimg11, cursor=" hand2 ", command=self.iExit)
        b5.place(x=1370, y=320, width=260, height=240)

        b1_5 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=1370, y=560, width=260, height=40)

    # FUNCTION BUTTONS

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Exit the Application", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def Train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recog(self.new_window)

    def opem_img(self):
        os.startfile("Data")


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


#  ===================================REGISTER PAGE=======================================================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("R E G I S T E R")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        # ====================VARIABLES===========================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\nature-wallpaper-g2760245c8_1920.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ====== Login Frame =========================
        frame = Frame(self.root, bg='#040405', width=1200, height=800)
        frame.place(x=370, y=120)

        register_lbl = Label(frame, text="REGISTER HERE", font=('times new roman', 20, "bold"), bg="black", fg="white")
        register_lbl.place(x=500, y=20)

        # ===================LABEL AND ENTRY==========================================================
        fname = Label(frame, text="First Name", font=('times new roman', 15, "bold"), bg="black", fg="white")
        fname.place(x=100, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=('times new roman', 15, "bold"))
        fname_entry.place(x=100, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=('times new roman', 15, "bold"), bg="black", fg="white")
        l_name.place(x=820, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman', 15, "bold"))
        self.txt_lname.place(x=820, y=130, width=250)

        # --------------------row2
        contact = Label(frame, text="Contact", font=('times new roman', 15, "bold"), bg="black", fg="white")
        contact.place(x=100, y=200)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=('times new roman', 15, "bold"))
        self.txt_contact.place(x=100, y=230, width=230)

        email = Label(frame, text="E-Mail", font=('times new roman', 15, "bold"), bg="black", fg="white")
        email.place(x=820, y=200)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=('times new roman', 15, "bold"))
        self.txt_email.place(x=820, y=230, width=250)

        # ---------------------row3
        select_Q = Label(frame, text="Selct Security Question", font=('times new roman', 15, "bold"), bg="black",
                         fg="white")
        select_Q.place(x=100, y=300)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=('times new roman', 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Birthdate", "Your Favourite Car")
        self.combo_security_Q.place(x=100, y=330, width=250)
        self.combo_security_Q.current(0)

        security_answer = Label(frame, text="Security Answer", font=('times new roman', 15, "bold"), bg="black",
                                fg="white")
        security_answer.place(x=820, y=300)

        self.txt_s_answer = ttk.Entry(frame, textvariable=self.var_securityA, font=('times new roman', 15, "bold"))
        self.txt_s_answer.place(x=820, y=330, width=250)

        # -------------------row4
        password = Label(frame, text="Password", font=('times new roman', 15, "bold"), bg="black", fg="white")
        password.place(x=100, y=400)

        self.txt_password = ttk.Entry(frame, textvariable=self.var_pass, font=('times new roman', 15, "bold"))
        self.txt_password.place(x=100, y=430, width=250)

        c_pass = Label(frame, text="Confirm Password", font=('times new roman', 15, "bold"), bg="black", fg="white")
        c_pass.place(x=820, y=400)

        self.txt_c_pass = ttk.Entry(frame, textvariable=self.var_cpass, font=('times new roman', 15, "bold"))
        self.txt_c_pass.place(x=820, y=430, width=250)

        # ----------------------BUTTONS-------------------------------
        img = Image.open("images/18461-red-submit-button-design.png")
        img = img.resize((200, 100), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1_1 = Button(frame, command=self.register_data, text="SUBMIT", cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="#FF7B54", fg="black")
        b1_1.place(x=300, y=590, width=260, height=50)

        img = Image.open("images/18461-red-submit-button-design.png")
        img = img.resize((200, 100), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1_1 = Button(frame, command=self.return_login, text="Login Now", cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="#FF7B54", fg="black")
        b1_1.place(x=600, y=590, width=260, height=50)

        # ============================Function Declaration=====================================



    def login_window(self):
        self.new_window = Toplevel(self.root)
        self.app = LoginPage(self.new_window)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are Required")
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password does not match!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "E-mail already exists")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                    self.var_cpass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")
    def return_login(self):
        self.root.destroy()


if __name__ == '__main__':
    main()
