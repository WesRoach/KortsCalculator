# SkillsView.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4 import QtGui, QtCore

class SkillsView(QtGui.QListView):
    def __init__(self, parent = None):
        QtGui.QListView.__init__(self, parent)
        # Improve the look of QListView - should have no background
        #
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(0,0,0,0))
        palette.setBrush(QtGui.QPalette.Base, QtGui.QBrush(QtGui.QColor(0,0,0,0)))
        self.setPalette(palette)
        self.sizehint = QtCore.QSize(QtGui.QListView.sizeHint(self))

    def sizeHint(self):
        return QtCore.QSize(self.sizehint)

    def setSizeHint(self, width, height = None):
        if isinstance(width, QtCore.QSize) and height is None:
            self.sizehint = width
        else:
            self.sizehint = QtCore.QSize(width, height)
        self.bestFit()

    def bestFit(self):
        self.rowheight = self.sizeHintForRow(0)
        if self.rowheight < 1: return
        bestheight = self.sizehint.height()
        if (self.horizontalScrollBarPolicy() != 
                    QtCore.Qt.ScrollBarAlwaysOff):
            scrollheight = self.horizontalScrollBar().sizeHint().height() + 1
        else:
            scrollheight = 0
        bestheight -= scrollheight
        rows = (bestheight + 4) / self.rowheight
        bestheight = (rows * self.rowheight) + scrollheight
        minheight = self.rowheight * 3 + scrollheight
        self.sizehint.setHeight(bestheight)
        self.setMinimumHeight(minheight)
