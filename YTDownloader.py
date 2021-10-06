from tkinter import *
from tkinter import messagebox
from pytube import YouTube


root = Tk()
root.geometry('550x300')
root.resizable(0, 0)
root.title("YT Downloader")
root.configure(background="#171717")
link = StringVar()


def search():
    try:
        yt = YouTube(str(link.get()))
        title = yt.title
        l5.config(text=(title[:47]+".."))
        views = yt.views
        l7.config(text="{:,}".format(views))
    except:
        messagebox.showwarning("Error", "Invalid Link")
        link_enter.delete(0, 'end')
        l5.config(text="")
        l7.config(text="")

def Download():
    try:
        yt = YouTube(str(link.get()))
        ys = yt.streams.first()
        ys.download()
        messagebox.showinfo("Done", "Successfully Download")
   
    except:
        messagebox.showwarning("Error", "Invalid Link")
        link_enter.delete(0, 'end')
    


icon = PhotoImage(file="icon.png")


root.iconphoto(False, icon)
l1 = Label(root, image=icon, bg="#171717")
l2 = Label(root, text="TESSA YT Downloader", bg="#171717",
           fg='#ffffff', font='arial 20 bold')

l1.grid(row=0, column=0, sticky=W, pady=2, ipadx='5px', ipady='5px')
l2.grid(row=0, column=1, sticky=W, pady=2, padx='15px')

l3 = Label(root, text="Enter URL", bg="#171717",
           fg='#ffffff', font='arial 10 bold')
l3.grid(row=1, column=0, sticky=W, pady=2,  ipadx='5px')

link_enter = Entry(root, width=50, textvariable=link)
link_enter.grid(row=1, column=1, sticky=W, pady=2, padx='15px')

search = Button(root, text="search", bg="#ffffff", fg="#171717",
                font='arial 10 bold', command=search, activebackground="#171717", activeforeground="#ffffff")
search.grid(row=1, column=2)


l4 = Label(root, text="Title", bg="#171717",
           fg='#ffffff', font='arial 10 bold')
l4.grid(row=2, column=0, sticky=W, pady=2,  ipadx='5px')

l5 = Label(root, text="", bg="#171717", fg='#ffffff', font='arial 10 bold')
l5.grid(row=2, column=1, sticky=W, pady=2, padx='15px')

l6 = Label(root, text="Views", bg="#171717",
           fg='#ffffff', font='arial 10 bold')
l6.grid(row=3, column=0, sticky=W, pady=2,  ipadx='5px')

l7 = Label(root, text="", bg="#171717", fg='#ffffff', font='arial 10 bold')
l7.grid(row=3, column=1, sticky=W, pady=2, padx='15px')

l8 = Label(root, text="Qualities", bg="#171717",
           fg='#ffffff', font='arial 10 bold')
l8.grid(row=4, column=0, sticky=W, pady=2,  ipadx='5px')


options = [
    ""
]

# Create Dropdown menu
drop = OptionMenu(root, "--", *options)
drop.grid(row=4, column=1, sticky=W, pady=2, padx='15px', ipady=2)


Download = Button(root, text="Downoad", bg="#b33f40",
                  fg="#ffffff", font='arial 10 bold', command=Download)
Download.grid(row=5, column=1, sticky=E, pady=2, padx='15px', ipady=2)


root.mainloop()
