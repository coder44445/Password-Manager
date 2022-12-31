from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwfun():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    charlist = [random.choice(letters) for char in range(nr_letters)]

    sylist = [random.choice(symbols) for char in range(nr_symbols)]

    numlis =[random.choice(numbers) for char in range(nr_numbers)]


    password_list = charlist+sylist+numlis
    random.shuffle(password_list)
    passwinput.insert(0,''.join(password_list))
    pyperclip.copy(f"{''.join(password_list)}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saves():
    if len(websinput.get()) ==0 or len(passwinput.get()) ==0 :
        messagebox.showinfo(title="Nooooo..",message="Empty field Detected")
    else:   
        yes_or_no = messagebox.askyesno(title="Is it ok to save",message=f"Website: {websinput.get()}\nEmail/username: {emailinput.get()}\nPassword: {passwinput.get()}")
        if yes_or_no:
            new_data ={ 
            websinput.get():{
                "Email":emailinput.get(),
                "Password":passwinput.get()
                }
            }
            try:
                with open("savepass.json",mode="r") as savefile: 
                    data = json.load(fp = savefile)
                    data.update(new_data)
            except FileNotFoundError :
                with open("savepass.json",mode="w") as savefile:
                    json.dump(new_data,fp= savefile,indent=4)
            else:
                with open("savepass.json",mode="w") as savefile:
                    json.dump(data,fp= savefile,indent=4)

            websinput.delete(0,END)
            passwinput.delete(0,END)
def find_password():
    website = websinput.get()
    try:
        with open("savepass.json") as file:
            creds = json.load(file)
            if website in creds:
                messagebox.showinfo(title="Credentials",message= f"Email: { creds[website]['Email'] }\nPassword: {creds[website]['Password']}")
            else:
                messagebox.showerror(title="Error",message="website not Found.Enter correctly")
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data found")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
lockimage = PhotoImage(file="enter your file path")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image = lockimage)
canvas.grid(row= 0,column= 1)
webs = Label(text="Websites:-")
webs.grid(row=1,column=0)
websinput = Entry(width=32)
websinput.focus()
websinput.grid(row=1,column=1)
searchbutton = Button(text="Search",width=14,command=find_password)
searchbutton.grid(row=1,column=2,columnspan=1)
email = Label(text="Email/Username:-")
email.grid(row=2,column=0)
emailinput = Entry(width=50)
emailinput.insert(END,"@gmail.com")
emailinput.grid(row=2,column=1,columnspan=2)
passw = Label(text="Password:-")
passw.grid(row=3,column=0)
passwinput = Entry(width=32)
passwinput.grid(row=3,column=1,columnspan=1)
gpbutton = Button(text="Generate Password",width=14,command=passwfun)
gpbutton.grid(row=3,column=2,columnspan=1)
addbutton = Button(text="Add",width=43,command=saves)
addbutton.grid(row=5,column=1,columnspan=2)
window.mainloop()