# ScrollArea.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


from PyQt4 import QtGui, QtCore


class ScrollArea(QtGui.QScrollArea):

    def __init__(self, parent = None):
        QtGui.QScrollArea.__init__(self, parent)

        # REMOVE THE BACKGROUND FROM 'QScrollArea'
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(0,0,0,0))
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(QtGui.QColor(0,0,0,0)))
        self.setPalette(palette)

        self.sizehint = QtCore.QSize(QtGui.QScrollArea.sizeHint(self))
        self.rowheight = -1

        self.verticalScrollBar().valueChanged.connect(self.positionNearest)

    def setWidget(self, widget):
        QtGui.QScrollArea.setWidget(self, widget)
        self.bestFit()

    def sizeHint(self):
        return QtCore.QSize(self.sizehint)

    def setSizeHint(self, width, height = None):
        if isinstance(width, QtCore.QSize) and height is None:
            self.sizehint = width
        else:
            self.sizehint = QtCore.QSize(width, height)

    def setRowHeight(self, rowheight):
        self.rowheight = rowheight
        self.bestFit()

    def resizeHeight(self):
        if self.rowheight < 0: return
        if self.widget() is None: return

        bestheight = self.widget().sizeHint().height()
        rows = ((bestheight - 1) / self.rowheight) + 1
        bestheight = rows * self.rowheight

        viewheight = self.size().height()

        if self.horizontalScrollBarPolicy() != QtCore.Qt.ScrollBarAlwaysOff and self.horizontalScrollBar().isVisible():
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

        if self.horizontalScrollBarPolicy() == QtCore.Qt.ScrollBarAlwaysOn:
            bestheight += self.horizontalScrollBar().sizeHint().height()

        rows = ((minheight - 1) / self.rowheight) + 1
        minheight += minheight - (rows * self.rowheight)

        if self.verticalScrollBarPolicy() != QtCore.Qt.ScrollBarAlwaysOff:
            minheight += self.verticalScrollBar().sizeHint().height()

        self.setMinimumHeight(minheight)
        self.setMaximumHeight(bestheight)
        bestwidth = self.widget().sizeHint().width()

        if self.verticalScrollBarPolicy() != QtCore.Qt.ScrollBarAlwaysOff:
            bestwidth += self.verticalScrollBar().sizeHint().width()

        self.setSizeHint(bestwidth, bestheight)
        self.resizeHeight()

    def resizeEvent(self, e):
        self.resizeHeight()
        QtGui.QScrollArea.resizeEvent(self, e)

    def positionNearest(self, value):
        row = (value + self.rowheight / 2) / self.rowheight
        self.verticalScrollBar().setSliderPosition(row * self.rowheight)
