# coding=utf-8

# ComboListView.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import QEvent, QSize, Qt, qVersion
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QListView


class ComboListView(QListView):

    def __init__(self, p, cb):
        QListView.__init__(self, p)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def showEvent(self, e):
        QListView.showEvent(self, e)

    # DOESN'T REALLY SEEM TO DO ANYTHING
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Tab or e.key() == Qt.Key_Backtab:
            e.accept()
            ev = QKeyEvent(QEvent.KeyPress, e.key(), e.modifiers(), e.text(), e.isAutoRepeat(), e.count())
            QApplication.postEvent(self.parent().parent(), ev)

            return

        QListView.keyPressEvent(self, e)

    # DOESN'T REALLY SEEM TO DO ANYTHING
    def event(self, e):
        if e.type() == QEvent.ShortcutOverride and e.key() == Qt.Key_Escape:
            self.clearSelection()

        return QListView.event(self, e)

    # THE FOCUS OUT EVENT MIGHT NOT BE NEEDED ...
    def focusOutEvent(self, e):
        combobox = self.parent().parent()

        if e.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason,):
            combobox.hidePopup()

        idxs = self.selectedIndexes()

        if len(idxs) > 0 and combobox.currentIndex() != idxs[0].row():
            combobox.setCurrentIndex(idxs[0].row())
            combobox.activated[int].emit(combobox.currentIndex())
            combobox.activated[str].emit(combobox.currentText())

        QListView.focusOutEvent(self, e)
