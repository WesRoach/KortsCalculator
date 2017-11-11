# coding = utf-8

# SC.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from Item import *
import re


def formatCost(cost):
    plat = (cost // 10000000) % 1000
    gold = (cost // 10000) % 1000
    silver = (cost // 100) % 100
    copper = cost % 100
    val = ''

    if plat > 0:
        val += '%dp ' % plat

    if gold > 0 or plat > 0:
        val += '%dg ' % gold

    if silver > 0 or gold > 0 or plat > 0:
        val += '%ds ' % silver

    val += '%dc' % copper
    return val


def getGemNameParts(gemname):
    # returns level, liquid prefix and dust suffix
    if gemname == '':
        return ['', '', '']

    gemwords = str.split(gemname, ' ', 3)

    if gemwords[0] not in GemNames:
        return ['', '', '']

    # Prefix (two words distinguish some borked gems)
    if gemwords[1] not in GemLiquids:
        dbg = "Could not find liquid " + gemwords[1] + "\r\n"
        gemwords[1] += " " + gemwords[2]

        if gemwords[1] not in GemLiquids:
            return ['', '', '']

    # Suffix (may include second prefix word) to distinguish dust
    gemwords[2] = " ".join(gemwords[2:])

    if gemwords[2] not in GemDusts:
        dbg = "Could not find dust " + gemwords[2] + "\r\n"
        gemwords[2] = gemwords[3]

        if gemwords[2] not in GemDusts:
            return ['', '', '']

    if len(gemwords) > 3:
        gemwords.pop()

    return gemwords


def gemTypeSort(a, b):
    if MaterialGems.index(a) < MaterialGems.index(b):
        return -1

    elif MaterialGems.index(a) > MaterialGems.index(b):
        return 1

    else:
        return 0


def gemNameSort(a, b):
    essence_re = re.compile("essence", re.IGNORECASE);
    shielding_re = re.compile("shielding", re.IGNORECASE);
    battle_re = re.compile("battle", re.IGNORECASE);
    war_re = re.compile("war", re.IGNORECASE);
    tincture_re = re.compile("tincture", re.IGNORECASE);

    t_a = tincture_re.search(a)
    t_b = tincture_re.search(b)

    if not (t_a is None and t_b is None):

        if t_a is None:
            return -1

        if t_b is None:
            return 1

        return (a > b) - (a < b)

    gemlevel_a, r = str.split(a, ' ', 1)
    gemlevel_b, r = str.split(b, ' ', 1)

    if GemNames.index(gemlevel_a) < GemNames.index(gemlevel_b):
        return -1

    elif GemNames.index(gemlevel_a) > GemNames.index(gemlevel_b):
        return 1

    e_a = essence_re.search(a)
    e_b = essence_re.search(b)

    if e_a is not None:

        if e_b is not None:
            return (a > b) - (a < b)

        else:
            return -1

    s_a = shielding_re.search(a)
    s_b = shielding_re.search(b)

    if s_a is not None:

        if s_b is not None:
            return (a > b) - (a < b)

        elif e_b is not None:
            return 1

        else:
            return -1

    b_a = battle_re.search(a)
    b_b = battle_re.search(b)

    if b_a is not None:

        if s_b is not None:
            return 1

        elif e_b is not None:
            return 1

        elif b_b is not None:
            return (a > b) - (a < b)

        else:
            return -1

    w_a = war_re.search(a)
    w_b = war_re.search(b)

    if w_a is not None:

        if s_b is not None:
            return 1

        elif e_b is not None:
            return 1

        elif b_b is not None:
            return 1

        elif w_b is not None:
            return (a > b) - (a < b)

        else:
            return -1

    return (a > b) - (a < b)
