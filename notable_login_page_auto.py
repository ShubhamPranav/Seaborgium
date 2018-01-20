# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notable_login_page.ui'
#
# Created: Sat Jan 20 14:38:04 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(998, 834)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 981, 281))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(330, 10, 351, 81))
        self.label.setStyleSheet(_fromUtf8("font: 38pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(600, 80, 71, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(170, 170, 255);\n"
"font: 11pt \"Candara\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(380, 150, 251, 61))
        self.label_3.setStyleSheet(_fromUtf8("font: 30pt \"Candara\";\n"
"background-color: rgb(255, 151, 23);\n"
"\n"
"color: rgb(255, 255, 255);\n"
""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(650, 150, 91, 61))
        self.label_8.setStyleSheet(_fromUtf8("image: url(:/notable/Slide2.png);"))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 311, 251))
        self.label_9.setStyleSheet(_fromUtf8("image: url(:/ /element_106_sg_seSeaborgium.jpg);"))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 511, 511))
        self.groupBox_2.setStyleSheet(_fromUtf8("font: 20pt \"Candara\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 151, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 151, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 151, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.rb_student = QtGui.QRadioButton(self.groupBox_2)
        self.rb_student.setGeometry(QtCore.QRect(40, 380, 171, 31))
        self.rb_student.setObjectName(_fromUtf8("rb_student"))
        self.rb_teacher = QtGui.QRadioButton(self.groupBox_2)
        self.rb_teacher.setGeometry(QtCore.QRect(280, 380, 171, 31))
        self.rb_teacher.setObjectName(_fromUtf8("rb_teacher"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 151, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pb_sign_in = QtGui.QPushButton(self.groupBox_2)
        self.pb_sign_in.setGeometry(QtCore.QRect(320, 440, 151, 51))
        self.pb_sign_in.setStyleSheet(_fromUtf8("background-color: rgb(255, 151, 23);\n"
""))
        self.pb_sign_in.setObjectName(_fromUtf8("pb_sign_in"))
        self.lne_name = QtGui.QLineEdit(self.groupBox_2)
        self.lne_name.setGeometry(QtCore.QRect(180, 60, 291, 41))
        self.lne_name.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.lne_name.setObjectName(_fromUtf8("lne_name"))
        self.lne_class = QtGui.QLineEdit(self.groupBox_2)
        self.lne_class.setGeometry(QtCore.QRect(180, 220, 291, 41))
        self.lne_class.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.lne_class.setObjectName(_fromUtf8("lne_class"))
        self.lne_password = QtGui.QLineEdit(self.groupBox_2)
        self.lne_password.setGeometry(QtCore.QRect(180, 140, 291, 41))
        self.lne_password.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.lne_password.setObjectName(_fromUtf8("lne_password"))
        self.lne_school = QtGui.QLineEdit(self.groupBox_2)
        self.lne_school.setGeometry(QtCore.QRect(180, 290, 291, 41))
        self.lne_school.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.lne_school.setObjectName(_fromUtf8("lne_school"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(540, 290, 451, 511))
        self.groupBox_3.setStyleSheet(_fromUtf8("font: 20pt \"Candara\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pb_student = QtGui.QPushButton(self.groupBox_3)
        self.pb_student.setGeometry(QtCore.QRect(80, 120, 291, 91))
        self.pb_student.setStyleSheet(_fromUtf8("background-color: rgb(255, 151, 23);\n"
""))
        self.pb_student.setObjectName(_fromUtf8("pb_student"))
        self.pb_teacher = QtGui.QPushButton(self.groupBox_3)
        self.pb_teacher.setGeometry(QtCore.QRect(80, 310, 291, 91))
        self.pb_teacher.setStyleSheet(_fromUtf8("background-color: rgb(255, 151, 23);\n"
""))
        self.pb_teacher.setObjectName(_fromUtf8("pb_teacher"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(180, 40, 151, 41))
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
""))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Seaborgium", None))
        self.label_2.setText(_translate("MainWindow", "Presents", None))
        self.label_3.setText(_translate("MainWindow", "    Notable", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Login", None))
        self.label_4.setText(_translate("MainWindow", "Name:", None))
        self.label_5.setText(_translate("MainWindow", "Password:", None))
        self.label_6.setText(_translate("MainWindow", "Class:", None))
        self.rb_student.setText(_translate("MainWindow", "Student", None))
        self.rb_teacher.setText(_translate("MainWindow", "Teacher", None))
        self.label_7.setText(_translate("MainWindow", "School:", None))
        self.pb_sign_in.setText(_translate("MainWindow", "Sign In", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sign Up", None))
        self.pb_student.setText(_translate("MainWindow", "Student", None))
        self.pb_teacher.setText(_translate("MainWindow", "Teacher", None))

import try_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

