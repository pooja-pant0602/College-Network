
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

root= Tk()
root.title('College Network')
root.config(background='light blue')
root.geometry('550x500')
username= StringVar()
pwd= StringVar()
new_uname= StringVar()
new_pwd= StringVar()
gender= IntVar()
batch=StringVar()
batch_msg=StringVar()

def create_account():
    login_frame.pack_forget()
    main_heading['text']='SIGN UP'
    cr_frame.pack()

def log():
    cr_frame.pack_forget()
    main_heading['text']='LOGIN'
    username.set('')
    pwd.set('')
    login_frame.pack()

def logout():
    main_heading['text']='LOGIN'
    username.set('')
    pwd.set('')
    main_frame.pack_forget()
    login_frame.pack()

def send_msg():
    ms.showinfo('Success!','Your message has been sent')
    batch_msg.set('Batch List')
    msg_box.delete('1.0',END)

def login():
    uname_db=username.get()
    pwd_db=pwd.get()

    conn=sqlite3.connect('TeacherDatabase.db')
    with conn:
        cur=conn.cursor()
        cur.execute('SELECT * FROM Teacher WHERE Username=? AND Password=?',[uname_db,pwd_db])
        result=cur.fetchall()

        if len(result)!=0:
            login_frame.pack_forget()
            main_heading['text']='COLLEGE NETWORK'
            main_frame.pack()

        else:
            ms.showerror('Error!', 'Account does not exist! Check Username and Password or Create new account')
            username.set('')
            pwd.set('')

    conn.close()


def signup():
    uname_db=new_uname.get()
    pwd_db=new_pwd.get()
    gender_db=gender.get()
    batch_db=batch.get()
    if(gender_db==1):
        gender_db='Male'
    else:
        gender_db='Female'

    conn=sqlite3.connect('TeacherDatabase.db')
    with conn:
        cur=conn.cursor()
        cur.execute('SELECT * FROM Teacher where Username=?',[uname_db])
        result=cur.fetchall()

        if len(result)==0:
            ms.showinfo('Success!', 'Account Created!')
            cur.execute('INSERT INTO Teacher VALUES (?,?,?,?)',[uname_db, pwd_db, gender_db,batch_db])
            new_uname.set('')
            new_pwd.set('')
            gender.set('0')
            batch.set('Select your batch')
            log()

        else:
            ms.showerror('Error!', 'Username taken! Try a different username...')
            new_uname.set('')
            new_pwd.set('')
            gender.set('0')
            batch.set('Select your batch')
    conn.close()


conn=sqlite3.connect('TeacherDatabase.db')
with conn:
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Teacher(
                        Username TEXT NOT NULL,
                        Password TEXT NOT NULL,
                        Gender TEXT,
                        Batch NUMBER)''')

conn.close()
main_heading= Label(root, text='LOGIN', font=('Arial', 25),bg='light blue')
main_heading.pack()

login_frame= Frame(root, bg='light blue')
name_label=Label(login_frame, text='Username:', font=('Arial', 20), pady=20,padx=10,bg='light blue').grid(sticky=W)
name_entry=Entry(login_frame, textvar=username, bd=5, width=30).grid(row=0,column=1, sticky=W)
pwd_label=Label(login_frame, text='Password:', font=('Arial', 20), pady=20,padx=10,bg='light blue').grid(sticky=W)
pwd_entry=Entry(login_frame, textvar=pwd, bd=5, width=30, show='*').grid(row=1,column=1, sticky=W)
login_button=Button(login_frame, text='Login', font=('Arial', 12), pady=20, padx=10, width=15,command=login, fg='white', bg='steel blue').grid(sticky=W)
createacc_button=Button(login_frame, text='Create Account',font=('Arial', 12), pady=20, padx=10,width=15,command=create_account,fg='white', bg='steel blue').grid(row=2,column=1, sticky=E)

login_frame.pack()

cr_frame=Frame(root, bg='light blue')
batch_list=[1,2,3,4,5]
new_name_label=Label(cr_frame, text='Username:',font=('Arial', 20), pady=20,padx=10,bg='light blue').grid(sticky=W)
new_name_entry=Entry(cr_frame, textvar=new_uname, bd=5, width=30).grid(row=0,column=1, sticky=W)
new_pwd_label=Label(cr_frame, text='Password:', font=('Arial', 20), pady=20,padx=10,bg='light blue').grid(sticky=W)
new_pwd_entry=Entry(cr_frame, textvar=new_pwd, bd=5, width=30, show='*').grid(row=1,column=1, sticky=W)
gender_label=Label(cr_frame,text='Gender:',font=('Arial', 20), pady=20,padx=10,bg='light blue').grid(sticky=W)
male_button=Radiobutton(cr_frame, text='Male', bd=5, variable=gender, value=1, font=('Arial', 12),bg='light blue').grid(row=2,column=1, sticky=W)
female_button=Radiobutton(cr_frame, text='Female', bd=5, variable=gender, value=2, font=('Arial', 12),bg='light blue').grid(row=2, column=1, sticky=E)
batch_label=Label(cr_frame, text='Batches:',font=('Arial', 20), pady=20,padx=10,bg='light blue').grid()
drop_list=OptionMenu(cr_frame, batch, *batch_list)
drop_list.config(width=15)
batch.set('Select your batch')
drop_list.grid(row=3, column=1, sticky=E)

signup_button=Button(cr_frame, text='Sign Up', font=('Arial', 12), pady=20, padx=10, width=15, command=signup,fg='white', bg='steel blue').grid(sticky=W)
back_button=Button(cr_frame, text='Go Back',font=('Arial', 12), pady=20, padx=10,width=15, command=log,fg='white', bg='steel blue').grid(row=4,column=1, sticky=E)

main_frame=Frame(root, bg='light blue')
select_batch=Label(main_frame, text='Select a batch to send message:',font=('Arial', 12), pady=20,padx=10,bg='light blue').grid(sticky=W,pady=(50,20))
drop_list_new=OptionMenu(main_frame, batch_msg, *batch_list)
drop_list_new.config(width=15)
batch_msg.set('Batch List')
drop_list_new.grid(row=0,column=1,sticky=W)
msg_label=Label(main_frame, text='Enter your message:',font=('Arial', 15),padx=20,pady=20,bg='light blue').grid(row=1,column=0,sticky=E)
msg_box=Text(main_frame,padx=20,pady=20,borderwidth=2,relief=SUNKEN,height=2,width=25)
msg_box.grid(row=1,column=1,sticky=W) #grid doesnt return anything

send_msg = Button(main_frame, text='SEND MESSAGE', font=('Arial', 13),fg='white', bg='steel blue',command=send_msg).grid(row=3,column=0,sticky=E, pady=20,padx=20)
logout = Button(main_frame, text='LOG OUT', font=('Arial', 13),command=logout,fg='white', bg='steel blue').grid(row=3,column=1,sticky=W, pady=20,padx=20)

root.mainloop()