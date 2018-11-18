# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 
import userWindow
import assests.images

class Ui_MainWindow(object):
    name = 'Friend'
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def welcomeBackWindowShow(self):
        self.welcomeBackWindow = QtWidgets.QMainWindow()
        self.ui = userWindow.Ui_MainWindow()
        self.ui.setupUi(self.welcomeBackWindow)
        self.welcomeBackWindow.show()
    def loginCheck(self):
        loginEmail = self.login_email_lineEdit.text()
        loginPassword = self.login_password_lineEdit.text()
      
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE EMAIL = ? AND PASSWORD = ?",(loginEmail,loginPassword))
        ##find the number of rows of users, if they exist 
        allUserInfo = result.fetchall()
        print(allUserInfo)
        if (len(allUserInfo) > 0):
            print("User Found!")
            global name
            name = allUserInfo[0][0]
            self.welcomeBackWindowShow()
        else:
            print("User Not Found!")
            if (loginEmail == '' or loginPassword == ''):
                self.showMessageBox('Warning','Please enter something')
            else:
                self.showMessageBox('Warning','Email or Password entered is incorrect')
        connection.close()
            
    def insertNewUserData(self):
        newName = self.name_lineEdit.text()
        newEmail = self.register_email_lineEdit.text()
        newPassword = self.register_password_lineEdit.text()
        confirmPass = self.register_confirmPassword_lineEdit.text()
        if (newName == '' or newEmail == '' or newPassword == '' or confirmPass == ''):
            self.showMessageBox('Warning','Please enter something')
        connection = sqlite3.connect("login.db")
        ## You need to pass in a sequence, but you forgot the comma to make your parameters a tuple. <Github> or use [newEmail] instead of comma
        ## Without comma it is just a grouped expression.
        checkEmail = connection.execute("SELECT * FROM USERS WHERE EMAIL = ?", (newEmail,))
        if ((str(newPassword) == str(confirmPass)) and len(checkEmail.fetchall()) == 0):
            connection.execute("INSERT INTO USERS VALUES (?,?,?)",(newName,newEmail,newPassword))
            connection.commit()
            self.showMessageBox("Registration Sucessful","Congratulations! Please Login to continue.")
        elif(len(checkEmail.fetchall()) > 0):  
            self.showMessageBox("Warning","Email already registered! Please Login.")
        else:
            self.showMessageBox("Warning","Passwords don't match. Please enter passwords again.")
        connection.close()    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 786)
        MainWindow.setStyleSheet("color: white;\n""background-color: rgb(170, 180, 200)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.login_groupBox.setGeometry(QtCore.QRect(810, 30, 311, 191))
        self.login_groupBox.setStyleSheet("background-color: rgb(0, 85, 127)")
        self.login_groupBox.setObjectName("login_groupBox")
        self.login_email_label = QtWidgets.QLabel(self.login_groupBox)
        self.login_email_label.setGeometry(QtCore.QRect(20, 40, 41, 16))
        self.login_email_label.setObjectName("login_email_label")
        self.login_password_label = QtWidgets.QLabel(self.login_groupBox)
        self.login_password_label.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.login_password_label.setObjectName("login_password_label")
        self.login_email_lineEdit = QtWidgets.QLineEdit(self.login_groupBox)
        self.login_email_lineEdit.setGeometry(QtCore.QRect(90, 40, 181, 22))
        self.login_email_lineEdit.setObjectName("login_email_lineEdit")
        self.login_password_lineEdit = QtWidgets.QLineEdit(self.login_groupBox)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(90, 90, 181, 22))
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.login_pushButton = QtWidgets.QPushButton(self.login_groupBox)
        self.login_pushButton.setGeometry(QtCore.QRect(110, 130, 93, 28))
        self.login_pushButton.setObjectName("login_pushButton")
        ### LOGIN BUTTON EVENT by vr97
        self.login_pushButton.clicked.connect(self.loginCheck)
        ###        
        self.register_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.register_groupBox.setGeometry(QtCore.QRect(810, 320, 311, 301))
        self.register_groupBox.setStyleSheet("background-color:rgb(0, 85, 127);")
        self.register_groupBox.setObjectName("register_groupBox")
        self.name_label = QtWidgets.QLabel(self.register_groupBox)
        self.name_label.setGeometry(QtCore.QRect(20, 40, 41, 20))
        self.name_label.setObjectName("name_label")
        self.register_email_label = QtWidgets.QLabel(self.register_groupBox)
        self.register_email_label.setGeometry(QtCore.QRect(20, 90, 41, 21))
        self.register_email_label.setObjectName("register_email_label")
        self.register_password_label = QtWidgets.QLabel(self.register_groupBox)
        self.register_password_label.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.register_password_label.setObjectName("register_password_label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.register_groupBox)
        self.name_lineEdit.setGeometry(QtCore.QRect(90, 40, 181, 22))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.register_email_lineEdit = QtWidgets.QLineEdit(self.register_groupBox)
        self.register_email_lineEdit.setGeometry(QtCore.QRect(90, 90, 181, 22))
        self.register_email_lineEdit.setObjectName("register_email_lineEdit")
        self.register_password_lineEdit = QtWidgets.QLineEdit(self.register_groupBox)
        self.register_password_lineEdit.setGeometry(QtCore.QRect(90, 140, 181, 22))
        self.register_password_lineEdit.setObjectName("register_password_lineEdit")
        self.register_confirmPassword_label = QtWidgets.QLabel(self.register_groupBox)
        self.register_confirmPassword_label.setGeometry(QtCore.QRect(20, 180, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.register_confirmPassword_label.setFont(font)
        self.register_confirmPassword_label.setObjectName("register_confirmPassword_label")
        self.register_confirmPassword_lineEdit = QtWidgets.QLineEdit(self.register_groupBox)
        self.register_confirmPassword_lineEdit.setGeometry(QtCore.QRect(90, 190, 181, 22))
        self.register_confirmPassword_lineEdit.setObjectName("register_confirmPassword_lineEdit")
        self.register_pushButton = QtWidgets.QPushButton(self.register_groupBox)
        self.register_pushButton.setGeometry(QtCore.QRect(110, 240, 93, 28))
        self.register_pushButton.setObjectName("register_pushButton")
        ### REGISTER BUTTON EVENT by vr97
        self.register_pushButton.clicked.connect(self.insertNewUserData)
        ###
        self.Or_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.Or_groupbox.setGeometry(QtCore.QRect(950, 260, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Or_groupbox.setFont(font)
        self.Or_groupbox.setStyleSheet("color:black")
        self.Or_groupbox.setObjectName("Or_groupbox")
        self.contactUs_label = QtWidgets.QLabel(self.centralwidget)
        self.contactUs_label.setGeometry(QtCore.QRect(550, 665, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.contactUs_label.setFont(font)
        self.contactUs_label.setStyleSheet("color:black;\n""")
        self.contactUs_label.setObjectName("contactUs_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(190, 380, 431, 101))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color:black;")
        self.title_label.setObjectName("title_label")
        self.icon_label = QtWidgets.QLabel(self.centralwidget)
        self.icon_label.setGeometry(QtCore.QRect(100, 360, 81, 101))
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap(":/assests/shopbag.png"))
        self.icon_label.setObjectName("icon_label")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(140, 40, 511, 291))
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap(":/assests/image1.png"))
        self.image_label.setObjectName("image_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 710, 51, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 710, 301, 51))
        self.label_3.setObjectName("label_3")
        self.subtitle_label = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_label.setGeometry(QtCore.QRect(360, 480, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle_label.setFont(font)
        self.subtitle_label.setStyleSheet("color:black;\n""")
        self.subtitle_label.setObjectName("subtitle_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WELCOME TO FASHIONISTA"))
        self.login_groupBox.setTitle(_translate("MainWindow", "Welcome back Fashionista!"))
        self.login_email_label.setText(_translate("MainWindow", "Email"))
        self.login_password_label.setText(_translate("MainWindow", "Password"))
        self.login_pushButton.setText(_translate("MainWindow", "Login"))
        self.register_groupBox.setTitle(_translate("MainWindow", "Join our family"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.register_email_label.setText(_translate("MainWindow", "Email"))
        self.register_password_label.setText(_translate("MainWindow", "Password"))
        self.register_confirmPassword_label.setText(_translate("MainWindow", "<html><head/><body><p>Confirm </p><p>Password</p></body></html>"))
        self.register_pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.Or_groupbox.setTitle(_translate("MainWindow", "OR"))
        self.contactUs_label.setText(_translate("MainWindow", "Follow Us"))
        self.title_label.setText(_translate("MainWindow", "FASHIONISTA !"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/fb.png\"/><img src=\":/assests/twitter.png\"/><img src=\":/assests/insta.png\"/><img src=\":/assests/youtube.png\"/><img src=\":/assests/snap.png\"/><img src=\":/assests/googlePlus.png\"/></p></body></html>"))
        self.subtitle_label.setText(_translate("MainWindow", "<html><head/><body><p>IT\'S SHOPPING TIME!</p></body></html>"))

#import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

