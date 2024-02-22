from tkinter import *
import cx_Oracle
from tkinter import simpledialog

from tkinter import messagebox
from PIL import ImageTk
import smtplib
from email.mime.text import MIMEText
import time
from tqdm import tqdm
def login():
    # Get the username and password entered by the user
    username = usernameEntry.get()
    password = passwordEntry.get()
    conStr = cx_Oracle.connect('system/strong@localhost:1521/xe')
    print("Connected to Oracle database successfully")

    cursor = conStr.cursor()
    print("Cursor created successfully")

    cursor.execute("SELECT email, password FROM admin")


    result = cursor.fetchone()
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"result: {result}")

    # Check if the username and password fields are empty
    if username == '' or password == '':
        messagebox.showerror('Erreur!', ' Les champs ne peuvent pas être vides')

    # Check if the username is correct
    elif not result:
        messagebox.showerror('Erreur!', 'Veuillez entrer des identifiants corrects')

    # Check if the password is correct
    elif result[1] == password:
        # allow access to the functionality
        # insert your code here
        messagebox.showinfo('Succès', 'Bienvenue ! \n Admin ')
        window.destroy()
        import admin_interface
    else:
        # display an error message
        messagebox.showerror('Erreur!', 'Le mot de passe est incorrect')



window = Tk()


def forgotPassword():
    email = simpledialog.askstring("Réinitialisation du mot de passe", "Enter your email address or phone number:",
                                   parent=window)

    # Generate a unique password reset token and store it in the database
    # ...

    # Send a password reset link to the user's email
    msg = MIMEText(
        "Click the following link to reset your password: https://example.com/reset_password?token=<password_reset_token>")
    msg['Subject'] = 'Password reset'
    msg['From'] = 'noreply@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('youremail@gmail.com', 'yourpassword')
        smtp.send_message(msg)


window.geometry('1534x830')
window.title('Systéme De Connexion')

#window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bgbg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)
loginFrame = Frame(window, bg='#F5DEB3')
loginFrame.place(x=520, y=410)

logoImage = PhotoImage(file='logo.png')
error_label = Label(window, text="", fg="red")
error_label.pack()

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text="Nom d'utilisateur", compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)
usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Mot de passe', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
#i make the password as it's typed !
passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue', show='*')

passwordEntry.grid(row=2, column=1, pady=10, padx=20)
forgotPasswordButton = Button(loginFrame, text='Mot de passe oublié?', font=('times new roman', 12), fg='white', bg='#0072C6', activebackground='#0072C6', activeforeground='white', cursor='hand2', command=forgotPassword)
forgotPasswordButton.grid(row=4, column=1, pady=10)

loginButton = Button(loginFrame, text='Connexion', font=('times new roman', 14, 'bold'), width=15
                     , fg='black', bg='yellow', activebackground='cornflowerblue',
                     activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)




window.mainloop()
