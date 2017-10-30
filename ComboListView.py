# coding=utf-8

# ComboListView.py: Kort's Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
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
        if qVersion() < '4.2':
            QListView.showEvent(self, e)
        return
        e.accept()
        model = self.model()
        rows = model.rowCount()
        col = self.modelColumn()
        mx = 0

        for i in range(0, rows):
            item = model.item(i, col)
            mx = max(mx, item.sizeHint().width())
        if rows:
            sz = QSize(mx, item.sizeHint().height())
        for i in range(0, rows):
            model.item(i, col).setSizeHint(sz)

        mx += 25

        if mx > self.parent().parent().width():
            self.setGeometry(self.pos().x(), self.pos().y(), mx, self.height())
            self.parent().setGeometry(self.parent().pos().x(), self.parent().pos().y(), mx, self.parent().height())

        QListView.showEvent(self, e)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Tab or e.key() == Qt.Key_Backtab:
            e.accept()
            ev = QKeyEvent(QEvent.KeyPress, e.key(), e.modifiers(), e.text(), e.isAutoRepeat(), e.count())
            QApplication.postEvent(self.parent().parent(), ev)
            return

        QListView.keyPressEvent(self, e)

    def event(self, e):
        if e.type() == QEvent.ShortcutOverride and e.key() == Qt.Key_Escape:
            self.clearSelection()
        return QListView.event(self, e)

    def focusOutEvent(self, e):
        # from the focus events posted at our combobox, we must...
        combobox = self.parent().parent()
        if e.reason() in (Qt.TabFocusReason, Qt.BacktabFocusReason,):
            combobox.hidePopup()
        idxs = self.selectedIndexes()
        if len(idxs) > 0 and combobox.currentIndex() != idxs[0].row():
            combobox.setCurrentIndex(idxs[0].row())
            combobox.activated[int].emit(combobox.currentIndex())
            combobox.activated[str].emit(combobox.currentText())
        QListView.focusOutEvent(self, e)
