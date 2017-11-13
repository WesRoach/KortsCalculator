# coding = utf-8

# ScrollArea.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license

# TODO: THIS MIGHT NOT BE NECESSARY ANYMORE ...

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QScrollArea


class ScrollArea(QScrollArea):
    def __init__(self, parent=None):
        QScrollArea.__init__(self, parent)

        # TODO: REMOVE THE BACKGROUND FROM 'QScrollArea'
        palette = QPalette(self.palette())
        palette.setColor(QPalette.Window, QColor(0, 0, 0, 0))
        palette.setBrush(QPalette.Window, QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)

        self.sizehint = QSize(QScrollArea.sizeHint(self))
        self.rowheight = -1

        self.verticalScrollBar().valueChanged[int].connect(self.positionNearest)

    def setWidget(self, widget):
        QScrollArea.setWidget(self, widget)
        self.bestFit()

    def sizeHint(self):
        return QSize(self.sizehint)

    def setSizeHint(self, width, height=None):
        if isinstance(width, QSize) and height is None:
            self.sizehint = width
        else:
            self.sizehint = QSize(width, height)

    def setRowHeight(self, rowheight):
        self.rowheight = rowheight
        self.bestFit()

    def resizeHeight(self):
        if self.rowheight < 0:
            return
        if self.widget() is None:
            return

        bestheight = self.widget().sizeHint().height()
        rows = ((bestheight - 1) / self.rowheight) + 1
        bestheight = rows * self.rowheight

        viewheight = self.size().height()

        if self.horizontalScrollBarPolicy() != Qt.ScrollBarAlwaysOff and self.horizontalScrollBar().isVisible():
            viewheight -= self.horizontalScrollBar().height()

        if bestheight <= viewheight:
            self.widget().setFixedHeight(viewheight)
            return

        rows = viewheight / self.rowheight
        bestheight += viewheight - (rows * self.rowheight)
        self.widget().setFixedHeight(bestheight)

        self.verticalScrollBar().setSingleStep(self.rowheight)
        self.verticalScrollBar().setPageStep(self.rowheight * rows)

    def bestFit(self):

        if self.rowheight < 0:
            return

        if self.widget() is None:
            return

        bestheight = self.widget().sizeHint().height()
        minheight = self.verticalScrollBar().sizeHint().height()
        rows = ((bestheight - 1) / self.rowheight) + 1
        bestheight += bestheight - (rows * self.rowheight)

        if self.horizontalScrollBarPolicy() == Qt.ScrollBarAlwaysOn:
            bestheight += self.horizontalScrollBar().sizeHint().height()

        rows = ((minheight - 1) / self.rowheight) + 1
        minheight += minheight - (rows * self.rowheight)

        if self.verticalScrollBarPolicy() != Qt.ScrollBarAlwaysOff:
            minheight += self.verticalScrollBar().sizeHint().height()

        self.setMinimumHeight(minheight)
        self.setMaximumHeight(bestheight)
        bestwidth = self.widget().sizeHint().width()

        if self.verticalScrollBarPolicy() != Qt.ScrollBarAlwaysOff:
            bestwidth += self.verticalScrollBar().sizeHint().width()

        self.setSizeHint(bestwidth, bestheight)
        self.resizeHeight()

    def resizeEvent(self, e):
        self.resizeHeight()
        QScrollArea.resizeEvent(self, e)

    def positionNearest(self, value):
        row = (value + self.rowheight / 2) / self.rowheight
        self.verticalScrollBar().setSliderPosition(row * self.rowheight)
