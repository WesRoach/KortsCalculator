# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_B_ReportWindow(object):
    def setupUi(self, B_ReportWindow):
        B_ReportWindow.setObjectName("B_ReportWindow")
        B_ReportWindow.resize(566, 565)
        self.vboxlayout = QtWidgets.QVBoxLayout(B_ReportWindow)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.ReportText = QtWidgets.QTextBrowser(B_ReportWindow)
        self.ReportText.setObjectName("ReportText")
        self.vboxlayout1.addWidget(self.ReportText)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.PushButton1 = QtWidgets.QPushButton(B_ReportWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton1.sizePolicy().hasHeightForWidth())
        self.PushButton1.setSizePolicy(sizePolicy)
        self.PushButton1.setObjectName("PushButton1")
        self.hboxlayout.addWidget(self.PushButton1)
        self.PushButton1_2 = QtWidgets.QPushButton(B_ReportWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton1_2.sizePolicy().hasHeightForWidth())
        self.PushButton1_2.setSizePolicy(sizePolicy)
        self.PushButton1_2.setObjectName("PushButton1_2")
        self.hboxlayout.addWidget(self.PushButton1_2)
        spacerItem = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.PushButton2 = QtWidgets.QPushButton(B_ReportWindow)
        self.PushButton2.setObjectName("PushButton2")
        self.hboxlayout1.addWidget(self.PushButton2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(B_ReportWindow)

    def retranslateUi(self, B_ReportWindow):
        _translate = QtCore.QCoreApplication.translate
        B_ReportWindow.setWindowTitle(_translate("B_ReportWindow", "B_ReportWindow"))
        self.PushButton1.setText(_translate("B_ReportWindow", "Save As HTML"))
        self.PushButton1_2.setText(_translate("B_ReportWindow", "Save As Text"))
        self.PushButton2.setText(_translate("B_ReportWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    B_ReportWindow = QtWidgets.QDialog()
    ui = Ui_B_ReportWindow()
    ui.setupUi(B_ReportWindow)
    B_ReportWindow.show()
    sys.exit(app.exec_())

