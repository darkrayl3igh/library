from tkinter import *
import profilePage as PP
import tkMessageBox
def loginTester(username,password):
    IDs=open("IDs.txt")
    loginIDs=IDs.readlines()
    IDs.close()
    if username+" "+password+"\n" in loginIDs:
        loginPage.destroy()
        tkMessageBox.showinfo("Login Successful","Welcome to SALA Library "+username)
        PP.profileFinder(username)
    else:
        tkMessageBox.showerror("Login Failed","Please check credentials and try again")
def loginPageCreator(event):
    global loginPage
    loginPage=Tk()
    loginPage.tk_setPalette(background="#f6f5f5")
    loginPage.title("Login Page")
    loginPage.geometry("250x375")
    container=Frame(loginPage,bg="#dbd8d8",height=325,width=200,bd=0)
    libraryLogo=Label(container,width=10,height=5,bg="black",bd=2)
    L1=Label(container,height=4,width=1,bg="#f04d4c",bd=0)
    L2=Label(container,height=1,width=6,bg="#f04d4c",bd=0)
    I=Label(container,height=2,width=1,bg="#f04d4c",bd=0)
    Bi=Label(container,height=6,width=1,bg="#13759a",bd=0)
    patchBi=Label(container,height=2,width=5,bg="#dbd8d8",bd=0)
    usernameEntry=Entry(container,width=17,font="corbel 11",bd=0,bg="white")
    passwordEntry=Entry(container,width=17,font="corbel 11",bd=0,bg="white",show="*")
    loginButton=Button(container,width=9,font="corbel 11 bold",bd=0,bg="#f04d4c",fg="white",text="Login",command=lambda:loginTester(usernameEntry.get(),passwordEntry.get()))
    libraryLogo.place(x=57,y=50,border=INSIDE)
    L1.place(x=64,y=60,border=INSIDE)
    L2.place(x=64,y=105,border=INSIDE)
    I.place(x=94,y=70,border=INSIDE)
    Bi.place(x=117,y=50,border=INSIDE)
    patchBi.place(x=92,y=131,border=INSIDE)
    container.place(x=25,y=25,border=INSIDE)
    usernameEntry.place(x=30,y=160,border=INSIDE)
    passwordEntry.place(x=30,y=190,border=INSIDE)
    loginButton.place(x=62,y=220,border=INSIDE)
    loginPage.mainloop()
