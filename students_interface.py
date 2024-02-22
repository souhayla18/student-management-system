from tkinter import *
from tkinter import messagebox

import pandas as pd
import cx_Oracle
from PIL import Image, ImageTk

from tkinter import ttk
import tkinter as tk
window = tk.Tk()
# right frame
Detail_Frame = Frame(window, bd=4, relief=RIDGE, bg="pink")
Detail_Frame.place(x=580, y=120, width=800, height=550)
add_pic=tk.PhotoImage(file='grad.png')
#hhh

#working in the infromation student
# Connect to Oracle database
conStr = cx_Oracle.connect('system/strong@localhost:1521/xe')

# Get the student_id of the current user
cursor = conStr.cursor()
# Fetch the student details from the student_profile table using the current_user_id
query = f"SELECT first_name, last_name, email, phone, dob, filiere  FROM student_profile WHERE student_id IN (SELECT student_id FROM students WHERE current_user = 1)"
cursor.execute(query)
result = cursor.fetchall()


student_n_label = tk.Label(Detail_Frame, text=f"Nom : {result[0][0]}", font=("bahnschrift condensed", 14, "bold"), bg='pink')

student_n_label.pack(pady=20,padx=5)
student_p_label = tk.Label(Detail_Frame, text=f"Prénom: {result[0][1]} ", font=("bahnschrift condensed", 14, "bold"),bg='pink')
student_p_label.pack(pady=10,padx=5)
student_e_label = tk.Label(Detail_Frame, text=f"Email :{result[0][2]}", font=("bahnschrift condensed", 14, "bold"),bg='pink')
student_e_label.pack(pady=10,padx=5)
student_t_label = tk.Label(Detail_Frame, text=f"télé :{result[0][3]}", font=("bahnschrift condensed", 14, "bold"),bg='pink')
student_t_label.pack(pady=10,padx=5)
student_db_label = tk.Label(Detail_Frame, text=f"date de naissance  :{result[0][4]}", font=("bahnschrift condensed", 14, "bold"),bg='pink')
student_db_label.pack(pady=10,padx=5)
student_f_label = tk.Label(Detail_Frame, text=f"Filiére :{result[0][5]}", font=("bahnschrift condensed", 14, "bold"),bg='pink')
student_f_label.pack(pady=10,padx=5)
#student_name=tk.Text(Detail_Frame,text="Email : ",font=("bahnschrift condensed", 14, "bold"))
#student_name.pack(pady=20)




# Close the cursor and commit changes
cursor.close()
conStr.commit()

# Close the connection
conStr.close()


#working in the infromation student
#frame pour image
add_pic_section=tk.Frame(Detail_Frame,highlightbackground="beige",highlightthickness=2)
add_pic_section.place(x=5,y=5,width=160,height=160)
add_pic_section_btn=tk.Button(add_pic_section,image=add_pic,bd=0)
add_pic_section_btn.pack()
# lift frame
Manage_Frame = Frame(window, bd=4, relief=RIDGE, bg='pink')
Manage_Frame.place(x=100, y=40, width=420, height=710)

def accuiel():
    window.destroy()
    import Firstwindow
def Formulaire_inscription():
    import regisrtforum_stu
def loug_out():
    window.destroy()

def complaint_box():
    # Create a new window for the complaint box
    complaint_window = Toplevel(window)
    complaint_window.geometry("500x500")
    complaint_window.title("Complaint Box")

    # Create a label and a text box for the complaint
    complaint_label = Label(complaint_window, text="Veuillez écrire votre plainte ici :")
    complaint_label.pack()

    complaint_text = Text(complaint_window, height=10, width=50)
    complaint_text.pack()

    def submit_complaint():
        # Open the file in append mode
        with open("complaints.txt", "a") as file:
            # Write the complaint text to the file
            file.write(complaint_text.get("1.0", END))
            # Add a separator between each complaint for readability
            file.write("\n------------------------\n")

        # Show a message to the user that their complaint has been submitted
        messagebox.showinfo('Succès', 'Votre plainte a été enregistrée.')

    # Create a button to submit the complaint
    submit_button = Button(complaint_window, text="Submit", command=submit_complaint)
    submit_button.pack()



admin_button = tk.Button(Manage_Frame,text="Accuiel", width=30, font=("bahnschrift condensed", 14, "bold"), fg='black',
                       bg='beige',command=accuiel).grid(row=4, column=3, padx=110, pady=90)

admin_button = tk.Button(Manage_Frame,text="Formulaire d'inscription", width=30, font=("bahnschrift condensed", 14, "bold"), fg='black',
                       bg='beige',command=Formulaire_inscription).grid(row=5, column=3, padx=50, pady=40)

admin_button = tk.Button(Manage_Frame,text="Cours", width=30, font=("bahnschrift condensed", 14, "bold"), fg='black',
                       bg='beige').grid(row=6, column=3, padx=50, pady=40)

# Add the complaint_box() function to the command argument of the button
admin_button = tk.Button(Manage_Frame,text="Service informatique", width=30, font=("bahnschrift condensed", 14, "bold"), fg='black',
                       bg='beige', command=complaint_box).grid(row=7, column=3, padx=50, pady=40)

admin_button = tk.Button(Manage_Frame,text="Déconnexion", width=30, font=("bahnschrift condensed", 14, "bold"), fg='black',
                       bg='beige',command=loug_out).grid(row=8, column=3, padx=50, pady=40)

window.geometry("1510x810+0+0")
window.configure(background='beige')
window.mainloop()
