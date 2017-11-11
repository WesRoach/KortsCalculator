# coding = utf-8

# DisplayWindow.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from B_DisplayWindow import *
from Constants import *


class DisplayWindow(QDialog, Ui_B_DisplayWindow):

    def __init__(self, parent = None, name = None, modal = False, fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_DisplayWindow.setupUi(self, self)

        if name:
            self.setObjectName(name)

        if modal:
            self.setModal(modal)

        self.PushButton1.clicked.connect(self.CloseWindow)
        self.DisplayText.itemActivated['QListWidgetItem *'].connect(self.LocationClicked)

        self.scwindow = parent

    def loadLocations(self, locs):
        strlist = ['%s: %s' % (x[0], x[1]) for x in locs]
        self.DisplayText.clear()
        self.DisplayText.insertItems(0, strlist)

    def CloseWindow(self):
        self.done(1)

    def LocationClicked(self, a0):
        if a0 is None: return
        tabname, rest = str.split(str(a0.text()), ':', 1)

        if tabname in JewelTabList:
            col = JewelTabList.index(tabname)
            self.scwindow.PieceTab.setCurrentIndex(1, col)

        elif tabname in PieceTabList:
            col = PieceTabList.index(tabname)
            self.scwindow.PieceTab.setCurrentIndex(0, col)

        self.done(1)
