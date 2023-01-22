from tkinter import *
from PIL import ImageTk, Image #PIL -> Pillow
import pymysql
import matplotlib as plt

from AddBook import *
from ViewBooks import *
from IssueBook import *
from DeleteBook import *
from ReturnBook import *

mypass = "root"
mydatabase="db" #The database name
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25
# Adding a background image
background_image = Image.open("lib.jpeg")

img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root, width=1600, height=900)


Canvas1.pack(expand=True, fill=BOTH)
Canvas1.create_image(0, 0, image=img, anchor='nw')
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("libb.jpeg")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   Canvas1.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
root.bind("<Configure>", resize_image)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Lambton College Library", bg='white', fg='black', font='Courier 18 bold')
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='white', fg='black', font='Courier 14 bold', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='white', fg='black', font='Courier 14 bold', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='white', fg='black', font='Courier 14 bold', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='white', font='Courier 14 bold', fg='black', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='white', fg='black', font='Courier 14 bold', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()