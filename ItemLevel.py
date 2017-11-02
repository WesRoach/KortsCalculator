# coding = utf-8

# ItemLevel.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QDialog
from B_ItemLevel import *
from Constants import *
import re


class ItemLevel(QDialog, Ui_B_ItemLevel):

    def __init__(self, parent = None, name = None, modal = False, fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_ItemLevel.setupUi(self, self)

        if name:
            self.setObjectName(name)
        if modal:
            self.setModal(modal)

        self.Armor.clicked.connect(self.TypeChanged)
        self.ClothArmor.clicked.connect(self.TypeChanged)
        self.Weapon.clicked.connect(self.TypeChanged)
        self.Shield.clicked.connect(self.TypeChanged)
        self.ReinforcedShield.clicked.connect(self.TypeChanged)
        self.Level.textChanged[str].connect(self.LevelChanged)
        self.Level.editingFinished.connect(self.LevelDone)
        self.AFDPS.textChanged[str].connect(self.AFDPSChanged)

        # TODO: VALUE DOES NOT AUTO CORRECT WHEN > 102 FOR ARMOR OR > 51 FOR CLOTH
        self.AFDPS.editingFinished.connect(self.AFDPSDone)
        self.ShieldType.activated[str].connect(self.ShieldChanged)
        self.OK.clicked.connect(self.OkClicked)
        self.Cancel.clicked.connect(self.CancelClicked)

        self.ShieldType.hide()
        self.level = 51
        self.afdps = 102
        self.inchange = True
        self.Level.setText(str(self.level))
        self.inchange = False
        self.TypeChanged()

    def OkClicked(self):
        self.done(self.level)

    def CancelClicked(self):
        self.done(-1)

    def ShieldChanged(self, value):
        if self.inchange: return
        self.inchange = True

        if self.Shield.isChecked():
            self.level = max(self.ShieldType.currentIndex() * 5, 2)
        elif self.ReinforcedShield.isChecked():
            self.level = self.ShieldType.currentIndex() * 5 + 26
        self.Level.setText(str(self.level))

        self.afdps = float(self.level) * 0.3 + 1.2
        self.AFDPS.setText(str(self.afdps))

        self.inchange = False

    def AFDPSChanged(self, value):
        if self.inchange: return
        self.inchange = True

        if isinstance(value, bool):
            fix = value
            value = self.AFDPS.text()
        else:
            fix = False

        try:
            if self.Armor.isChecked():
                self.afdps = int(int(str(value)) / 2) * 2
                self.level = int(self.afdps / 2)
            elif self.ClothArmor.isChecked():
                self.afdps = int(int(str(value)) / 2) * 2
                self.level = self.afdps
            else:
                self.afdps = float(str(value))
                self.level = max(min(int((self.afdps - 1.2) / 0.3), 51), 1)
                self.afdps = float(self.level) * 0.3 + 1.2
                if self.Shield.isChecked():
                    tier = min(int(self.level / 5), 9)
                    self.level = max(tier * 5, 2)
                    self.ShieldType.setCurrentIndex(tier)
                elif self.ReinforcedShield.isChecked():
                    tier = max(int((self.level - 26) / 5), 0)
                    self.level = tier * 5 + 26
                    self.ShieldType.setCurrentIndex(tier)
        except:
            self.level = 1
            self.ShieldType.setCurrentIndex(0)

        self.Level.setText(str(self.level))

        if fix: 
            self.AFDPS.setText(str(self.afdps))

        self.inchange = False
            
    def AFDPSDone(self):
        self.AFDPSChanged(True)

    def LevelChanged(self, value):
        if self.inchange: return
        self.inchange = True

        if isinstance(value, bool):
            fix = value
            value = self.Level.text()
        else:
            fix = False

        try:
            self.level = max(min(int(str(value)), 51), 1)
        except:
            self.level = 1

        if self.Shield.isChecked():
            tier = min(int(self.level / 5), 9)
            self.level = max(tier * 5, 2)
            self.ShieldType.setCurrentIndex(tier)
        elif self.ReinforcedShield.isChecked():
            tier = max(int((self.level - 26) / 5), 0)
            self.level = tier * 5 + 26
            self.ShieldType.setCurrentIndex(tier)

        if self.Armor.isChecked():
            self.afdps = self.level * 2
        elif self.ClothArmor.isChecked():
            self.afdps = self.level
        else:
            self.afdps = float(self.level) * 0.3 + 1.2
        self.AFDPS.setText(str(self.afdps))

        if fix:
            self.Level.setText(str(self.level))

        self.inchange = False
        
    def LevelDone(self):
        self.LevelChanged(True)

    def TypeChanged(self):
        self.inchange = False

        if self.Armor.isChecked() or self.ClothArmor.isChecked():
            self.AFDPSLabel.setText('AF')
        else:
            self.AFDPSLabel.setText('DPS')

        if self.Armor.isChecked() or self.ClothArmor.isChecked() \
                                  or self.Weapon.isChecked():
            self.ShieldType.hide()
            self.LevelChanged(True)
            return

        if self.Shield.isChecked():
            self.ShieldType.clear()
            self.ShieldType.insertItems(0, list(ShieldTypes))
        elif self.ReinforcedShield.isChecked():
            self.ShieldType.clear()
            self.ShieldType.insertItems(0, list(ShieldTypes[4:]))
        self.LevelChanged(True)
        self.ShieldType.show()
