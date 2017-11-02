# coding = utf-8

# CraftBar.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import Qt, QVariant, QModelIndex
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QDialog, QHeaderView, QFileDialog
from B_CraftBar import *
from Character import *
from Constants import *
from SCOptions import SCOptions
import configparser
import glob
import os
import os.path
import re
import SC
import string
import sys


class IniConfigParser(configparser.RawConfigParser):
    def __init__(self, defaults=None):
        configparser.RawConfigParser.__init__(self,defaults)

    def write(self, fp):

        if self._defaults:
            fp.write("[%s]\n" % DEFAULTSECT)

            for (key, value) in list(self._defaults.items()):
                fp.write("%s=%s\n" % (key, str(value).replace('\n', '\n\t')))

            fp.write("\n")

        for section in self._sections:
            fp.write("[%s]\n" % section)

            for (key, value) in list(self._sections[section].items()):

                if key != "__name__":
                    fp.write("%s=%s\n" % (key, str(value).replace('\n', '\n\t')))

            fp.write("\n")

    def optionxform(self, optionstr):
        return optionstr

    
class CraftBar(QDialog, Ui_B_CraftBar):

    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_CraftBar.setupUi(self,self)

        self.model = QStandardItemModel(0, 3)
        self.model.setHeaderData(0, Qt.Horizontal, QVariant('Client'), Qt.DisplayRole)
        self.model.setHeaderData(1, Qt.Horizontal, QVariant('Server'), Qt.DisplayRole)
        self.model.setHeaderData(2, Qt.Horizontal, QVariant('Crafter'), Qt.DisplayRole)
        self.CharList.setModel(self.model)
        self.CharList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CharList.setShowGrid(False)
        self.CharList.verticalHeader().hide()
        self.CharList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.CharList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.CharList.setSelectionMode(QAbstractItemView.SingleSelection)

        if name:
            self.setObjectName(name)

        if modal:
            self.setModal(modal)

        self.parent = parent
        self.gemcount = 0
        self.piecelist = { }

        self.ItemSelect = [
            self.ChestSelect, self.ArmsSelect, self.HeadSelect,
            self.LegsSelect, self.FeetSelect, self.HandsSelect,
            self.SpareSelect, self.RHSelect, self.LHSelect,
            self.THSelect, self.RangedSelect]

        self.items = [
            'Chest', 'Arms', 'Head', 'Legs', 'Feet', 'Hands',
            'Spare', 'Right Hand', 'Left Hand', '2 Handed', 'Ranged']

        self.reini = re.compile('(\w+)-(\d+)\.ini$')
        self.resec = re.compile('\[(\w+)\]')
        self.rectl = re.compile('[Hh]otkey_(\d+)=44,13,')
        
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.PathSelectButton.setFixedWidth(50)
            self.PathSelectButton.setFixedHeight(32)

        self.PathSelectButton.clicked.connect(self.openFileDialog)
        self.PushButton19.clicked.connect(self.accept)
        self.LoadGemsButton.clicked.connect(self.loadGems)
        self.DaocPath.textChanged[str].connect(self.findPath)
        self.HotbarNum.valueChanged[int].connect(self.hotbarNumChanged)
        self.HotbarRow.valueChanged[int].connect(self.hotbarNumChanged)
        self.HotbarPos.valueChanged[int].connect(self.hotbarNumChanged)
        self.CharList.selectionModel().selectionChanged.connect(self.charChanged)

        for i in range(0, len(self.ItemSelect)):
            self.ItemSelect[i].clicked.connect(self.pieceBoxChanged)
            item = self.parent.itemattrlist[self.items[i]]

            # Changed from
            # while item.ActiveState == 'drop' and item.__next__ is not None:
            #     item = item.__next__

            while item.ActiveState == 'drop' and item.next is not None:
                item = item.next


            if item.ActiveState == 'drop':
                self.ItemSelect[i].setEnabled(False)
                continue

            done = True
            unused = True

            for slot in item.slots():

                 if slot.crafted():
                     unused = False

                     if slot.makes() == "0":
                         done = False
                         break

            if unused:
                self.ItemSelect[i].setEnabled(False)
                continue

            if not done and item == self.parent.itemattrlist[self.items[i]]:
                self.ItemSelect[i].setCheckState(Qt.Checked)

        self.HotbarNum.setValue(1)
        self.HotbarRow.setValue(1)
        self.HotbarPos.setValue(1)

        if sys.platform == 'win32':
            path = os.environ.get('APPDATA', '')

            if not os.path.isdir(path):
                path = os.environ.get('HOMEDRIVE', '')
                path = os.path.join(path, os.environ.get('HOMEPATH', ''))
                path = os.path.join(path, 'Application Data')

            path = os.path.join(path, 'Electronic Arts\Dark Age of Camelot')

        else:
            path = os.environ.get('HOME', '')

        self.DaocPath.setText(SCOptions.instance().getOption('DaocIniPath', path))
        self.pieceBoxChanged()
        self.computeGemCount()
        self.computeBarEnd()

    def loadGems(self):
        indexList = self.CharList.selectedIndexes()

        if len(indexList) == 0:
            return

        for idx in indexList:

            if idx.column() == 0:
                server = str(idx.data().toString())

        row = indexList[0].row()
        fileIndex = self.model.index(row, 0)
        filename = str(self.model.data(fileIndex, Qt.UserRole).toString())
        
        self.LoadGemsButton.setEnabled(0)
        self.LoadGemsButton.update()

        f = open(filename, 'r')
        g = open(filename + '.bak', 'w')
        g.write(f.read())
        f.close()
        g.close()
        CP = IniConfigParser()
        CP.read([filename])
        buttons = [-1, -1, -1]
        newbuttons = []
        slotcounter = 0

        while slotcounter <= 99:

            try:
                buttonstr=CP.get('Macros', 'Macro_%d' % slotcounter)

            except:
                if len(newbuttons) < 3:
                    newbuttons.append(slotcounter)

            else:
                buttonval = str.split(buttonstr, ',', 1)

                if len(buttonval) > 1 and buttonval[1][:7].lower() == '/craft ':

                    if buttonval[1][7].lower() in "ahm":
                        buttons['ahm'.index(buttonval[1][7].lower())] = slotcounter

            slotcounter += 1

        for i in (0, 1, 2):

            if buttons[i] < 0 and len(newbuttons) > 0:
                buttons[i] = newbuttons.pop(0)
                CP.set('Macros', 'Macro_%d' % buttons[i], "%s,/craft %s" % (Realms[i][0:3], Realms[i]))
        
        realm = self.parent.realm
        slotcounter = (self.HotbarNum.value() - 1) * 100 + (self.HotbarRow.value() - 1) * 10 + self.HotbarPos.value() - 1
        startslot = slotcounter

        for loc in TabList:
            item = self.piecelist.get(loc, None)

            if item is None:
                continue

            if item.ActiveState == 'player':

                for slot in item.slots():

                    if slot.crafted():
                        gemname = slot.gemName(realm, 3)

                        if slotcounter >= 300:
                            sys.stdout.write("Out of slots!\n")
                            continue

                        if gemname not in HotkeyGems[realm]:
                            for i in (0, 1, 2):
                                gemname = slot.gemName(Realms[i], 3)

                                if realm == Realms[i]:
                                    continue

                                if gemname in HotkeyGems[Realms[i]]:
                                    realm = Realms[i]
                                    buttonstr = 'Hotkey_%d' % buttons[i]

                                    if slotcounter >= 200:
                                        CP.set('Quickbar3', 'Hotkey_%d' % slotcounter - 200, buttonstr)

                                    elif slotcounter >= 100:
                                        CP.set('Quickbar2', 'Hotkey_%d' % slotcounter - 100, buttonstr)

                                    else:
                                        CP.set('Quickbar', 'Hotkey_%d' % slotcounter, buttonstr)

                                    slotcounter += 1
                                    break

                        if gemname in HotkeyGems[realm]:
                            val = HotkeyGems[realm][gemname]
                            buttonstr = '45,13%03d%02d,,-1' % (val, slot.gemLevel() - 1)

                            if slotcounter >= 200:
                                CP.set('Quickbar3', 'Hotkey_%d' % (slotcounter - 200), buttonstr)

                            elif slotcounter >= 100:
                                CP.set('Quickbar2', 'Hotkey_%d' % (slotcounter - 100), buttonstr)

                            else:
                                CP.set('Quickbar', 'Hotkey_%d' % slotcounter, buttonstr)
                            slotcounter += 1

                        else:
                            sys.stdout.write(realm + " has no '" + gemname + "' gem\n")

        f = open(filename, 'w')
        CP.write(f)
        f.close()
        self.LabelNumGems.setText('Number of Quickbar Buttons Loaded:')
        self.NumGems.setText(str(slotcounter - startslot))
        self.HotbarNum.setValue(int(slotcounter / 100) + 1)
        self.HotbarRow.setValue(int(slotcounter / 10) % 10 + 1)
        self.HotbarPos.setValue(slotcounter % 10 + 1)
        self.piecelist = { }

        for ctl in self.ItemSelect:

            if ctl.checkState() == Qt.Checked:
                ctl.setCheckState(Qt.PartiallyChecked)

        self.gemcount = 0
        self.computeBarEnd()

    def findPath(self,rootpath):
        servers = ServerCodes

        if self.parent.euroServers:
            servers = EuroServerCodes

        self.model.removeRows(0, self.model.rowCount())
        rootpath = str(rootpath)

        if os.path.isdir(rootpath):
            filelist = glob.glob(rootpath+'/*-*.ini')
            filelist.extend(glob.glob(rootpath+'/*/*-*.ini'))
            filelist.extend(glob.glob(rootpath+'/*/*/*-*.ini'))

            for file in filelist:
                path = file[len(rootpath)+1:]
                slash = path.rfind('/')
                slash = max(slash, path.rfind('\\'))
                m = self.reini.search(path[(slash+1):])

                if slash < 0:
                    path = ''

                else:
                    path = path[:slash]

                if m is None or m.group(2) not in servers:
                    continue

                # search the section(s) for the pattern
                # [Quickbar[2-3]*]
                # Hotkey_[0-9]*=44,13,
                # corresponding to an SC'er menu quickbar item
                f = open(file, 'r')
                find = 0

                for txt in f:
                    sec = self.resec.match(txt)

                    if sec is not None:

                        if sec.group(1)[:8] == 'Quickbar':
                            find = 1

                        else:
                            find = 0

                        continue

                    if find == 1 and self.rectl.match(txt) is not None:
                        find = 2
                        break

                f.close()

                if find < 2:
                    continue

                server = servers[m.group(2)]
                self.model.insertRows(self.model.rowCount(), 1)
                index = self.model.index(self.model.rowCount()-1, 0, QModelIndex())
                self.model.setData(index, QVariant(path), Qt.DisplayRole)
                self.model.setData(index, QVariant(file), Qt.UserRole)
                index = self.model.index(self.model.rowCount()-1, 1, QModelIndex())
                self.model.setData(index, QVariant(server), Qt.DisplayRole)
                index = self.model.index(self.model.rowCount()-1, 2, QModelIndex())
                self.model.setData(index, QVariant(m.group(1)), Qt.DisplayRole)

                if self.model.rowCount() == 1:
                    self.CharList.selectRow(0)

            if len(filelist) > 0:
                SCOptions.instance().setOption('DaocIniPath', rootpath)

        self.CharList.resizeRowsToContents()

    def openFileDialog(self):
        daocdir = QFileDialog.getExistingDirectory(self, 'Select DAoC Directory', self.DaocPath.text())

        if daocdir:
            self.DaocPath.setText(os.path.abspath(str(daocdir)))

    def computeBarEnd(self):
        pos = (self.HotbarNum.value() - 1) * 100 + (self.HotbarRow.value() - 1) * 10 + self.HotbarPos.value() - 1
        eb = int((pos + self.gemcount - 1) / 100) + 1
        er = int((pos + self.gemcount - 1) / 10) % 10 + 1
        ep = (pos + self.gemcount - 1) % 10 + 1

        if eb > 3 or self.gemcount == 0:
            self.LoadGemsButton.setEnabled(0)
            self.LoadGemsButton.update()
            self.EndBar.setText('-')
            self.EndRow.setText('-')
            self.EndPos.setText('-')

        else:
            self.LoadGemsButton.setEnabled(len(self.CharList.selectedIndexes()) > 0)
            self.LoadGemsButton.update()
            self.EndBar.setText(str(eb))
            self.EndRow.setText(str(er))
            self.EndPos.setText(str(ep))

    def hotbarNumChanged(self,a0):
        self.computeBarEnd()

    def computeGemCount(self):
        self.gemcount = 0

        for loc, item in list(self.piecelist.items()):

            if item.ActiveState == 'player':

                for slot in item.slots():

                    if slot.crafted():
                        self.gemcount += 1

        self.LabelNumGems.setText('Total Number of Gems to Load:')
        self.NumGems.setText(str(self.gemcount))

    def pieceBoxChanged(self):
        self.piecelist = {}

        for i in range(0, len(self.ItemSelect)):

            if self.ItemSelect[i].checkState() == Qt.Checked:
                item = self.parent.itemattrlist[self.items[i]]

                # Changed from
                # while item.ActiveState == 'drop' and item.__next__ is not None:
                #     item = item.__next__

                while item.ActiveState == 'drop' and item.next is not None:
                    item = item.next

                self.piecelist[self.items[i]] = item

        self.computeGemCount()
        self.computeBarEnd()

    def charChanged(self, a1, a2):
        self.computeBarEnd()
