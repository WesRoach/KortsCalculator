# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SearchingCombo import SearchingCombo


class Ui_B_ItemLevel(object):
    def setupUi(self, B_ItemLevel):
        B_ItemLevel.setObjectName("B_ItemLevel")
        B_ItemLevel.resize(333, 192)
        self.hboxlayout = QtWidgets.QHBoxLayout(B_ItemLevel)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.ButtonGroup3 = QtWidgets.QFrame(B_ItemLevel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonGroup3.sizePolicy().hasHeightForWidth())
        self.ButtonGroup3.setSizePolicy(sizePolicy)
        self.ButtonGroup3.setMinimumSize(QtCore.QSize(180, 130))
        self.ButtonGroup3.setBaseSize(QtCore.QSize(0, 0))
        self.ButtonGroup3.setObjectName("ButtonGroup3")
        self.verticalLayout = QtWidgets.QWidget(self.ButtonGroup3)
        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 160, 111))
        self.verticalLayout.setObjectName("verticalLayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.verticalLayout)
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.Armor = QtWidgets.QRadioButton(self.verticalLayout)
        self.Armor.setChecked(True)
        self.Armor.setObjectName("Armor")
        self.vboxlayout1.addWidget(self.Armor)
        self.ClothArmor = QtWidgets.QRadioButton(self.verticalLayout)
        self.ClothArmor.setObjectName("ClothArmor")
        self.vboxlayout1.addWidget(self.ClothArmor)
        self.Weapon = QtWidgets.QRadioButton(self.verticalLayout)
        self.Weapon.setObjectName("Weapon")
        self.vboxlayout1.addWidget(self.Weapon)
        self.Shield = QtWidgets.QRadioButton(self.verticalLayout)
        self.Shield.setObjectName("Shield")
        self.vboxlayout1.addWidget(self.Shield)
        self.ReinforcedShield = QtWidgets.QRadioButton(self.verticalLayout)
        self.ReinforcedShield.setObjectName("ReinforcedShield")
        self.vboxlayout1.addWidget(self.ReinforcedShield)
        self.hboxlayout1.addWidget(self.ButtonGroup3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.LevelLabel = QtWidgets.QLabel(B_ItemLevel)
        self.LevelLabel.setObjectName("LevelLabel")
        self.hboxlayout2.addWidget(self.LevelLabel)
        self.Level = QtWidgets.QLineEdit(B_ItemLevel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Level.sizePolicy().hasHeightForWidth())
        self.Level.setSizePolicy(sizePolicy)
        self.Level.setMinimumSize(QtCore.QSize(52, 0))
        self.Level.setAlignment(QtCore.Qt.AlignRight)
        self.Level.setObjectName("Level")
        self.hboxlayout2.addWidget(self.Level)
        self.vboxlayout2.addLayout(self.hboxlayout2)
        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.AFDPSLabel = QtWidgets.QLabel(B_ItemLevel)
        self.AFDPSLabel.setObjectName("AFDPSLabel")
        self.hboxlayout3.addWidget(self.AFDPSLabel)
        self.AFDPS = QtWidgets.QLineEdit(B_ItemLevel)
        self.AFDPS.setMinimumSize(QtCore.QSize(58, 0))
        self.AFDPS.setAlignment(QtCore.Qt.AlignRight)
        self.AFDPS.setObjectName("AFDPS")
        self.hboxlayout3.addWidget(self.AFDPS)
        self.vboxlayout2.addLayout(self.hboxlayout3)
        self.ShieldType = SearchingCombo(B_ItemLevel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShieldType.sizePolicy().hasHeightForWidth())
        self.ShieldType.setSizePolicy(sizePolicy)
        self.ShieldType.setObjectName("ShieldType")
        self.vboxlayout2.addWidget(self.ShieldType)
        self.hboxlayout1.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.OK = QtWidgets.QPushButton(B_ItemLevel)
        self.OK.setObjectName("OK")
        self.hboxlayout4.addWidget(self.OK)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem1)
        self.Cancel = QtWidgets.QPushButton(B_ItemLevel)
        self.Cancel.setObjectName("Cancel")
        self.hboxlayout4.addWidget(self.Cancel)
        self.vboxlayout.addLayout(self.hboxlayout4)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(B_ItemLevel)
        self.Armor.clicked.connect(B_ItemLevel.TypeChanged)
        self.ClothArmor.clicked.connect(B_ItemLevel.TypeChanged)
        self.Weapon.clicked.connect(B_ItemLevel.TypeChanged)
        self.Shield.clicked.connect(B_ItemLevel.TypeChanged)
        self.ReinforcedShield.clicked.connect(B_ItemLevel.TypeChanged)
        self.Level.textChanged[str].connect(B_ItemLevel.LevelChanged)
        self.Level.editingFinished.connect(B_ItemLevel.LevelDone)
        self.AFDPS.textChanged[str].connect(B_ItemLevel.AFDPSChanged)
        self.AFDPS.editingFinished.connect(B_ItemLevel.AFDPSDone)
        self.ShieldType.activated[str].connect(B_ItemLevel.ShieldChanged)
        self.OK.clicked.connect(B_ItemLevel.OkClicked)
        self.Cancel.clicked.connect(B_ItemLevel.CancelClicked)
        QtCore.QMetaObject.connectSlotsByName(B_ItemLevel)

    def retranslateUi(self, B_ItemLevel):
        _translate = QtCore.QCoreApplication.translate
        B_ItemLevel.setWindowTitle(_translate("B_ItemLevel", "Item Level"))
        self.Armor.setText(_translate("B_ItemLevel", "Armor"))
        self.ClothArmor.setText(_translate("B_ItemLevel", "Cloth Armor"))
        self.Weapon.setText(_translate("B_ItemLevel", "Weapon"))
        self.Shield.setText(_translate("B_ItemLevel", "Shield"))
        self.ReinforcedShield.setText(_translate("B_ItemLevel", "Reinforced Shield"))
        self.LevelLabel.setText(_translate("B_ItemLevel", "Level:"))
        self.AFDPSLabel.setText(_translate("B_ItemLevel", "AF/DPS:"))
        self.OK.setText(_translate("B_ItemLevel", "OK"))
        self.Cancel.setText(_translate("B_ItemLevel", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    B_ItemLevel = QtWidgets.QDialog()
    ui = Ui_B_ItemLevel()
    ui.setupUi(B_ItemLevel)
    B_ItemLevel.show()
    sys.exit(app.exec_())

