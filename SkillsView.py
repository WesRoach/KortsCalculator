# coding = utf-8

# SkillsView.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QListView


class SkillsView(QListView):
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        palette.setBrush(QPalette.Base, QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.sizehint = QSize(QListView.sizeHint(self))

    def sizeHint(self):
        return QSize(self.sizehint)

    def setSizeHint(self, width, height=None):
        if isinstance(width, QSize) and height is None:
            self.sizehint = width
        else:
            self.sizehint = QSize(width, height)
        self.bestFit()

    def bestFit(self):
        self.rowheight = self.sizeHintForRow(0)
        if self.rowheight < 1: return
        bestheight = self.sizehint.height()
        if (self.horizontalScrollBarPolicy() !=
                Qt.ScrollBarAlwaysOff):
            scrollheight = self.horizontalScrollBar().sizeHint().height() + 1
        else:
            scrollheight = 0
        bestheight -= scrollheight
        rows = (bestheight + 4) / self.rowheight
        bestheight = (rows * self.rowheight) + scrollheight
        minheight = self.rowheight * 3 + scrollheight
        self.sizehint.setHeight(bestheight)
        self.setMinimumHeight(minheight)
