import tkinter as tk
import cx_Oracle
from PIL import Image, ImageTk
from tkinter import filedialog
import base64

class StudentRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Registration Form')

        # for image
        self.image = Image.open('grad.png').resize((150, 150), resample=Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        # image place in window
        self.add_pic_section = tk.Frame(root, highlightbackground="red", highlightthickness=2)
        self.add_pic_section.place(x=20, y=20, width=160, height=160)
        self.pic_label = tk.Label(self.add_pic_section, image=self.photo, bd=0)
        self.pic_label.pack(side="top", fill="both", expand=True)
        self.add_pic_text_btn = tk.Button(root, text='Add Picture', command=self.choose_image, bd=0,
                                          font=("bahnschrift condensed", 18, "bold"), fg='red')
        self.add_pic_text_btn.place(x=30, y=180)

        # create labels and entry fields for the form
        tk.Label(root, text='Full Name :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=20)
        self.full_name_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.full_name_entry.place(x=420, y=20)

        tk.Label(root, text="Father's Name :",bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=70)
        self.father_name_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.father_name_entry.place(x=420, y=70)

        tk.Label(root, text="Mother's Name :",bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=120)
        self.mother_name_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.mother_name_entry.place(x=420, y=120)

        tk.Label(root, text='Date of Birth :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=170)
        self.dob_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.dob_entry.place(x=420, y=170)

        tk.Label(root, text='Gender :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=220)
        self.gender_male = tk.Radiobutton(root, text='Male', value='male',font=("bahnschrift condensed", 13, "bold"))
        self.gender_male.place(x=420, y=220)
        self.gender_female = tk.Radiobutton(root, text='Female', value='female',font=("bahnschrift condensed", 13, "bold"))
        self.gender_female.place(x=500, y=220)
        self.gender_other = tk.Radiobutton(root, text='Other', value='other',font=("bahnschrift condensed", 13, "bold"))
        self.gender_other.place(x=580, y=220)

        tk.Label(root, text='Nationality :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=270)
        self.nationality_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.nationality_entry.place(x=420, y=270)

        tk.Label(root, text='Address :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=320)
        self.address_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.address_entry.place(x=420, y=320)

        tk.Label(root, text='Phone Number :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=370)
        self.phone_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.phone_entry.place(x=420, y=370)


        tk.Label(root, text='Email Address :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=420)
        self.email_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.email_entry.place(x=420, y=420)

        tk.Label(root, text="Father's Occupation :",bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=470)
        self.father_occupation_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.father_occupation_entry.place(x=420, y=470)

        tk.Label(root, text="Mother's Occupation :",bd=10, font=("bahnschrift condensed", 13, "bold")).place(x=220, y=520)
        self.mother_occupation_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.mother_occupation_entry.place(x=420, y=520)

        tk.Label(root, text='Annual Income :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=570)
        self.income_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.income_entry.place(x=420, y=570)

        tk.Label(root, text='Previous School Name :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=620)
        self.school_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.school_entry.place(x=420, y=620)

        tk.Label(root, text='Percentage/Grade :',bd=10,font=("bahnschrift condensed", 13, "bold")).place(x=220, y=670)
        self.grade_entry = tk.Entry(root,width=40,font=("bahnschrift condensed", 13, "bold"))
        self.grade_entry.place(x=420, y=670)
        # create a submit button
        self.submit_button = tk.Button(root, text='Submit', command=self.submit_form,bd=5,width=20,font=("bahnschrift condensed", 13, "bold"))
        self.submit_button.place(x=420, y=720)
        self.submit_button = tk.Button(root, text='Annuler', command=self.cancel, bd=5, width=20,
                                       font=("bahnschrift condensed", 13, "bold"))
        self.submit_button.place(x=420, y=770)

    def submit_form(self):
        # get values from entry fields
        full_name = self.full_name_entry.get()
        father_name = self.father_name_entry.get()
        mother_name = self.mother_name_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_male.cget('value')
        nationality = self.nationality_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        father_occupation = self.father_occupation_entry.get()
        mother_occupation = self.mother_occupation_entry.get()
        income = self.income_entry.get()
        school_name = self.school_entry.get()
        grade = self.grade_entry.get()

        # check if any of the required fields are empty
        if not full_name or not father_name or not mother_name or not dob or not nationality or not address or not phone or not email\
                or not father_occupation or not mother_occupation or not income:
            tk.messagebox.showerror('Error', 'Please fill in all required fields.')
            return

        # save data to database
        try:
            conn = cx_Oracle.connect('system/strong@localhost:1521/xe')
            c = conn.cursor()
            query = "INSERT INTO student_registration (full_name, father_name, mother_name, dob, gender, nationality, address, " \
                    "phone, email, father_occupation, mother_occupation,income,school_name,grade) VALUES (:1, :2, :3, TO_DATE(:4, 'DD/MM/YYYY'), :5, :6, :7, :8, :9, :10, :11,:12,:13,:14)"
            c.execute(query, (
            full_name, father_name, mother_name, dob, gender, nationality, address, phone, email, father_occupation,
            mother_occupation,income,school_name,grade))
            conn.commit()
            tk.messagebox.showinfo('Success', 'Data saved successfully.')
            self.clear_fields()
        except Exception as e:
            tk.messagebox.showerror('Error', str(e))
        finally:
            c.close()
            conn.close()

            # clear the form
            self.full_name_entry.delete(0, 'end')
            self.father_name_entry.delete(0, 'end')
            self.mother_name_entry.delete(0, 'end')
            self.dob_entry.delete(0, 'end')
            self.gender_male.deselect()
            self.gender_female.deselect()
            self.gender_other.deselect()
            self.nationality_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.phone_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.father_occupation_entry.delete(0, 'end')
            self.mother_occupation_entry.delete(0, 'end')
            self.income_entry.delete(0, 'end')
            self.school_entry.delete(0, 'end')
            self.grade_entry.delete(0, 'end')
    def cancel(self):
        root.destroy()

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=(
        ("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")))
        if file_path:
            self.image = Image.open(file_path).resize((150, 150), resample=Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.pic_label.config(image=self.photo)
root = tk.Tk()
root.geometry("887x820")
#root.configure(background='rosy brown')
app = StudentRegistrationForm(root)
root.mainloop()