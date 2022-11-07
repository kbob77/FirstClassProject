from fileinput import close
import os

# dir_path = r'C:\users\kelly\onedrive\documents\whitworth class\class5\madlibs'

class Dinner:
    'Dinner Ideas'
    dinnercount = 0
    def __init__(self, name= '', type_of_food= '', ingredients = [], preperation_time = 'int'):
        self.name = name
        self.type_of_food = type_of_food
        self.ingredients = []
        self.preperation_time = ''
        Dinner.dinnercount += 1
        
    def __str__(self):
        return '\nDinner: ' + self.name +  '\t\t Type: ' + self.type_of_food + '\t \t Ingredients: '+ self.ingredients + ' \t\t Preperation time: '+ self.preperation_time + ' minutes' 
        
def getdinner(name):
    d = Dinner()
    d.name = name
    d.type_of_food = input ( "what type of food is it? IE.. mexican, italian etc..  ")
    d.ingredients = input ('what are the ingredients for this dinner? ')
    d.preperation_time = input ('what is the estimated preperation time in minutes? ')
    print(str(d)) 
    return d

dinnerlist = []

name = ''
while name != 'done':

    name = input ('Please add a Dinner or done to exit. ')

    if name != 'done':
        dinnerlist.append(getdinner(name))
        
for d in dinnerlist:
    print(str(d))




    f = open('dinners.txt', 'a')
    f.write(str(d))
    f.close()       





