from tkinter import *
from tkinter import messagebox
import random

t = (r'F:\OneDrive\Documents\GitHub\FirstClassProject\test.txt')
root = Tk()
root.geometry("1100x333")

root.title("Dinner Program")

def randomDinner():
  # with open('test.txt') as d:
  #   rdin = [line.strip() for line in d]
  rdin = open('dinners.txt').read().splitlines()
  # result = random.choice(rdin)
  index = random.randint(0, len(rdin)-1)
  print(index)
  result = rdin[index]
  
  # random_dinner = Label(root, text=result)
  # random_dinner.grid(row=24)
  
  

def delete():
    dinnerentry.delete(0, 'end')
    typeentry.delete(0, 'end')
    ingrediententry.delete(0, 'end')
    prepentry.delete(0, 'end')

def option_selected(*args):
  print(selected.get())
  
pickdinner = Label(root, text="Would you like to pick from a list of dinners? ")
pickdinner.grid(row=1, columnspan=2)
selected = StringVar()   

with open('test.txt', 'r') as f:
  options = [line.strip() for line in f]
  
  
dropdown = OptionMenu(root, selected, *options)
dropdown.grid(row=1, column=2)
    

selected.trace("w", option_selected)

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
    messagebox.showerror('Error', 'All fields are required to add a dinner')
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

Button(text="Submit", command=getvals).grid(row=16, column=0)
Button(text="clear", command=delete).grid(row=16, column=1)


random = Label(root, text="Or would you like me to randomly pick a dinner for you???")
random.grid(row=20, columnspan=2)

Button(text="yes", command=randomDinner).grid(row=21, columnspan=2)


root.mainloop()