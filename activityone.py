#tkinter
import tkinter

#open a window
app = tkinter.Tk()

app.title('My app')
app.geometry('500x400')
app.configure(bg='pink')
intro_label=tkinter.Label(app,text='LOGIN PAGE',fg='black',font=('Tunga',15,'bold')).pack()
username=tkinter.Label(app,text='Username',font=('Calibri',14)).place(x=4,y=40)
username_ntry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=40)

password=tkinter.Label(app,text='Password',font=('Calibri',14)).place(x=4,y=85)
password_entry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=85)

email=tkinter.Label(app,text='Email',font=('Calibri',14)).place(x=4,y=130)
email_entry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=130)

age=tkinter.Label(app,text='Age',font=('Calibri',14)).place(x=4,y=175)
age_entry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=175)

location=tkinter.Label(app,text='Location',font=('Calibri',14)).place(x=4,y=215)
location_entry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=215)

tribe=tkinter.Label(app,text='Tribe',font=('Calibri',14)).place(x=4,y=255)
tribe_entry=tkinter.Entry(app,font=('Calibri',13)).place(x=100,y=255)

regbutton=tkinter.Button(app,text='Login',font=('Calibri',14)).place(x=100,y=300)

#close
app.mainloop()
