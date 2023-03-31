from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np


class Face_Recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x720+500+180")
        self.root.title("Face Recognition")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        title_lbl = Label(self.root, text="FACE RECOGNIZATION",
                          font=("times new roman", 30, "bold"), bg="#341073", fg="#21b8fc")
        title_lbl.place(x=0, y=0, width=900, height=45)

        img_top = Image.open(r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\FR.jpg")
        img_top = img_top.resize((900, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=900, height=700)

        b1_5 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog,
                      font=("times new roman", 18, "bold"),
                      bg="#044273", fg="#21b8fc")
        b1_5.place(x=120, y=440, width=250, height=50)

        # ========================================ATTENDANCE=======================================

    def mark_attendance(self,r,n,d):
        with open("AttendanceReport/Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{dtString},{d1},Present")


    def face_recog(self):
        def draw_boudary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select name from student where ID=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select Roll_No from student where ID=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select Dep from student where ID=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)


                    if confidence > 77:
                        cv2.putText(img, f"Student ID:{r}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y - 45), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{d}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(r,n,d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    coord = [x, y, w, h]
                return coord

        def recogize(img, clf, faceCascade):
            coord = draw_boudary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recogize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog(root)
    root.mainloop()
