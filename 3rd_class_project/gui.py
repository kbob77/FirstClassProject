from PyQt6.QtWidgets import *
import mysql.connector
import sys
from dotenv import load_dotenv
import os


class mainwindow(QWidget):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(150, 150, 800, 400)
        self.setWindowTitle("Dinner Picker")
        
        load_dotenv()

        labels = ['Add Dinner: ', 'Add Type: ', 'Add Ingredients: ', 'Add Preperation time: ']
        self.textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            txt = QLineEdit()
            layout.addRow(l, txt)
            self.textboxes[l] = txt

        # finally, add a button
        b = QPushButton("Submit")
        b.clicked.connect(self.button_clicked)
        layout.addWidget(b)
        
         # finally, add a button
        b = QPushButton("Pick Random Dinner")
        b.clicked.connect(self.pick_random_dinner)
        layout.addWidget(b)
        
         # Create an exit button
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_application)
        layout.addWidget(exit_button)

        # Create a label, leave it empty, and add it to the bottom
        self.labelResult = QLabel()
        layout.addWidget(self.labelResult)
        
    def exit_application(self):
         sys.exit()

    def button_clicked(self):
        
        # get the dinner information entered by the user
        dinner = self.textboxes['Add Dinner: '].text()
        type = self.textboxes['Add Type: '].text()
        ingredients = self.textboxes['Add Ingredients: '].text()
        prep_time = self.textboxes['Add Preperation time: '].text()
        
        if not dinner or not type or not ingredients or not prep_time:
            QMessageBox.warning(self, "Missing Information", "Please fill in all the fields.")
            return

        # connect to the MySQL database
        cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database= os.getenv("DB_NAME")
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

        # clear the form
        self.textboxes['Add Dinner: '].setText('')
        self.textboxes['Add Type: '].setText('')
        self.textboxes['Add Ingredients: '].setText('')
        self.textboxes['Add Preperation time: '].setText('')
          
    def pick_random_dinner(self):
        cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database= os.getenv("DB_NAME")
        )
        cursor = cnx.cursor()

        # Call the grab_dinner stored procedure
        cursor.callproc("grab_dinner")

        # Retrieve the result set from the stored procedure
        for result in cursor.stored_results():
            rows = result.fetchall()
            if rows:
                chosen_dinner = rows[0]  # Assuming the dinner is in the first row
                self.labelResult.setText(f"Here is the dinner we chose for you: {chosen_dinner}")
                break
            else:
                self.labelResult.setText("No dinner found in the database.")

        cursor.close()
        cnx.close()

def main():
    app = QApplication([])
    
    qss = open('cs100.qss')
    app.setStyleSheet(qss.read())
    w = mainwindow()
    w.show()
    app.exec()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
