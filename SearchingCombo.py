# coding = utf-8

# SearchingCombo.py
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import QItemSelectionModel, QSize, Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QComboBox, QStyle, QStyleOptionComboBox
from ComboListView import ComboListView
import string
import sys


class SearchingCombo(QComboBox):

    def __init__(self, parent=None, name=None, editable=False):
        QComboBox.__init__(self, parent)
        self.setMaxVisibleItems(20)
        self.setEditable(editable)
        self.maxWidth = 0

        if name is not None:
            self.setObjectName(name)

        # save the model, use our view, create a new selection model
        model = self.model()
        oldview = self.view()
        self.setView(ComboListView(self, self))
        self.view().setModel(model)
        self.view().setSelectionModel(QItemSelectionModel(model,self.view()))

    def insertItems(self, idx, lst):
        self.minWidth = 0

        if isinstance(lst, str):
            lst = [lst,]

        if not isinstance(lst, list):
            lst = list(lst)

        QComboBox.insertItems(self, idx, lst)

    def getMinimumWidth(self, items = None):
        fm = QFontMetrics(self.font())
        opt = QStyleOptionComboBox()
        style = self.style()
        mw = self.maxWidth

        if items is not None:

            for str in items:
                opt.currentText = str
                sz = QSize(fm.width(opt.currentText), fm.height())
                mw = max(mw, style.sizeFromContents(QStyle.CT_ComboBox, opt, sz, self).width())

        elif mw == 0 and self.count() > 0:

            for i in range(0, self.count()):
                opt.currentText = self.itemText(i)
                sz = QSize(fm.width(opt.currentText), fm.height())
                mw = max(mw, style.sizeFromContents(QStyle.CT_ComboBox, opt, sz, self).width())

        elif mw == 0:
            opt.currentText = ' '
            sz = QSize(fm.width(opt.currentText), fm.height())
            mw = max(mw, style.sizeFromContents(QStyle.CT_ComboBox, opt, sz, self).width())

        self.maxWidth = mw
        return mw

    def buildItemKeys(self):
        keys = []

        for i in range(0, self.count()):
            txt = str(self.itemText(i))
            keys.append('.'.join([s[0] for s in txt.split()]).upper())
            print(keys)
        return keys

    def keyPressEvent(self, e):
        keycode = e.key()

        if keycode == Qt.Key_Up and (e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) and self.currentIndex() > 0:
            self.setCurrentIndex(self.currentIndex()-1)
            self.activated[int].emit(self.currentIndex())
            self.activated[str].emit(self.currentText())
            e.accept()
            return

        if keycode == Qt.Key_Down and (e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) and self.currentIndex() < self.count()-1:
            self.setCurrentIndex(self.currentIndex()+1)
            self.activated[int].emit(self.currentIndex())
            self.activated[str].emit(self.currentText())
            e.accept()
            return

        if not self.isEditable() and len(e.text()) > 0:
            key = str(e.text()).upper()
            indexlist = []

            if len(key) == 1:
                itemkeys = self.buildItemKeys()

                for i in range(0, len(itemkeys)):

                    if key in itemkeys[i]:
                        indexlist.append(i)

            if len(indexlist):

                if self.currentIndex() >= indexlist[-1]:
                    self.setCurrentIndex(indexlist[0])

                else:
                    i = [x for x in indexlist if x > self.currentIndex()][0]
                    self.setCurrentIndex(i)

                self.activated[int].emit(self.currentIndex())
                self.activated[str].emit(self.currentText())

            e.accept()
            return

        QComboBox.keyPressEvent(self, e)
