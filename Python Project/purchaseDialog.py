# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchaseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import assests.images
import random
import datetime
import time


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 473)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 111))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(10, 10, 591, 91))
        self.logo_label.setObjectName("logo_label")
        self.final_frame = QtWidgets.QFrame(Dialog)
        self.final_frame.setGeometry(QtCore.QRect(0, 110, 611, 361))
        self.final_frame.setStyleSheet("background-color: rgba(0, 170, 255, 100);")
        self.final_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.final_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.final_frame.setObjectName("final_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.final_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.orderID_label = QtWidgets.QLabel(self.final_frame)
        self.orderID_label.setObjectName("orderID_label")
        self.gridLayout.addWidget(self.orderID_label, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.final_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.payment_label = QtWidgets.QLabel(self.final_frame)
        self.payment_label.setObjectName("payment_label")
        self.gridLayout.addWidget(self.payment_label, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.final_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.success_label = QtWidgets.QLabel(self.final_frame)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.success_label.setFont(font)
        self.success_label.setStyleSheet("background-color: rgba(0, 170, 255, 0);")
        self.success_label.setObjectName("success_label")
        self.gridLayout.addWidget(self.success_label, 1, 0, 1, 2)
        self.deliveryTo_label = QtWidgets.QLabel(self.final_frame)
        self.deliveryTo_label.setObjectName("deliveryTo_label")
        self.gridLayout.addWidget(self.deliveryTo_label, 2, 0, 1, 1)
        self.cod_label = QtWidgets.QLabel(self.final_frame)
        self.cod_label.setObjectName("cod_label")
        self.gridLayout.addWidget(self.cod_label, 6, 1, 1, 1)
        self.sysDate_label = QtWidgets.QLabel(self.final_frame)
        self.sysDate_label.setObjectName("sysDate_label")
        self.gridLayout.addWidget(self.sysDate_label, 3, 1, 1, 1)
        self.date_label = QtWidgets.QLabel(self.final_frame)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 3, 0, 1, 1)
        self.congrats_label = QtWidgets.QLabel(self.final_frame)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.congrats_label.setFont(font)
        self.congrats_label.setStyleSheet("background-color: rgba(0, 170, 255, 0);")
        self.congrats_label.setObjectName("congrats_label")
        self.gridLayout.addWidget(self.congrats_label, 0, 0, 1, 2)
        self.final_frame.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        randNum = str(random.randint(1000,9999))
        randomeDate = str(datetime.date.today() + datetime.timedelta(3))
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logo_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><img src=\":/assests/shopbag.png\"/></p></body></html>"))
        self.orderID_label.setText(_translate("Dialog", "Order ID:"))
        self.label_5.setText(_translate("Dialog", randNum))
        self.payment_label.setText(_translate("Dialog", "Payment Method:"))
        self.label_3.setText(_translate("Dialog", "personName"))
        self.success_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Your Order has been placed successfully!!</p></body></html>"))
        self.deliveryTo_label.setText(_translate("Dialog", "Delivery to:"))
        self.cod_label.setText(_translate("Dialog", "CASH ON DELIVERY"))
        self.sysDate_label.setText(_translate("Dialog", randomeDate))
        self.date_label.setText(_translate("Dialog", "Expected Date of Delivery:"))
        self.congrats_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Congratulations!</p></body></html>"))

#import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

