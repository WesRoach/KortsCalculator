# coding = utf-8

# UIXML.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtWidgets import QMessageBox, QFileDialog
from lxml import etree
import os.path


def uixml(scwin, uixslt):
    extidx = uixslt.rindex('.')
    xslt2 = uixslt[:extidx] + "Post" + uixslt[extidx:]
    sctemplate = etree.fromstring(scwin.asXML(True).toxml())

    try:
        xslt_xml = etree.parse(uixslt)
        transform = etree.XSLT(xslt_xml)
        uixmlstr = transform(sctemplate)

        if os.path.exists(xslt2):
            xslt2_xml = etree.parse(xslt2)
            transform2 = etree.XSLT(xslt2_xml)
            uixmlstr = transform2(uixmlstr)

    except Exception as e:
        QMessageBox.critical(None, 'Error!', 'Error with XSLT transform!\n\n'+str(e), 'OK')
        return
        
    path = os.path.join(scwin.ReportPath, 'custom1_window.xml')
    filename, filters = QFileDialog.getSaveFileName(scwin, "Save UI Window as", path, "UI Window XML (*_window.xml);;All Files (*.*)")

    if str(filename) == '':
        return

    try:
        f = open(str(filename), 'w')
        f.write(str(uixmlstr))
        f.close()

    except IOError:
        QMessageBox.critical(None, 'Error!', 
            'Error opening file: ' + filename, 'OK')
        return

