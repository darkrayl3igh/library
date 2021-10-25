from tkinter import *
import profilePage as PP
import tkMessageBox
def profileEditor(username):
    profiles=open("Profiles.txt")
    profileList=profiles.readlines()
    profiles.close()
    for Entry in  profileList:
        profile=Entry.split(" ")
        if username==profile[1]:
            break
    profilePageEdit=Tk()
    profilePageEdit.title("Edit Profile")
    profilePageEdit.tk_setPalette(background="#f6f5f5")
    profilePageEdit.geometry("400x600")
    profilePageEdit.mainloop()
def validifierFunc(username,password):
    profiles=open("Profiles.txt")
    profileList=profiles.readlines()
    profiles.close()
    for value in  profileList:
        profile=value.split(" ")
        if username==profile[1]:
            break
    if password==profile[2]:
        validifierWindow.destroy()
        PP.profilePage.destroy()
        profileEditor(username)
    else:
        tkMessageBox.showerror("Verification Falied","Password is incorrect")
        answerEntry.delete(0, END)
def validifier(user):
    global validifierWindow,answerEntry
    validifierWindow=Tk()
    validifierWindow.title("Verify account")
    validifierWindow.tk_setPalette(background="#f6f5f5")
    validifierWindow.geometry("350x150")
    containerValidifier=Frame(validifierWindow,bg="#dbd8d8",width=330,height=130,bd=0)
    questionLabel=Label(containerValidifier,text="Please verify your account by entering your password",font="corbel 10",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    answerEntry=Entry(containerValidifier,font="corbel 10",bd=0,show="*")
    verifyButton=Button(containerValidifier,text="Verify",width=9,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:validifierFunc(user,answerEntry.get()))
    containerValidifier.place(x=10,y=10,border=INSIDE)
    questionLabel.place(x=20,y=20,border=INSIDE)
    answerEntry.place(x=90,y=45,border=INSIDE)
    verifyButton.place(x=125,y=70,border=INSIDE)
    validifierWindow.mainloop()
