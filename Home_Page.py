import random
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from Train import Train
from attendance import Attendance
from developer import Developer
from face_recog import Face_Recog
import os




class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recogniton System")
        self.root.wm_iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")


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

        b3 = Button(bg_img, image=self.photoimg6,command=self.Attendance_data, cursor=" hand2 ")
        b3.place(x=980, y=150, width=260, height=240)

        b1_3 = Button(bg_img, text="Attedance", cursor="hand2",command=self.Attendance_data, font=("times new roman", 20, "bold"),
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

        b5 = Button(bg_img, image=self.photoimg10, cursor=" hand2 ",command=self.Developer)
        b5.place(x=980, y=500, width=260, height=240)

        b1_5 = Button(bg_img, text="Developer", cursor="hand2",command=self.Developer, font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=980, y=740, width=260, height=40)

        # EXIT
        img11 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-kelly-3861798.jpg")
        img11 = img11.resize((260, 240), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b5 = Button(bg_img, image=self.photoimg11, cursor=" hand2 ",command=self.iExit)
        b5.place(x=1370, y=320, width=260, height=240)

        b1_5 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 20, "bold"),
                      bg="#be4d25", fg="black")
        b1_5.place(x=1370, y=560, width=260, height=40)

    # FUNCTION BUTTONS

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Exit the Application",parent=self.root)
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


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
