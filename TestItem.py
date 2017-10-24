from xml.dom.minidom import *
import XMLHelper
import traceback
import glob
import sys

# This program is designed to collect the data from
# http://ethinarg.com/itemdb/tools/complete.zip
# to ensure the entire breadth of values and fields
# can be recorded

def testTreeXML(itemnode, slots):
    text = ''
    if itemnode.tagName[0:4] == "SLOT":
        global rootslot
        slots = rootslot['SLOT']
    for child in itemnode.childNodes:
        if child.nodeType == Node.TEXT_NODE: continue
        tag = child.tagName
        value = XMLHelper.getText(child.childNodes)
        if not slots.has_key(child.tagName):
            slots[child.tagName] = {}
            slots[child.tagName][None] = {}
            slots[child.tagName][None][None] = {}
        if len(value) > 0:
            if not slots[child.tagName][None][None].has_key(value):
                slots[child.tagName][None][None][value] = None
        for attr, value in child.attributes.items():
            if not slots[child.tagName][None].has_key(attr):
                slots[child.tagName][None][attr] = {}
            if not slots[child.tagName][None][attr].has_key(value):
                slots[child.tagName][None][attr][value] = None
        testTreeXML(child, slots[child.tagName])

def dumptree(slots, depth):
    for key, val in slots.iteritems():
        sys.stdout.write("%*c%s\n" % (depth, ' ', str(key)))
        if val is not None:
            dumptree(val, depth + 2)

if __name__ == '__main__':
    global rootslot
    rootslot = {}
    rootslot['SLOT'] = {}
    rootslot['SLOT'][None] = {}
    rootslot['SLOT'][None][None] = {}
    for filename in glob.glob("items/*/*/*.xml"):
        f = None
        try:
            f = file(filename, 'r')
            docstr = f.read()
            xmldoc = parseString(docstr)
            items = xmldoc.getElementsByTagName('SCItem')
            for item in items:
                testTreeXML(item, rootslot)
        except:
            traceback.print_exc()
            sys.stderr.write("Error reading file: %s\n" % filename)
        if f is not None:
            f.close()
    dumptree(rootslot,1)