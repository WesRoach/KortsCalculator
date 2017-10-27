# ChooseSlot.py: Kort's Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import Qt, QMetaObject
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QSizePolicy
from PyQt5.QtWidgets import QRadioButton, QVBoxLayout, QDialogButtonBox
import sys

class Ui_ChooseSlot(object):
    def setupUi(self, ChooseSlot, buttonlabels):
        ChooseSlot.setObjectName("ChooseSlot")
        ChooseSlot.setWindowModality(Qt.ApplicationModal)

        sizePolicy = QSizePolicy(QSizePolicy.Policy(0),QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChooseSlot.sizePolicy().hasHeightForWidth())
        ChooseSlot.setSizePolicy(sizePolicy)

        self.vboxlayout = QVBoxLayout(ChooseSlot)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QVBoxLayout()
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.Label = QLabel(ChooseSlot)
        self.Label.setObjectName("Label")
        self.vboxlayout1.addWidget(self.Label)

        self.Buttons = []
        for button in buttonlabels:
            self.Buttons.append(QRadioButton(ChooseSlot))
            self.Buttons[-1].setObjectName("Button[%d]" % (len(self.Buttons) - 1))
            self.Buttons[-1].setText(QApplication.translate("ChooseSlot", button, None, QApplication.UnicodeUTF8))
            self.vboxlayout1.addWidget(self.Buttons[-1])
        if len(self.Buttons):
            self.Buttons[0].setChecked(Qt.Checked)

        self.vboxlayout.addLayout(self.vboxlayout1)

        self.buttonBox = QDialogButtonBox(ChooseSlot)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChooseSlot)
        ChooseSlot.resize(ChooseSlot.minimumSizeHint())
        QMetaObject.connectSlotsByName(ChooseSlot)

    def retranslateUi(self, ChooseSlot):
        ChooseSlot.setWindowTitle(QApplication.translate("ChooseSlot", "Choose Slot", None, QApplication.UnicodeUTF8))
        self.Label.setText(QApplication.translate("ChooseSlot", "Add Item to Slot", None, QApplication.UnicodeUTF8))

class ChooseSlot(QDialog, Ui_ChooseSlot):
    def __init__(self, parent=None, buttons=tuple()):
        QDialog.__init__(self,parent)
        Ui_ChooseSlot.setupUi(self,self,buttons)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.reject)

    def rejected(self):
        self.done(-1)

    def accepted(self):
        for button in range(0,len(self.Buttons)):
            if self.Buttons[button].isChecked():
                self.done(button)
                return
        self.done(-2)

if __name__ == '__main__':
    app = QApplication([])
    dlg = ChooseSlot(buttons=("Left Ring","Right Ring","Spare"))
    res = dlg.exec_()
    import sys
    sys.stdout.write('Exited with ' + str(res))

