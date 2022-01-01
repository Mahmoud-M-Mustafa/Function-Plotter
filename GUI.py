import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
from input_checker import Validator
from PlotCanvas import *
import sip
from styles import *
from ErrorDialog import Error


class GUI(QMainWindow):
    def __init__(self):
        # setiing the main window
        super(GUI,self).__init__()
        self.setGeometry(400,200,2000,1300)
        self.setWindowTitle("Plotter")
        self.initUI()
    

    def initUI(self):
      
        self.setStyleSheet("QMainWindow {background: '#f1f1f1';}")
     
        
        self.label=MLabel("F(x)",self,25,50)
        self.labe2=MLabel2("x minimum",self,25,190)
        self.labe2=MLabel2("x maximum",self,25,290)


        self.min_x=MLineEdit2(self,125,200)
        self.max_x=MLineEdit2(self,125,300)

        self.function=MLineEdit(self,100,50)
        self.function.textChanged.connect(self.onChanged)

        self.b1=MPushButton(self)
        self.b1.clicked.connect(self.clicked)


        self.sc = MplCanvas( width=5, height=10, dpi=100)
        self.toolbar =MplCanvas( width=5, height=10, dpi=100)

        self.layout = QVBoxLayout()
        

        # Create a placeholder widget to hold our toolbar and canvas.
        self.widget = QWidget(self)
        self.widget.setLayout(self.layout)
        self.widget.setGeometry(QRect(500,10,800,800))
        self.layout.addWidget(self.sc)
        


        





    

    def clicked(self):
        """
        function definition: Plot Button Event triggered function

        validates user input 
            return if user input  incorrect
        otherwise
            plots user entered function

        """
        v=Validator()
        
        if(v.inp_x(self.min_x.text()) == False and \
           v.inp_x(self.max_x.text()) == False):

            Error('Please enter a valid Range for x ')
            return

        
        if(v.inp_x(self.min_x.text())==False):
            Error('Please enter a valid minimum x value')
            return
   
        if(v.inp_x(self.max_x.text())==False):
            Error('Please enter a valid Maximum x value')
            return


        coeffs=v.function_check(self.function.text())
        if(coeffs):
            self.plot(self.min_x.text(),self.max_x.text(),coeffs)
        else:
            Error("Please type a valid F(x) \t\t \n ex: 5*x^3+24*x+2")



    def plot(self,min_x,max_x,coeffs):
        """
            plots using matplotlib and numpy 
        """
        if(coeffs and min_x and max_x):
            x = np.linspace(float(min_x),float(max_x),50)
            y=0.0

            # y=F(X)= coeff * x ** power
            for k,v in coeffs.items():
                y += v*x**int(k)
        
            # removing widget to re-plot them
            self.layout.removeWidget(self.sc)
            self.layout.removeWidget(self.toolbar)

            sip.delete(self.sc)
            sip.delete(self.toolbar)
            self.sc = MplCanvas( width=5, height=4, dpi=150)
            self.toolbar = NavigationToolbar(self.sc, self)
            self.sc.ax.plot(x,y)
            self.layout.addWidget(self.toolbar)
            self.layout.addWidget(self.sc)


    def onChanged(self):
        """
            Event triggered function when Edittext is changed 
            validates the input every change in text
             --> valid input changes label color to green
             --> invalid input changes label color to red
        """
        v=Validator()
        coeffs=v.function_check(self.function.text()) 
        if(coeffs):
            self.label.setStyleSheet("color:rgb(99,153 ,1);"
                        "Font: italic Bold;"
                        "font-size:30px;"
                        "font-family: 'Times New Roman', Symbola, serif;")
        else:
            self.label.setStyleSheet("color: #cd1d18;"
                        "Font: italic Bold;"
                        "font-size:30px;"
                        "font-family: 'Times New Roman', Symbola, serif;")
        
        if self.function.text()=="":
            self.label.setStyleSheet("color: rgb(71,129,185);"
                        "Font: italic Bold;"
                        "font-size:30px;"
                        "font-family: 'Times New Roman', Symbola, serif;")
               


############################## END OF GUI #################################

def  main():
    app=QApplication(sys.argv)
    win=GUI()    
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()