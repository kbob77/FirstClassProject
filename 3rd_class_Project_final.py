from tkinter import *
import tkinter.messagebox
import customtkinter
import random
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk


customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue") 
bold_font = ('times', 12, 'bold')

t = 'dinners.txt'
root = customtkinter.CTk()
root.geometry("1450x533")
root.title("Dinner Program")


class Dinner:
    dinnercount = 0
    def __init__(self, name= '', type_of_food= '', ingredients = [], preperation_time = ''):
        self.name = name
        self.type_of_food = type_of_food
        self.ingredients = ingredients
        self.preperation_time = preperation_time
        
        Dinner.dinnercount += 1
        
        def __str__(self):
          return 'Dinner: ' + self.name +  '\tType: ' + self.type_of_food + '\tIngredients: '+ ', '.join(self.ingredients) + ' \tPreperation time: '+ str(self.preperation_time) + ' minutes'
dinners = []
with open('dinners.txt', 'r') as f:
    for dinner in dinners:
        f.write('Dinner: ' + dinner.name +  '\t\t Type: ' + dinner.type_of_food + '\t\t Ingredients: '+ ', '.join(dinner.ingredients) + ' \t\t Prep time: '+ str(dinner.preperation_time) + ' Minutes' )


def quit_program():
    root.quit()

def randomDinner():
  with open('dinners.txt', 'r') as f:
    dinners = list(line.strip() for line in f)
  if len(dinners) > 0:
    index = random.randint(0, len(dinners)-1)
    result = str(dinners[index])
    random_dinner = Label(root, text='Here is the Dinner I chose for you:  ' + result, font=bold_font)
    random_dinner.grid(row=24, columnspan=3)
    add_to_file = tkinter.messagebox.askyesno('Add to file', 'Do you want to add this dinner to a new text file?')
    if add_to_file:
        file_name = filedialog.asksaveasfilename(defaultextension='.txt')
        with open(file_name, 'w') as d:
            d.write(result)
            d.write('\n')
  else:
    print("No dinners available")


def delete():
    dinnerentry.delete(0, 'end')
    typeentry.delete(0, 'end')
    ingrediententry.delete(0, 'end')
    prepentry.delete(0, 'end')

def dinner_selected(*args):
  selected_dinner = selected.get()
  selected_dinner = None
  for dinner in dinners:
    if dinner.name == selected_dinner:
        selected_dinner = dinner
  add_to_file = tkinter.messagebox.askyesno('Add to file', 'Would you like to add this dinner to a new text file?')
  if add_to_file:
    file_name = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_name, 'r') as d:
      d.write(str(selected_dinner))
      d.write('\n')


pickdinner = Label(root, text="Would you like to pick from a list of dinners? " ,  font=bold_font)
pickdinner.grid(row=1, columnspan=2)
selected = StringVar() 
 

with open('dinners.txt', 'r') as f:
 options = list(line.strip() for line in f)
  

selected = StringVar()
selected.set("Dinner options") 

dropdown = OptionMenu(root, selected, *options )
dropdown.config(width=135)
dropdown.grid(row=1, column=2)
selected.trace("w", dinner_selected)

space = Label(root, text="            ")
space.grid(row=3)

Question1 = Label(root, text=" Or would you like to add a dinner to the List? " , font=bold_font)
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
      f.write("\t\t Type: " + f"{typevalue.get()}" )
      f.write("\t\t Ingredients: " + f"{ingredientsvalue.get()}" )
      f.write("\t\t Prep time: " + f"{prepvalue.get()}" + " Minutes" )


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
Button2 = customtkinter.CTkButton(master=root, text="Clear", command=delete).grid(row=16, column=1)

space = Label(root, text="")
space.grid(row=18, columnspan=2)


randomdin = Label(root, text="Or would you like me to randomly pick a dinner for you? or Exit? ",  font=bold_font)
randomdin.grid(row=20, columnspan=2)
Button3 = customtkinter.CTkButton(master=root, text="yes", command=randomDinner).grid(row=21, columnspan=1)

Button4 = customtkinter.CTkButton(master=root, text="Exit", command=quit_program).grid(row=21, column=1)



Button5 = customtkinter.CTkButton(master=root, text="All Done", command=quit_program).grid(row=25, columnspan=2)


root.mainloop()