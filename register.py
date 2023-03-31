from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("R E G I S T E R")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        #====================VARIABLES===========================
        self.var_fname=StringVar()
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
        frame= Frame(self.root, bg='#040405', width=1200, height=800)
        frame.place(x=370, y=120)

        register_lbl=Label(frame,text="REGISTER HERE",font=('times new roman', 20, "bold"),bg="black",fg="white")
        register_lbl.place(x=500,y=20)

        #===================LABEL AND ENTRY==========================================================
        fname=Label(frame,text="First Name",font=('times new roman', 15, "bold"),bg="black",fg="white")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman', 15, "bold"))
        fname_entry.place(x=100,y=130,width=250)

        l_name = Label(frame, text="Last Name", font=('times new roman', 15, "bold"), bg="black", fg="white")
        l_name.place(x=820, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman', 15, "bold"))
        self.txt_lname.place(x=820, y=130, width=250)

        #--------------------row2
        contact = Label(frame, text="Contact", font=('times new roman', 15, "bold"), bg="black", fg="white")
        contact.place(x=100, y=200)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=('times new roman', 15, "bold"))
        self.txt_contact.place(x=100, y=230, width=230)

        email = Label(frame, text="E-Mail", font=('times new roman', 15, "bold"), bg="black", fg="white")
        email.place(x=820, y=200)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=('times new roman', 15, "bold"))
        self.txt_email.place(x=820, y=230, width=250)

        #---------------------row3
        select_Q = Label(frame, text="Selct Security Question", font=('times new roman', 15, "bold"), bg="black", fg="white")
        select_Q.place(x=100, y=300)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman', 15, "bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Birthdate","Your Favourite Car")
        self.combo_security_Q.place(x=100,y=330,width=250)
        self.combo_security_Q.current(0)


        security_answer = Label(frame, text="Security Answer", font=('times new roman', 15, "bold"), bg="black", fg="white")
        security_answer.place(x=820, y=300)

        self.txt_s_answer = ttk.Entry(frame,textvariable=self.var_securityA, font=('times new roman', 15, "bold"))
        self.txt_s_answer.place(x=820, y=330, width=250)


        #-------------------row4
        password = Label(frame, text="Password", font=('times new roman', 15, "bold"), bg="black", fg="white")
        password.place(x=100, y=400)

        self.txt_password = ttk.Entry(frame,textvariable=self.var_pass, font=('times new roman', 15, "bold"))
        self.txt_password.place(x=100, y=430, width=250)

        c_pass = Label(frame, text="Confirm Password", font=('times new roman', 15, "bold"), bg="black", fg="white")
        c_pass.place(x=820, y=400)

        self.txt_c_pass = ttk.Entry(frame,textvariable=self.var_cpass, font=('times new roman', 15, "bold"))
        self.txt_c_pass.place(x=820, y=430, width=250)


        #----------------------BUTTONS-------------------------------
        img=Image.open("images/18461-red-submit-button-design.png")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1_1 = Button(frame,command=self.register_data, text="SUBMIT", cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="#FF7B54", fg="black")
        b1_1.place(x=300, y=590, width=260, height=50)

        img = Image.open("images/18461-red-submit-button-design.png")
        img = img.resize((200, 100), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1_1 = Button(frame, text="Login Now", cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="#FF7B54", fg="black")
        b1_1.place(x=600, y=590, width=260, height=50)


        #============================Function Declaration=====================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are Required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password does not match!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","E-mail already exists")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
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
            messagebox.showinfo("Success","Registered Successfully")






if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()