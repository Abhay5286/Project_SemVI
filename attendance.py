from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import csv
import cv2
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Atendance Window")
        self.root.iconbitmap("explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")

    #===================================VARIABLES===========================
        self.var_atten_id=StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_std_id = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        img = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\jr-korpa-9XngoIpxcEo-unsplash.jpg")
        img = img.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1920, height=250)

        img3 = Image.open(
            r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\jr-korpa-9XngoIpxcEo-unsplash.jpg")
        img3 = img3.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=250, width=1920, height=800)

        # TITLE
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 30, "bold"), bg="#341073", fg="white")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1870, height=730)

        # LEFT LABEL FRAME
        Left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=710)

        img_left = Image.open(r"C:\Users\abhay\OneDrive\Desktop\PROGRAMMING\Face Recognition\images\pexels-fox-1595391.jpg")
        img_left = img_left.resize((580, 1080), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=680, height=180)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=185, width=680, height=490)

        # LABEL AND ENTRY
        # ATTENDANCE ID
        #attendancID_lbl = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"),
                               # bg="white")
        #attendancID_lbl.grid(row=0, column=0, padx=10, pady=15, sticky=W)

        #attendancID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        #attendancID_entry.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        # NAME
        name_lbl = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"),
                         bg="white")
        name_lbl.grid(row=0, column=0, padx=10, pady=15, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 13, "bold"))
        name_entry.grid(row=0, column=1, pady=15)

        # Student ID
        roll_lbl = Label(left_inside_frame, text="Student ID:", font=("times new roman", 12, "bold"),
                         bg="white")
        roll_lbl.grid(row=0, column=2, padx=10, pady=15, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_std_id, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, pady=15)

        # Department
        dep_lbl = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"),
                        bg="white")
        dep_lbl.grid(row=1, column=0, padx=4, pady=15, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("times new roman", 13, "bold"))
        dep_entry.grid(row=1, column=1, pady=15)

        # Time
        name_lbl = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),
                         bg="white")
        name_lbl.grid(row=1, column=2, padx=10, pady=15, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=3, pady=15)

        # Date
        date_lbl = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"),
                         bg="white")
        date_lbl.grid(row=2, column=0, padx=4, pady=15, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 13, "bold"))
        date_entry.grid(row=2, column=1, pady=15)

        # Attendance Status
        attendancestatus_lbl = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"),
                                     bg="white")
        attendancestatus_lbl.grid(row=2, column=2, padx=10, pady=15, sticky=W)

        attendancestatus_combo = ttk.Combobox(left_inside_frame,
                                              font=("times new roman", 12, "bold"),textvariable=self.var_atten_attendance, state="readonly", width=20)
        attendancestatus_combo["values"] = ("Status", "Present", "Absent")
        attendancestatus_combo.current(0)
        attendancestatus_combo.grid(row=2, column=3, padx=10, pady=15, sticky=W)

        # BUTTON FRAME
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=115, y=350, width=400, height=70)

        # IMPORT BUTTON
        import_btn = Button(btn_frame, text="Import", command=self.importCSV, width=20,
                            font=("times new roman", 13, "bold"),
                            bg="#1857a4", fg="White")
        import_btn.grid(row=0, column=0)

        # UPDATE BUTTON
        update_btn = Button(btn_frame, text="Update", width=20,
                            font=("times new roman", 13, "bold"), bg="#1857a4", fg="White")
        update_btn.grid(row=1, column=0)

        # RESET BUTTON
        reset_btn = Button(btn_frame, text="Reset", width=20,command=self.reset_data,
                           font=("times new roman", 13, "bold"), bg="#1857a4",
                           fg="White")
        reset_btn.grid(row=1, column=1)

        # EXPORT BUTTON
        export_btn = Button(btn_frame, text="Export",command=self.exportCSV, width=20,
                            font=("times new roman", 13, "bold"), bg="#1857a4",
                            fg="White")
        export_btn.grid(row=0, column=1)

        right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=720, y=10, width=1135, height=710)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=1120, height=670)

        # SCROLL BAR TABLE
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=(
         "Name", "Student ID", "Department", "Time", "Date", "Attendance Status"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Student ID", text="Student ID")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance Status", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #============================================ FETCH DATA=======================================

    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # IMPORT CSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                           filetypes=(("CSV File", "*csv"), ("All FIle", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # EXPORT CSV
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                               filetypes=(("CSV File", "*csv"), ("All FIle", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data Exported to " + os.path.basename(fln) + " Succesfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_name.set(row[0])
        self.var_atten_std_id.set(row[1])
        self.var_atten_dep.set(row[2])
        self.var_atten_time.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_attendance.set(row[5])


    #RESET
    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_std_id.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
















if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
