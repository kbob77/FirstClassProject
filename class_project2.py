from fileinput import close
import os

dir_path = r'C:\users\kelly\onedrive\documents\whitworth class\class5\madlibs'

class Dinner:
    'Dinner Ideas'
    dinnercount = 0
    def __init__(self, name= '', type_of_food= '', ingredients = [], preperation_time = 'int'):
        self.name = name
        self.type_of_food = type_of_food
        self.ingredients = []
        self.preperation_time = ''
        
        Dinner.dinnercount += 1
        
def displaydinner(self):
    print('Name of Dinner ', self.name, "type ", self.type_of_food, 'Ingredients ',  self.Ingredients)
        
        
d = Dinner()


def getdinner(d):
    d.name = input ('what is the name of the Dinner: ')
    d.type_of_food = input ( "what type of food is it? IE.. mexican, italian etc..  ")
    d.ingredients = input ('what are the ingredients for this dinner? ')
    d.preperation_time = input ('what is the estimated preperation time in minutes? ')
    print('You entered this dinner: ',  d.name +  ', Type of food: ' + d.type_of_food + ', the ingredients '+ d.ingredients + ', Preperation time: '+ d.preperation_time + ' minutes') 

#displaydinner(d)


# z = getdinner(d)
# f = open('dinners.txt', 'w')
# f.write('Dinner: '+ str(d.name)+'\t'+'Type: '+str(d.type_of_food+'\t'+'Ingredients: '+str(d.ingredients)+'\t'+'Preperation Time: '+str(d.preperation_time)+ ' minutes') )
# f.close()

files = os.listdir()
if 'dinners.txt' not in files:
    l = getdinner(d)
    f = open('dinners.txt', 'w')
    
    while l != 'done':
        f.write('Dinner: '+ str(d.name)+'\t'+'Type: '+str(d.type_of_food+'\t'+'Ingredients: '+str(d.ingredients)+'\t'+'Preperation Time: '+str(d.preperation_time)+ ' minutes') )
        l = input('would you like to add another dinner? type done to exit')
    f.close()

# files = os.listdir()
# # filename = dinnerlist.txt
# # f= open(filename, 'a' )
# if 'dinners.txt' not in files:
#     gd = getdinner(d)
#     f = open('dinners.txt', 'w')
#     while gd != 'done':
#         f.write(gd + '\n')
#         gd = input("Did you want to add another dinner or done to exit ")
#     f.close()
# # f = open(filename, 'a')
# # f.write(d.name +  '\t ' )
# # f.write(d.type_of_food + " \t" )
# # f.write(d.ingredients + "\t" )
# # msg = ''
# # while msg != 'done':
# #     msg = input('give me a message, or done to exit: ')
# #     if msg != 'done':
# #         f.write(d.name)
# # f.close()

# f = open('dinners.txt', 'r')
# lineno=1
# for line in f:
#     print(str(lineno) + ": " + line)
#     lineno = lineno+1
# f.close()

