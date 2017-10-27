# Options.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_Options import *
import re
import types
import XMLHelper
import sys
import os.path
import Constants
from xml.dom.minidom import *
from MyStringIO import UnicodeStringIO
from SCOptions import SCOptions


class Options(QDialog, Ui_B_Options):

    def __init__(self, parent = None ,name = None ,modal = False, fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_Options.setupUi(self, self)

        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.TierPriceTable.verticalHeader().hide()
        self.TierPriceTable.setHorizontalHeaderItem(0, QTableWidgetItem('Tier'))
        self.TierPriceTable.setHorizontalHeaderItem(1, QTableWidgetItem('Price'))

        for i in range(0, self.TierPriceTable.rowCount()):
            item = QTableWidgetItem('%d %s / %s' % (i + 1, Constants.MaterialGems[i], Constants.GemNames[i]))
            item.setFlags(Qt.ItemIsSelectable)
            self.TierPriceTable.setItem(i, 0, item)
            item = QTableWidgetItem('0')
            self.TierPriceTable.setItem(i, 1, item)

        self.TierPriceTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.TierPriceTable.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.TierPriceTable.resizeRowsToContents()

        self.OK.clicked.connect(self.ok_pressed)
        self.Cancel.clicked.connect(self.cancel_pressed)

        # TODO: REMOVE THE PRICING TAB IN OPTIONS
        self.TierPriceTable.itemChanged['QTableWidgetItem *'].connect(self.tierPriceSet)

        self.parent = parent
        skilllist = list(range(1000, -1, -50))
        self.Skill.clear()
        self.Skill.addItems([str(x) for x in skilllist])
        self.TierPricing = {}
        self.loadOptions()

    # TODO: REMOVE EURO SERVERS SINCE THEY DON'T EXIST ANYMORE
    def loadOptions(self):
        li = self.Skill.findText(str(SCOptions.instance().getOption('CrafterSkill', 1000)))
        self.Skill.setCurrentIndex(li)
        self.ShowDoneGems.setChecked(SCOptions.instance().getOption('DontShowDoneGems', False))
        self.loadPriceInfo(SCOptions.instance().getOption('Pricing', {}))
        self.Coop.setChecked(SCOptions.instance().getOption('Coop', False))
        self.IncludeRR.setChecked(SCOptions.instance().getOption('IncludeRRInTotals', False))
        self.ShowScrollingSlots.setChecked(SCOptions.instance().getOption('ShowScrollingSlots', True))
        self.CapDistance.setChecked(SCOptions.instance().getOption('DistanceToCap', False))
        self.HideNonClassSkills.setChecked(SCOptions.instance().getOption('HideNonClassSkills', False))
        self.EuroServers.setChecked(SCOptions.instance().getOption('EuroServers', False))

    # TODO: REMOVE EURO SERVERS SINCE THEY DON'T EXIST ANYMORE
    def saveOptions(self):
        SCOptions.instance().setOption('CrafterSkill', int(str(self.Skill.currentText())))
        SCOptions.instance().setOption('DontShowDoneGems', self.ShowDoneGems.isChecked())
        SCOptions.instance().setOption('Pricing', self.getPriceInfo())
        SCOptions.instance().setOption('Coop', self.Coop.isChecked())
        SCOptions.instance().setOption('IncludeRRInTotals', self.IncludeRR.isChecked())
        SCOptions.instance().setOption('ShowScrollingSlots', self.ShowScrollingSlots.isChecked())
        SCOptions.instance().setOption('DistanceToCap', self.CapDistance.isChecked())
        SCOptions.instance().setOption('HideNonClassSkills', self.HideNonClassSkills.isChecked())
        SCOptions.instance().setOption('EuroServers', self.EuroServers.isChecked())

    def ok_pressed(self):
        self.saveOptions()
        self.done(1)

    def cancel_pressed(self):
        self.done(-1)

    def tierMarkupSet(self, a0):
        st = re.sub('[^\d]', '', str(a0))
        if st == '': st = '0'
        self.TierPrice.setText(st)
        self.TierPricing[str(self.Tier.currentText())] = int(st)

    def tierPriceSet(self, a0):
        st = re.sub('[^\d]', '', str(a0.text()))
        if st == '': st = '0'
        a0.setText(st)
        self.TierPricing[str(a0.row() + 1)] = int(st)

    def getPriceInfo(self):
        pricing = { }
        pricing['CostInPrice'] = self.CostInPrice.isChecked()
        pricing['PPGem'] = int(str(self.PPGem.text()))
        pricing['PPItem'] = int(str(self.PPItem.text()))
        pricing['PPOrder'] = int(str(self.PPOrder.text()))
        pricing['PPInclude'] = self.PPInclude.isChecked()
        pricing['PPLevel'] = int(str(self.PPLevel.text()))
        pricing['PPImbue'] = int(str(self.PPImbue.text()))
        pricing['PPOC'] = int(str(self.PPOC.text()))
        pricing['General'] = float(str(self.GenMarkup.text()))
        pricing['TierInclude'] = self.TierInclude.isChecked()
        pricing['Tier'] = self.TierPricing
        pricing['HourInclude'] = self.HourInclude.isChecked()
        pricing['Hour'] = int(str(self.HourPrice.text()))

        return pricing

    def loadPriceInfo(self, pinfo):
        if 'PPGem' not in pinfo: return

        # do some consistency checks
        if 'Tier' not in pinfo or not isinstance(pinfo['Tier'], dict):
            pinfo['Tier'] = {}

        self.PPGem.setText(str(pinfo['PPGem']))
        self.PPItem.setText(str(pinfo['PPItem']))
        self.PPOrder.setText(str(pinfo['PPOrder']))
        self.GenMarkup.setText(str(pinfo['General']))

        if pinfo['PPInclude']:
            self.PPInclude.setChecked(1)
        else:
            self.PPInclude.setChecked(0)

        self.PPLevel.setText(str(pinfo['PPLevel']))
        self.PPImbue.setText(str(pinfo['PPImbue']))
        self.PPOC.setText(str(pinfo['PPOC']))

        if pinfo['TierInclude']:
            self.TierInclude.setChecked(1)
        else:
            self.TierInclude.setChecked(0)

        self.TierPricing = pinfo['Tier']

        if pinfo['HourInclude']:
            self.HourInclude.setChecked(1)
        else:
            self.HourInclude.setChecked(0)

        self.HourPrice.setText(str(pinfo['Hour']))

        if pinfo['CostInPrice']:
            self.CostInPrice.setChecked(1)
        else:
            self.CostInPrice.setChecked(0)

        for tier, price in list(self.TierPricing.items()):
            tnum = int(tier)
            self.TierPriceTable.item(tnum - 1, 1).setText(str(price))
