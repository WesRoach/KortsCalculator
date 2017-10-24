# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created: Wed Dec 27 21:57:50 2006
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_DisplayWindow(object):
    def setupUi(self, B_DisplayWindow):
        B_DisplayWindow.setObjectName("B_DisplayWindow")
        B_DisplayWindow.resize(QtCore.QSize(QtCore.QRect(0,0,238,310).size()).expandedTo(B_DisplayWindow.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_DisplayWindow)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.DisplayText = QtGui.QListWidget(B_DisplayWindow)
        self.DisplayText.setObjectName("DisplayText")
        self.vboxlayout1.addWidget(self.DisplayText)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.PushButton1 = QtGui.QPushButton(B_DisplayWindow)
        self.PushButton1.setObjectName("PushButton1")
        self.hboxlayout.addWidget(self.PushButton1)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(B_DisplayWindow)

    def retranslateUi(self, B_DisplayWindow):
        self.PushButton1.setText(QtGui.QApplication.translate("B_DisplayWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

