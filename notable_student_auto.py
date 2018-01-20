

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
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0,0,0);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
""))
        MainWindow.resize(999, 886)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pb_qod = QtGui.QPushButton(self.centralwidget)
        self.pb_qod.setGeometry(QtCore.QRect(0, -20, 511, 181))
        self.pb_qod.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop: 0 rgba( 85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"font: 28pt \"Candara\";"))
        self.pb_qod.setObjectName(_fromUtf8("pb_qod"))
        self.pb_fod = QtGui.QPushButton(self.centralwidget)
        self.pb_fod.setGeometry(QtCore.QRect(490, -20, 511, 181))
        self.pb_fod.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba( 85, 170, 255, 255), stop:0 rgba(255, 255, 255, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"font: 28pt \"Candara\";"))
        self.pb_fod.setObjectName(_fromUtf8("pb_fod"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 190, 331, 71))
        self.label.setStyleSheet(_fromUtf8("font: 75 28pt \"Candara\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"text-decoration: underline;\n"
"\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.notable_points = QtGui.QLCDNumber(self.centralwidget)
        self.notable_points.setGeometry(QtCore.QRect(540, 200, 151, 51))
        self.notable_points.setStyleSheet(_fromUtf8("color: rgb(0, 255, 255);"))
        self.notable_points.setObjectName(_fromUtf8("notable_points"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 170, 352, 201))
        self.calendarWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Candara\";"))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.tv_classlist = QtGui.QTableView(self.centralwidget)
        self.tv_classlist.setGeometry(QtCore.QRect(705, 210, 281, 511))
        self.tv_classlist.setObjectName(_fromUtf8("tv_classlist"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(780, 170, 141, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 16pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gv_latest_notes = QtGui.QGraphicsView(self.centralwidget)
        self.gv_latest_notes.setGeometry(QtCore.QRect(10, 380, 681, 341))
        self.gv_latest_notes.setObjectName(_fromUtf8("gv_latest_notes"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 340, 181, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Candara\";\n"
"color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 730, 981, 121))
        self.label_4.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop: 0 rgba( 85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(255, 255, 255);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 340, 111, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop: 0 rgba( 85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"font: 13pt \"Candara\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 750, 101, 81))
        self.pushButton_2.setStyleSheet(_fromUtf8("image: url(:/notable/Slide2.png);"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 750, 101, 81))
        self.pushButton_3.setStyleSheet(_fromUtf8("image: url(:/notable/Slide4.png);"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 750, 101, 81))
        self.pushButton_4.setStyleSheet(_fromUtf8("image: url(:/notable/Slide1.png);"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 750, 101, 81))
        self.pushButton_5.setStyleSheet(_fromUtf8("\n"
"image: url(:/notable/Slide3.png);"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Home Page", None))
        self.pb_qod.setText(_translate("MainWindow", "Question of the Day", None))
        self.pb_fod.setText(_translate("MainWindow", "Fact of the Day", None))
        self.label.setText(_translate("MainWindow", "Notable", None))
        self.label_2.setText(_translate("MainWindow", "Classmates :", None))
        self.label_3.setText(_translate("MainWindow", "Latest notes : ", None))
        self.pushButton.setText(_translate("MainWindow", "View More", None))

import try_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

