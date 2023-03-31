from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Details")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

        # VARIABLES
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # TOP IMAGE
        img = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\jr-korpa-9XngoIpxcEo-unsplash.jpg")
        img = img.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1920, height=250)

        # BACKFROUND IMAGE
        img3 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\jr-korpa-9XngoIpxcEo-unsplash.jpg")
        img3 = img3.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=250, width=1920, height=1080)

        # TITLE
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="#341073", fg="white")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1870, height=730)

        # LEFT LABEL FRAME
        Left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=900, height=700)

        img_left = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-fox-1595391.jpg")
        img_left = img_left.resize((880, 1080), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=880, height=180)

        # CURRENT COURSE INFO
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=190, width=880, height=130)

        # DEPARTEMENT
        dep_lbl = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "BBI", "Bsc IT", "BCom")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # CURRENT COURSE
        course_lbl = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FY", "SY", "TY")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # YEAR
        year_lbl = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_lbl.grid(row=0, column=4, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=0, column=5, padx=2, pady=10, sticky=W)

        # SEMESTER
        course_lbl = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        course_lbl.grid(row=1, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                    font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # CLASS STUDENT INFO
        class_studentinfo_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information",
                                             font=("times new roman", 12, "bold"))
        class_studentinfo_frame.place(x=5, y=320, width=880, height=350)

        # STUDENT NO
        studentID_lbl = Label(class_studentinfo_frame, text="Student No", font=("times new roman", 12, "bold"),
                              bg="white")
        studentID_lbl.grid(row=1, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_std_id, width=20,
                                    font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=1, column=1, padx=10, sticky=W)

        # STUDENT NAME
        studename_lbl = Label(class_studentinfo_frame, text="Student Name", font=("times new roman", 12, "bold"),
                              bg="white")
        studename_lbl.grid(row=1, column=2, padx=50, sticky=W)

        studentname_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_std_name, width=20,
                                      font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=1, column=3, padx=10, sticky=W)

        # CLASS DIVISION
        classdevision_lbl = Label(class_studentinfo_frame, text="Class Division", font=("times new roman", 12, "bold"),
                                  bg="white")
        classdevision_lbl.grid(row=2, column=0, padx=10, pady=20, sticky=W)

        classdevision_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_div, width=20,
                                        font=("times new roman", 12, "bold"))
        classdevision_entry.grid(row=2, column=1, padx=10, pady=20, sticky=W)

        # Student ID
        std_id_lbl = Label(class_studentinfo_frame, text="Student ID", font=("times new roman", 12, "bold"),
                           bg="white")
        std_id_lbl.grid(row=2, column=2, padx=50, pady=20, sticky=W)

        std_id_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_roll, width=20,
                                 font=("times new roman", 12, "bold"))
        std_id_entry.grid(row=2, column=3, padx=10, pady=20, sticky=W)

        # GENDER
        gender_lbl = Label(class_studentinfo_frame, text="Gender", font=("times new roman", 12, "bold"),
                           bg="white")
        gender_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        # gender_entry = ttk.Entry(class_studentinfo_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        # gender_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_studentinfo_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_lbl = Label(class_studentinfo_frame, text="DOB", font=("times new roman", 12, "bold"),
                        bg="white")
        dob_lbl.grid(row=3, column=2, padx=50, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # EMAIL
        email_lbl = Label(class_studentinfo_frame, text="Email", font=("times new roman", 12, "bold"),
                          bg="white")
        email_lbl.grid(row=4, column=0, padx=10, pady=20, sticky=W)

        email_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=4, column=1, padx=10, pady=20, sticky=W)

        # PHONE NO
        classdevision_lbl = Label(class_studentinfo_frame, text="Phone No", font=("times new roman", 12, "bold"),
                                  bg="white")
        classdevision_lbl.grid(row=4, column=2, padx=50, pady=20, sticky=W)

        classdevision_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_phone, width=20,
                                        font=("times new roman", 12, "bold"))
        classdevision_entry.grid(row=4, column=3, padx=10, pady=20, sticky=W)

        # ADDRESS
        classdevision_lbl = Label(class_studentinfo_frame, text="Address", font=("times new roman", 12, "bold"),
                                  bg="white")
        classdevision_lbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        classdevision_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_address, width=20,
                                        font=("times new roman", 12, "bold"))
        classdevision_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # TEACHER NAME
        classdevision_lbl = Label(class_studentinfo_frame, text="Teacher Name", font=("times new roman", 12, "bold"),
                                  bg="white")
        classdevision_lbl.grid(row=5, column=2, padx=50, pady=5, sticky=W)

        classdevision_entry = ttk.Entry(class_studentinfo_frame, textvariable=self.var_teacher, width=20,
                                        font=("times new roman", 12, "bold"))
        classdevision_entry.grid(row=5, column=3, padx=10, pady=5, sticky=W)

        # RADIO BUTTONS
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_studentinfo_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_studentinfo_frame, variable=self.var_radio1, text="No Photo Sample",
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # BUTTON FRAME
        btn_frame = Frame(class_studentinfo_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=15, y=250, width=830, height=35)

        # SAVE BUTTON
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=22, font=("times new roman", 12, "bold"),
                          bg="#341073", fg="White")
        save_btn.grid(row=0, column=0)

        # UPDATE BUTTON
        update_btn = Button(btn_frame, text="Upadte", command=self.update_data, width=22,
                            font=("times new roman", 12, "bold"), bg="#341073", fg="White")
        update_btn.grid(row=0, column=1)

        # RESET BUTTON
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22,
                           font=("times new roman", 12, "bold"), bg="#341073",
                           fg="White")
        reset_btn.grid(row=0, column=2)

        # DELETE BUTTON
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=22,
                            font=("times new roman", 12, "bold"), bg="#341073",
                            fg="White")
        delete_btn.grid(row=0, column=3)

        btn_frame = Frame(class_studentinfo_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=15, y=285, width=830, height=35)

        # TAKE PHOTO SAMPLE
        take_photo_btn = Button(btn_frame, command=self.gen_dataset, text="Take Photo Sample", width=92,
                                font=("times new roman", 12, "bold"),
                                bg="#341073",
                                fg="White")
        take_photo_btn.grid(row=1, column=0)
        # UPDATE PHOTO SAMPLE
        #update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=45, font=("times new roman", 12, "bold"),
         #                         bg="#341073",
          #                      fg="White")
        #update_photo_btn.grid(row=1, column=1)

        # RIGHT FRAME
        right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=930, y=10, width=925, height=700)

        img_right = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-fox-1595391.jpg")
        img_right = img_right.resize((880, 1080), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=900, height=180)

        # TABLE FRAME
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=190, width=900, height=480)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "Dep", "Course", "year", "Sem", "ID", "name", "Div", "Roll_No", "Gender", "DOB", "Email", "Teacher_Name",
            "Phone_no", "Address", "Photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Departement")
        self.student_table.heading("Course", text="Cours")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll_No", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Teacher_Name", text="Tacher Name")
        self.student_table.heading("Phone_no", text="Phone No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="PhotoSamepleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=150)
        self.student_table.column("Course", width=120)
        self.student_table.column("year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Roll_No", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Teacher_Name", width=100)
        self.student_table.column("Phone_no", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # FUNCTION DECLARATION
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # FETCH DATA
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    # GET CURSOR
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # UPDATE FUNCTION
    def update_data(self):
        global conn
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update Student Details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set `Dep`=%s, `Course`=%s, `year`=%s, `Sem`=%s,`name`=%s, `Div`=%s, `Roll_No`=%s, `Gender`=%s,`DOB`=%s, `Email`=%s, `Teacher_Name`=%s,`Phone_no`=%s, `Address`=%s, `Photo`=%s where `ID`=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # DELETE FUNCTION
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully delete student details", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # RESET
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ===================GENERATE DATA SET OR TAKE PHOTO SAMPLES====================================
    def gen_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set `Dep`=%s, `Course`=%s, `year`=%s, `Sem`=%s,`name`=%s, `Div`=%s, `Roll_No`=%s, `Gender`=%s,`DOB`=%s, `Email`=%s, `Teacher_Name`=%s,`Phone_no`=%s, `Address`=%s, `Photo`=%s where `ID`=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_teacher.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                # ===========LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV===================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Dataset Completed", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                print(es)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
