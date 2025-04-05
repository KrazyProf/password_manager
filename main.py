from random import choice , randint , shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip , json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_entry.delete(0 , END)
        #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0 , password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try :
        with open('password.json' , 'r') as file:
            # reading the file
            data = json.load(file)  
    except :
        messagebox.showerror(title='Error' , message='No Data Found')
    
    else:
        try:
            email_pass = [value for (key,value) in data.items() if key == website]
            messagebox.showinfo(title="Details" , message=f"Email: {email_pass[0]['email']}\nPassword: {email_pass[0]['password']}")
        except:
            messagebox.showerror(title='Error' , message='No Details of the website exists.')

def save_pass():

    website = website_entry.get()
    email = email_entry.get()
    password =  password_entry.get()
    new_data = {
         website : {
              "email" : email,
              "password" : password
         }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error' , message = "Please don't leave fields empty")
    else:
        try:
            with open('password.json' , 'r') as file:
                # reading the file
                data = json.load(file)            
        except: 
            with open('password.json' , 'w') as file:
                json.dump(new_data , file , indent=4)
        else:
            # updating the file
            data.update(new_data)
            with open('password.json' , 'w') as file:
                # writing the data
                json.dump(data , file , indent=4)
          
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50 , pady=50)
window.title('Password Manager')


canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100 , 100 , image = img)
canvas.grid(column=1 ,row=0)

# Label 
website_label = Label(text='Website: ' , padx=1 , pady=1)
website_label.grid(column=0 ,row=1)

email_label = Label(text='Email: ', padx=1 , pady=1 )
email_label.grid(column=0 ,row=2)

password_label = Label(text='Password: ', padx=1 , pady=1)
password_label.grid(column=0 ,row=3)


# Entry
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1 ,row=1 , columnspan=1)

email_entry = Entry(width=53)
email_entry.insert(0 , 'ayushkaithwas860@gmail.com')
email_entry.grid(column=1 ,row=2 , columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1 ,row=3 , columnspan=1)


# Button
generate_pass = Button(text='Generate Password' , command=generate_pass)
generate_pass.grid(column=2 , row=3, columnspan=1)

add_btn = Button(text='Add' ,width=45 , command=save_pass)
add_btn.grid(column=1 , row=4 , columnspan=2)

search_btn = Button(text='Search' , width=14 , command=search)
search_btn.grid(column=2 , row=1 , columnspan=1)



window.mainloop()