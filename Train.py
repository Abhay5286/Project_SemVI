from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x720+500+180")
        self.root.title("Train Data")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"), bg="#341073", fg="white")
        title_lbl.place(x=0, y=0, width=900, height=45)

        img_top = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\jr-korpa-9XngoIpxcEo-unsplash.jpg")
        img_top = img_top.resize((900, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=900, height=720)

        b1_5 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"),
                      bg="#341073", fg="WHITE")
        b1_5.place(x=320, y=350, width=300, height=50)

    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # =================TRAIN THE CLASSIFIER AND SAVE=========================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Traing Datasets Completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
