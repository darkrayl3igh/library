from tkinter import *
import tkMessageBox
import time
class newID:
    def __init__(self,u,p,g,e,a,s,m):
        self.profiles=open("Profiles.txt","a")
        self.profiles.write(s+" "+u+" "+p+" "+a+" "+g+" "+e+" "+str(m)+" "+time.strftime("%d/%m/%y %H:%M", time.localtime(time.time()))+"None\n")
        self.profiles.close()
        self.IDs=open("IDs.txt","a")
        self.IDs.write(u+" "+p+"\n")
        self.IDs.close()
def validityChecker(username,password1,password2,gender,email,age,studentID,membership):
    profiles=open("Profiles.txt")
    profileList=profiles.readlines()
    profiles.close()
    for value in profileList:
        if (" " in username) or (" " in password1) or (" " in email) or (" " in age) or (" " in studentID):
            tkMessageBox.showerror("Registration Failed","Please do not use spaces")
            break
        profile=value.split(" ")
        if username!=profile[1] and username!="":
            if (studentID!=profile[0]) and (len(studentID)==6) :
                if len(password1)>6:
                    if password1==password2:
                        if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHER":
                            if ("@GMAIL.COM" in email.upper()) or ("@YAHOO.COM" in email.upper()) or ("@HOTMAIL.COM" in email.upper()):
                                tkMessageBox.showinfo("Registration Successful","Your account has been successfully created")
                                ID=newID(username,password1,gender,email,age,studentID,membership)
                                registrationPage.destroy()
                                break
                            else:
                                tkMessageBox.showerror("Registration Failed","Please enter a valid E-mail address\nWe support gmail, yahoo and hotmail.")
                                emailEntry.delete(0, END)
                        else:
                            tkMessageBox.showerror("Registration Failed","Please enter a valid gender\nMale, Female or Other.")
                            genderEntry.delete(0, END)
                    else:
                        tkMessageBox.showerror("Registration Failed","Passwords do not match")
                        passwordEntry.delete(0, END)
                        confirmPasswordEntry.delete(0, END)
                else:
                    tkMessageBox.showerror("Registration Failed","Please choose a longer password")
            else:
                tkMessageBox.showerror("Registration Failed","Student ID already registered/Student ID invalid")
                studentIDEntry.delete(0, END)
        else:
            tkMessageBox.showerror("Registration Failed","Please choose another username")
            usernameEntry.delete(0, END)
def registrationPageCreator(event):
    global registrationPage,usernameEntry,passwordEntry,emailEntry,ageEntry,confirmPasswordEntry,genderEntry,studentIDEntry,membershipTime
    registrationPage=Tk()
    membershipTime=1
    def timeChanger(func):
        global membershipTime
        if membershipTime>=0:
            if func=="add":
                minusTime.config(state=NORMAL)
                membershipTime+=1
            else:
                membershipTime-=1
        if membershipTime==0:
            minusTime.config(state=DISABLED)
        membershipValue.config(text=str(membershipTime)+" Month(s)")
    registrationPage.title("Signup for a new account")
    registrationPage.tk_setPalette(background="#f6f5f5")
    registrationPage.geometry("300x500")
    container=Frame(registrationPage,width=280,height=480,bg="#dbd8d8")
    libraryLogoLabel=Label(container,bg="black",width=10,height=5,bd=0)
    studentIDLabel=Label(container,text="Student ID",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    passwordLabel=Label(container,text="Password",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    confirmPasswordLabel=Label(container,text="Confirm Password",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    ageLabel=Label(container,text="Age",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    genderLabel=Label(container,text="Gender",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    emailLabel=Label(container,text="E-mail",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    membershipLabel=Label(container,text="Membership Interval",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    usernameEntry=Entry(container,font="corbel 11",bd=0,fg="black",width=15)
    passwordEntry=Entry(container,font="corbel 11",bd=0,fg="black",show="*",width=18)
    confirmPasswordEntry=Entry(container,font="corbel 11",bd=0,fg="black",show="*",width=18)
    emailEntry=Entry(container,font="corbel 11",bd=0,fg="black",width=25)
    ageEntry=Entry(container,font="corbel 11",bd=0,fg="black",width=6)
    genderEntry=Entry(container,font="corbel 11",bd=0,fg="black",width=10)
    studentIDEntry=Entry(container,font="corbel 11",bd=0,fg="black",width=8)
    addTime=Button(container,text="+",width=5,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:timeChanger("add"))
    minusTime=Button(container,text="-",width=5,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:timeChanger("minus"))
    registerButton=Button(container,text="Register",width=11,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:validityChecker(usernameEntry.get(),passwordEntry.get(),confirmPasswordEntry.get(),genderEntry.get(),emailEntry.get(),ageEntry.get(),studentIDEntry.get(),membershipTime))
    membershipValue=Label(container,text=str(membershipTime)+" Month(s)",font="corbel 11",bd=0,fg="black",bg="#f6f5f5",anchor="s",width=14)
    L1=Label(container,height=4,width=1,bg="#f04d4c",bd=0)
    L2=Label(container,height=1,width=6,bg="#f04d4c",bd=0)
    I=Label(container,height=2,width=1,bg="#f04d4c",bd=0)
    Bi=Label(container,height=6,width=1,bg="#13759a",bd=0)
    patchBi=Label(container,height=2,width=5,bg="#dbd8d8",bd=0)
    usernameLabel=Label(container,text="Username",font="corbel 8",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    L1.place(x=17,y=20,border=INSIDE)
    L2.place(x=17,y=65,border=INSIDE)
    I.place(x=47,y=30,border=INSIDE)
    Bi.place(x=65,y=10,border=INSIDE)
    patchBi.place(x=45,y=87,border=INSIDE)
    usernameLabel.place(x=10,y=110,border=INSIDE)
    libraryLogoLabel.place(x=10,y=10,border=INSIDE)
    usernameEntry.place(x=10,y=125,border=INSIDE)
    studentIDLabel.place(x=140,y=110,border=INSIDE)
    studentIDEntry.place(x=140,y=125,border=INSIDE)
    passwordLabel.place(x=10,y=150,border=INSIDE)
    passwordEntry.place(x=10,y=165,border=INSIDE)
    confirmPasswordLabel.place(x=10,y=190,border=INSIDE)
    confirmPasswordEntry.place(x=10,y=205,border=INSIDE)
    ageLabel.place(x=10,y=230,border=INSIDE)
    ageEntry.place(x=10,y=245,border=INSIDE)
    genderLabel.place(x=90,y=230,border=INSIDE)
    genderEntry.place(x=90,y=245,border=INSIDE)
    emailLabel.place(x=10,y=270,border=INSIDE)
    emailEntry.place(x=10,y=285,border=INSIDE)
    membershipLabel.place(x=10,y=310,border=INSIDE)
    membershipValue.place(x=10,y=325,border=INSIDE)
    addTime.place(x=20,y=350,border=INSIDE)
    minusTime.place(x=70,y=350,border=INSIDE)
    registerButton.place(x=176,y=442,border=INSIDE)
    container.place(x=10,y=10,border=INSIDE)
    registrationPage.mainloop()
