from fileinput import close
import os
import random
from PyQt6.QtWidgets import *


    

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
#function to get new dinner Item for dinners.txt       
def getdinner(name):
    d = Dinner()
    d.name = name
    d.type_of_food = input ( "what type of food is it? IE.. mexican, italian etc..  ")
    d.ingredients = input ('what are the ingredients for this dinner? ')
    d.preperation_time = input ('what is the estimated preperation time in minutes? ')
    print(str(d)) 
    return d

dinnerlist = []
#adding a dinner to the list
name = ''
while name != 'done':
    name = input ('Would you like to add a dinner or type done to exit. ')
    if name != 'done':
        dinnerlist.append(getdinner(name))
        
for d in dinnerlist:
    print(str(d))
    f = open('dinners.txt', 'a')
    f.write(str(d))
    f.close()  
    
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']
    
# Random dinner picker from the dinners.txt file     
while True:
    r = input("Would you like me to randomly pick a dinner for you, type yes or no ? ").lower()
    if r.lower() in yes_choices:
        rdin = open('dinners.txt').read().splitlines()
        result = random.choice(rdin)
        print('Here is a good idea for dinner : \n' + '\t' + result)
        break
    elif r.lower() in no_choices:
        l = input("would you like a list of dinners printed out? type yes/no: ")
        if l.lower() in yes_choices:
                rdin = open('dinners.txt').read()
                print(rdin)
        else:
            print('Ok maybe next time')
        break
    else :
        print('type yes or no')
        continue


    

