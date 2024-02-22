from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import csv
import cx_Oracle
# Create a database connection
conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
# Create a cursor object
cursor = conn.cursor()
class Student:
    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1450x790+0+0")
        # -*******les variables ****
        self.CNE_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.email_var = StringVar()
        self.tele_var = StringVar()
        self.dob_var = StringVar()
        self.filiere_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


        title = Label(self.root, text="Système de gestion des étudiants", bd=15,
                      font=("bahnschrift condensed", 35, "bold"), bg='rosy brown', fg='navy')

        title.pack(side=TOP, fill=X)
        # frame detail
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="rosy brown")
        Detail_Frame.place(x=500, y=90, width=920, height=650)
        # button detail frame
        lbl_search = Label(Detail_Frame, text="rechercher par", bg="rosy brown", fg="white",
                           font=("bahnschrift condensed", 16, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        # rechercher par icone
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by,width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ["CNE", "tele", "email"]
        combo_search.grid(row=0, column=1, padx=1, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt
                           ,width=18, font=("bahnschrift condensed", 12, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        # button detail frame
        search_btn = Button(Detail_Frame, text="rechercher", width=10, pady=4,
                            font=("bahnschrift condensed", 12, "bold"),command=self.search_data, fg='navy', bg='beige').grid(row=0, column=3,
                                                                                                    padx=10, pady=10)
        load_btn = Button(Detail_Frame, text="télécharger", width=10, pady=4,
                            font=("bahnschrift condensed", 12, "bold"),command=self.export_students_to_csv, fg='navy', bg='brown').grid(row=0, column=5,
                                                                                                    padx=10, pady=10)
        affish_btn = Button(Detail_Frame, text="afficher tout", width=10, pady=4,
                            font=("bahnschrift condensed", 12, "bold"), fg='navy', bg='coral', command=self.fetch_data)
        affish_btn.grid(row=0, column=4, padx=10, pady=10)

        affish_btn = Button(Detail_Frame, text="sing up ", width=10, pady=4,
                            font=("bahnschrift condensed", 12, "bold"), fg='navy', bg='gold',
                            command=self.sign_up).grid(row=0, column=6,
                                                          padx=10, pady=10)
        affish_btn = Button(Detail_Frame, text="list_login", width=10, pady=4,
                            font=("bahnschrift condensed", 12, "bold"), fg='navy', bg='red',
                            command=self.show_students).grid(row=0, column=7,
                                                       padx=10, pady=10)

        # === table frame ==
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="beige")
        Table_Frame.place(x=10, y=70, width=890, height=560)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame, columns=("CNE", "Prénom", "Nom", "email", "dob", "Télé","Filiére"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table .xview)
        scroll_y.config(command=self.student_table .yview)
        self.student_table .heading("CNE", text="CNE")
        self.student_table.heading("Prénom", text="Prénom")
        self.student_table.heading("Nom", text="Nom")
        self.student_table.heading("email", text="email", )
        self.student_table .heading("dob", text="dob")
        self.student_table .heading("Télé", text="Télé")
        self.student_table .heading("Filiére", text="Filiére")

        self.student_table ['show'] = 'headings'
        self.student_table .column("CNE", width=50)
        self.student_table .column("Nom", width=100)
        self.student_table.column("Prénom", width=100)
        self.student_table .column("email", width=180)
        self.student_table .column("Télé", width=110)
        self.student_table .column("dob", width=90)
        self.student_table .column("Filiére", width=150)

        self.student_table .pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        # Manage frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="rosy brown")
        Manage_Frame.place(x=10, y=95, width=470, height=620)
        # button frame manage
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="rosy brown")
        btn_Frame.place(x=10, y=520, width=450)

        adbtn = Button(btn_Frame, text="Ajouter", width=10, font=("bahnschrift condensed", 14, "bold"), fg='navy',
                       bg='blue', command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updbtn = Button(btn_Frame, text="mettre à jour", width=10, font=("bahnschrift condensed", 14, "bold"),
                        fg='navy', bg='turquoise', command=self.update_student).grid(row=0, column=1, padx=10, pady=10)
        dlbtn = Button(btn_Frame, text="supprimer", width=10, font=("bahnschrift condensed", 14, "bold"), fg='navy',
                       bg='coral', command=self.delete_student).grid(row=0, column=2, padx=10, pady=10)
        clrbtn = Button(btn_Frame, text="Clair", width=10, font=("bahnschrift condensed", 14, "bold"), fg='navy',
                        bg='red', command=self.clear_fields).grid(row=0, column=3, padx=10, pady=10)
        # title frame manage
        m_title = Label(Manage_Frame, text="gérer les étudiants", bg="rosy brown", fg="dark blue",
                        font=("bahnschrift condensed", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)
        # id_students
        lbl_roll = Label(Manage_Frame, text="CNE", bg="rosy brown", fg="white",
                         font=("bahnschrift condensed", 16, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_Roll = Entry(Manage_Frame, textvariable=self.CNE_var, font=("times new roman", 18, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=5, sticky="w")
        # first_name
        lbl_first_name = Label(Manage_Frame, text="prénom", bg="rosy brown", fg="white",
                               font=("bahnschrift condensed", 16, "bold"))
        lbl_first_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_first_name = Entry(Manage_Frame, textvariable=self.first_name_var, font=("times new roman", 18, "bold"),
                               bd=5, relief=GROOVE)
        txt_first_name.grid(row=2, column=1, pady=10, padx=5, sticky="w")
        # last_name
        lbl_last_name = Label(Manage_Frame, text="Nom", bg="rosy brown", fg="white",
                              font=("bahnschrift condensed", 16, "bold"))
        lbl_last_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_last_name = Entry(Manage_Frame, textvariable=self.last_name_var, font=("times new roman", 18, "bold"), bd=5,
                              relief=GROOVE)
        txt_last_name.grid(row=3, column=1, pady=10, padx=5, sticky="w")
        # email
        lbl_email = Label(Manage_Frame, text="Email", bg="rosy brown", fg="white",
                          font=("bahnschrift condensed", 16, "bold"))
        lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 18, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=5, sticky="w")
        # bd
        lbl_db = Label(Manage_Frame, text="annive", bg="rosy brown", fg="white",
                       font=("bahnschrift condensed", 16, "bold"))
        lbl_db.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_db = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 18, "bold"), bd=5,
                       relief=GROOVE)
        txt_db.grid(row=5, column=1, pady=10, padx=5, sticky="w")
        # tele
        lbl_tele = Label(Manage_Frame, text="Télé", bg="rosy brown", fg="white",
                         font=("bahnschrift condensed", 16, "bold"))
        lbl_tele.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_tele = Entry(Manage_Frame, textvariable=self.tele_var, font=("times new roman", 18, "bold"), bd=5,
                         relief=GROOVE)
        txt_tele.grid(row=6, column=1, pady=10, padx=5, sticky="w")
        # Filiére
        lbl_filiere = Label(Manage_Frame, text="Filiére", bg="rosy brown", fg="white",
                            font=("bahnschrift condensed", 16, "bold"))
        lbl_filiere.grid(row=7, column=0, pady=10, padx=18, sticky="w")
        txt_filiere = Entry(Manage_Frame, textvariable=self.filiere_var, font=("times new roman", 18, "bold"), bd=5,
                            relief=GROOVE)
        txt_filiere.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        # ===============partie des fonctions =====================

    # function
    def add_students(self):
        conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
        cursor = conn.cursor()

        # get values from the input fields
        cne = self.CNE_var.get()
        firstname = self.first_name_var.get()
        lastname = self.last_name_var.get()
        email = self.email_var.get()
        tele = self.tele_var.get()
        dob = self.dob_var.get()
        filiere = self.filiere_var.get()

        # Check if any field is empty
        if not all([cne, firstname, lastname, email, tele, dob, filiere]):
            messagebox.showerror("Error", "Veuillez remplir tous les champs")
            return

        # Insert the values into the database
        cursor.execute("INSERT INTO student VALUES(:1,:2,:3,:4,:5,:6,:7)",
                       (cne, firstname, lastname, email, tele, dob, filiere))

        # Commit the transaction
        conn.commit()

        # Show a success message
        self.clear_fields()
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès !")
        cursor.close()
        # refresh the table

        self.fetch_data()

        conn.close()

    def update_student(self):
        # get the values from the entries
        cne = self.CNE_var.get()
        firstname = self.first_name_var.get()
        lastname = self.last_name_var.get()
        email = self.email_var.get()
        tele = self.tele_var.get()
        dob = self.dob_var.get()
        filiere = self.filiere_var.get()

        # get the selected row from the table
        selected_row = self.student_table.focus()
        if not selected_row:
            messagebox.showerror("Error", "Please select a student to update")
            return
        values = self.student_table.item(selected_row, 'values')

        # check if all fields are filled
        if cne == '' or firstname == '' or lastname == '' or email == '' or tele == '' or dob == '' or filiere == '':
            messagebox.showerror("Error", "All fields are required")
            return

        # connect to the database
        try:
            conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
            cursor = conn.cursor()

            # update the selected row in the database
            cursor.execute(
                "UPDATE student SET first_name=:1, last_name=:2, email=:3, tele=:4, anniv=:5, filiere=:6 WHERE cne=:7",
                (firstname, lastname, email, tele, dob, filiere, values[0]))

            # commit the changes and close the connection
            conn.commit()
            cursor.close()
            conn.close()

            # clear the entries and show success message
            self.clear_fields()
            messagebox.showinfo("Success", "Student updated successfully")

            # refresh the table

            self.fetch_data()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error", f"Database error: {e}")
            return

    # delete function
    def delete_student(self):
        # get the selected row from the table
        selected_row = self.student_table.focus()
        if not selected_row:
            messagebox.showerror("Error", "Please select a student to delete")
            return
        values = self.student_table.item(selected_row, 'values')

        cne = values[0]

        # connect to the database
        try:
            conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
            cursor = conn.cursor()

            # delete the student record from the database
            cursor.execute("DELETE FROM student WHERE cne = :cne", {"cne": cne})

            # commit the changes and close the connection
            conn.commit()
            cursor.close()
            conn.close()

            # refresh the table
            self.student_table.delete(*self.student_table.get_children())
            self.fetch_data()

            # show success message
            messagebox.showinfo("Success", "Student deleted successfully")

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error", f"Database error: {e}")
            return

    # clair fonction
    def clear_fields(self):
        self.CNE_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.email_var.set("")
        self.tele_var.set("")
        self.dob_var.set("")
        self.filiere_var.set("")

    # ***************function table frame

    def fetch_data(self):
        # connect to the database
        conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute("select * from student")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:

                self.student_table.insert('',END,values=row)
        conn.commit()
    conn.close()

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.CNE_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.email_var.set(row[3])
        self.tele_var.set(row[4])
        self.dob_var.set(row[5])
        self.filiere_var.set(row[6])
#function search
    def search_data(self):
        # connect to the database
        conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
        cursor = conn.cursor()

        try:
            # execute the search query using the search box inputs
            cursor.execute(
                "select * from student where " + str(self.search_by.get()) + "=" + str(self.search_txt.get()))
            rows = cursor.fetchall()

            if len(rows) != 0:
                # clear the existing table data
                self.student_table.delete(*self.student_table.get_children())

                # populate the table with the search results
                for row in rows:
                    self.student_table.insert('', END, values=row)
            else:
                # show message if no data found
                messagebox.showinfo("Aucune donnée trouvée", "Aucune donnée ne correspond à votre recherche.")

        except cx_Oracle.DatabaseError as e:
            # show error message if the search identifier is not valid
            messagebox.showerror("Erreur de recherche", "Identificateur de recherche non valide: " + str(e))

        conn.commit()
        conn.close()

    #function telecharger
    import csv

    def export_students_to_csv(self):
        try:
            conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
            cursor = conn.cursor()
            with open('students.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['CNE', 'First Name', 'Last Name', 'Email', 'Birthday', 'Phone', 'Major'])
                cursor.execute('SELECT * FROM student')
                rows = cursor.fetchall()
                for row in rows:
                    writer.writerow(row)
            messagebox.showinfo("Success", "Student details exported to CSV file successfully!")

            # close the database connection
            cursor.close()
            conn.close()



        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error", f"Database error: {e}")

    #function to sign up students in login tables students
    def sign_up(self):
        import Student_registre

    def show_students(self):
        try:
            conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
            cursor = conn.cursor()

            # Query the database for all students
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()

            # Create a new window to display the results
            result_window = tk.Toplevel()
            result_window.title('List of Students')

            # Create a table to display the results
            table = tk.Frame(result_window)
            table.pack()

            # Add column labels to the table
            labels = ['ID', 'First Name', 'Last Name', 'Email', 'Password', 'Phone', 'Address', 'Birthdate']
            for i, label in enumerate(labels):
                label_widget = tk.Label(table, text=label)
                label_widget.grid(row=0, column=i)

            # Add rows to the table
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    cell_widget = tk.Label(table, text=value)
                    cell_widget.grid(row=i + 1, column=j)

            # close the database connection
            cursor.close()
            conn.close()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error", f"Database error: {e}")




root = Tk()
root.configure(background='rosy brown')
ob = Student(root)
root.mainloop()



