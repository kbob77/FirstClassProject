import pickle



class Dinner:
    'Dinner Ideas'
    dinnercount = 0
    def __init__(self) :
        self.name = input ('what is the name of the Dinner: ')
        self.type_of_food = input ( "what type of food is it? IE.. mexican, italian etc..  ")
        self.Ingredients = input ('what are the ingredients for this dinner? ')
        self.preperation_time = input ('what is the estimated preperation time? ')
        
        Dinner.dinnercount += 1
        
    def displaydinner(self):
        print('Name of Dinner ', self.name, "type ", self.type_of_food, 'Ingredients ',  self.Ingredients)
        
       
    
    
    
    # name = ''
    # type_of_food = ''
    # Ingredients = []
    # Preperation_time = -1
    
    
d = Dinner()

d.name = 'Pizza'
d.type_of_food = 'italian'
d.Ingredients = {"dough", "suace", "mozzarella cheese", "pepperoni"}
d.Preperation_time = 45


print(d.Ingredients)

d2 = Dinner('Taco\'s', 'Mexican', {'taco shell', "taco meat", 'salsa', 'cheese'}, 35)
d3 = Dinner('Spaghetti', 'Italian', {'Spaghetti noodles', 'spaghetti sauce', 'Meatballs', 'parmesan cheese', 'garlic bread'}, 25)
d4 = Dinner('Fried Rice', 'Asian', {'cooked rice', 'carrots', 'green onions', 'soy sauce', 'fried egg'}, 40)


print(d2.name, d2.Ingredients)

#d2.save(d2.name)
#save
# with open(f'Dinners', 'wb') as file:
#     pickle.dump(d, file)
#  #load   
# with open(f'Dinners', 'rb') as file2:
#     d_new = pickle.load(file2)
print('total number of dinners: ', Dinner.dinnercount)

# print(d.name, d.Ingredients)


import os

filename = input('what filename should I write to? ')
if '.' not in filename:
    filename = filename + '.txt'

f = open(filename, 'w')
f.write('# this is python code\n')
msg = ''
while msg != 'done':
    msg = input('give me a message, or done to exit: ')
    if msg != 'done':
        f.write('print("' + msg + '")\n')
f.close()

f = open(filename, 'r')
lineno=1
for line in f:
    print(str(lineno) + ": " + line)
    lineno = lineno+1
f.close()

import os

files = os.listdir()
if 'groceries.txt' not in files:
    item = input("let's go to the store. What do we need? ")
    f = open('groceries.txt', 'w')
    #get items from the user, and close the file when they type done
    while item != 'done':
        f.write(item + '\n')
        item = input("What else do we need? Type 'done' to quit. ")
    f.close()

print("Let's go shopping!")
# keep track of whether we need to go to another store
storeTrip = True
while storeTrip == True:
    newList = []
    f = open('groceries.txt', 'r')
    for item in f:
        # we need the strip() function here to remove the newline character
        # at the end of item
        found = input('did you find ' + item.strip() + '? (y or n) ')
        if found == 'n':
            # keep track of the items not found at the store for a new list
            newList.append(item.strip())
    f.close()
    storeTrip = len(newList) > 0
    if storeTrip == True:
        #ugh, we have to keep shopping
        print("Let's go to another store.")
        # overwrite the groceries text file
        f = open('groceries.txt', 'w')
        # for each item note found yet, put them in the grocery file
        for item in newList:
            f.write(item + '\n')
        f.close()
print('Whew! We are done!')

f = open('madlibtest.txt', 'r')
#start with an empty string to store the story
story = ''
for line in f:
    if line.startswith('*'):
        #prompt the user for this thing.
        # Remove the *, and strip the whitespace
        text = input('Give me a(n) ' + line[1:].strip() + ': ')
    else:
        #just store the item
        text = line

    #whatever we have in text, add it to story
    story = story + ' ' + text.strip()

#now that we've built the story, let's read it
print("here's your story\n")
print(story)

f.close()

f = open('madlibstory.txt', 'w')
f.write(story)
f.close()
