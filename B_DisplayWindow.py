# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_B_DisplayWindow(object):
    def setupUi(self, B_DisplayWindow):
        B_DisplayWindow.setObjectName("B_DisplayWindow")
        B_DisplayWindow.resize(238, 310)
        B_DisplayWindow.setWindowTitle("")
        self.vboxlayout = QtWidgets.QVBoxLayout(B_DisplayWindow)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.DisplayText = QtWidgets.QListWidget(B_DisplayWindow)
        self.DisplayText.setObjectName("DisplayText")
        self.vboxlayout1.addWidget(self.DisplayText)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.PushButton1 = QtWidgets.QPushButton(B_DisplayWindow)
        self.PushButton1.setObjectName("PushButton1")
        self.hboxlayout.addWidget(self.PushButton1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(B_DisplayWindow)

    def retranslateUi(self, B_DisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        self.PushButton1.setText(_translate("B_DisplayWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    B_DisplayWindow = QtWidgets.QDialog()
    ui = Ui_B_DisplayWindow()
    ui.setupUi(B_DisplayWindow)
    B_DisplayWindow.show()
    sys.exit(app.exec_())

