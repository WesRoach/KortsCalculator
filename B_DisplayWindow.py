# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_B_DisplayWindow(object):
    def setupUi(self, B_DisplayWindow):
        B_DisplayWindow.setObjectName(_fromUtf8("B_DisplayWindow"))
        B_DisplayWindow.resize(238, 310)
        B_DisplayWindow.setWindowTitle(_fromUtf8(""))
        self.vboxlayout = QtGui.QVBoxLayout(B_DisplayWindow)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.DisplayText = QtGui.QListWidget(B_DisplayWindow)
        self.DisplayText.setObjectName(_fromUtf8("DisplayText"))
        self.vboxlayout1.addWidget(self.DisplayText)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.PushButton1 = QtGui.QPushButton(B_DisplayWindow)
        self.PushButton1.setObjectName(_fromUtf8("PushButton1"))
        self.hboxlayout.addWidget(self.PushButton1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(B_DisplayWindow)

    def retranslateUi(self, B_DisplayWindow):
        self.PushButton1.setText(_translate("B_DisplayWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    B_DisplayWindow = QtGui.QDialog()
    ui = Ui_B_DisplayWindow()
    ui.setupUi(B_DisplayWindow)
    B_DisplayWindow.show()
    sys.exit(app.exec_())

