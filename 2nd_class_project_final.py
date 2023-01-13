from tkinter import *
import tkinter.messagebox
import customtkinter
import random
from tkinter import filedialog

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue") 

t = (r'F:\OneDrive\Documents\GitHub\FirstClassProject\dinners.txt')
root = customtkinter.CTk()
root.geometry("1350x333")
root.title("Dinner Program")

def quit_program():
    root.quit()

def randomDinner():
  rdin = open('test.txt').read().splitlines()
  index = random.randint(0, len(rdin)-1)
  result = rdin[index]
  
  random_dinner = Label(root, text=result)
  random_dinner.grid(row=24, columnspan=3)
  
  add_to_file = tkinter.messagebox.askyesno('Add to file', 'Do you want to add this dinner to a new text file?')
  if add_to_file:
    file_name = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_name, 'w') as d:
      d.write(result)
      d.write('\n')

def delete():
    dinnerentry.delete(0, 'end')
    typeentry.delete(0, 'end')
    ingrediententry.delete(0, 'end')
    prepentry.delete(0, 'end')

def dinner_selected(*args):
  add_to_file = tkinter.messagebox.askyesno('Add to file', 'Would you like to add this dinner to a new text file?')
  if add_to_file:
    file_name = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_name, 'w') as d:
      d.write(selected.get())
      d.write('\n')  



pickdinner = Label(root, text="Would you like to pick from a list of dinners? ")
pickdinner.grid(row=1, columnspan=2)
selected = StringVar() 
 

with open('test.txt', 'r') as f:
  options = [line.strip() for line in f]
  
selected.set("Dinner options") 

dropdown = OptionMenu(root, selected, *options )
dropdown.config(width=135)
dropdown.grid(row=1, column=2)
selected.trace("w", dinner_selected)

space = Label(root, text="            ")
space.grid(row=3)

Question1 = Label(root, text=" Or would you like to add a dinner to the List? ")
Question1.grid(row=10, columnspan=2)
dinner = Label(root, text="Add Dinner: ")
type = Label(root, text="Type: ")
ingredients = Label(root, text="Ingredients: ")
prep = Label(root, text="Prep Time: ")

dinner.grid(row=11)
type.grid(row=12)
ingredients.grid(row=13)
prep.grid(row=14)


def getvals():
  if not dinnervalue.get() or not typevalue.get() or not ingredientsvalue.get() or not prepvalue.get():
    tkinter.messagebox.showerror('Error', 'All fields are required to add a dinner')
  else:
    with open(t, "a") as f:
      f.write('\n')
      f.write("Dinner: " + f"{dinnervalue.get()}" + '\t\t ' )
      f.write("\t\t Type: 'Type: " + f"{typevalue.get()}" )
      f.write("\t\t Type: 'Ingredients: " + f"{ingredientsvalue.get()}" )
      f.write("\t\t Type: 'Prep time: " + f"{prepvalue.get()}" + " Minutes" )


dinnervalue = StringVar()
typevalue = StringVar()
ingredientsvalue = StringVar()
prepvalue = StringVar()


dinnerentry = Entry(root, textvariable = dinnervalue)
typeentry = Entry(root, textvariable = typevalue)
ingrediententry = Entry(root, textvariable = ingredientsvalue)
prepentry = Entry(root, textvariable = prepvalue)

dinnerentry.grid(row=11, column=1)
typeentry.grid(row=12, column=1)
ingrediententry.grid(row=13, column=1)
prepentry.grid(row=14, column=1)

Button1 = customtkinter.CTkButton(master=root, text="Submit", command=getvals).grid(row=16, column=0)
Button2 = customtkinter.CTkButton(master=root, text="Clear", command=getvals).grid(row=16, column=1)

space = Label(root, text="")
space.grid(row=18, columnspan=2)


randomdin = Label(root, text="Or would you like me to randomly pick a dinner for you? or Exit?")
randomdin.grid(row=20, columnspan=2)
Button3 = customtkinter.CTkButton(master=root, text="yes", command=randomDinner).grid(row=21, columnspan=1)

Button4 = customtkinter.CTkButton(master=root, text="Exit", command=quit_program).grid(row=21, column=1)



Button5 = customtkinter.CTkButton(master=root, text="All Done", command=quit_program).grid(row=25, columnspan=2)


root.mainloop()