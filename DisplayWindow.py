# DisplayWindow.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_DisplayWindow import *
from Constants import *
import string


class DisplayWindow(QDialog, Ui_B_DisplayWindow):
    def __init__(self, parent=None, name=None, modal=False, fl=Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_DisplayWindow.setupUi(self, self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.connect(self.PushButton1, SIGNAL("clicked()"), self.CloseWindow)
        self.connect(self.DisplayText, SIGNAL("itemActivated(QListWidgetItem*)"), self.LocationClicked)

        self.scwindow = parent

    def loadLocations(self, locs):
        strlist = map(lambda (x): '%s: %s' % (x[0], x[1]), locs)
        self.DisplayText.clear()
        self.DisplayText.insertItems(0, strlist)

    def CloseWindow(self):
        self.done(1)

    def LocationClicked(self, a0):
        if a0 is None: return
        tabname, rest = string.split(str(a0.text()), ':', 1)
        if tabname in JewelTabList:
            col = JewelTabList.index(tabname)
            self.scwindow.PieceTab.setCurrentIndex(1, col)
        elif tabname in PieceTabList:
            col = PieceTabList.index(tabname)
            self.scwindow.PieceTab.setCurrentIndex(0, col)
        self.done(1)
