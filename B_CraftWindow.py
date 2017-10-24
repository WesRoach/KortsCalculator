# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CraftWindow.ui'
#
# Created: Wed Jan 24 22:22:21 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_CraftWindow(object):
    def setupUi(self, B_CraftWindow):
        B_CraftWindow.setObjectName("B_CraftWindow")
        B_CraftWindow.resize(QtCore.QSize(QtCore.QRect(0,0,525,509).size()).expandedTo(B_CraftWindow.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(B_CraftWindow)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.GroupBox1 = QtGui.QGroupBox(B_CraftWindow)
        self.GroupBox1.setObjectName("GroupBox1")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.GroupBox1)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(3)
        self.gridlayout.setObjectName("gridlayout")

        self.GemNameLabel = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GemNameLabel.sizePolicy().hasHeightForWidth())
        self.GemNameLabel.setSizePolicy(sizePolicy)
        self.GemNameLabel.setObjectName("GemNameLabel")
        self.gridlayout.addWidget(self.GemNameLabel,0,0,1,1)

        self.GemMakesLabel = QtGui.QLabel(self.GroupBox1)
        self.GemMakesLabel.setObjectName("GemMakesLabel")
        self.gridlayout.addWidget(self.GemMakesLabel,0,1,1,1)

        self.GemCostLabel = QtGui.QLabel(self.GroupBox1)
        self.GemCostLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GemCostLabel.setObjectName("GemCostLabel")
        self.gridlayout.addWidget(self.GemCostLabel,0,2,1,1)

        self.Gem1Name = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem1Name.sizePolicy().hasHeightForWidth())
        self.Gem1Name.setSizePolicy(sizePolicy)
        self.Gem1Name.setObjectName("Gem1Name")
        self.gridlayout.addWidget(self.Gem1Name,1,0,1,1)

        self.Gem1Makes = QtGui.QSpinBox(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem1Makes.sizePolicy().hasHeightForWidth())
        self.Gem1Makes.setSizePolicy(sizePolicy)
        self.Gem1Makes.setObjectName("Gem1Makes")
        self.gridlayout.addWidget(self.Gem1Makes,1,1,1,1)

        self.Gem1Cost = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem1Cost.sizePolicy().hasHeightForWidth())
        self.Gem1Cost.setSizePolicy(sizePolicy)
        self.Gem1Cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Gem1Cost.setObjectName("Gem1Cost")
        self.gridlayout.addWidget(self.Gem1Cost,1,2,1,1)

        self.Gem2Name = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem2Name.sizePolicy().hasHeightForWidth())
        self.Gem2Name.setSizePolicy(sizePolicy)
        self.Gem2Name.setObjectName("Gem2Name")
        self.gridlayout.addWidget(self.Gem2Name,2,0,1,1)

        self.Gem2Makes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem2Makes.setObjectName("Gem2Makes")
        self.gridlayout.addWidget(self.Gem2Makes,2,1,1,1)

        self.Gem2Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem2Cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Gem2Cost.setObjectName("Gem2Cost")
        self.gridlayout.addWidget(self.Gem2Cost,2,2,1,1)

        self.Gem3Name = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem3Name.sizePolicy().hasHeightForWidth())
        self.Gem3Name.setSizePolicy(sizePolicy)
        self.Gem3Name.setObjectName("Gem3Name")
        self.gridlayout.addWidget(self.Gem3Name,3,0,1,1)

        self.Gem3Makes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem3Makes.setObjectName("Gem3Makes")
        self.gridlayout.addWidget(self.Gem3Makes,3,1,1,1)

        self.Gem3Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem3Cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Gem3Cost.setObjectName("Gem3Cost")
        self.gridlayout.addWidget(self.Gem3Cost,3,2,1,1)

        self.Gem4Name = QtGui.QLabel(self.GroupBox1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gem4Name.sizePolicy().hasHeightForWidth())
        self.Gem4Name.setSizePolicy(sizePolicy)
        self.Gem4Name.setObjectName("Gem4Name")
        self.gridlayout.addWidget(self.Gem4Name,4,0,1,1)

        self.Gem4Makes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem4Makes.setObjectName("Gem4Makes")
        self.gridlayout.addWidget(self.Gem4Makes,4,1,1,1)

        self.Gem4Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem4Cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Gem4Cost.setObjectName("Gem4Cost")
        self.gridlayout.addWidget(self.Gem4Cost,4,2,1,1)
        self.vboxlayout2.addLayout(self.gridlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.GroupBox2_2 = QtGui.QGroupBox(self.GroupBox1)
        self.GroupBox2_2.setObjectName("GroupBox2_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.GroupBox2_2)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.MatsUsed = QtGui.QTextEdit(self.GroupBox2_2)
        self.MatsUsed.setObjectName("MatsUsed")
        self.vboxlayout3.addWidget(self.MatsUsed)
        self.hboxlayout1.addWidget(self.GroupBox2_2)

        self.GroupBox2_2_2 = QtGui.QGroupBox(self.GroupBox1)
        self.GroupBox2_2_2.setObjectName("GroupBox2_2_2")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.GroupBox2_2_2)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.MatsExpected = QtGui.QTextEdit(self.GroupBox2_2_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MatsExpected.sizePolicy().hasHeightForWidth())
        self.MatsExpected.setSizePolicy(sizePolicy)
        self.MatsExpected.setObjectName("MatsExpected")
        self.vboxlayout4.addWidget(self.MatsExpected)
        self.hboxlayout1.addWidget(self.GroupBox2_2_2)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.vboxlayout1.addLayout(self.vboxlayout2)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.TextLabel8 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel8.setObjectName("TextLabel8")
        self.hboxlayout3.addWidget(self.TextLabel8)

        self.TotalCost = QtGui.QLabel(self.GroupBox1)
        self.TotalCost.setObjectName("TotalCost")
        self.hboxlayout3.addWidget(self.TotalCost)
        self.hboxlayout2.addLayout(self.hboxlayout3)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.vboxlayout.addWidget(self.GroupBox1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        spacerItem = QtGui.QSpacerItem(16,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem)

        self.Close = QtGui.QPushButton(B_CraftWindow)
        self.Close.setObjectName("Close")
        self.hboxlayout4.addWidget(self.Close)

        spacerItem1 = QtGui.QSpacerItem(102,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout4)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(B_CraftWindow)
        QtCore.QMetaObject.connectSlotsByName(B_CraftWindow)

    def retranslateUi(self, B_CraftWindow):
        B_CraftWindow.setWindowTitle(QtGui.QApplication.translate("B_CraftWindow", "Working Item Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox1.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Gems", None, QtGui.QApplication.UnicodeUTF8))
        self.GemNameLabel.setText(QtGui.QApplication.translate("B_CraftWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.GemMakesLabel.setText(QtGui.QApplication.translate("B_CraftWindow", "Makes:", None, QtGui.QApplication.UnicodeUTF8))
        self.GemCostLabel.setText(QtGui.QApplication.translate("B_CraftWindow", "Cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2_2.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Materials (used)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2_2_2.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Materials (one make)", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_CraftWindow", "Total Cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalCost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Close.setText(QtGui.QApplication.translate("B_CraftWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

