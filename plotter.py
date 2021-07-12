from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np
import random
import matplotlib.pyplot as plt
from sympy import var
from sympy import sympify

def nameError(self):
    QMessageBox.warning(self, "Name Error", "Please use variable x when entering the function")

def syntaxError(self):
    QMessageBox.warning(self, "Syntax Error", "Multiplication has to have *  i.e. 5*x not 5x")

def error(self):
    QMessageBox.warning(self, "Error", "Please Enter a Valid Input")

class pltWidget(QWidget):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)    

class MainWidget(QWidget):
    
    def __init__(self):
        
        QWidget.__init__(self)

        designer_file = QFile("funcplt_gui.ui")
        designer_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        loader.registerCustomWidget(pltWidget)
        self.ui = loader.load(designer_file, self)

        designer_file.close()

        self.ui.plot.clicked.connect(self.plot_graph)

        self.setWindowTitle("Function Plotter")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)


    def plot_graph(self):
        try:
            y = []
            list = []
            x = var('x')

    
            func_input = self.ui.lineEdit.text()                        #taking the function as input through the lineEdit widget
            func_input = func_input.replace("e^","exp")
            func_input = func_input.replace("e**","exp")
            expr = sympify(func_input)                  #lib to transform any equation from string format to math format 

            x_min = self.ui.lineEdit_2.text()
            x_min = float(x_min)
            
            x_max = self.ui.lineEdit_3.text()
            x_max = float(x_max)

            list = np.linspace(x_min,x_max , 100)        

            for i in list:                      #substituting in the equation to get the y-values
                res = expr.subs(x, i)
                y.append(res)
            
            self.ui.pltWidget.canvas.axes.clear()
            self.ui.pltWidget.canvas.axes.plot(list,y)
            self.ui.pltWidget.canvas.draw()
            

        except NameError:
            self.nameError()            #handling name errors
             
        
        except SyntaxError:
            self.syntaxError()          #handling syntax errors

        except:
            self.error()                #handling any other kind of errors


        
    


            
        

app = QApplication([])
window = MainWidget()
window.show()
app.exec_()