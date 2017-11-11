# coding = utf-8

# Item.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtWidgets import QMessageBox
from xml.dom.minidom import *
from Constants import *
from MyStringIO import UnicodeStringIO
import re
import SC
import string
import sys
import types
import XMLHelper

class ItemSlot:

    def __init__(self, slottype='player', type='Unused', amount='0', effect='', requirement='', makes='0'):
        self.__dict__ = {'SlotType': str(slottype), 'Type': '', 'Effect': '', 'Amount': '', 'Requirement': '', 'Makes': '', }
        self.setAll(type, amount, effect, requirement, makes)

    def setAll(self, type='Unused', amount='0', effect='', requirement='', makes='0'):
        self.Type = str(type)
        self.Amount = str(amount)
        self.Effect = str(effect)
        self.Makes = str(makes)
        self.Requirement = str(requirement)
        self.fixEffect()
        self.CraftOk = False

    def getAttr(self, attrname):
        if attrname in self.__dict__:
            return self.__dict__[attrname]

    def setAttr(self, attrname, value):
        self.CraftOk = False

        if attrname in self.__dict__:
            self.__dict__[attrname] = str(value)

    def fixEffect(self):
        if self.Type in FixTypeTable:
            self.Type = FixTypeTable[self.Type]

        if self.Type == 'Focus' and len(self.Effect) > 6 and self.Effect[-6:] == ' Focus':
            self.Effect = self.Effect[:-6]

        if self.Effect in FixEffectsTable:
            self.Effect = FixEffectsTable[self.Effect]

    def slotType(self):
        return self.SlotType

    def setSlotType(self, slottype):
        self.CraftOk = False
        self.SlotType = str(slottype)

    def type(self):
        return self.Type

    def setType(self, type):
        self.CraftOk = False

        if type == 'Unused' or type == '':
            self.setAll()

        else:
            self.Type = str(type)

    def amount(self):
        if self.Type == 'Unused': return ''
        return self.Amount

    def setAmount(self, amount):
        self.CraftOk = False

        if amount == '':
            amount = '0'

        self.Amount = str(amount)

    def effect(self):
        return self.Effect

    def setEffect(self, effect):
        self.CraftOk = False
        self.Effect = str(effect)

    def requirement(self):
        return self.Requirement

    def setRequirement(self, requirement):
        self.CraftOk = False
        self.Requirement = str(requirement)

    def makes(self):
        return self.Makes

    def setMakes(self, makes):
        if makes == '':
            makes = '0'

        self.Makes = str(makes)

    def crafted(self):
        if self.CraftOk:
            return True

        if self.Type == '' or self.Type == 'Unused':
            return False

        if self.Effect == '':
            return False

        if not self.SlotType in ('player', 'effect',):
            return False

        if self.gemLevel() < 0:
            return False

        self.CraftOk = True
        return self.CraftOk

    def gemLevel(self):
        if (self.SlotType != 'player' and self.SlotType != 'effect') or self.Type not in ValuesLists:
            return -1

        amountlist = ValuesLists[self.Type]

        if not isinstance(amountlist, tuple):

            if self.Effect in amountlist:
                amountlist = amountlist[self.Effect]

                if isinstance(amountlist[0], tuple):
                    amountlist = amountlist[0]

            elif None in amountlist:
                amountlist = amountlist[None]

            else:
                return -1

        if not self.Amount in amountlist:
            return -1

        return amountlist.index(self.Amount) + 1

    def gemImbue(self):
        mval = 0

        if not self.crafted(): return 0.0

        if self.Type == 'Stat':

            if self.Effect == 'Hits':
                return int(self.Amount) / 4.0

            elif self.Effect == 'Power':
                mval = (int(self.Amount) - 1) * 2.0

            else:
                # return ((int(self.Amount) - 1) / 3.0) * 2.0 + 1.0
                return round((int(self.Amount) - 1) / 1.7)

        elif self.Type == 'Resist':
            mval = (int(self.Amount) - 1) * 2.0

        elif self.Type == 'Skill':
            mval = (int(self.Amount) - 1) * 5.0

        if mval < 1:
            return 1.0

        return mval

    def gemUtility(self, skilltable={}):
        if self.Amount == '0' or self.Amount == '':
            return 0.0

        # Go lambda!
        try:
            return {
                'Stat': lambda x: (self.Effect == 'Hits' and [x / 4.0] or [x * 2.0 / 3.0])[0],
                'Resist': lambda x: x * 2,
                'Power': lambda x: x * 2,
                'Skill': lambda x: x * 5,
                'Focus': lambda x: 1.0
            }[self.Type](float(self.Amount))

        except KeyError:
            return 0

    def gemName(self, realm, parts=7):
        if self.SlotType == 'crafted':
            return '(Crafted Item Bonus)'

        if realm not in GemTables:
            return ''

        if not self.crafted():
            return ''

        amountindex = self.gemLevel() - 1

        if self.Type[-6:] == 'Effect':

            if self.Type not in EffectTypeNames:
                return ''

            if self.Type == 'Charged Effect':
                effectItemNames = StableItemNames

            else:
                effectItemNames = ProcItemNames

            if self.Effect not in effectItemNames:
                return ''

            if not (isinstance(ValuesLists[self.Type], dict) and self.Effect in ValuesLists[self.Type] and isinstance(ValuesLists[self.Type][self.Effect][0], tuple)):
                return ''

            amountindex += ValuesLists[self.Type][self.Effect][2]

            if len(effectItemNames[self.Effect]) > 2 and EffectMetal['All'][amountindex] == "":
                return str.strip(' '.join([EffectTypeNames[self.Type][0],
                                           effectItemNames[self.Effect][2],
                                           "Tincture (Drop)"]))

            else:
                return str.strip(' '.join([effectItemNames[self.Effect][0],
                                           EffectTypeNames[self.Type][0],
                                           effectItemNames[self.Effect][1],
                                           EffectMetal['All'][amountindex],
                                           EffectTypeNames[self.Type][1]]))

        if self.Type not in GemTables[realm]:
            return ''

        gemlist = GemTables[realm][self.Type]

        if self.Effect not in gemlist:
            gemlist = GemTables['All'][self.Type]

            if self.Effect not in gemlist:
                return ''

        if parts == 7:
            return str.strip(' '.join([GemNames[amountindex],gemlist[self.Effect][0],gemlist[self.Effect][1]]))

        else:
            name = ""

            if parts & 4:
                name += GemNames[amountindex] + ' '

            if parts & 2:
                name += gemlist[self.Effect][0] + ' '

            if parts & 1:
                name += gemlist[self.Effect][1] + ' '

            return str.strip(name)

    def gemMaterials(self, realm):
        ret = {'Gems': {}, 'Dusts': {}, 'Liquids': {}}

        if not self.crafted() or realm not in GemTables:
            return ret

        gemindex = self.gemLevel() - 1
        gemlist = GemTables[realm][self.Type]

        if self.Effect not in gemlist:
            gemlist = GemTables['All'][self.Type]

            if self.Effect not in gemlist:
                return ret

        gemdust = gemlist[self.Effect][2]
        gemliquid = gemlist[self.Effect][3]
        ret['Gems'][MaterialGems[gemindex]] = 1

        if self.Effect[0:4] == 'All ':

            if self.Type == 'Focus':
                ret['Gems'][MaterialGems[gemindex]] = 3

            ret['Dusts'][gemdust] = (gemindex * 5) + 1
            ret['Liquids'][gemliquid[0]] = (gemindex * 6) + 2
            ret['Liquids'][gemliquid[1]] = (gemindex * 6) + 2
            ret['Liquids'][gemliquid[2]] = (gemindex * 6) + 2

        elif self.Type == 'Focus' or self.Type == 'Resist':
            ret['Dusts'][gemdust] = (gemindex * 5) + 1
            ret['Liquids'][gemliquid] = gemindex + 1

        else:
            ret['Dusts'][gemdust] = (gemindex * 4) + 1
            ret['Liquids'][gemliquid] = gemindex + 1

        return ret

    def gemMakes(self):
        makes = int(self.Makes)

        if makes == 0:
            makes = 1

        return makes

    def gemCost(self, makes=0):
        if not self.crafted():
            return 0

        if makes <= 0:
            makes = self.gemMakes()

        costindex = self.gemLevel() - 1
        cost = GemCosts[costindex]

        if self.Effect[0:4] == 'All ':

            if self.Type == 'Focus':
                cost = cost * 3 + 180 * costindex

            else:
                cost += 200 + 180 * costindex

        elif self.Type == 'Resist' or self.Type == 'Focus':
            cost += 60 * costindex

        cost *= makes

        return cost

    def gemPrice(self, pricingInfo, makes=0):
        price = 0
        cost = self.gemCost(makes)

        if cost > 0:
            price += int(pricingInfo.get('PPGem', 0) * 10000)

            if pricingInfo.get('TierInclude', 0):
                gemlvl = str(self.gemLevel())
                tierp = pricingInfo.get('Tier', {})
                price += int(float(tierp.get(gemlvl, 0)) * 10000)

            price += int(cost * pricingInfo.get('General', 0) / 100.0)

            if pricingInfo.get('CostInPrice', 1):
                price += cost

        return price

    def asXML(self, slotnode, realm='', rich=False):
        document = Document()

        if self.Type == 'Unused' or self.Type == '':
            savexml = [('Type', 'Unused',), ]

        else:
            savexml = [('Type', self.Type,), ('Effect', self.Effect,), ('Amount', self.Amount,)]

            if self.SlotType == 'player':
                savexml.extend([('Makes', self.Makes,)])

            if len(self.Requirement) > 0:
                savexml.append(('Requirement', self.Requirement,))

            if rich:

                if self.Type[-6:] != "Effect":
                    savexml.append(('Utility', "%.1f" % self.gemUtility(),))

                name = self.gemName(realm)

                if len(name) > 0:
                    savexml.append(('Name', name,))

                if self.crafted():
                    savexml.extend([('Imbue', "%.1f" % self.gemImbue(),), ('Level', str(self.gemLevel()),), ('Cost', str(self.gemCost()),)])

        for attrkey, attrval in savexml:

            if not rich and (attrval == '0' or attrval == ''):
                continue

            valnode = document.createElement(attrkey)
            valtext = document.createTextNode(attrval)
            valnode.appendChild(valtext)
            slotnode.appendChild(valnode)

        if rich and (self.SlotType == 'player') and self.crafted():
            matslist = self.gemMaterials(realm)

            for mattype in ('Gems', 'Dusts', 'Liquids',):
                matnames = list(matslist[mattype].keys())
                matnames.sort()

                for mat in matnames:
                    matsort = MaterialsOrder.index(mat)
                    matnode = document.createElement('Material')
                    matnode.setAttribute('Amount', str(matslist[mattype][mat]))
                    matnode.setAttribute('Type', mattype)
                    matnode.setAttribute('Name', str(mat))
                    matnode.setAttribute('Order', str(matsort))
                    slotnode.appendChild(matnode)


