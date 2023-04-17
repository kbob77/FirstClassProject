import pymysql
from random import randint
import random

crsr = None
db = None

def random_dinner():
    db = pymysql.connect(host='localhost', user ='root', password="Roze0806...",database='dinners')
    db.autocommit(True)
  
    crsr = db.cursor()

    sql = "call grab_dinner()"
    res = crsr.execute(sql)
    print(f"Executed SQL: {sql}")
    print(f"Number of rows returned: {res}")
    
    while True:
        random_input = input("Would you like to pick a dinner randomly? (y/n): ")
        if random_input.lower() == 'y':
            num = random.randint(0, num_rows - 1)
            break
        elif random_input.lower() == 'n':
            while True:
                try:
                    num = int(input(f"Please enter a number between 0 and {num_rows-1}: "))
                    if 0 <= num < num_rows:
                        break
                    else:
                        print(f"Please enter a number between 0 and {num_rows-1}")
                except ValueError:
                    print("Please enter a valid number")
            break
        else:
            print("Please enter 'y' or 'n'")


    # num_rows = crsr.fetchone()[0]
    # print(f"Number of rows: {num_rows}")

    # num = random.randint(0, num_rows - 1)
    # print(f"Selected row index: {num}")

    sql = "call grab_dinner(%s)"
    print(sql)
    crsr = db.cursor()
    res = crsr.execute(sql, [num])
    print(f"Executed SQL: {sql}")
    print(f"Number of rows returned: {res}")

    for row in crsr:
        print('Dinner:' + ' ' + row[0] + ' ' + '  Type:' + ' ' + row[1]+ ' ' + '  Ingredients:' + ' '  + row[2]+ ', ' +  '  Prep Time:' + ' '  + str(int(row[3])) + ' minutes' )

    if crsr is not None:
        crsr.close()
    if db is not None:
        db.close()

    random_dinner()


# def random_dinner():
  
#   db = pymysql.connect(host='localhost', user ='root', password="Roze0806...",database='dinners')
#   db.autocommit(True)
  
#   crsr = db.cursor()


#   num = 0
#   sql = "call grab_dinner(%s)"
#   res = crsr.execute(sql, [num])
#   num_rows = crsr.fetchone()[0]
#   # sql = "call grab_dinner(%s)"
#   # res = crsr.execute(sql)
#   # num_rows = crsr.fetchone()[0]
  

  
#   num = random.randint(0, num_rows - 1)
  
#   sql = "call grab_dinner(%s)"
#   print(sql)
#   crsr = db.cursor()
#   res = crsr.execute(sql, [num])
#   for row in crsr:
#     print('Dinner:' + ' ' + row[0] + ' ' + '  Type:' + ' ' + row[1]+ ' ' + '  Ingredients:' + ' '  + row[2]+ ', ' +  '  Prep Time:' + ' '  + str(int(row[3])) + ' minutes' )
  
#   # sql = "call grab_dinner(%s)"
#   # print(sql)
#   # crsr = db.cursor()
#   # res = crsr.execute(sql, [num])
#   # for row in crsr:
#   #     print('Dinner:' + ' ' + row[0] + ' ' + '  Type:' + ' ' + row[1]+ ' ' + '  Ingredients:' + ' '  + row[2]+ ', ' +  '  Prep Time:' + ' '  + str(int(row[3])) + ' minutes' )
# if crsr is not None:
#     crsr.close()
# if db is not None:
#     db.close()
    
# # num = input("input a number: ")
# random_dinner()





def add_dinner(dinner_name, dinner_type, dinner_ingredients, dinner_prep):
  db = pymysql.connect(host='localhost', user ='root', password="Roze0806...",database='dinners')
  db.autocommit(True)
  
  sql = "call add_dinner(%s, %s, %s, %s)"
  # print(sql)
  crsr = db.cursor()
  res = crsr.execute(sql, [dinner_name, dinner_type, dinner_ingredients, dinner_prep])
  for row in crsr:
    print(row[0] + ' ' + row[1])
  print('almost done')
  if crsr is not None:
    crsr.close()
  if db is not None:
    db.close()
    
dinner_name = input('Input the name of a dinner:  ')
dinner_type = input('input the Type of Food: ')
dinner_ingredients = input('Input the ingredients:  ')
dinner_prep = input('Input the Prep time:  ')
add_dinner(dinner_name, dinner_type, dinner_ingredients, dinner_prep)


def get_dinner_details(dinner_name):
  db = pymysql.connect(host='localhost', user='root', password='Roze0806...', database='dinners')
  db.autocommit(True)
  
  sql = "select `dinner`, `type`, `ingredients`, `prep_time` from dinners where `dinner`='"+dinner_name+"'"
  crsr = db.cursor()
  res = crsr.execute(sql)
  for row in crsr:
      print('Dinner:' + ' ' + row[0] + ' ' + '  Type:' + ' ' + row[1]+ ' ' + '  Ingredients:' + ' '  + row[2]+ ', ' +  '  Prep Time:' + ' '  + str(int(row[3])) + ' minutes' )

  crsr.close()
  db.close()
  
dinner_name = input('Dinner you are looking for: ')
get_dinner_details(dinner_name)
