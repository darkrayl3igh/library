from tkinter import *
def bookCompiler(pN):
    intermediate=[]
    for value in pages[pN]:
        intermediate.append(value)
    for value in range(1,len(pages[pN]),40):
        change=value
        if intermediate[change-1]==" ":
            intermediate.insert(value,"\n")
        elif " " in intermediate[change-15:change]:
            for term in range(change-15,change):
                if intermediate[term]==" ":
                    intermediate[term]="\n"
                    break
    compiledPage=""
    for value in intermediate:
        compiledPage+=value
    return compiledPage
def bookWindow(book):
    global pageNumber,pages
    bookNameWindow.destroy()
    pageNumber=1
    book=open(book+".txt")
    pages=book.readlines()
    book.close()
    def pageChanger(key):
        global pageNumber
        if pageNumber==1:
            prevPageButton.config(state=DISABLED)
        if pageNumber==len(pages)-2:
            nextPageButton.config(state=DISABLED)
        if pageNumber<=len(pages)-1:
            if key=="next":
                prevPageButton.config(state=NORMAL)
                pageNumber+=1
            elif key=="prev" and pageNumber>0:
                nextPageButton.config(state=NORMAL)
                pageNumber-=1
        page.config(text=bookCompiler(pageNumber))
        pageNumberLabel.config(text="Page "+str(pageNumber))
    bookReader=Tk()
    bookReader.title(pages[0])
    bookReader.tk_setPalette(background="#f6f5f5")
    bookReader.geometry("350x400")
    container=Frame(bookReader,bg="#dbd8d8",width=320,height=370,bd=0)
    page=Label(container,text=bookCompiler(pageNumber),font="corbel 11",bd=0,fg="black",bg="#dbd8d8",justify="left")
    pageNumberLabel=Label(container,text="Page "+str(pageNumber),font="corbel 10 bold underline",bd=0,fg="black",bg="#dbd8d8",anchor="s")
    nextPageButton=Button(container,text=">",width=5,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:pageChanger("next"))
    prevPageButton=Button(container,text="<",width=5,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:pageChanger("prev"))
    page.place(x=15,y=20,border=INSIDE)
    pageNumberLabel.place(x=120,y=330,border=INSIDE)
    prevPageButton.place(x=15,y=326,border=INSIDE)
    nextPageButton.place(x=265,y=326,border=INSIDE)
    container.place(x=15,y=15,border=INSIDE)
    bookReader.mainloop()
def bookName():
    global bookNameWindow
    bookNameWindow=Tk()
    bookNameWindow.title("Choose a Book")
    bookNameWindow.tk_setPalette(background="#f6f5f5")
    bookNameWindow.geometry("350x150")
    containerbookName=Frame(bookNameWindow,bg="#dbd8d8",width=330,height=130,bd=0)
    questionLabel=Label(containerbookName,text="Please enter the name of the book",font="corbel 10",bd=0,fg="black",bg="#dbd8d8",width=40)
    answerEntry=Entry(containerbookName,font="corbel 10",bd=0)
    verifyButton=Button(containerbookName,text="Submit",width=9,bd=0,bg="#f04d4c",font="corbel 11 bold",fg="white",command=lambda:bookWindow(answerEntry.get()))
    containerbookName.place(x=10,y=10,border=INSIDE)
    questionLabel.place(x=20,y=20,border=INSIDE)
    answerEntry.place(x=90,y=45,border=INSIDE)
    verifyButton.place(x=125,y=70,border=INSIDE)
    bookNameWindow.mainloop()
