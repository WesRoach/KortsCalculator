# coding = utf-8

# ItemList.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtWidgets import QApplication, QFileDialog, QListWidget
from Character import *
from Constants import *
from Item import *
from SCOptions import SCOptions
import sys


class ItemPreview(QListWidget):
    def __init__(self, parent, realm, charclass):
        QListWidget.__init__(self, None)
        parent.layout().addWidget(self, 1, 4, 1, 2)
        self.realm = realm
        self.charclass = charclass

    def preview(self, filename):
        self.clear()
        item = Item(realm=self.realm)
        if item.load(str(filename), silent = 1) == -2:
            return
        stattext = []
        for slot in item.slots():
            gemtype = slot.type()
            if not gemtype or gemtype == 'Unused':
                continue
            statstr = slot.effect() + ' ' + slot.amount()
            if slot.type() == 'Resist' or slot.type() == 'Focus' or slot.type() == 'Cap Increase':
                statstr += ' '+ slot.type()
            stattext.append(statstr)
        classinfo = AllBonusList[self.realm][self.charclass]
        listtext = [
            str(item.ItemName),
            "Level: %s   Quality: %s" % (item.Level, item.ItemQuality),
            "AF/DPS: %s   Speed: %s" % (item.AFDPS, item.Speed),
            "Utility: %.1f   Bonus: %s" 
                    % (item.utility(classinfo), item.Bonus),
        ]
        self.addItems(listtext)
        self.addItems(stattext)

    
class ItemListDialog(QFileDialog):
    def __init__(self, parent = None, caption = None, itemdir = None, filter = None, realm = None, charclass = None):
        QFileDialog.__init__(self, parent, caption, itemdir, filter)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setFileMode(QFileDialog.ExistingFile)
        self.setViewMode(QFileDialog.List)
        self.preview = ItemPreview(self, realm, charclass)

        self.currentChanged[str].connect(self.onCurrentChanged)
        self.finished[int].connect(self.finish)

        self.loadOptions()

    def onCurrentChanged(self, file):
        self.preview.preview(file)

    def finish(self, res):
        self.saveOptions()

    def saveOptions(self):
        SCOptions.instance().setOption('ItemListX', self.pos().x())
        SCOptions.instance().setOption('ItemListY', self.pos().y())
        SCOptions.instance().setOption('ItemListW', self.width())
        SCOptions.instance().setOption('ItemListH', self.height())

    def loadOptions(self):
        x = SCOptions.instance().getOption('ItemListX', self.pos().x())
        y = SCOptions.instance().getOption('ItemListY', self.pos().y())
        w = SCOptions.instance().getOption('ItemListW', self.width())
        h = SCOptions.instance().getOption('ItemListH', self.height())

        screenWidth = QApplication.desktop().width()
        screenHeight = QApplication.desktop().height()

        if w < 100:
            w = 780
        if h < 100:
            w = 490

        if w > screenWidth:
            w = 780
        if h > screenHeight:
            h = 490

        if x < 20 or x > (screenWidth - 20):
            x = 20
        if y < 20 or y > (screenHeight - 20):
            y = 20

        self.resize(w, h)
        self.move(x, y)
        self.updateGeometry()


