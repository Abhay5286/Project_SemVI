from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720+400+180")
        self.root.title("Developer")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        title_lbl = Label(self.root, text="DEVELOPER",
                          font=("times new roman", 30, "bold"), bg="#0c162f", fg="#b8021c")
        title_lbl.place(x=0, y=0, width=1200, height=55)

        img_top = Image.open(r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\daniel-josef-AMssSjUaTY4-unsplash.jpg")
        img_top = img_top.resize((1200, 720 ), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1200, height=720)

        #FRAME
        main_frame = Frame(f_lbl, bd=2, bg="#0c162f")
        main_frame.place(x=750, y=15, width=400, height=350)

        img_top1 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\motivational-wallpaper-1920x1080.jpg")
        img_top1 = img_top1.resize((260, 180), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=5, y=20, width=180, height=180)


        #DEVELOPER INFO
        dev_label=Label(main_frame,text="Hello, My name is Abhay Maurya",font=("times new roman",18,"bold"),fg="#b8021c",bg="#0c162f")
        dev_label.place(x=0,y=250)











if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()