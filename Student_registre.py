from tkinter import *
import cx_Oracle
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("Student Registration Form")

# connecte the databases with oracle
conStr = 'system/strong@localhost:1521/xe'
conn = cx_Oracle.connect(conStr)

# Create labels for each field
label_f_name = Label(root, text="First Name")
label_l_name = Label(root, text="Last Name")
label_email = Label(root, text="Email")
label_password = Label(root, text="Password")
label_address = Label(root, text="Address")
label_phone = Label(root, text="Phone Number")
label_brd = Label(root, text="Birth Day")

# Create entry fields for each label
entry_first_name = Entry(root, width=35,highlightbackground="yellow", borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="red")
entry_last_name = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")
entry_email = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")
entry_password = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")
entry_address = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")
entry_phone = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")
entry_brd = Entry(root, width=35, borderwidth=3, font=('Arial', 12),bd=5, relief=GROOVE,fg="black")

# Add labels and entry fields to the grid
label_f_name.grid(row=0, column=0, pady=20)
label_l_name.grid(row=1, column=0, pady=20)
label_email.grid(row=2, column=0, pady=20)
label_password.grid(row=3, column=0, pady=20)
label_address.grid(row=4, column=0, pady=20)
label_phone.grid(row=5, column=0, pady=20)
label_brd.grid(row=6, column=0, pady=20)

entry_first_name.grid(row=0, column=1)
entry_last_name.grid(row=1, column=1)
entry_email.grid(row=2, column=1)
entry_password.grid(row=3, column=1)
entry_address.grid(row=4, column=1)
entry_phone.grid(row=5, column=1)
entry_brd.grid(row=6, column=1)

# Add a submit button
def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    phone = entry_phone.get()
    address = entry_address.get()
    brd = entry_brd.get()

    # Check if the email address is valid
    import re
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror('Error!', 'Invalid email address')
        return

    # Check if the password meets the policy
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(password_regex, password):
        messagebox.showerror('Error!', 'Password must contain at least 8 characters including 1 uppercase, 1 lowercase, 1 digit and 1 special character')
        return

    try:
        # Check if the email already exists in the database
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM students WHERE email=:email", {'email': email})
        result = cursor.fetchone()
        if result is not None:
            messagebox.showerror('Error!', 'Email already exists in the database')
            return

        conStr = cx_Oracle.connect('system/strong@localhost:1521/xe')
        cursor = conStr.cursor()
        cursor.execute(
            "INSERT INTO students(first_name, last_name, email, password, phone, address, brd) VALUES (:1, :2, :3, :4, :5, :6, TO_DATE(:7, 'DD/MM/YYYY'))",
            (first_name, last_name, email, password, phone, address, brd))
        conStr.commit()
        conStr.close()
        messagebox.showinfo('Succès', 'Étudiant enregistré avec succès')

        refresh_students()
        return
    except cx_Oracle.Error as error:
          messagebox.showerror('Erreur', 'Erreur lors de l\'enregistrement de l\'étudiant: {}'.format(error))
          return
def refresh_students():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for i, row in enumerate(rows):
            for j in range(len(row)):
                e = Entry(root, width=10, fg='blue')
                e.grid(row=i+10, column=j)
                e.insert(END, row[j])
    except cx_Oracle.Error as error:
        messagebox.showerror('Error', 'Error fetching data from database: {}'.format(error))


button_submit = Button(root, text="Submit", command=submit_form)
button_submit.grid(row=8, column=0)

root.mainloop()