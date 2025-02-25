import tkinter as t
import tkinter.messagebox as k

reg_infor = {}

def register():
    name = name_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not name or not email or not username or not password or not confirm_password:
        k.showerror("Error", "Please input all fields!")
        return

    if password != confirm_password:
        k.showerror("Error", "Input passwords do not match")
        return

    if "@" not in email or "." not in email:
        k.showerror("Error", "Invalid email format")
        return

    if username in reg_infor:
        k.showerror("Error", "Username already exists! Please choose a new one.")
        return

    reg_infor[username] = {"name": name, "email": email, "password": password}
    k.showinfo("Success", "Successfully registered!")

    name_entry.delete(0,t.END)
    email_entry.delete(0,t.END)
    username_entry.delete(0,t.END)
    password_entry.delete(0,t.END)
    confirm_password_entry.delete(0,t.END)

    login()

def login():
    login_page=t.Toplevel(app)
    login_page.title("Login page")
    login_page.configure(bg='pink')
    login_page.geometry('300x200')

    username_login = t.Label(login_page, text='Username:', font=('Calibri', 15))
    username_login.place(x=4, y=40) 
    username_login_entry = t.Entry(login_page, font=('Calibri', 13))
    username_login_entry.place(x=120, y=40)

    password_login=t.Label(login_page,text='Password:',font=('Calibri', 15))
    password_login.place(x=4,y=80)
    password_login_entry=t.Entry(login_page,font=('Calibri', 13),show="*")
    password_login_entry.place(x=120,y=80)

    def login_verification():
        username=username_login_entry.get()
        password=password_login_entry.get()

        if username in  reg_infor and reg_infor[username]["password"] ==password:
            k.showinfo("Congrats!","Login successfull")

            login_page.destroy()

        else:
              k.showinfo("Invalid username or password")
              
    login_button = t.Button(login_page, text="Login", font=('Calibri', 14), command=login_verification)
    login_button.place(x=100, y=120)
              


app = t.Tk()
app.title('My Application')
app.geometry('500x400')
app.configure(bg='pink')

heading = t.Label(app, text=" Application Form", font=("Calibri", 20, "bold"), fg="black",bg="pink")
heading.pack(pady=20)

name_label = t.Label(app, text="Name:", font=("Calibri", 14), bg="pink")
name_label.place(x=50, y=60)
name_entry = t.Entry(app, font=("Calibri", 13))
name_entry.place(x=200, y=60)

email_label = t.Label(app, text="Email:", font=("Calibri", 14), bg="pink")
email_label.place(x=50, y=90)
email_entry = t.Entry(app, font=("Calibri", 13))
email_entry.place(x=200, y=90)

username_label = t.Label(app, text="Username:", font=("Calibri", 14), bg="pink")
username_label.place(x=50, y=120)
username_entry = t.Entry(app, font=("Calibri", 13))
username_entry.place(x=200, y=120)

password_label = t.Label(app, text="Password:", font=("Calibri", 14), bg="pink")
password_label.place(x=50, y=150)
password_entry = t.Entry(app, font=("Calibri", 13), show="*") 
password_entry.place(x=200, y=150)

confirm_password_label = t.Label(app, text="Confirm Password:", font=("Calibri", 14), bg="pink")
confirm_password_label.place(x=50, y=180)
confirm_password_entry = t.Entry(app, font=("Calibri", 13), show="*")  
confirm_password_entry.place(x=200, y=180)

register_button = t.Button(app, text="Register", font=("Calibri", 14), bg="white", fg="black", command=register)
register_button.place(x=200, y=230)

app.mainloop()








