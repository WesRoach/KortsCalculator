import sys
import re


import Item
from Constants import statList, resistList, skillTable, otherBonusList

f = file(sys.argv[1], 'rU')
lines = f.readlines()
f.close()

time_exp = re.compile(r'\[\d+:\d+:\d+\] ')
begin_exp = re.compile(r'^<Begin Info: (.*?)>')
in_item = False
cur_item = None
pve = False

def updateRealm(lst):
    realm = lst[0]
    print 'realm: %s' % realm

def isPlayerMade():
    print 'player made!'

def stat(lst):
    t = lst[0]
    amount = lst[1]
    print 'stat %s %s' % (t, amount)

def resist(lst):
    t = lst[0]
    amount = lst[1]
    print 'resist %s %s' % (t, amount)

def power(lst):
    t = lst[0]
    amount = lst[1]
    print 'power %s %s' % (t, amount)

def hits(lst):
    t = lst[0]
    amount = lst[1]
    print 'hits %s %s' % (t, amount)

def skill(lst):
    t = lst[0]
    amount = lst[1]
    print 'skill %s %s' % (t, amount)

def outOfItem():
    global in_item
    print 'out'
    in_item = False
    
def otherBonus(lst):
    t = lst[0]
    amount = lst[1]

    oblist = map(lambda x: x[0].lower(), otherBonusList)
    words = t.split(' ')
    if t.endswith('bonus cap'):
        if t.find(' attribute ') != -1:
            print '%s cap increase: %s' % (words[0], amount)
        elif t.find('hit points ') != -1:
            print 'hits cap increase: %s' % amount
    if t in oblist:
        print 'other bonus: %s %s' % (t, amount)

        


def af(lst):
    amount = lst[0]
    print 'af %s' % amount

def qua(lst):
    amount = lst[0]
    print 'qua %s' % amount

def dps(lst):
    amount = lst[0]
    print 'dps %s' % amount

def speed(lst):
    amount = lst[0]
    print 'speed %s' % amount

print '|'.join(list(statList) + list(resistList))
re_table = [
    (re.compile(r'Realm: (\w+)'), 1, updateRealm),
    (re.compile(r'Crafted By:'), 0, isPlayerMade),
    (re.compile(r'- (?:\[L\d+\]: )?(' + r'|'.join(list(statList)) + '): (\d+) pts'),
        2, stat),
    (re.compile(r'- (?:\[L\d+\]: )?(' + r'|'.join(list(resistList)) + '): (\d+)%'),
        2, resist),
    (re.compile(r'- (?:\[L\d+\]: )?(' + r'|'.join(
        skillTable['Albion'].keys() + skillTable['Midgard'].keys() +
        skillTable['Hibernia'].keys()) + '): (\d+) pts'),
        2, skill),
    (re.compile(r'- (?:\[L\d+\]: )?(Hits): (\d+) pts'), 2, hits),
    (re.compile(r'- (?:\[L\d+\]: )?(Power): (\d+)'), 2, power),
    (re.compile(r'<End Info>'), 0, outOfItem),
    (re.compile(r'(?:\[L\d+\]: )?Bonus to (.*?): (\d+)'), 2, otherBonus),
    (re.compile(r'- (\d+) Base Factor'), 1, af),
    (re.compile(r'- (\d+)% Quality'), 1, qua),
    (re.compile(r'- ([0-9.]+) Base DPS'), 1, dps),
    (re.compile(r'- ([0-9.]+) Weapon Speed'), 1, speed),
]

print re_table


for line in lines:
    line = time_exp.sub('', line)
    if not in_item:
        m = begin_exp.match(line)
        if m:
            item_name = m.group(1)
            print item_name
            in_item = True
    else:
        pve = (line.find('PvE Only') != -1)
        for exp, groups, func in re_table:
            m = exp.match(line)
            if m:
                if groups > 0:
                    func(m.groups()[0:groups])
                else:
                    func()
                break

        
        
    
