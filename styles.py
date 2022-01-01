from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

## Overides PyQT5 widgets 

class MLineEdit(QLineEdit):
    def __init__(self,parent,x,y):
        super(MLineEdit,self).__init__(parent)
        self.setGeometry(x,y,300,60)
        self.setStyleSheet(
                        # "background-color: rgb(99,153 ,1);"
                        "selection-background-color: rgb(71,129,185);"
                        "Font: italic 'Times New Roman' ;"
                        "font-size:30px;"
                        "font-family: 'Times New Roman', Symbola, serif;"
                        "focus { border: 2px solid #006080;}")

class MLineEdit2(QLineEdit):
    def __init__(self,parent,x,y):
        super(MLineEdit2,self).__init__(parent)
        self.setGeometry(x,y,60,40)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet(
                        # "background-color: rgb(99,153 ,1);"
                        "selection-background-color: rgb(71,129,185);"
                        "Font:  'Times New Roman' ;"
                        "font-size:20px;"
                        "font-family: 'Times New Roman', Symbola, serif;"
                        "focus { border: 2px solid #006080;}")




class MLabel(QLabel):

    def __init__(self,text,parent,x,y):
        super(MLabel,self).__init__(parent)
        self.setGeometry(x,y,60,60)
        self.setText(text)
        self.setStyleSheet(
                        # "background-color: rgb(99,153 ,1);"
                        "color: rgb(71,129,185);"
                        "Font: Bold italic ;"
                        "font-size:30px;"
                        "font-family: 'Times New Roman', Symbola, serif;")



class MLabel2(QLabel):

    def __init__(self,text,parent,x,y):
        super(MLabel2,self).__init__(parent)
        self.setGeometry(x,y,180,60)
        self.setText(text)
        self.setStyleSheet(
                        # "background-color: rgb(99,153 ,1);"
                        "color: rgb(71,129,185);"
                        "Font: normal ;"
                        "font-size:20px;"
                        "font-family: 'Times New Roman', Symbola, serif;")




class MPushButton(QPushButton):
    def __init__(self,parent):
        super(MPushButton,self).__init__(parent)
        # img=QIcon(QPixmap("R.png"))
        # self.setIcon(img)
        # self.setIconSize(QSize(100,100))
        self.setText("Plot")
        self.setGeometry(200,600,80,50)
        self.setStyleSheet("QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 rgb(185,185,185));"
                                "border-style: solid;"
                               "border-color: rgb(71,129,185);"
                                "border-width: 2px;"
                               " border-radius: 10px;"
                               "Font: normal ;"
                                "font-size:20px;"
                                "font-family: 'Times New Roman', Symbola, serif;}"
                                )

        # img=QIcon(QPixmap("R.png"))
        # self.setIcon(img)
        # self.setIconSize(QSize(100,100))
        
