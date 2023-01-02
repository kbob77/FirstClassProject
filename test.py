from tkinter import *
t = (r'C:\Users\kelly\OneDrive\Documents\Whitworth class\FirstClassProject\test.txt')
root = Tk()
root.geometry("655x333")

root.title("Dinner Program")

def delete():
    dinnerentry.delete(0, 'end')
    typeentry.delete(0, 'end')
    ingrediententry.delete(0, 'end')
    prepentry.delete(0, 'end')

dinner = Label(root, text="Add Dinner: ")
type = Label(root, text="Type: ")
ingredients = Label(root, text="Ingredients: ")
prep = Label(root, text="Prep Time: ")
dinner.grid()
type.grid(row=1)
ingredients.grid(row=2)
prep.grid(row=3)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
def getvals():
  with open(t, "a") as f:
    f.write(f"{dinnervalue.get()}"+ ' ' )
    # f.write('\n')
    f.write(f"{typevalue.get()}"+ ' ')
    f.write(f"{ingredientsvalue.get()}"+ ' ')
    f.write(f"{prepvalue.get()}"+ ' ')


dinnervalue = StringVar()
typevalue = StringVar()
ingredientsvalue = StringVar()
prepvalue = StringVar()


dinnerentry = Entry(root, textvariable = dinnervalue)
typeentry = Entry(root, textvariable = typevalue)
ingrediententry = Entry(root, textvariable = ingredientsvalue)
prepentry = Entry(root, textvariable = prepvalue)

dinnerentry.grid(row=0, column=1)
typeentry.grid(row=1, column=1)
ingrediententry.grid(row=2, column=1)
prepentry.grid(row=3, column=1)

Button(text="Submit", command=getvals).grid()
Button(text="clear", command=delete).grid()
#mybutton = Button(root, text = "Delete", command = delete)
#Clear = Button(root,text="Clear", command=clear_text).pack()
##Button(text= "clear", command=clearToTextInput)
# btn=Button(win,height=1,width=10, text="Clear",command=clearToTextInput)
# btn.pack()

root.mainloop()