# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
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

class Ui_B_ReportWindow(object):
    def setupUi(self, B_ReportWindow):
        B_ReportWindow.setObjectName(_fromUtf8("B_ReportWindow"))
        B_ReportWindow.resize(566, 565)
        self.vboxlayout = QtGui.QVBoxLayout(B_ReportWindow)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.ReportText = QtGui.QTextBrowser(B_ReportWindow)
        self.ReportText.setObjectName(_fromUtf8("ReportText"))
        self.vboxlayout1.addWidget(self.ReportText)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.PushButton1 = QtGui.QPushButton(B_ReportWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton1.sizePolicy().hasHeightForWidth())
        self.PushButton1.setSizePolicy(sizePolicy)
        self.PushButton1.setObjectName(_fromUtf8("PushButton1"))
        self.hboxlayout.addWidget(self.PushButton1)
        self.PushButton1_2 = QtGui.QPushButton(B_ReportWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton1_2.sizePolicy().hasHeightForWidth())
        self.PushButton1_2.setSizePolicy(sizePolicy)
        self.PushButton1_2.setObjectName(_fromUtf8("PushButton1_2"))
        self.hboxlayout.addWidget(self.PushButton1_2)
        spacerItem = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.PushButton2 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton2.setObjectName(_fromUtf8("PushButton2"))
        self.hboxlayout1.addWidget(self.PushButton2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(B_ReportWindow)

    def retranslateUi(self, B_ReportWindow):
        B_ReportWindow.setWindowTitle(_translate("B_ReportWindow", "B_ReportWindow", None))
        self.PushButton1.setText(_translate("B_ReportWindow", "Save As HTML", None))
        self.PushButton1_2.setText(_translate("B_ReportWindow", "Save As Text", None))
        self.PushButton2.setText(_translate("B_ReportWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    B_ReportWindow = QtGui.QDialog()
    ui = Ui_B_ReportWindow()
    ui.setupUi(B_ReportWindow)
    B_ReportWindow.show()
    sys.exit(app.exec_())

