# ReportWindow.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_ReportWindow import *
from Character import *
from Constants import *
from HTMLPlus import *
from SC import *
from MyStringIO import UnicodeStringIO
import XMLHelper
import Item
import string
import re
import sys
import os.path
from lxml import etree


class ReportWindow(QDialog, Ui_B_ReportWindow):
    def __init__(self, parent=None, name=None, modal=False, fl=Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_ReportWindow.setupUi(self, self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.PushButton2.clicked.connect(self.closeWindow)
        self.PushButton1.clicked.connect(self.saveToHTML)
        self.PushButton1_2.clicked.connect(self.saveToText)

        self.parent = parent
        self.gemnames = None
        self.materials = None
        self.totalcost = 0

    def materialsReport(self, itemlist, showslot=0):
        self.setWindowTitle('Materials Report')
        self.materials = {'Gems': {}, 'Liquids': {}, 'Dusts': {}}
        self.gemnames = {}
        self.totalcost = 0
        for loc, item in itemlist.items():
            if item.ActiveState != 'player':
                continue
            for slot in item.slots():
                if slot.slotType() != 'player':
                    continue
                if int(slot.makes()) > 0 \
                        and showslot == 0 \
                        and self.parent.showDoneInMatsList:
                    continue
                gemtype = slot.type()
                if gemtype == 'Unused':
                    continue
                effect = slot.effect()
                amount = slot.amount()
                for mattype, matl in slot.gemMaterials(self.parent.realm).items():
                    for mat, val in matl.items():
                        if self.materials[mattype].has_key(mat):
                            self.materials[mattype][mat] += val
                        else:
                            self.materials[mattype][mat] = val
                gemname = slot.gemName(self.parent.realm)
                if self.gemnames.has_key(gemname):
                    self.gemnames[gemname] += 1
                else:
                    self.gemnames[gemname] = 1

                cost = slot.gemCost(1)
                self.totalcost += cost
        keys = self.gemnames.keys()
        keys.sort(gemNameSort)
        self.gemnames = map(lambda (x): [x, self.gemnames.get(x)], keys)
        for type, matlist in self.materials.items():
            if type == 'Gems':
                keys = matlist.keys()
                keys.sort(gemTypeSort)
                matlist = map(lambda (x): [x, matlist.get(x)], keys)
            elif type == 'Liquids':
                keys = matlist.keys()
                keys.sort()
                matlist = map(lambda (x): [x, matlist.get(x)], keys)
            elif type == 'Dusts':
                keys = matlist.keys()
                keys.sort()
                matlist = map(lambda (x): [x, matlist.get(x)], keys)
            self.materials[type] = matlist
        self.printMaterials()

    def printMaterials(self):
        materialsstr = '<b>Total Cost:</b> <font color="#FF0000">%s</font>\n' % formatCost(self.totalcost)
        materialsstr += '<hr><center><b>Gem Names</b></center><ul>\n'
        for name, amount in self.gemnames:
            materialsstr += '<li>%d %s</li>\n' % (amount, name)
        materialsstr += '</ul><hr><center><b>Materials List</b></center><dl>\n'
        for type in ['Gems', 'Liquids', 'Dusts']:
            matlist = self.materials[type]
            materialsstr += '<dt><b>%s</b></dt>\n' % type
            for matl, val in matlist:
                materialsstr += '<dd>%d %s</dd>\n' % (val, matl)
        materialsstr += '</dl>\n'
        self.reportHtml = materialsstr
        self.ReportText.setHtml(self.reportHtml)

    def parseConfigReport(self, filename, scxmldoc):
        source = etree.fromstring(scxmldoc.toxml())

        try:
            xslt_xml = etree.parse(filename)
            transform = etree.XSLT(xslt_xml)

            report = transform(source)
            self.reportHtml = str(report)

        except Exception, e:
            QMessageBox.critical(None, 'Error!', 'Error composing report ' + filename + "\n\n" + str(e), 'OK')
            return

        self.setWindowTitle('Configuration Report')
        self.ReportText.setHtml(self.reportHtml)

    def saveToHTML(self):
        filename = os.path.join(self.parent.ReportPath,
                                str(self.parent.CharName.text()) + "_report.html")
        filename = QFileDialog.getSaveFileName(self, "Save HTML Report", filename,
                                               "HTML (*.html *.htm);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.html$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.html'
                f = open(str(filename), 'w')
                f.write('<HTML>' + self.reportHtml + '</HTML>')
                f.close()
                self.parent.ReportPath = os.path.dirname(os.path.abspath(filename))
            except IOError:
                QMessageBox.critical(None, 'Error!',
                                     'Error writing to file: ' + filename, 'OK')

    def saveToText(self):
        filename = os.path.join(self.parent.ReportPath,
                                str(self.parent.CharName.text()) + "_report.txt")
        filename = QFileDialog.getSaveFileName(self, "Save HTML Report", filename,
                                               "Text (*.txt);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.txt$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.txt'
                f = open(str(filename), 'w')
                w = DimWriter(f)
                s = ObtuseFormatter(w)
                p = HTMLPlusParser(s)
                p.feed(self.reportHtml)
                p.close()
                w.flush()
                f.close()
                self.parent.ReportPath = os.path.dirname(os.path.abspath(str(filename)))
            except IOError:
                QMessageBox.critical(None, 'Error!',
                                     'Error writing to file: ' + filename, 'OK')

    def closeWindow(self):
        self.done(1)


class XSLTMessageHandler:
    def __init__(self):
        self.content = ''

    def write(self, msg):
        self.content = self.content + msg

    def getContent(self):
        return self.content
