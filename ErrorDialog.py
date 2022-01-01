
from PyQt5.QtWidgets import QMessageBox

class Error(QMessageBox):
    def __init__(self,text) :
        super(Error,self).__init__()
        self.setWindowTitle("Error")
        self.setText(text)
        self.setIcon(QMessageBox.Critical)
        self.setStyleSheet(
                        # "background-color: rgb(99,153 ,1);"
                        "Font:  'Times New Roman' ;"
                        "font-size:20px;"
                        )

        self.exec_()