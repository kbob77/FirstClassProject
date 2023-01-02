from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(150,150,800,400)
        self.setWindowTitle("Dinner Picker")

        labels = ['Add Dinner: ', 'Add Type: ', 'Add Ingredients: ', 'Add Preperation time: ']
        textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            #now add a label and a textbox,
            # and also hold the textbox in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addRow(l, txt)
            textboxes[l] = txt

        #finally, add a button
        b = QPushButton("Submit")
        b.clicked.connect(self.button_clicked)
        layout.addWidget(b)

        #Create a label, leave it empty, and add it to the bottom
        self.labelResult = QLabel()
        layout.addWidget(self.labelResult)
    
    def button_clicked(self):
        self.labelResult.setText(self.textboxes['Add Dinner'].text())

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

