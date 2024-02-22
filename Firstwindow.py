import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
# Create a new window
window = tk.Tk()
window.title("Systeme de Gestion des Etudiants")
window.geometry("1534x830")

backgroundImage = ImageTk.PhotoImage(file='kk.jpg')
# create a label widget and set it as the background of the window
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0,relwidth=1, relheight=1)
loginFrame = Frame(window, bg='#F5DEB3')
loginFrame.place(x=400, y=305)

# create a label widget and set it as the background of the window
titre_projet = Label(window, text="About project", font=("bahnschrift condensed", 25, "bold"), fg="cornflowerblue")


titre_projet.pack(pady=20)
# Add the logo image
logo_image = Image.open("test.jpg")
logo_image = logo_image.resize((150, 150), resample=Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(image=logo_photo)
logo_label.image = logo_photo
logo_label.pack(pady=10)

# Add project description
project_description = "Bienvenue à notre système de gestion des étudiants! Notre plateforme offre une " \
                      "solution complète pour gérer les informations et les dossiers académiques " \
                      "des étudiants. Avec deux niveaux d'accès distincts, les étudiants et les" \
                      " administrateurs peuvent naviguer efficacement dans le système pour accéder " \
                      "à diverses fonctionnalités. Pour les étudiants," \
                      " notre système propose une " \
                      "inscription facile, la gestion de profil, la sélection de cours et le suivi " \
                      "de la présence. Les administrateurs ont le pouvoir de gérer les dossiers des " \
                      "étudiants, de créer de nouveaux profils d'étudiants, de mettre à jour les dossiers " \
                      "existants, de télécharger des fichiers importants, de marquer la présence et plus " \
                      "encore. Avec notre système de gestion des étudiants, vous pouvez rationaliser " \
                      "l'administration académique et offrir aux étudiants une expérience d'apprentissage optimale."
description_label = tk.Label(window, text=project_description, wraplength=380, font=("bahnschrift condensedl", 12,'bold'),  justify="center")
description_label.pack(pady=10)
#import loginform for student and admin
def student_login():
    window.destroy()
    import login_students
def admin_login():
    window.destroy()
    import login_admin
# Add student and admin mode buttons
student_button = tk.Button(window, text="Mode Étudiant",font=('bahnschrift condensed', 16, 'bold'), width=15
                     , fg='black', bg='cornflowerblue', activebackground='cornflowerblue',
                     activeforeground='white', cursor='hand2', command=student_login)
student_button.pack(side=tk.LEFT, padx=300,pady=20)
admin_button = tk.Button(window, text="M.Administrateur", font=('bahnschrift condensed', 16, 'bold'),
                         width=16, fg='black', bg='cornflowerblue', activebackground='cornflowerblue',
                         activeforeground='white', cursor='hand2', compound='left',command=admin_login)

admin_button.pack(side=tk.RIGHT, padx=300,pady=20 )

# Start the GUI
window.mainloop()
