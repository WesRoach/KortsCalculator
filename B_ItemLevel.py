# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created: Wed Dec 27 21:57:51 2006
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt4 import QtCore, QtGui
from SearchingCombo import SearchingCombo


class Ui_B_ItemLevel(object):
    def setupUi(self, B_ItemLevel):
        B_ItemLevel.setObjectName("B_ItemLevel")
        B_ItemLevel.resize(QtCore.QSize(QtCore.QRect(0,0,333,192).size()).expandedTo(B_ItemLevel.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(B_ItemLevel)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.ButtonGroup3 = QtGui.QFrame(B_ItemLevel)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonGroup3.sizePolicy().hasHeightForWidth())
        self.ButtonGroup3.setSizePolicy(sizePolicy)
        self.ButtonGroup3.setMinimumSize(QtCore.QSize(180,130))
        self.ButtonGroup3.setBaseSize(QtCore.QSize(0,0))
        self.ButtonGroup3.setObjectName("ButtonGroup3")

        self.verticalLayout = QtGui.QWidget(self.ButtonGroup3)
        self.verticalLayout.setGeometry(QtCore.QRect(10,10,160,111))
        self.verticalLayout.setObjectName("verticalLayout")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.verticalLayout)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.Armor = QtGui.QRadioButton(self.verticalLayout)
        self.Armor.setChecked(True)
        self.Armor.setObjectName("Armor")
        self.vboxlayout1.addWidget(self.Armor)

        self.ClothArmor = QtGui.QRadioButton(self.verticalLayout)
        self.ClothArmor.setObjectName("ClothArmor")
        self.vboxlayout1.addWidget(self.ClothArmor)

        self.Weapon = QtGui.QRadioButton(self.verticalLayout)
        self.Weapon.setObjectName("Weapon")
        self.vboxlayout1.addWidget(self.Weapon)

        self.Shield = QtGui.QRadioButton(self.verticalLayout)
        self.Shield.setObjectName("Shield")
        self.vboxlayout1.addWidget(self.Shield)

        self.ReinforcedShield = QtGui.QRadioButton(self.verticalLayout)
        self.ReinforcedShield.setObjectName("ReinforcedShield")
        self.vboxlayout1.addWidget(self.ReinforcedShield)
        self.hboxlayout1.addWidget(self.ButtonGroup3)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.LevelLabel = QtGui.QLabel(B_ItemLevel)
        self.LevelLabel.setObjectName("LevelLabel")
        self.hboxlayout2.addWidget(self.LevelLabel)

        self.Level = QtGui.QLineEdit(B_ItemLevel)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Level.sizePolicy().hasHeightForWidth())
        self.Level.setSizePolicy(sizePolicy)
        self.Level.setMinimumSize(QtCore.QSize(52,0))
        self.Level.setAlignment(QtCore.Qt.AlignRight)
        self.Level.setObjectName("Level")
        self.hboxlayout2.addWidget(self.Level)
        self.vboxlayout2.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.AFDPSLabel = QtGui.QLabel(B_ItemLevel)
        self.AFDPSLabel.setObjectName("AFDPSLabel")
        self.hboxlayout3.addWidget(self.AFDPSLabel)

        self.AFDPS = QtGui.QLineEdit(B_ItemLevel)
        self.AFDPS.setMinimumSize(QtCore.QSize(58,0))
        self.AFDPS.setAlignment(QtCore.Qt.AlignRight)
        self.AFDPS.setObjectName("AFDPS")
        self.hboxlayout3.addWidget(self.AFDPS)
        self.vboxlayout2.addLayout(self.hboxlayout3)

        self.ShieldType = SearchingCombo(B_ItemLevel)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShieldType.sizePolicy().hasHeightForWidth())
        self.ShieldType.setSizePolicy(sizePolicy)
        self.ShieldType.setObjectName("ShieldType")
        self.vboxlayout2.addWidget(self.ShieldType)
        self.hboxlayout1.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.OK = QtGui.QPushButton(B_ItemLevel)
        self.OK.setObjectName("OK")
        self.hboxlayout4.addWidget(self.OK)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem1)

        self.Cancel = QtGui.QPushButton(B_ItemLevel)
        self.Cancel.setObjectName("Cancel")
        self.hboxlayout4.addWidget(self.Cancel)
        self.vboxlayout.addLayout(self.hboxlayout4)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(B_ItemLevel)

        QtCore.QMetaObject.connectSlotsByName(B_ItemLevel)

    def retranslateUi(self, B_ItemLevel):
        B_ItemLevel.setWindowTitle(QtGui.QApplication.translate("B_ItemLevel", "Item Level", None, QtGui.QApplication.UnicodeUTF8))
        self.Armor.setText(QtGui.QApplication.translate("B_ItemLevel", "Armor", None, QtGui.QApplication.UnicodeUTF8))
        self.ClothArmor.setText(QtGui.QApplication.translate("B_ItemLevel", "Cloth Armor", None, QtGui.QApplication.UnicodeUTF8))
        self.Weapon.setText(QtGui.QApplication.translate("B_ItemLevel", "Weapon", None, QtGui.QApplication.UnicodeUTF8))
        self.Shield.setText(QtGui.QApplication.translate("B_ItemLevel", "Shield", None, QtGui.QApplication.UnicodeUTF8))
        self.ReinforcedShield.setText(QtGui.QApplication.translate("B_ItemLevel", "Reinforced Shield", None, QtGui.QApplication.UnicodeUTF8))
        self.LevelLabel.setText(QtGui.QApplication.translate("B_ItemLevel", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.AFDPSLabel.setText(QtGui.QApplication.translate("B_ItemLevel", "AF/DPS:", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("B_ItemLevel", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("B_ItemLevel", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
