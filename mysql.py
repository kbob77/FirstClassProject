import pymysql

db = pymysql.connect(host='localhost', user='root', password='Roze0806...', database='northwind')
db.autocommit(True)
lname = input('give me a last name to search for: ')
sql = "select `first name`, `last name` from employees where `last name`='"+lname+"'"
crsr = db.cursor()
res = crsr.execute(sql)
for row in crsr:
    print(row[0] + ' ' + row[1])

crsr.close()
db.close()



# db = pymysql.connect(host='localhost', user='root', password='Roze0806...', database='northwind')
# db.autocommit(True)
# lname = input('give me a character to search for: ')
# sql = "select `first name`, `last name` from customers where `last name` like '%"+lname+"%'"
# print(sql)
# crsr = db.cursor()
# res = crsr.execute(sql)
# for row in crsr:
#     print(row[0] + ' ' + row[1])

# crsr.close()
# db.close()
crsr = None
db = None

# try:
#     db = pymysql.connect(host='localhost', user='root', password='Roze0806...', database='northwind')
#     db.autocommit(True)
#     input1 = input('Find products within a standard cost range 2 numbers: ')
#     input2 = input('input the second value: ')
#     sql = "call get_Standardcost_range(%s, %s)"
#     print(sql)
#     crsr = db.cursor()
#     res = crsr.execute(sql, [input1, input2])
#     for row in crsr:
#         print(row[0] + ' ' + row[1])
    
# except pymysql.Error as dberror:
#       (errcode, errmsg) = dberror.args
#       print(errmsg)
# except Exception as err:
#       print('some non-db error occurred' + str(err))
    
# print('almost done')


# if crsr is not None:
#   crsr.close()
# if db is not None:
#   db.close()

try:
    db = pymysql.connect(host='localhost', user='root', password='Roze0806...', database='northwind')
    db.autocommit(True)
    input1 = input('Find products within a standard cost range 2 numbers: ')
    input2 = input('input the second value: ')
    sql = "call get_Standardcost_range(%s, %s)"
    print(sql)
    crsr = db.cursor()
    res = crsr.execute(sql, [input1, input2])
    for row in crsr:
        print(row[0] + ' ' + row[1])
    
except pymysql.Error as dberror:
      (errcode, errmsg) = dberror.args
      print(errmsg)
except Exception as err:
      print('some non-db error occurred' + str(err))
    
print('almost done')


if crsr is not None:
  crsr.close()
if db is not None:
  db.close()