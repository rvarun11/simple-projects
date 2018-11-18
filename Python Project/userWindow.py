# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import assests.images
import homepage
import purchaseDialog

class Ui_MainWindow (object):
        
    def buyNowClicked(self):
        self.purchaseWindow = QtWidgets.QDialog()
        self.ui = purchaseDialog.Ui_Dialog()
        self.ui.setupUi(self.purchaseWindow)
        self.purchaseWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.title_horizontalFrame.setGeometry(QtCore.QRect(0, 0, 1241, 141))
        self.title_horizontalFrame.setAutoFillBackground(False)
        self.title_horizontalFrame.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.title_horizontalFrame.setObjectName("title_horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_label = QtWidgets.QLabel(self.title_horizontalFrame)
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout.addWidget(self.icon_label)
        self.welcomeBack_label = QtWidgets.QLabel(self.title_horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeBack_label.setFont(font)
        self.welcomeBack_label.setStyleSheet("color: white")
        self.welcomeBack_label.setObjectName("welcomeBack_label")
        self.horizontalLayout.addWidget(self.welcomeBack_label)
        self.ourProducts_label = QtWidgets.QLabel(self.centralwidget)
        self.ourProducts_label.setGeometry(QtCore.QRect(0, 140, 1241, 101))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ourProducts_label.setFont(font)
        self.ourProducts_label.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.ourProducts_label.setObjectName("ourProducts_label")
        self.products_Frame = QtWidgets.QFrame(self.centralwidget)
        self.products_Frame.setGeometry(QtCore.QRect(0, 240, 1231, 661))
        self.products_Frame.setAutoFillBackground(False)
        self.products_Frame.setStyleSheet("background-color: rgba(0, 170, 255, 20)")
        self.products_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.products_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.products_Frame.setObjectName("products_Frame")
        self.widget = QtWidgets.QWidget(self.products_Frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1221, 651))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.prod_groupBox = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox.setTitle("")
        self.prod_groupBox.setObjectName("prod_groupBox")
        self.pImage_label = QtWidgets.QLabel(self.prod_groupBox)
        self.pImage_label.setGeometry(QtCore.QRect(12, 30, 231, 171))
        self.pImage_label.setObjectName("pImage_label")
        self.widget1 = QtWidgets.QWidget(self.prod_groupBox)
        self.widget1.setGeometry(QtCore.QRect(0, 200, 254, 91))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pName_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label.setFont(font)
        self.pName_label.setObjectName("pName_label")
        self.verticalLayout.addWidget(self.pName_label)
        self.pDesc_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label.setFont(font)
        self.pDesc_label.setObjectName("pDesc_label")
        self.verticalLayout.addWidget(self.pDesc_label)
        self.buy_pushButton = QtWidgets.QPushButton(self.widget1)
        self.buy_pushButton.setObjectName("buy_pushButton")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout.addWidget(self.buy_pushButton)
        self.gridLayout.addWidget(self.prod_groupBox, 0, 0, 1, 1)
        self.prod_groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_2.setTitle("")
        self.prod_groupBox_2.setObjectName("prod_groupBox_2")
        self.pImage_label_2 = QtWidgets.QLabel(self.prod_groupBox_2)
        self.pImage_label_2.setGeometry(QtCore.QRect(12, 30, 231, 171))
        self.pImage_label_2.setObjectName("pImage_label_2")
        self.layoutWidget = QtWidgets.QWidget(self.prod_groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 200, 241, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pName_label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_2.setFont(font)
        self.pName_label_2.setObjectName("pName_label_2")
        self.verticalLayout_2.addWidget(self.pName_label_2)
        self.pDesc_label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_2.setFont(font)
        self.pDesc_label_2.setObjectName("pDesc_label_2")
        self.verticalLayout_2.addWidget(self.pDesc_label_2)
        self.buy_pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.buy_pushButton_2.setObjectName("buy_pushButton_2")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_2.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_2.addWidget(self.buy_pushButton_2)
        self.gridLayout.addWidget(self.prod_groupBox_2, 0, 1, 1, 1)
        self.prod_groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_4.setTitle("")
        self.prod_groupBox_4.setObjectName("prod_groupBox_4")
        self.pImage_label_4 = QtWidgets.QLabel(self.prod_groupBox_4)
        self.pImage_label_4.setGeometry(QtCore.QRect(20, 10, 191, 191))
        self.pImage_label_4.setObjectName("pImage_label_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.prod_groupBox_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 200, 241, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pName_label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pName_label_5.setFont(font)
        self.pName_label_5.setObjectName("pName_label_5")
        self.verticalLayout_4.addWidget(self.pName_label_5)
        self.pDesc_label_5q = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_5q.setFont(font)
        self.pDesc_label_5q.setObjectName("pDesc_label_5q")
        self.verticalLayout_4.addWidget(self.pDesc_label_5q)
        self.buy_pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buy_pushButton_4.setObjectName("buy_pushButton_4")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_4.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_4.addWidget(self.buy_pushButton_4)
        self.gridLayout.addWidget(self.prod_groupBox_4, 0, 4, 1, 1)
        self.prod_groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_5.setTitle("")
        self.prod_groupBox_5.setObjectName("prod_groupBox_5")
        self.pImage_label_6 = QtWidgets.QLabel(self.prod_groupBox_5)
        self.pImage_label_6.setGeometry(QtCore.QRect(12, 30, 231, 171))
        self.pImage_label_6.setObjectName("pImage_label_6")
        self.layoutWidget_5 = QtWidgets.QWidget(self.prod_groupBox_5)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pName_label_6 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_6.setFont(font)
        self.pName_label_6.setObjectName("pName_label_6")
        self.verticalLayout_6.addWidget(self.pName_label_6)
        self.pDesc_label_6 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_6.setFont(font)
        self.pDesc_label_6.setObjectName("pDesc_label_6")
        self.verticalLayout_6.addWidget(self.pDesc_label_6)
        self.buy_pushButton_6 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.buy_pushButton_6.setObjectName("buy_pushButton_6")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_6.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_6.addWidget(self.buy_pushButton_6)
        self.gridLayout.addWidget(self.prod_groupBox_5, 1, 0, 1, 1)
        self.prod_groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_7.setTitle("")
        self.prod_groupBox_7.setObjectName("prod_groupBox_7")
        self.pImage_label_8 = QtWidgets.QLabel(self.prod_groupBox_7)
        self.pImage_label_8.setGeometry(QtCore.QRect(40, 30, 161, 171))
        self.pImage_label_8.setObjectName("pImage_label_8")
        self.layoutWidget_7 = QtWidgets.QWidget(self.prod_groupBox_7)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pName_label_9 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_9.setFont(font)
        self.pName_label_9.setObjectName("pName_label_9")
        self.verticalLayout_8.addWidget(self.pName_label_9)
        self.pDesc_label_9 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_9.setFont(font)
        self.pDesc_label_9.setObjectName("pDesc_label_9")
        self.verticalLayout_8.addWidget(self.pDesc_label_9)
        self.buy_pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.buy_pushButton_8.setObjectName("buy_pushButton_8")
        self.verticalLayout_8.addWidget(self.buy_pushButton_8)
        self.gridLayout.addWidget(self.prod_groupBox_7, 1, 3, 1, 1)
        self.prod_groupBox_8 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_8.setTitle("")
        self.prod_groupBox_8.setObjectName("prod_groupBox_8")
        self.pImage_label_9 = QtWidgets.QLabel(self.prod_groupBox_8)
        self.pImage_label_9.setGeometry(QtCore.QRect(12, 30, 231, 171))
        self.pImage_label_9.setObjectName("pImage_label_9")
        self.layoutWidget_8 = QtWidgets.QWidget(self.prod_groupBox_8)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pName_label_10 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_10.setFont(font)
        self.pName_label_10.setObjectName("pName_label_10")
        self.verticalLayout_9.addWidget(self.pName_label_10)
        self.pDesc_label_10 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_10.setFont(font)
        self.pDesc_label_10.setObjectName("pDesc_label_10")
        self.verticalLayout_9.addWidget(self.pDesc_label_10)
        self.buy_pushButton_9 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.buy_pushButton_9.setObjectName("buy_pushButton_9")
        self.verticalLayout_9.addWidget(self.buy_pushButton_9)
        self.gridLayout.addWidget(self.prod_groupBox_8, 1, 4, 1, 1)
        self.prod_groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_3.setTitle("")
        self.prod_groupBox_3.setObjectName("prod_groupBox_3")
        self.pImage_label_3 = QtWidgets.QLabel(self.prod_groupBox_3)
        self.pImage_label_3.setGeometry(QtCore.QRect(12, 30, 231, 171))
        self.pImage_label_3.setObjectName("pImage_label_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.prod_groupBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pName_label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_3.setFont(font)
        self.pName_label_3.setObjectName("pName_label_3")
        self.verticalLayout_3.addWidget(self.pName_label_3)
        self.pDesc_label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_3.setFont(font)
        self.pDesc_label_3.setObjectName("pDesc_label_3")
        self.verticalLayout_3.addWidget(self.pDesc_label_3)
        self.buy_pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buy_pushButton_3.setObjectName("buy_pushButton_3")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_3.clicked.connect(self.buyNowClicked)
        ###
        
        self.verticalLayout_3.addWidget(self.buy_pushButton_3)
        self.gridLayout.addWidget(self.prod_groupBox_3, 0, 2, 1, 1)
        self.prod_groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_9.setTitle("")
        self.prod_groupBox_9.setObjectName("prod_groupBox_9")
        self.pImage_label_10 = QtWidgets.QLabel(self.prod_groupBox_9)
        self.pImage_label_10.setGeometry(QtCore.QRect(30, 20, 181, 171))
        self.pImage_label_10.setObjectName("pImage_label_10")
        self.layoutWidget_9 = QtWidgets.QWidget(self.prod_groupBox_9)
        self.layoutWidget_9.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pName_label_4 = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_4.setFont(font)
        self.pName_label_4.setObjectName("pName_label_4")
        self.verticalLayout_10.addWidget(self.pName_label_4)
        self.pDesc_label_4 = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_4.setFont(font)
        self.pDesc_label_4.setObjectName("pDesc_label_4")
        self.verticalLayout_10.addWidget(self.pDesc_label_4)
        self.buy_pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_9)
        self.buy_pushButton_10.setObjectName("buy_pushButton_10")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_10.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_10.addWidget(self.buy_pushButton_10)
        self.gridLayout.addWidget(self.prod_groupBox_9, 0, 3, 1, 1)
        self.prod_groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_6.setTitle("")
        self.prod_groupBox_6.setObjectName("prod_groupBox_6")
        self.pImage_label_7 = QtWidgets.QLabel(self.prod_groupBox_6)
        self.pImage_label_7.setGeometry(QtCore.QRect(30, 30, 171, 161))
        self.pImage_label_7.setObjectName("pImage_label_7")
        self.layoutWidget_6 = QtWidgets.QWidget(self.prod_groupBox_6)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pName_label_7 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_7.setFont(font)
        self.pName_label_7.setObjectName("pName_label_7")
        self.verticalLayout_7.addWidget(self.pName_label_7)
        self.pDesc_label_7 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pDesc_label_7.setFont(font)
        self.pDesc_label_7.setObjectName("pDesc_label_7")
        self.verticalLayout_7.addWidget(self.pDesc_label_7)
        self.buy_pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.buy_pushButton_7.setObjectName("buy_pushButton_7")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_7.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_7.addWidget(self.buy_pushButton_7)
        self.gridLayout.addWidget(self.prod_groupBox_6, 1, 1, 1, 1)
        self.prod_groupBox_10 = QtWidgets.QGroupBox(self.widget)
        self.prod_groupBox_10.setTitle("")
        self.prod_groupBox_10.setObjectName("prod_groupBox_10")
        self.pImage_label_11 = QtWidgets.QLabel(self.prod_groupBox_10)
        self.pImage_label_11.setGeometry(QtCore.QRect(40, 20, 161, 171))
        self.pImage_label_11.setObjectName("pImage_label_11")
        self.layoutWidget_10 = QtWidgets.QWidget(self.prod_groupBox_10)
        self.layoutWidget_10.setGeometry(QtCore.QRect(0, 200, 251, 91))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pName_label_8 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pName_label_8.setFont(font)
        self.pName_label_8.setObjectName("pName_label_8")
        self.verticalLayout_11.addWidget(self.pName_label_8)
        self.pDesc_label_8 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pDesc_label_8.setFont(font)
        self.pDesc_label_8.setObjectName("pDesc_label_8")
        self.verticalLayout_11.addWidget(self.pDesc_label_8)
        self.buy_pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_10)
        self.buy_pushButton_11.setObjectName("buy_pushButton_11")
        
        ### PUSH BUTTON EVENT by vr97
        self.buy_pushButton_11.clicked.connect(self.buyNowClicked)
        ###  
        
        self.verticalLayout_11.addWidget(self.buy_pushButton_11)
        self.gridLayout.addWidget(self.prod_groupBox_10, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        ## PRODUCTS INFOS
        connection = sqlite3.connect("productsInfo.db")
        results = connection.execute("SELECT * FROM PRODUCTS")
        allInfo = results.fetchall()
        ###
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.icon_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/assests/shopbag.png\"/></p></body></html>"))
        self.welcomeBack_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WELCOME BACK, " + homepage.Ui_MainWindow.name + "</p></body></html>"))
        self.ourProducts_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OUR PRODUCTS</p></body></html>"))
        self.pImage_label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p1.png\"/></p></body></html>"))
        self.pName_label.setText(_translate("MainWindow", allInfo[0][1]))
        self.pDesc_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">" + allInfo[0][2] + "</p></body></html>"))
        self.buy_pushButton.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p2.png\"/></p></body></html>"))
        self.pName_label_2.setText(_translate("MainWindow", allInfo[1][1]))
        self.pDesc_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">" + allInfo[1][2] + "</p></body></html>"))
        self.buy_pushButton_2.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p5.png\"/></p></body></html>"))
        self.pName_label_5.setText(_translate("MainWindow", allInfo[4][1]))
        self.pDesc_label_5q.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"+ allInfo[4][2] +"</p></body></html>"))
        self.buy_pushButton_4.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p6.png\"/></p></body></html>"))
        self.pName_label_6.setText(_translate("MainWindow", allInfo[5][1]))
        self.pDesc_label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+ allInfo[5][2] +"</span></p></body></html>"))
        self.buy_pushButton_6.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p9.png\"/></p></body></html>"))
        self.pName_label_9.setText(_translate("MainWindow", allInfo[8][1]))
        self.pDesc_label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"+ allInfo[8][2] +"</p></body></html>"))
        self.buy_pushButton_8.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p10.png\"/></p></body></html>"))
        self.pName_label_10.setText(_translate("MainWindow", allInfo[9][1]))
        self.pDesc_label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"+ allInfo[9][2] +"</p></body></html>"))
        self.buy_pushButton_9.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p3.png\"/></p></body></html>"))
        self.pName_label_3.setText(_translate("MainWindow", allInfo[2][1]))
        self.pDesc_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+ allInfo[2][2] +"</span></p></body></html>"))
        self.buy_pushButton_3.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p4.png\"/></p></body></html>"))
        self.pName_label_4.setText(_translate("MainWindow", allInfo[3][1]))
        self.pDesc_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+ allInfo[3][2] +"</span></p></body></html>"))
        self.buy_pushButton_10.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p7.png\"/></p></body></html>"))
        self.pName_label_7.setText(_translate("MainWindow", allInfo[6][1]))
        self.pDesc_label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+ allInfo[6][2] +"</span></p></body></html>"))
        self.buy_pushButton_7.setText(_translate("MainWindow", "Buy Now"))
        self.pImage_label_11.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/assests/products/p8.png\"/></p></body></html>"))
        self.pName_label_8.setText(_translate("MainWindow", allInfo[7][1]))
        self.pDesc_label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"+ allInfo[7][2] +"</p></body></html>"))
        self.buy_pushButton_11.setText(_translate("MainWindow", "Buy Now"))
        
        connection.close()

#import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