class Item:
    def __init__(self, state='', loc='', realm='All', idx=-1):
        self.__dict__ = {
            'ActiveState': state,
            'Equipped': '0',
            'Location': loc,
            'Realm': realm,
            'Level': '51',
            'ItemQuality': '99',
            'ItemName': '',
            'AFDPS': '',
            'Speed': '',
            'Bonus': '',
            'TYPE': '',
            'SOURCE': '',
            'OFFHAND': '',
            'DAMAGETYPE': '',
            'DBSOURCE': 'kscraft',
            'CLASSRESTRICTIONS': list(),
            'Notes': '',
            'Requirement': '',
            'Time': '0',
            'TemplateIndex': idx,
        }

        self.itemslots = list()
        self.next = None

        if len(loc) > 0:

            if loc in JewelTabList:
                self.Equipped = '1'

            elif loc in PieceTabList:

                if loc in PieceTabList[:8]:
                    self.Equipped = '1'

                else:
                    self.Equipped = '0'

            if len(state) == 0:

                if loc in JewelTabList:
                    self.ActiveState = 'drop'

                elif loc in PieceTabList:
                    self.ActiveState = 'player'

        self.itemslots = self.makeSlots()

    def clearSlots(self):
        self.itemslots = self.makeSlots()

    def makeSlots(self, type=''):
        if type == '':
            type = self.ActiveState

        slots = []

        if type == 'drop':

            for slot in range(0, 12):
                slots.append(ItemSlot(type))

        elif type == 'player':

            for slot in range(0, 4):
                slots.append(ItemSlot(type))

            slots.append(ItemSlot('effect'))
            slots.append(ItemSlot('unused'))

        return slots

    def copy(self):
        item = Item()
        item.ActiveState = self.ActiveState
        item.Location = self.Location
        item.Realm = self.Realm
        item.Equipped = self.Equipped
        item.Level = self.Level
        item.ItemQuality = self.ItemQuality
        item.ItemName = self.ItemName
        item.AFDPS = self.AFDPS
        item.Speed = self.Speed
        item.Bonus = self.Bonus
        item.itemslots = self.itemslots[:]
        item.next = self.next
        return item

    def slot(self, index):
        return self.itemslots[index]

    def slotCount(self):
        return len(self.itemslots)

    def slots(self):
        return list(self.itemslots)

    def loadAttr(self, attrname, attrval):
        if attrname in self.__dict__:
            self.__dict__[attrname] = attrval

    def getAttr(self, attrname):
        if attrname in self.__dict__:
            return self.__dict__[attrname]

    def __repr__(self):
        return str(self.itemslots)

    def itemImbue(self):
        if self.ActiveState != "player": return 0

        try:
            itemlevel = int(self.Level)

        except:
            itemlevel = 0

        if itemlevel < 1 or itemlevel > 51:
            return 0.0

        if (self.Level == self.AFDPS) and (itemlevel % 2 == 1) and (itemlevel > 1) and (itemlevel != 51):
            itemlevel -= 1

        itemimbue = ImbuePts[itemlevel - 1]
        return itemimbue

    def listGemImbue(self):
        if self.ActiveState != 'player':
            return 0.0, 0.0, 0.0, 0.0

        mvals = [self.slot(0).gemImbue(), self.slot(1).gemImbue(), self.slot(2).gemImbue(), self.slot(3).gemImbue()]
        maximbue = max(mvals)

        for j in range(0, len(mvals)):
            if j == mvals.index(maximbue):
                continue

            mvals[j] /= 2.0

        return mvals

    def totalImbue(self):
        if self.ActiveState != "player":
            return 0.0

        return sum(self.listGemImbue())

    def overchargeSuccess(self, crafterSkill=1000):
        itemimbue = self.itemImbue()
        gemimbue = self.listGemImbue()
        imbuepts = sum(gemimbue)
        if imbuepts == 0:
            return 0

        if (imbuepts - itemimbue) >= 6:
            return -100

        elif imbuepts < (itemimbue + 1.0):
            return 100

        success = 34 + ItemQualOCModifiers[self.ItemQuality]
        success -= OCStartPercentages[int(imbuepts - itemimbue)]
        skillbonus = int(crafterSkill / 10)

        if skillbonus > 100:
            skillbonus = 100

        success += skillbonus
        fudgefactor = int(100.0 * ((skillbonus / 100.0 - 1.0) * (OCStartPercentages[int(imbuepts - itemimbue)] / 200.0)))
        success += fudgefactor

        if success > 100:
            success = 100

        return success

    def cost(self):
        cost = 0

        for slot in self.slots():
            cost += slot.gemCost()

        return cost

    def price(self, pricingInfo):
        price = 0
        cost = 0

        for slot in self.slots():
            cost += slot.gemCost()

        if cost == 0:
            return 0

        for slot in self.slots():
            price += slot.gemPrice(pricingInfo, -1)

        if cost > 0:
            imbuepts = self.totalImbue()

            if pricingInfo.get('PPInclude', 0):
                price += int(pricingInfo.get('PPImbue', 0) * 10000 * imbuepts)
                price += int(pricingInfo.get('PPOC', 0) * 10000 * max(0, int(imbuepts - self.itemImbue())))
                price += int(pricingInfo.get('PPLevel', 0) * 10000 * int(self.Level))

            if pricingInfo.get('HourInclude', 0):
                price += int(pricingInfo.get('Hour', 0) * 10000 * int(self.Time) / 60.0)

            price += int(pricingInfo.get('PPItem', 0) * 10000)

        return price

    def utility(self, skilltable={}):
        utility = 0.0

        for slot in self.slots():
            utility += slot.gemUtility(skilltable)

        return utility

    def isEmpty(self):
        for num in range(0, len(self.itemslots)):

            if self.itemslots[num].type() != "Unused":
                return False

        return True

    def asXML(self, pricingInfo=None, crafterSkill=1000, realm=None, rich=False, writeIndex=False):
        if realm is None:
            realm = self.Realm

        document = Document()
        rootnode = document.createElement('SCItem')
        document.appendChild(rootnode)

        fields = [('ActiveState', self.ActiveState,),
                  ('Location', self.Location,),
                  ('Realm', self.Realm,),
                  ('ItemName', self.ItemName,),
                  ('AFDPS', self.AFDPS,),
                  ('Speed', self.Speed,),
                  ('Bonus', self.Bonus,),
                  ('ItemQuality', self.ItemQuality,),
                  ('Equipped', self.Equipped,),
                  ('Level', self.Level,),
                  ('Notes', self.Notes,),
                  ('Requirement', self.Requirement,),
                  ('TYPE', self.TYPE,),
                  ('SOURCE', self.SOURCE,),
                  ('OFFHAND', self.OFFHAND,),
                  ('DAMAGETYPE', self.DAMAGETYPE,),
                  ('DBSOURCE', self.DBSOURCE,), ]

        if self.Time > "0":
            fields.extend([('Time', self.Time,)])

        if writeIndex:
            fields.extend([('TemplateIndex', str(self.TemplateIndex),)])

        if rich:
            imbuevals = self.listGemImbue()
            fields.extend([
                ('Utility', "%.1f" % self.utility(),),
                ('Cost', str(self.cost()),),
                ('Price', str(self.price(pricingInfo)),),
                ('Imbue', "%.1f" % sum(imbuevals),),
                ('ItemImbue', str(self.itemImbue()),),
                ('Success',
                 str(self.overchargeSuccess(crafterSkill)),), ])

        for key, val in fields:

            if not rich and val == '':
                continue

            if not isinstance(val, str):
                sys.stderr.write("%s value %s is not a string\n" % (key, str(val)))

            elem = document.createElement(key)
            elem.appendChild(document.createTextNode(str(val)))
            rootnode.appendChild(elem)

        if len(self.CLASSRESTRICTIONS) > 0:
            elem = document.createElement('CLASSRESTRICTIONS')
            rootnode.appendChild(elem)

            for val in self.CLASSRESTRICTIONS:

                if not isinstance(val, str):
                    sys.stderr.write("CLASSRESTRICTION %s is not a string\n" % str(val))

                classnode = document.createElement('CLASS')
                classnode.appendChild(document.createTextNode(str(val)))
                elem.appendChild(classnode)

        slotnode = None

        for num in range(0, len(self.itemslots)):

            if self.itemslots[num].type() == "Unused":
                continue

            slotnode = document.createElement('SLOT')
            slotnode.setAttribute('Number', str(num))

            if rich or self.itemslots[num].slotType() != self.ActiveState:
                slotnode.setAttribute('Type', str(self.itemslots[num].slotType()))

            self.itemslots[num].asXML(slotnode, realm, rich)

            if rich and num < len(imbuevals) and imbuevals[num] > 0:
                imbuenode = slotnode.getElementsByTagName('Imbue')[0]
                elem = document.createTextNode("%.1f" % imbuevals[num])
                imbuenode.replaceChild(elem, imbuenode.childNodes[0])

            rootnode.appendChild(slotnode)

        return document

    def save(self, filename):
        itemxml = self.asXML()

        if itemxml is None:
            QMessageBox.critical(None, 'Error!', 'There was no item to save!', 'OK')
            return

        try:
            f = open(filename, 'w')

        except IOError:
            QMessageBox.critical(None, 'Error!', 'Error opening file: ' + filename, 'OK')
            return

        f.write(XMLHelper.writexml(itemxml, UnicodeStringIO(), '', '\t', '\n'))
        f.close()

    def load(self, filename, namehint='', silent=0):
        try:
            f = open(filename)

        except IOError:
            if not silent:
                QMessageBox.critical(None, 'Error!', 'Error opening item file: ' + filename, 'OK')

            return -2

        docstr = f.read()

        if re.compile('^<\?xml').match(docstr) is not None:

            try:
                xmldoc = parseString(docstr)
                items = xmldoc.getElementsByTagName('SCItem')
                self.loadFromXML(items[0], namehint)

            except:
                if not silent:
                    QMessageBox.critical(None, 'Error!', 'Error loading item:', 'OK')

                f.close()
                return -1

        else:
            f.seek(0)

            if re.compile('^QUALITY').match(docstr) is None:
                self.importLela(f)

            else:
                self.loadLelaItemFromSCC(0, f.readlines(), self.Realm, True)

        f.close()

    def loadFromXML(self, itemnode, namehint='', convert=False):
        slots = {}

        for child in itemnode.childNodes:

            if child.nodeType == Node.TEXT_NODE:
                continue

            if child.tagName == 'SLOT':
                slotval = child.getAttribute("Number")
                itemslot = self.itemslots[int(slotval)]
                slottype = child.getAttribute("Type")

                if slottype is not None and slottype != '':
                    itemslot.setSlotType(slottype)

                for attr in child.childNodes:

                    if attr.nodeType == Node.TEXT_NODE:
                        continue

                    val = XMLHelper.getText(attr.childNodes)

                    if attr.tagName in itemslot.__dict__:
                        itemslot.setAttr(attr.tagName, val)

                    itemslot.fixEffect()

            elif child.tagName == 'CLASSRESTRICTIONS':

                for classnode in child.childNodes:

                    if classnode.nodeType == Node.TEXT_NODE:
                        continue

                    val = XMLHelper.getText(classnode.childNodes)
                    val = val.strip()

                    if len(val) > 0:
                        self.CLASSRESTRICTIONS.append(val)

            # POSSIBLE BUG
            elif child.tagName[-4:] == "ITEM":
                type = str.lower(child.tagName[:-4])
                slots[type] = self.makeSlots(type)

                if len(slots[type]) == 0:
                    slots.pop(type)

                slotnum = -1
                found = False

                for slot in child.childNodes:

                    if slot.nodeType == Node.TEXT_NODE:
                        continue

                    slot_match = re.compile("SLOT(\d+)").match(slot.tagName)

                    if slot_match is None:
                        slotval = slot.getAttribute("Number")

                        if slotval is None or slotval == '':
                            slotnum += 1

                        else:
                            slotnum = int(slotval)

                    else:
                        slotnum = int(slot_match.group(1))

                    for attr in slot.childNodes:

                        if attr.nodeType == Node.TEXT_NODE:
                            continue

                        val = XMLHelper.getText(attr.childNodes)
                        itemslot = slots[type][slotnum]

                        if attr.tagName in itemslot.__dict__:
                            itemslot.setAttr(attr.tagName, val)

                    if itemslot.type() != 'Unused':
                        found = True

                    itemslot.fixEffect()

                if not (convert or found):
                    slots.pop(type)

            elif child.tagName in self.__dict__:
                setattr(self, child.tagName, XMLHelper.getText(child.childNodes))

                if child.tagName == 'ActiveState':
                    self.itemslots = self.makeSlots()

                elif child.tagName == 'TemplateIndex':
                    self.TemplateIndex = int(self.TemplateIndex)

        if len(slots) > 0:

            if self.ActiveState in slots:
                self.itemslots = slots[self.ActiveState]
                self.itemslots = slots.pop(self.ActiveState)

            if len(slots) > 0:
                self.next = self.copy()
                type = list(slots.keys())[0]
                self.next.Equipped = '0'
                self.next.ActiveState = type
                self.next.itemslots = slots[type]

                if self.ActiveState == 'player':
                    self.ItemName = ''

                if self.next.ActiveState == 'player':
                    self.next.ItemName = ''

        item = self

        while item:

            if item.ActiveState == 'player' and len(item.ItemName) == 0:
                item.ItemName = 'Crafted Item' + namehint

            elif len(item.ItemName) == 0:
                item.ItemName = 'Drop Item' + namehint

            item = item.next
