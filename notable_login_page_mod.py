import sys
import os
import sqlite3
from PyQt4 import QtCore, QtGui, uic


     

from notable_login_page_auto import *


class MyClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pb_sign_in.clicked.connect(self.pb_sign_in_clicked)
        self.conn = sqlite3.connect('Notable.db')

    def pb_sign_in_clicked(self):
        
            text = self.lne_name.text()    
            cursor = self.conn.cursor()
            cursor.execute("SELECT password, notablepoints, student from users where name = '"+ text +"'")
            row = cursor.fetchall()
            print(row)
            for i in row :
                password, notablepoints, student = i
                a = password
            
            if a == self.lne_password.text():
           
                details = MyWindowClass(self)
                details.show()
                










import sys
import os
import sqlite3
from PyQt4 import QtCore, QtGui, uic
from notable_student_auto import *



class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.conn = sqlite3.connect('Notable.db')








app = QtGui.QApplication(sys.argv)
MainWindow = MyClass(None)
MainWindow.show()
app.exec_()


app = QtGui.QApplication(sys.argv)
MainWindow = MyWindowClass(None)
MainWindow.show()
app.exec_()                
            
                

     
