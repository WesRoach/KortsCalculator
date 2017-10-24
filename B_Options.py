# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created: Fri Apr 13 03:51:29 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Options(object):
    def setupUi(self, B_Options):
        B_Options.setObjectName("B_Options")
        B_Options.resize(QtCore.QSize(QtCore.QRect(0,0,627,530).size()).expandedTo(B_Options.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_Options)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.Tab = QtGui.QTabWidget(B_Options)
        self.Tab.setEnabled(True)
        self.Tab.setObjectName("Tab")

        self.General = QtGui.QWidget()
        self.General.setObjectName("General")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.General)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.TextLabel1 = QtGui.QLabel(self.General)
        self.TextLabel1.setObjectName("TextLabel1")
        self.hboxlayout.addWidget(self.TextLabel1)

        self.Skill = QtGui.QComboBox(self.General)
        self.Skill.setObjectName("Skill")
        self.hboxlayout.addWidget(self.Skill)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout3.addLayout(self.hboxlayout)

        self.CapDistance = QtGui.QCheckBox(self.General)
        self.CapDistance.setObjectName("CapDistance")
        self.vboxlayout3.addWidget(self.CapDistance)

        self.ShowDoneGems = QtGui.QCheckBox(self.General)
        self.ShowDoneGems.setObjectName("ShowDoneGems")
        self.vboxlayout3.addWidget(self.ShowDoneGems)

        self.ShowScrollingSlots = QtGui.QCheckBox(self.General)
        self.ShowScrollingSlots.setObjectName("ShowScrollingSlots")
        self.vboxlayout3.addWidget(self.ShowScrollingSlots)

        self.EuroServers = QtGui.QCheckBox(self.General)
        self.EuroServers.setChecked(True)
        self.EuroServers.setObjectName("EuroServers")
        self.vboxlayout3.addWidget(self.EuroServers)

        self.IncludeRR = QtGui.QCheckBox(self.General)
        self.IncludeRR.setChecked(True)
        self.IncludeRR.setObjectName("IncludeRR")
        self.vboxlayout3.addWidget(self.IncludeRR)

        self.HideNonClassSkills = QtGui.QCheckBox(self.General)
        self.HideNonClassSkills.setChecked(True)
        self.HideNonClassSkills.setObjectName("HideNonClassSkills")
        self.vboxlayout3.addWidget(self.HideNonClassSkills)

        self.Coop = QtGui.QCheckBox(self.General)
        self.Coop.setObjectName("Coop")
        self.vboxlayout3.addWidget(self.Coop)

        self.TextLabel2_5 = QtGui.QLabel(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel2_5.sizePolicy().hasHeightForWidth())
        self.TextLabel2_5.setSizePolicy(sizePolicy)
        self.TextLabel2_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TextLabel2_5.setObjectName("TextLabel2_5")
        self.vboxlayout3.addWidget(self.TextLabel2_5)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem1)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.Tab.addTab(self.General,"")

        self.Price = QtGui.QWidget()
        self.Price.setObjectName("Price")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.Price)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setMargin(0)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.GroupBox1 = QtGui.QGroupBox(self.Price)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupBox1.sizePolicy().hasHeightForWidth())
        self.GroupBox1.setSizePolicy(sizePolicy)
        self.GroupBox1.setObjectName("GroupBox1")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.GroupBox1)
        self.hboxlayout3.setMargin(9)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.PPGem = QtGui.QLineEdit(self.GroupBox1)
        self.PPGem.setObjectName("PPGem")
        self.gridlayout.addWidget(self.PPGem,0,1,1,1)

        self.TextLabel1_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2.setObjectName("TextLabel1_2")
        self.gridlayout.addWidget(self.TextLabel1_2,0,0,1,1)

        self.PPOrder = QtGui.QLineEdit(self.GroupBox1)
        self.PPOrder.setObjectName("PPOrder")
        self.gridlayout.addWidget(self.PPOrder,2,1,1,1)

        self.TextLabel1_2_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2_2.setObjectName("TextLabel1_2_2")
        self.gridlayout.addWidget(self.TextLabel1_2_2,1,0,1,1)

        self.TextLabel1_2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2_3.setObjectName("TextLabel1_2_3")
        self.gridlayout.addWidget(self.TextLabel1_2_3,2,0,1,1)

        self.PPItem = QtGui.QLineEdit(self.GroupBox1)
        self.PPItem.setObjectName("PPItem")
        self.gridlayout.addWidget(self.PPItem,1,1,1,1)
        self.vboxlayout7.addLayout(self.gridlayout)

        self.TextLabel2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel2_3.setObjectName("TextLabel2_3")
        self.vboxlayout7.addWidget(self.TextLabel2_3)
        self.hboxlayout3.addLayout(self.vboxlayout7)
        self.hboxlayout2.addWidget(self.GroupBox1)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setMargin(0)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.GroupBox6 = QtGui.QGroupBox(self.Price)
        self.GroupBox6.setObjectName("GroupBox6")

        self.vboxlayout9 = QtGui.QVBoxLayout(self.GroupBox6)
        self.vboxlayout9.setMargin(9)
        self.vboxlayout9.setSpacing(6)
        self.vboxlayout9.setObjectName("vboxlayout9")

        self.vboxlayout10 = QtGui.QVBoxLayout()
        self.vboxlayout10.setMargin(0)
        self.vboxlayout10.setSpacing(6)
        self.vboxlayout10.setObjectName("vboxlayout10")

        self.HourPrice = QtGui.QLineEdit(self.GroupBox6)
        self.HourPrice.setObjectName("HourPrice")
        self.vboxlayout10.addWidget(self.HourPrice)

        self.HourInclude = QtGui.QCheckBox(self.GroupBox6)
        self.HourInclude.setObjectName("HourInclude")
        self.vboxlayout10.addWidget(self.HourInclude)
        self.vboxlayout9.addLayout(self.vboxlayout10)
        self.vboxlayout8.addWidget(self.GroupBox6)

        self.GroupBox4 = QtGui.QGroupBox(self.Price)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupBox4.sizePolicy().hasHeightForWidth())
        self.GroupBox4.setSizePolicy(sizePolicy)
        self.GroupBox4.setObjectName("GroupBox4")

        self.vboxlayout11 = QtGui.QVBoxLayout(self.GroupBox4)
        self.vboxlayout11.setMargin(9)
        self.vboxlayout11.setSpacing(6)
        self.vboxlayout11.setObjectName("vboxlayout11")

        self.vboxlayout12 = QtGui.QVBoxLayout()
        self.vboxlayout12.setMargin(0)
        self.vboxlayout12.setSpacing(6)
        self.vboxlayout12.setObjectName("vboxlayout12")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.GenMarkup = QtGui.QLineEdit(self.GroupBox4)
        self.GenMarkup.setObjectName("GenMarkup")
        self.hboxlayout4.addWidget(self.GenMarkup)

        self.TextLabel11 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel11.setObjectName("TextLabel11")
        self.hboxlayout4.addWidget(self.TextLabel11)
        self.vboxlayout12.addLayout(self.hboxlayout4)

        self.TextLabel12 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel12.setObjectName("TextLabel12")
        self.vboxlayout12.addWidget(self.TextLabel12)
        self.vboxlayout11.addLayout(self.vboxlayout12)
        self.vboxlayout8.addWidget(self.GroupBox4)
        self.hboxlayout2.addLayout(self.vboxlayout8)
        self.vboxlayout6.addLayout(self.hboxlayout2)

        self.GroupBox3 = QtGui.QGroupBox(self.Price)
        self.GroupBox3.setObjectName("GroupBox3")

        self.vboxlayout13 = QtGui.QVBoxLayout(self.GroupBox3)
        self.vboxlayout13.setMargin(9)
        self.vboxlayout13.setSpacing(6)
        self.vboxlayout13.setObjectName("vboxlayout13")

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.PPInclude = QtGui.QCheckBox(self.GroupBox3)
        self.PPInclude.setObjectName("PPInclude")
        self.gridlayout1.addWidget(self.PPInclude,3,0,1,1)

        self.PPImbue = QtGui.QLineEdit(self.GroupBox3)
        self.PPImbue.setObjectName("PPImbue")
        self.gridlayout1.addWidget(self.PPImbue,1,0,1,2)

        self.TextLabel9 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel9.setObjectName("TextLabel9")
        self.gridlayout1.addWidget(self.TextLabel9,2,3,1,2)

        self.PPOC = QtGui.QLineEdit(self.GroupBox3)
        self.PPOC.setObjectName("PPOC")
        self.gridlayout1.addWidget(self.PPOC,2,0,1,3)

        self.TextLabel8 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel8.setObjectName("TextLabel8")
        self.gridlayout1.addWidget(self.TextLabel8,1,2,1,3)

        self.PPLevel = QtGui.QLineEdit(self.GroupBox3)
        self.PPLevel.setObjectName("PPLevel")
        self.gridlayout1.addWidget(self.PPLevel,0,0,1,4)

        self.TextLabel7 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel7.setObjectName("TextLabel7")
        self.gridlayout1.addWidget(self.TextLabel7,0,4,1,1)

        self.TextLabel10 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel10.setObjectName("TextLabel10")
        self.gridlayout1.addWidget(self.TextLabel10,3,2,1,3)
        self.vboxlayout13.addLayout(self.gridlayout1)
        self.vboxlayout6.addWidget(self.GroupBox3)
        self.hboxlayout1.addLayout(self.vboxlayout6)

        self.GroupBox5 = QtGui.QGroupBox(self.Price)
        self.GroupBox5.setObjectName("GroupBox5")

        self.vboxlayout14 = QtGui.QVBoxLayout(self.GroupBox5)
        self.vboxlayout14.setMargin(9)
        self.vboxlayout14.setSpacing(6)
        self.vboxlayout14.setObjectName("vboxlayout14")

        self.vboxlayout15 = QtGui.QVBoxLayout()
        self.vboxlayout15.setMargin(0)
        self.vboxlayout15.setSpacing(6)
        self.vboxlayout15.setObjectName("vboxlayout15")

        self.TierPriceTable = QtGui.QTableWidget(self.GroupBox5)
        self.TierPriceTable.setObjectName("TierPriceTable")
        self.vboxlayout15.addWidget(self.TierPriceTable)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.TierInclude = QtGui.QCheckBox(self.GroupBox5)
        self.TierInclude.setObjectName("TierInclude")
        self.hboxlayout5.addWidget(self.TierInclude)

        self.TextLabel15 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel15.setObjectName("TextLabel15")
        self.hboxlayout5.addWidget(self.TextLabel15)
        self.vboxlayout15.addLayout(self.hboxlayout5)
        self.vboxlayout14.addLayout(self.vboxlayout15)
        self.hboxlayout1.addWidget(self.GroupBox5)
        self.vboxlayout5.addLayout(self.hboxlayout1)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem2)

        self.CostInPrice = QtGui.QCheckBox(self.Price)
        self.CostInPrice.setChecked(True)
        self.CostInPrice.setObjectName("CostInPrice")
        self.hboxlayout6.addWidget(self.CostInPrice)

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem3)
        self.vboxlayout5.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem4)

        self.TextLabel2_4 = QtGui.QLabel(self.Price)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel2_4.sizePolicy().hasHeightForWidth())
        self.TextLabel2_4.setSizePolicy(sizePolicy)
        self.TextLabel2_4.setObjectName("TextLabel2_4")
        self.hboxlayout7.addWidget(self.TextLabel2_4)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem5)
        self.vboxlayout5.addLayout(self.hboxlayout7)
        self.vboxlayout4.addLayout(self.vboxlayout5)
        self.Tab.addTab(self.Price,"")
        self.vboxlayout1.addWidget(self.Tab)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(25)
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem6)

        self.OK = QtGui.QPushButton(B_Options)
        self.OK.setObjectName("OK")
        self.hboxlayout8.addWidget(self.OK)

        self.Cancel = QtGui.QPushButton(B_Options)
        self.Cancel.setObjectName("Cancel")
        self.hboxlayout8.addWidget(self.Cancel)

        spacerItem7 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem7)
        self.vboxlayout1.addLayout(self.hboxlayout8)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_Options)
        self.Tab.setCurrentIndex(2)

        QtCore.QMetaObject.connectSlotsByName(B_Options)
        B_Options.setTabOrder(self.PPGem,self.PPItem)
        B_Options.setTabOrder(self.PPItem,self.PPOrder)
        B_Options.setTabOrder(self.PPOrder,self.PPLevel)
        B_Options.setTabOrder(self.PPLevel,self.PPImbue)
        B_Options.setTabOrder(self.PPImbue,self.PPOC)
        B_Options.setTabOrder(self.PPOC,self.PPInclude)
        B_Options.setTabOrder(self.PPInclude,self.GenMarkup)
        B_Options.setTabOrder(self.GenMarkup,self.TierInclude)
        B_Options.setTabOrder(self.TierInclude,self.HourPrice)
        B_Options.setTabOrder(self.HourPrice,self.HourInclude)
        B_Options.setTabOrder(self.HourInclude,self.CostInPrice)
        B_Options.setTabOrder(self.CostInPrice,self.OK)
        B_Options.setTabOrder(self.OK,self.Cancel)
        B_Options.setTabOrder(self.Cancel,self.Skill)
        B_Options.setTabOrder(self.Skill,self.CapDistance)
        B_Options.setTabOrder(self.CapDistance,self.ShowDoneGems)
        B_Options.setTabOrder(self.ShowDoneGems,self.IncludeRR)
        B_Options.setTabOrder(self.IncludeRR,self.HideNonClassSkills)
        B_Options.setTabOrder(self.HideNonClassSkills,self.Coop)
        B_Options.setTabOrder(self.Coop,self.Tab)

    def retranslateUi(self, B_Options):
        B_Options.setWindowTitle(QtGui.QApplication.translate("B_Options", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1.setText(QtGui.QApplication.translate("B_Options", "Crafter Skill:", None, QtGui.QApplication.UnicodeUTF8))
        self.CapDistance.setText(QtGui.QApplication.translate("B_Options", "Show Distance To Cap (instead of total)", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowDoneGems.setText(QtGui.QApplication.translate("B_Options", "Hide \"Made\" Gems from Materials List and Exported Gems", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowScrollingSlots.setText(QtGui.QApplication.translate("B_Options", "Scrollable Slots (allows your window to be shorter)", None, QtGui.QApplication.UnicodeUTF8))
        self.EuroServers.setText(QtGui.QApplication.translate("B_Options", "Export Gems to European/GOA Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.IncludeRR.setText(QtGui.QApplication.translate("B_Options", "Include Racial Resists in Totals", None, QtGui.QApplication.UnicodeUTF8))
        self.HideNonClassSkills.setText(QtGui.QApplication.translate("B_Options", "Hide Skills not usable by this Class", None, QtGui.QApplication.UnicodeUTF8))
        self.Coop.setText(QtGui.QApplication.translate("B_Options", "Co-op / PvP Server", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_5.setText(QtGui.QApplication.translate("B_Options", "        (Lets you access items from all realms)", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.General), QtGui.QApplication.translate("B_Options", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox1.setTitle(QtGui.QApplication.translate("B_Options", "Price per", None, QtGui.QApplication.UnicodeUTF8))
        self.PPGem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2.setText(QtGui.QApplication.translate("B_Options", "Gem:", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOrder.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_2.setText(QtGui.QApplication.translate("B_Options", "Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_3.setText(QtGui.QApplication.translate("B_Options", "Order:", None, QtGui.QApplication.UnicodeUTF8))
        self.PPItem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_3.setText(QtGui.QApplication.translate("B_Options", "(cost+ X)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox6.setTitle(QtGui.QApplication.translate("B_Options", "Per hour", None, QtGui.QApplication.UnicodeUTF8))
        self.HourPrice.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HourInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox4.setTitle(QtGui.QApplication.translate("B_Options", "General Markup", None, QtGui.QApplication.UnicodeUTF8))
        self.GenMarkup.setText(QtGui.QApplication.translate("B_Options", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel11.setText(QtGui.QApplication.translate("B_Options", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel12.setText(QtGui.QApplication.translate("B_Options", "(cost + (cost * X%))", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox3.setTitle(QtGui.QApplication.translate("B_Options", "Price per lvl/point", None, QtGui.QApplication.UnicodeUTF8))
        self.PPInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.PPImbue.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel9.setText(QtGui.QApplication.translate("B_Options", "per O/C pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOC.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_Options", "per imbue pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.PPLevel.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_Options", "per level", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel10.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox5.setTitle(QtGui.QApplication.translate("B_Options", "Price by Gem Tier", None, QtGui.QApplication.UnicodeUTF8))
        self.TierPriceTable.setRowCount(10)
        self.TierPriceTable.setColumnCount(2)
        self.TierPriceTable.clear()
        self.TierPriceTable.setColumnCount(2)
        self.TierPriceTable.setRowCount(10)
        self.TierInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel15.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
        self.CostInPrice.setText(QtGui.QApplication.translate("B_Options", "Include cost in price", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_4.setText(QtGui.QApplication.translate("B_Options", "All numbers (except percentages) are in amounts of Gold.", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.Price), QtGui.QApplication.translate("B_Options", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("B_Options", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("B_Options", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

