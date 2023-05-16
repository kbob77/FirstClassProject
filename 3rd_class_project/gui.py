from PyQt6.QtWidgets import *
import mysql.connector


class mainwindow(QWidget):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(150, 150, 800, 400)
        self.setWindowTitle("Dinner Picker")

        labels = ['Add Dinner: ', 'Add Type: ', 'Add Ingredients: ', 'Add Preperation time: ']
        self.textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            # now add a label and a textbox,
            # and also hold the textbox in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addRow(l, txt)
            self.textboxes[l] = txt

        # finally, add a button
        b = QPushButton("Submit")
        b.clicked.connect(self.button_clicked)
        layout.addWidget(b)

        # Create a label, leave it empty, and add it to the bottom
        self.labelResult = QLabel()
        layout.addWidget(self.labelResult)

    def button_clicked(self):
        # get the dinner information entered by the user
        dinner = self.textboxes['Add Dinner: '].text()
        type = self.textboxes['Add Type: '].text()
        ingredients = self.textboxes['Add Ingredients: '].text()
        prep_time = self.textboxes['Add Preperation time: '].text()

        # connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Roze0806...",
            database="dinners"
        )
        cursor = cnx.cursor()

        # execute an INSERT statement to add the dinner information to a table in the database
        add_dinner = "CALL add_dinner(%s, %s, %s, %s)"
        data_dinner = (dinner, type, ingredients, prep_time)
        cursor.execute(add_dinner, data_dinner)

        # commit the changes to the database and close the connection
        cnx.commit()
        cursor.close()
        cnx.close()

        # update the label to show that the dinner information was added to the database
        self.labelResult.setText("Dinner information added to the database.")

        self.show()


def main():
    app = QApplication([])
    qss = open('cs100.qss')
    app.setStyleSheet(qss.read())
    w = mainwindow()
    w.show()
    app.exec()


if __name__ == '__main__':
    main()




# from PyQt6.QtWidgets import *
# import mysql.connector

# def button_clicked(self):
#     # get the dinner information entered by the user
#     dinner = self.textboxes['Add Dinner'].text()
#     type = self.textboxes['Add Type'].text()
#     ingredients = self.textboxes['Add Ingredients'].text()
#     preparation_time = self.textboxes['Add Preperation time'].text()

#     # connect to the MySQL database
    
#     cnx = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Roze0806...",
#         database="dinners"
#     )
#     cursor = cnx.cursor()

#     # execute an INSERT statement to add the dinner information to a table in the database
#     add_dinner = ("INSERT INTO dinners "
#                   "(dinner, type, ingredients, preparation_time) "
#                   "VALUES (%s, %s, %s, %s)")
#     data_dinner = (dinner, type, ingredients, preparation_time)
#     cursor.execute(add_dinner, data_dinner)

#     # commit the changes to the database and close the connection
#     cnx.commit()
#     cursor.close()
#     cnx.close()

#     # update the label to show that the dinner information was added to the database
#     self.labelResult.setText("Dinner information added to the database.")

#     self.show()


# class mainwindow(QWidget):
#     def __init__(self, parent = None):
#         super(mainwindow, self).__init__(parent)
#         self.setGeometry(150,150,800,400)
#         self.setWindowTitle("Dinner Picker")

#         labels = ['Add Dinner: ', 'Add Type: ', 'Add Ingredients: ', 'Add Preperation time: ']
#         self.textboxes = {}

#         layout = QFormLayout()
#         self.setLayout(layout)

#         for l in labels:
#             #now add a label and a textbox,
#             # and also hold the textbox in the dictionary so we can use it later
#             txt = QLineEdit()
#             layout.addRow(l, txt)
#             self.textboxes[l] = txt

#         #finally, add a button
#         b = QPushButton("Submit")
#         b.clicked.connect(self.button_clicked)
#         layout.addWidget(b)

#         #Create a label, leave it empty, and add it to the bottom
#         self.labelResult = QLabel()
#         layout.addWidget(self.labelResult)
    
#     def button_clicked(self):
#         self.labelResult.setText(self.textboxes['Add Dinner'].text())

#         self.show()
        


# def main():
#     app = QApplication([])
#     qss = open('cs100.qss')
#     app.setStyleSheet(qss.read())
#     w = mainwindow()
#     w.show()
#     app.exec()

# if __name__ == '__main__':
#     main()

