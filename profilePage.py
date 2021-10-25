from tkinter import *
import time
import editProfile as EP
import bookReader as BR
def timeFinder(username):
    profiles=open("Profiles.txt")
    profileList=profiles.readlines()
    profiles.close()
    for value in  profileList:
        profile=value.split(" ")
        if username==profile[1]:
            break
    initTime=profile[7].split("/")
    initTime[1]=str(int(initTime[1])+int(profile[6]))
    if int(initTime[1])>12:
        initTime[1]=str(int(initTime[1])-12)
        initTime[2]=str(int(initTime[2])+1)
        if int(initTime[2])>99:
               initTime[2]=str(int(initTIme[2])-100)
    return profile[7]+" to "+initTime[0]+"/"+initTime[1]+"/"+initTime[2]
def profilePageCreator(user):
    global usernameValue,passwordValue,emailValue,ageValue,genderValue,studentIDValue,profilePage
    profiles=open("Profiles.txt")
    profileList=profiles.readlines()
    profiles.close()
    for value in  profileList:
        profile=value.split(" ")
        if user==profile[1]:
            break
    profilePage=Tk()
    profilePage.title(user+"'s Profile")
    profilePage.tk_setPalette(background="#f6f5f5")
    profilePage.geometry("400x500")
    container=Frame(profilePage,bg="#dbd8d8",width=370,height=470,bd=0)
    editButton=Button(container,text="Edit Profile",width=11,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:EP.validifier(user))
    bookButton=Button(container,text="Read a book",width=11,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=BR.bookName)
    userLogoLabel=Label(container,bg="black",width=10,height=5,bd=0)
    L1=Label(container,height=4,width=1,bg="#f04d4c",bd=0)
    L2=Label(container,height=1,width=6,bg="#f04d4c",bd=0)
    I=Label(container,height=2,width=1,bg="#f04d4c",bd=0)
    Bi=Label(container,height=6,width=1,bg="#13759a",bd=0)
    patchBi=Label(container,height=2,width=5,bg="#dbd8d8",bd=0)
    usernameLabel=Label(container,text="Username",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    studentIDLabel=Label(container,text="Student ID",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    passwordLabel=Label(container,text="Password",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    ageLabel=Label(container,text="Age",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    genderLabel=Label(container,text="Gender",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    emailLabel=Label(container,text="E-mail",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    membershipLabel=Label(container,text="Membership Interval",font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    usernameValue=Label(container,font=("gabriola",12),bd=0,fg="black",bg="#dbd8d8",width=15,text=profile[1],anchor="w")
    passwordValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=18,bg="#dbd8d8",text="*"*len(profile[2]),anchor="w")
    emailValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=25,bg="#dbd8d8",text=profile[5],anchor="w")
    ageValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=6,bg="#dbd8d8",text=profile[3],anchor="w")
    genderValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=10,bg="#dbd8d8",text=profile[4],anchor="w")
    studentIDValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=8,bg="#dbd8d8",text=profile[0],anchor="w")
    membershipValue=Label(container,font=("gabriola",12),bd=0,fg="black",width=20,bg="#dbd8d8",text=(profile[6]+" Month(s)\n"+timeFinder(profile[1])),anchor="w")
    bookButton.place(x=15,y=426,border=INSIDE)
    #editButton.place(x=263,y=15,border=INSIDE)
    userLogoLabel.place(x=15,y=15,border=INSIDE)
    L1.place(x=22,y=20,border=INSIDE)
    L2.place(x=22,y=65,border=INSIDE)
    I.place(x=52,y=30,border=INSIDE)
    Bi.place(x=70,y=15,border=INSIDE)
    patchBi.place(x=50,y=92,border=INSIDE)
    usernameLabel.place(x=10,y=110,border=INSIDE)
    usernameValue.place(x=10,y=125,border=INSIDE)
    studentIDLabel.place(x=140,y=110,border=INSIDE)
    studentIDValue.place(x=140,y=125,border=INSIDE)
    passwordLabel.place(x=10,y=160,border=INSIDE)
    passwordValue.place(x=10,y=175,border=INSIDE)
    ageLabel.place(x=10,y=210,border=INSIDE)
    ageValue.place(x=10,y=225,border=INSIDE)
    genderLabel.place(x=90,y=210,border=INSIDE)
    genderValue.place(x=90,y=225,border=INSIDE)
    emailLabel.place(x=10,y=260,border=INSIDE)
    emailValue.place(x=10,y=275,border=INSIDE)
    membershipLabel.place(x=10,y=310,border=INSIDE)
    membershipValue.place(x=10,y=325,border=INSIDE)
    container.place(x=15,y=15,border=INSIDE)
    profilePage.mainloop()
def profileFinder(username):
    profiles=open("IDs.txt")
    profileList=profiles.readlines()
    profiles.close()
    for value in profileList:
        profile=value.split(" ")
        if username==profile[0]:
            profilePageCreator(username)
