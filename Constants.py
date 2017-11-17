# coding = utf-8

# constants.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license

__all__ = [
    'ScVersion',
    'GemLists', 'DropLists', 'CraftedLists',
    'TypeList', 'EffectTypeList', 'DropTypeList', 'CraftedTypeList',
    'ValuesLists', 'CraftedValuesLists',
    'QualityValues', 'ImbuePts',
    'OCStartPercentages', 'ItemQualOCModifiers',
    'FileExt', 'Caps', 'HighCapBonusList', 'BodyHitOdds',
    'GemTables', 'GemDusts', 'GemLiquids', 'GemSubName', 'MaterialsOrder',
    'GemNames', 'MaterialGems', 'GemCosts', 'RemakeCosts',
    'EffectTypeNames', 'ProcItemNames', 'StableItemNames', 'EffectMetal',
    'FixTypeTable', 'FixEffectsTable', 'HotkeyGems', 'ImbueMultipliers',
    'ShieldTypes',
    'TabList', 'PieceTabList', 'JewelTabList',
    'ArmorTabList', 'WeaponTabList', 'FocusTabList',
]

ScVersion = "Kort's Spellcrafting Calulator 3.0.0"

from Character import *
from tuple2 import *
from dict2 import *
import sys

TypeList = t2((
    'Unused',
    'Stat',
    'Resist',
    'Focus',
    'Skill',
))

# This list is only for the 5th Alchemy imbue slot
#
EffectTypeList = t2((
    'Offensive Effect',
    'Reactive Effect',
    'Charged Effect',
))

# Duplicate the TypeList, plus non-craftable categories
#
DropTypeList = t2(
    TypeList + (
        'Cap Increase',
        'PvE Bonus',
        'Other Bonus',
    ) + EffectTypeList + (
        'Other Effect',
    ))

EffectTypeList = t2((
                        'Unused',
                    ) + EffectTypeList
                    )

# Placeholder
unusedTable = d2({})

unusedList = t2()

unusedValues = t2()

GemLiquids = d2({
    'Fiery': 'Draconic Fire',
    'Earthen': 'Treant Blood',
    'Vapor': 'Swamp Fog',
    'Airy': 'Air Elemental Essence',
    'Heated': 'Heat From an Unearthly Pyre',
    'Icy': 'Frost From a Wasteland',
    'Watery': 'Leviathan Blood',
    'Dusty': 'Undead Ash and Holy Water',
    'Fire': 'Draconic Fire',
    'Earth': 'Treant Blood',
    'Vapor': 'Swamp Fog',
    'Air': 'Air Elemental Essence',
    'Heat': 'Heat From an Unearthly Pyre',
    'Ice': 'Frost From a Wasteland',
    'Water': 'Leviathan Blood',
    'Dust': 'Undead Ash and Holy Water',
    'Ashen': 'Undead Ash and Holy Water',
    'Vacuous': 'Swamp Fog',
    'Salt Crusted': 'Mystic Energy',
    'Steaming Spell': 'Swamp Fog',
    'Steaming Nature': 'Swamp Fog',
    'Steaming Fervor': 'Heat From an Unearthly Pyre',
    'Oozing': 'Treant Blood',
    'Mineral Encrusted': 'Heat From an Unearthly Pyre',
    'Lightning Charged': 'Leviathan Blood',
    'Molten Magma': 'Leviathan Blood',
    'Light': 'Sun Light',
    'Blood': 'Giant Blood',
    'Mystical': 'Mystic Energy',
    'Mystic': 'Mystic Energy',
    'Brilliant': ('Draconic Fire', 'Mystic Energy', 'Treant Blood'),
    'Finesse': ('Draconic Fire', 'Mystic Energy', 'Treant Blood'),
    'Ethereal Spell': 'Swamp Fog',
    'Phantasmal Spell': 'Leviathan Blood',
    'Spectral Spell': 'Draconic Fire',
    'Ethereal Arcane': 'Leviathan Blood',
    'Phantasmal Arcane': 'Draconic Fire',
    'Spectral Arcane': 'Air Elemental Essence',
    'Aberrant': 'Treant Blood',
    'Embracing': 'Frost From a Wasteland',
    'Shadowy': 'Swamp Fog',
    'Blighted Primal': 'Air Elemental Essence',
    'Blighted Rune': 'Undead Ash and Holy Water',
    'Valiant': 'Swamp Fog',
    'Unholy': 'Air Elemental Essence',
    'Glacial': 'Frost From a Wasteland',
    'Cinder': 'Draconic Fire',
    'Radiant': 'Sun Light',
    'Magnetic': 'Mystic Energy',
    'Clout': 'Giant Blood',
})

GemDusts = d2({
    'Essence Jewel': 'Essence of Life',
    'Shielding Jewel': 'Ground Draconic Scales',
    'Spell Stone': 'Ground Draconic Scales',
    'Sigil': 'Ground Draconic Scales',
    'Rune': 'Ground Draconic Scales',
    'Chaos Rune': 'Soot From Niflheim',
    'Battle Jewel': 'Bloodied Battlefield Dirt',
    'War Rune': 'Ground Giant Bone',
    'Primal Rune': 'Ground Vendo Bone',
    'Evocation Sigil': 'Ground Cave Crystal',
    'Fervor Sigil': 'Ground Blessed Undead Bone',
    'War Sigil': 'Ground Caer Stone',
    'Nature Spell Stone': 'Fairy Dust',
    'War Spell Stone': 'Unseelie Dust',
    'Arcane Spell Stone': 'Other Worldly Dust',
})

type = 'Essence Jewel'

statTableOrdered = (
    ('Strength', 'Fiery',),
    ('Constitution', 'Earthen',),
    ('Dexterity', 'Vapor',),
    ('Quickness', 'Airy',),
    ('Intelligence', 'Dusty',),
    ('Piety', 'Watery',),
    ('Charisma', 'Icy',),
    ('Empathy', 'Heated',),
    ('Power', 'Mystical',),
    ('Hits', 'Blood',),
)

statTable = dict(statTableOrdered)
for (key, val) in list(statTable.items()):
    statTable[key] = (val, type, GemDusts[type], GemLiquids[val],)
statTable = d2(statTable)

statList = t2([x[0] for x in statTableOrdered])

del statTableOrdered

statValues = t2(('2', '5', '8', '11', '14', '17', '20', '23', '26', '29',))

hitsValues = t2(('4', '12', '20', '28', '36', '44', '52', '60', '68', '76',))

powerValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17'))

# Duplicate the Stat lists as DropStat lists, add non-craftable 'Acuity' stat
#
dropStatList = t2(statList + (
    'Acuity',
))

dropStatTable = dict().fromkeys(dropStatList)

type = 'Shielding Jewel'

resistTableOrdered = (
    ('Body', 'Dusty',),
    ('Cold', 'Icy',),
    ('Heat', 'Heated',),
    ('Energy', 'Light',),
    ('Matter', 'Earthen',),
    ('Spirit', 'Vapor',),
    ('Crush', 'Fiery',),
    ('Thrust', 'Airy',),
    ('Slash', 'Watery',),
)

resistTable = dict(resistTableOrdered)
for (key, val) in list(resistTable.items()):
    resistTable[key] = (val, type, GemDusts[type], GemLiquids[val])
resistTable = d2(resistTable)

resistList = t2([x[0] for x in resistTableOrdered])

resistValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17',))

# Duplicate the Resist lists as DropResist lists, add non-craftable 'Essence' stat
#
dropResistList = t2(resistList + (
    'Essence',
))

dropResistTable = dict().fromkeys(dropResistList)

del resistTableOrdered

focusTable = {

    'Albion': {

        'All Spell Lines': ('Brilliant', 'Sigil',),
        'Body Magic': ('Heat', 'Sigil',),
        'Cold Magic': ('Ice', 'Sigil',),
        'Death Servant': ('Ashen', 'Sigil',),
        'Deathsight': ('Vacuous', 'Sigil',),
        'Earth Magic': ('Earth', 'Sigil',),
        'Fire Magic': ('Fire', 'Sigil',),
        'Matter Magic': ('Dust', 'Sigil',),
        'Mind Magic': ('Water', 'Sigil',),
        'Painworking': ('Salt Crusted', 'Sigil',),
        'Spirit Magic': ('Vapor', 'Sigil',),
        'Wind Magic': ('Air', 'Sigil',),
    },

    'Hibernia': {

        'All Spell Lines': ('Brilliant', 'Spell Stone',),
        'Arboreal Path': ('Steaming', 'Spell Stone',),
        'Creeping Path': ('Oozing', 'Spell Stone',),
        'Enchantments': ('Vapor', 'Spell Stone',),
        'Ethereal Shriek': ('Ethereal', 'Spell Stone',),
        'Light': ('Fire', 'Spell Stone',),
        'Mana': ('Water', 'Spell Stone',),
        'Mentalism': ('Earth', 'Spell Stone',),
        'Phantasmal Wail': ('Phantasmal', 'Spell Stone',),
        'Spectral Guard': ('Spectral', 'Spell Stone',),
        'Verdant Path': ('Mineral Encrusted', 'Spell Stone',),
        'Void': ('Ice', 'Spell Stone',),
    },

    'Midgard': {

        'All Spell Lines': ('Brilliant', 'Rune',),
        'Bone Army': ('Ashen', 'Rune',),
        'Cursing': ('Blighted', 'Rune',),
        'Darkness': ('Ice', 'Rune',),
        'Runecarving': ('Heat', 'Rune',),
        'Summoning': ('Vapor', 'Rune',),
        'Suppression': ('Dust', 'Rune',),
    },
}

focusTable['All'] = {}
for realm in Realms:
    for (key, val) in list(focusTable[realm].items()):
        if val[0] in GemLiquids:
            liquid = GemLiquids[val[0]]
        else:
            liquid = GemLiquids[val[0] + " " + val[1].split()[0]]
        focusTable[realm][key] = (val[0], val[1], GemDusts[val[1]], liquid,)
    focusTable[realm] = d2(focusTable[realm])
    focusTable['All'].update(focusTable[realm])
focusTable['All'] = d2(focusTable['All'])
focusTable = d2(focusTable)

focusList = {}
for realm in list(focusTable.keys()):
    focusList[realm] = list(focusTable[realm].keys())
    focusList[realm].sort()
    focusList[realm] = t2(focusList[realm])
focusList = d2(focusList)

focusValues = t2(('5', '10', '15', '20', '25', '30', '35', '40', '45', '50',))

skillTable = {

    'Albion': {

        'All Magic Skills': ('Finesse', 'Fervor Sigil',),
        'All Melee Weapon Skills': ('Finesse', 'War Sigil',),
        'Archery': ('Airy', 'War Sigil',),
        'Aura Manipulation': ('Radiant', 'Fervor Sigil',),
        'Body Magic': ('Heated', 'Evocation Sigil',),
        'Chants': ('Earthen', 'Fervor Sigil',),
        'Cold Magic': ('Icy', 'Evocation Sigil',),
        'Critical Strike': ('Heated', 'Battle Jewel',),
        'Crossbow': ('Vapor', 'War Sigil',),
        'Crush': ('Fiery', 'War Sigil',),
        'Death Servant': ('Ashen', 'Fervor Sigil',),
        'Deathsight': ('Vacuous', 'Fervor Sigil',),
        'Dual Wield': ('Icy', 'War Sigil',),
        'Earth Magic': ('Earthen', 'Evocation Sigil',),
        'Enhancement': ('Airy', 'Fervor Sigil',),
        'Envenom': ('Dusty', 'Battle Jewel',),
        'Flexible': ('Molten Magma', 'War Sigil',),
        'Fire Magic': ('Fiery', 'Evocation Sigil',),
        'Fist Wraps': ('Glacial', 'War Sigil',),
        'Instruments': ('Vapor', 'Fervor Sigil',),
        'Magnetism': ('Magnetic', 'Fervor Sigil',),
        'Matter Magic': ('Dusty', 'Evocation Sigil',),
        'Mauler Staff': ('Cinder', 'War Sigil',),
        'Mind Magic': ('Watery', 'Evocation Sigil',),
        'Painworking': ('Salt Crusted', 'Fervor Sigil',),
        'Parry': ('Vapor', 'Battle Jewel',),
        'Polearm': ('Earthen', 'War Sigil',),
        'Power Strikes': ('Clout', 'Fervor Sigil',),
        'Rejuvenation': ('Watery', 'Fervor Sigil',),
        'Shield': ('Fiery', 'Battle Jewel',),
        'Slash': ('Watery', 'War Sigil',),
        'Smite': ('Fiery', 'Fervor Sigil',),
        'Soulrending': ('Steaming', 'Fervor Sigil',),
        'Spirit Magic': ('Vapor', 'Evocation Sigil',),
        'Staff': ('Earthen', 'Battle Jewel',),
        'Stealth': ('Airy', 'Battle Jewel',),
        'Thrust': ('Dusty', 'War Sigil',),
        'Two Handed': ('Heated', 'War Sigil',),
        'Wind Magic': ('Airy', 'Evocation Sigil',),
    },

    'Hibernia': {

        'All Magic Skills': ('Finesse', 'Nature Spell Stone',),
        'All Melee Weapon Skills': ('Finesse', 'War Spell Stone',),
        'Arboreal Path': ('Steaming', 'Nature Spell Stone',),
        'Archery': ('Airy', 'War Spell Stone',),
        'Aura Manipulation': ('Radiant', 'Nature Spell Stone'),
        'Blades': ('Watery', 'War Spell Stone',),
        'Blunt': ('Fiery', 'War Spell Stone',),
        'Celtic Dual': ('Icy', 'War Spell Stone',),
        'Celtic Spear': ('Earthen', 'War Spell Stone',),
        'Creeping Path': ('Oozing', 'Nature Spell Stone',),
        'Critical Strike': ('Heated', 'Battle Jewel',),
        'Dementia': ('Aberrant', 'Arcane Spell Stone',),
        'Enchantments': ('Vapor', 'Arcane Spell Stone',),
        'Envenom': ('Dusty', 'Battle Jewel',),
        'Ethereal Shriek': ('Ethereal', 'Arcane Spell Stone',),
        'Fist Wraps': ('Glacial', 'War Spell Stone'),
        'Large Weaponry': ('Heated', 'War Spell Stone',),
        'Light': ('Fiery', 'Arcane Spell Stone',),
        'Magnetism': ('Magnetic', 'Nature Spell Stone'),
        'Mana': ('Watery', 'Arcane Spell Stone',),
        'Mauler Staff': ('Cinder', 'War Spell Stone'),
        'Mentalism': ('Earthen', 'Arcane Spell Stone',),
        'Music': ('Airy', 'Nature Spell Stone',),
        'Nature': ('Earthen', 'Nature Spell Stone',),
        'Nurture': ('Fiery', 'Nature Spell Stone',),
        'Parry': ('Vapor', 'Battle Jewel',),
        'Phantasmal Wail': ('Phantasmal', 'Arcane Spell Stone',),
        'Piercing': ('Dusty', 'War Spell Stone',),
        'Power Strikes': ('Clout', 'Nature Spell Stone'),
        'Regrowth': ('Watery', 'Nature Spell Stone',),
        'Scythe': ('Light', 'War Spell Stone',),
        'Shadow Mastery': ('Shadowy', 'Arcane Spell Stone',),
        'Shield': ('Fiery', 'Battle Jewel',),
        'Spectral Guard': ('Spectral', 'Arcane Spell Stone',),
        'Staff': ('Earthen', 'Battle Jewel',),
        'Stealth': ('Airy', 'Battle Jewel',),
        'Valor': ('Airy', 'Arcane Spell Stone',),
        'Vampiiric Embrace': ('Embracing', 'Arcane Spell Stone',),
        'Verdant Path': ('Mineral Encrusted', 'Nature Spell Stone',),
        'Void': ('Icy', 'Arcane Spell Stone',),
    },

    'Midgard': {

        'All Magic Skills': ('Finesse', 'Primal Rune',),
        'All Melee Weapon Skills': ('Finesse', 'War Rune',),
        'Archery': ('Airy', 'War Rune',),
        'Augmentation': ('Airy', 'Chaos Rune',),
        'Aura Manipulation': ('Radiant', 'Primal Rune',),
        'Axe': ('Earthen', 'War Rune',),
        'Battlesongs': ('Airy', 'Primal Rune',),
        'Beastcraft': ('Earthen', 'Primal Rune',),
        'Bone Army': ('Ashen', 'Primal Rune',),
        'Cave Magic': ('Fiery', 'Chaos Rune',),
        'Critical Strike': ('Heated', 'Battle Jewel',),
        'Cursing': ('Blighted', 'Primal Rune',),
        'Darkness': ('Icy', 'Chaos Rune',),
        'Envenom': ('Dusty', 'Battle Jewel',),
        'Fist Wraps': ('Glacial', 'War Rune',),
        'Hammer': ('Fiery', 'War Rune',),
        'Hand To Hand': ('Lightning Charged', 'War Rune',),
        'Hexing': ('Unholy', 'Primal Rune',),
        'Left Axe': ('Icy', 'War Rune',),
        'Magnetism': ('Magnetic', 'Primal Rune',),
        'Mauler Staff': ('Cinder', 'War Rune',),
        'Mending': ('Watery', 'Chaos Rune',),
        'Odin\'s Will': ('Valiant', 'Primal Rune',),
        'Parry': ('Vapor', 'Battle Jewel',),
        'Power Strikes': ('Clout', 'Primal Rune',),
        'Runecarving': ('Heated', 'Chaos Rune',),
        'Shield': ('Fiery', 'Battle Jewel',),
        'Spear': ('Heated', 'War Rune',),
        'Staff': ('Earthen', 'Battle Jewel',),
        'Stealth': ('Airy', 'Battle Jewel',),
        'Stormcalling': ('Fiery', 'Primal Rune',),
        'Summoning': ('Vapor', 'Chaos Rune',),
        'Suppression': ('Dusty', 'Chaos Rune',),
        'Sword': ('Watery', 'War Rune',),
        'Thrown Weapons': ('Vapor', 'War Rune',),
    },
}

skillTable['All'] = {}
for realm in Realms:
    for (key, val) in list(skillTable[realm].items()):
        if val[0] in GemLiquids:
            liquid = GemLiquids[val[0]]
        else:
            liquid = GemLiquids[val[0] + " " + val[1].split()[0]]
        skillTable[realm][key] = (val[0], val[1], GemDusts[val[1]], liquid,)
    skillTable[realm] = d2(skillTable[realm])
    skillTable['All'].update(skillTable[realm])
skillTable['All'] = d2(skillTable['All'])
skillTable = d2(skillTable)

skillList = {}
dropSkillList = {}

for realm in list(skillTable.keys()):
    skills = list(skillTable[realm].keys())
    skills.sort()
    skillList[realm] = t2(skills)
    skills.insert(2, 'All Archery Skills')
    skills.insert(3, 'All Dual Wield Skills')
    # bug - CM Explorer shows +Witchcraft, but no craftable gem
    if realm == 'Midgard':
        skills.append('Witchcraft')
    dropSkillList[realm] = t2(skills)

skillList = d2(skillList)
dropSkillList = d2(dropSkillList)

skillValues = t2(('1', '2', '3', '4', '5', '6', '7', '8',))

capIncreaseList = t2(dropStatList + (
    'AF',
    'Fatigue',
))

otherBonusList = t2((
    '% Power Pool',
    'AF',
    'Archery Damage',
    'Archery Range',
    'Archery Speed',
    'Casting Speed',
    'Duration of Spells',
    'Fatigue',
    'Healing Effectiveness',
    'Melee Damage',
    'Melee Combat Speed',
    'Spell Damage',
    'Spell Piercing',
    'Spell Range',
    'Stat Buff Effectiveness',
    'Stat Debuff Effectiveness',
    'Style Damage',
    'Unique Bonus...',
))

pveBonusList = t2((
    'Arrow Recovery',
    'Bladeturn Reinforcement',
    'Block',
    'Concentration',
    'Damage Reduction',
    'Death Experience Loss Reduction',
    'Defensive',
    'Evade',
    'Negative Effect Duration Reduction',
    'Parry',
    'Piece Ablative',
    'Reactionary Style Damage',
    'Spell Power Cost Reduction',
    'Style Cost Reduction',
    'To Hit',
    'Unique PvE Bonus...',
))

# The tier (dropped), 10, 7, 5 repeat is for newer tinctures that
# jump from level 47 to 35 to 25.  The third elt of the tuples
# in the effects tables is an index to the metals (offset by the
# selected effect).  Drop tinctures have no metal, so they have
# been omitted from these lists.

metalCommon = ("", "Arcanium", "Netherium", "Asterite",
               "Adamantium", "Mithril", "Fine Alloy", "Alloy",
               "", "Arcanium", "Adamantium", "Fine Alloy",)
EffectMetal = d2({
    'All': metalCommon,
    'Albion': metalCommon,
    'Hibernia': ("", "Arcanite", "Netherite", "Diamond",
                 "Sapphire", "Carbide", "Cobolt", "Dolomite",
                 "", "Arcanite", "Sapphire", "Cobolt",),
    'Midgard': metalCommon,
})

ddEffDmgTable = t2(("95", "86", "77", "68", "59", "50", "41",))
ddEffReqLevel = ("47", "43", "40", "35", "30", "25", "20",)

offensiveEffectValues = d2({
    'Direct Damage (Fire)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Cold)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Energy)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Spirit)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Damage Over Time': (t2(("64",)), ("47",), 1,),
    'Self AF Shield': (t2(("75",)), ("47",), 1,),
    'Self Melee Haste': (t2(("20%",)), ("47",), 1,),
    'Self Damage Shield': (t2(("5.1",)), ("47",), 1,),
    'Self Melee Health Buffer': (t2(("150", "50",)), ("48", "47",), 0,),
    'Self Damage Add': (t2(("11.3",)), ("48",), 0,),
    'Lifedrain': (t2(("65",)), ("48",), 0,),
    'Heal': (t2(("80",)), ("48",), 0,),
    'Taunt': (t2(("2", "1",)), ("49", "45",), 1,),
    'Power Drain': (t2(("55", "35",)), ("49", "45",), 1,),
})

ddEffDmgTable = t2(ddEffDmgTable[0:3])

reactiveEffectValues = offensiveEffectValues.copy()
del reactiveEffectValues['Taunt']
reactiveEffectValues.update({
    'Direct Damage (Fire)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Cold)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Energy)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Direct Damage (Spirit)': (ddEffDmgTable, ddEffReqLevel, 1,),
    'Self AF Shield': (t2(("75", "56", "37",)),
                       ("47", "35", "25",), 9,),
    'Self Damage Shield': (t2(("5.1", "3.6", "2.6",)),
                           ("47", "35", "25",), 9,),
    'Self Melee Health Buffer': (t2(("150", "100", "75", "50",)),
                                 ("48", "47", "35", "25",), 8,),
    'Omni Lifedrain': (t2(("100", "75",)), ("49", "45",), 1,),
    'Speed Decrease': (t2(("35%", "30%",)), ("49", "45",), 1,),
})
reactiveEffectValues = d2(reactiveEffectValues)

chargedEffectValues = offensiveEffectValues.copy()
del chargedEffectValues['Heal']
del chargedEffectValues['Taunt']
del chargedEffectValues['Power Drain']
chargedEffectValues.update({
    'Self Melee Haste': (t2(("17%",)), ("47",), 1,),
    'Lifedrain': (t2(("65",)), ("47",), 1,),
    'Str/Con Debuff': (t2(("56",)), ("47",), 1,),
    'Dex/Qui Debuff': (t2(("56",)), ("47",), 1,),
    'Self Damage Add': (t2(("11.3",)), ("47",), 1,),
    'Power Regeneration': (t2(("2",)), ("48",), 0,),
    'Self Acuity Buff': (t2(("75", "56", "37",)),
                         ("47", "35", "25",), 9,),
    'Self AF Shield': (t2(("75", "56", "37",)),
                       ("47", "35", "25",), 9,),
    'Self Damage Shield': (t2(("4.2", "2.9", "2.1",)),
                           ("47", "35", "25",), 9,),
    'Self Melee Attack Speed': (t2(("15%", "10%",)),
                                ("49", "45",), 1,),
    'Power Transfer': (t2(("60",)), ("45",), 2,),
    'Health Transfer': (t2(("70",)), ("45",), 2,),
    'Self Cure Poison': (t2(("1",)), ("49",), 1,),
    'Self Cure Disease': (t2(("1",)), ("49",), 1,),
})
chargedEffectValues = d2(chargedEffectValues)

offensiveEffectList = list(offensiveEffectValues.keys())
offensiveEffectList.sort()
offensiveEffectList = t2(offensiveEffectList)

reactiveEffectList = list(reactiveEffectValues.keys())
reactiveEffectList.sort()
reactiveEffectList = t2(reactiveEffectList)

chargedEffectList = list(chargedEffectValues.keys())
chargedEffectList.sort()
chargedEffectList = t2(chargedEffectList)

otherEffectList = list(chargedEffectList) + [
    'Direct Damage (Body)',
    'Direct Damage (Energy)',
    'Dmg w/Resist Debuff (Fire)',
    'Dmg w/Resist Debuff (Cold)',
    'Dmg w/Resist Debuff (Body)',
    'Dmg w/Resist Debuff (Energy)',
    'Dmg w/Resist Debuff (Matter)',
    'Dmg w/Resist Debuff (Spirit)',
    'Heal',
    'Taunt',
    'Power Drain',
    'Omni Lifedrain',
    'Speed Decrease',
]
otherEffectList.sort()
otherEffectList = t2(otherEffectList + [
    'Unique Effect...',
])

ProcItemNames = d2({
    'Direct Damage (Fire)': t2(('Fiery', 'Fire',)),
    'Direct Damage (Cold)': t2(('', 'Cold',)),
    'Direct Damage (Energy)': t2(('', 'Energy',)),
    'Direct Damage (Spirit)': t2(('', 'Spirit',)),
    'Damage Over Time': t2(('', 'Eroding',)),
    'Self AF Shield': t2(('', 'Hardening',)),
    'Self Damage Shield': t2(('Barbed', 'Shard',)),
    'Self Melee Haste': t2(('', 'Celeric',)),
    'Self Melee Health Buffer': t2(('', 'Ablative', 'Harm Turning')),
    'Self Damage Add': t2(('', '', 'Retributive',)),
    'Lifedrain': t2(('', '', 'Soul Leeching',)),
    'Heal': t2(('', '', 'Mending',)),
    'Taunt': t2(('', 'Provoking',)),
    'Power Drain': t2(('', 'Depletion',)),
    'Omni Lifedrain': t2(('', 'Draining',)),
    'Speed Decrease': t2(('', 'Coil',)),
})

StableItemNames = ProcItemNames.copy()
del StableItemNames['Heal']
del StableItemNames['Taunt']
del StableItemNames['Power Drain']
del StableItemNames['Omni Lifedrain']
del StableItemNames['Speed Decrease']
StableItemNames.update({
    'Direct Damage (Cold)': t2(('Frostbringer', 'Cold',)),
    'Direct Damage (Energy)': t2(('Crackling', 'Energy',)),
    # Most Frenzied, some not (Fine Alloy, Admantium, Netherium)
    'Direct Damage (Spirit)': t2(('Frenzied', 'Spirit',)),
    'Damage Over Time': t2(('Illbane', 'Eroding',)),
    'Self AF Shield': t2(('Hardening', 'Hardening',)),
    'Self Damage Add': t2(('Keen', 'Honing',)),
    'Lifedrain': t2(('Soul Drinker', 'Leeching',)),
    'Self Acuity Buff': t2(('Owl-runed', 'Enlightening',)),
    'Dex/Qui Debuff': t2(('Crippling', 'Crippling',)),
    'Str/Con Debuff': t2(('', 'Withering',)),
    'Power Regeneration': t2(('', '', 'Mind\'s Eye',)),
    'Self Melee Attack Speed': t2(('', 'Greater Celeric',)),
    'Power Transfer': t2(('', 'Transference',)),
    'Health Transfer': t2(('', 'Shifting',)),
    'Self Cure Poison': t2(('', 'Neutralizing',)),
    'Self Cure Disease': t2(('', 'Revivifying',)),
})
StableItemNames = d2(StableItemNames)

EffectTypeNames = d2({
    'Charged Effect': t2(("Stable", "Tincture",)),
    'Reactive Effect': t2(("Reactive", "Armor Tincture",)),
    'Offensive Effect': t2(("Volatile", "Weapon Tincture",)),
})

GemTables = {
    'All': {
        'Unused': unusedTable,
        'Stat': statTable,
        'Resist': resistTable,
    }
}

GemLists = {
    'All': {
        'Unused': unusedList,
        'Stat': statList,
        'Resist': resistList,
        'Charged Effect': chargedEffectList,
        'Offensive Effect': offensiveEffectList,
        'Reactive Effect': reactiveEffectList,
    }
}

DropLists = {
    'All': {
        'Unused': unusedList,
        'Resist': dropResistList,
        'Stat': dropStatList,
        'Cap Increase': capIncreaseList,
        'PvE Bonus': pveBonusList,
        'Other Bonus': otherBonusList,
        'Charged Effect': otherEffectList,
        'Reactive Effect': otherEffectList,
        'Offensive Effect': otherEffectList,
        'Other Effect': otherEffectList,
    }
}

# Only use GemTables['All'] when the specific realm of craft isn't known as
# there are many multi-realm gems which have different names and recipes
#
for realm in Realms:
    GemTables[realm] = {}
    GemTables[realm].update(GemTables['All'])
    GemLists[realm] = {}
    GemLists[realm].update(GemLists['All'])
    DropLists[realm] = {}
    DropLists[realm].update(DropLists['All'])
for realm in list(GemTables.keys()):
    GemTables[realm]['Focus'] = focusTable[realm]
    GemTables[realm]['Skill'] = skillTable[realm]
    GemTables[realm] = d2(GemTables[realm])
    GemLists[realm]['Focus'] = focusList[realm]
    DropLists[realm]['Focus'] = focusList[realm]
    GemLists[realm]['Skill'] = skillList[realm]
    DropLists[realm]['Skill'] = dropSkillList[realm]
    GemLists[realm] = d2(GemLists[realm])
    DropLists[realm] = d2(DropLists[realm])
GemTables = d2(GemTables)
GemLists = d2(GemLists)
DropLists = d2(DropLists)

ValuesLists = d2({
    'Stat': d2({
        None: statValues,
        'Hits': hitsValues,
        'Power': powerValues,
    }),
    'Resist': resistValues,
    'Focus': focusValues,
    'Skill': skillValues,
    'Charged Effect': chargedEffectValues,
    'Offensive Effect': offensiveEffectValues,
    'Reactive Effect': reactiveEffectValues,
    'Unused': unusedValues,
})

CraftedTypeList = t2((
    'Unused',
    'Focus',
    'Skill',
    'Stat',
    'Cap Increase',
    'PvE Bonus',
    'Other Bonus',
    'Charged Effect',
    'Offensive Effect',
))

CraftedValuesLists = d2({
    'Unused': unusedValues,
    'Focus': t2(('50',)),
    'Skill': t2(('3',)),
    'Stat': d2({
        None: t2(('15',)),
        'Hits': t2(('40',)),
    }),
    'Cap Increase': d2({
        None: t2(('5',)),
        'Hits': t2(('40',)),
    }),
    'PvE Bonus': t2(('5',)),
    'PvE Bonus': d2({
        None: t2(('5',)),
        'To Hit': t2(('3',)),
    }),
    'Other Bonus': d2({
        None: t2(('5',)),
        'AF': t2(('10',)),
        'Archery Damage': t2(('2',)),
        'Melee Damage': t2(('2',)),
        'Spell Damage': t2(('2',)),
    }),
    'Charged Effect': t2(("60",)),
    'Offensive Effect': t2(("60", "25", "20",)),
})

CraftedLists = {
    'All': d2({
        'Unused':
            unusedList,
        'Focus': t2((
            'All Spell Lines',
        )),
        'Skill': t2((
            'All Archery Skills',
            'All Dual Wield Skills',
            'All Magic Skills',
            'All Melee Weapon Skills',
            'Shield',
        )),
        'Stat': t2(dropStatList[0:4] + dropStatList[9:]),
        'Cap Increase': t2((
            'Strength',
            'Constitution',
            'Dexterity',
            'Quickness',
            'Acuity',
            'Hits',
            'Power',
            'Fatigue',
        )),
        'Other Bonus': t2((
            '% Power Pool',
            'Fatigue',
            'AF',
            'Archery Damage',
            'Melee Damage',
            'Spell Damage',
            'Duration of Spells',
            'Healing Effectiveness',
            'Stat Buff Effectiveness',
        )),
        'PvE Bonus': t2((
            'Defensive',
            'To Hit',
        )),
        'Charged Effect': t2((
            'Dmg w/Resist Debuff (Fire)',
            'Dmg w/Resist Debuff (Cold)',
            'Dmg w/Resist Debuff (Matter)',
            'Dmg w/Resist Debuff (Spirit)',
        )),
        'Offensive Effect': t2((
            'Direct Damage (Fire)',
            'Direct Damage (Cold)',
            'Direct Damage (Energy)',
            'Dmg w/Resist Debuff (Fire)',
            'Dmg w/Resist Debuff (Cold)',
            'Dmg w/Resist Debuff (Matter)',
            'Dmg w/Resist Debuff (Spirit)',
        )),
    }),
}

for realm in Realms:
    CraftedLists[realm] = CraftedLists['All']
CraftedLists = d2(CraftedLists)

Caps = dict.fromkeys(resistList, 'Resist')
Caps.update(Caps.fromkeys(statList, 'Stat'))
Caps = d2(Caps)

# Bonuses are given as % of level + add constant
# e.g. [ .25,  1] is the level / 4 + 1
#      [   0, 10] is a fixed 10
#      [   4,  0] is the level * 4
#
HighCapBonusList = d2({
    'Death Experience Loss Reduction': (1.00, 0),
    'Hits': (4.00, 0),
    'Hits Cap': (8.00, 0),
    'Stat': (1.50, 0),
    'Focus': (1.00, 0),
    '% Power Pool Cap': (1.00, 0),
    'Power Cap': (1.00, 0),
    'AF Cap': (1.00, 0),
    'AF': (1.00, 0),
    'Arrow Recovery': (1.00, 0),
    'Resist': (.50, 1),
    'Power': (.50, 1),
    'Stat Cap': (.50, 1),
    '% Power Pool': (.50, 0),
    'Stat Buff Effectiveness': (.50, 0),
    'Stat Debuff Effectiveness': (.50, 0),
    'Healing Effectiveness': (.50, 0),
    'Duration of Spells': (.50, 0),
    # Fatigue Cap to Cap Bonus is a total guess :)
    'Fatigue Cap': (.50, 0),
    'Fatigue': (.50, 0),
    'Skill': (.20, 1),
    'PvE Bonus': (.20, 0),
    'Other Bonus': (.20, 0),
})

MaterialGems = t2(('Lo', 'Um', 'On', 'Ee', 'Pal', 'Mon', 'Ros', 'Zo', 'Kath', 'Ra',))

GemCosts = t2((160, 920, 3900, 13900, 40100, 88980, 133000, 198920, 258240, 296860,))

RemakeCosts = t2((120, 560, 1740, 5260, 14180, 30660, 45520, 67680, 87640, 100700,))

GemNames = t2(
    ('Raw', 'Uncut', 'Rough', 'Flawed', 'Imperfect', 'Polished', 'Faceted', 'Precious', 'Flawless', 'Perfect',))

liquidsOrder = (
    'Air Elemental Essence',
    'Draconic Fire',
    'Frost From a Wasteland',
    'Giant Blood',
    'Heat From an Unearthly Pyre',
    'Leviathan Blood',
    'Mystic Energy',
    'Sun Light',
    'Swamp Fog',
    'Treant Blood',
    'Undead Ash and Holy Water',
)

dustsOrder = (
    'Bloodied Battlefield Dirt',
    'Essence of Life',
    'Fairy Dust',
    'Ground Blessed Undead Bone',
    'Ground Caer Stone',
    'Ground Cave Crystal',
    'Ground Draconic Scales',
    'Ground Giant Bone',
    'Ground Vendo Bone',
    'Other Worldly Dust',
    'Soot From Niflheim',
    'Unseelie Dust',
)

MaterialsOrder = t2(MaterialGems + liquidsOrder + dustsOrder)

GemSubName = d2({
    'Stat': 'Essence Jewel',
    'Resist': 'Shielding Jewel',
    'Hits': 'Essence Jewel',
    'Power': 'Essence Jewel',
    'Focus': '',
    'Skill': '',
})

HotkeyGems = d2({
    'Albion': d2({
        'Fiery Essence Jewel': 0,
        'Earthen Essence Jewel': 2,
        'Vapor Essence Jewel': 4,
        'Airy Essence Jewel': 6,
        'Watery Essence Jewel': 8,
        'Heated Essence Jewel': 10,
        'Dusty Essence Jewel': 12,
        'Icy Essence Jewel': 14,
        'Earthen Shielding Jewel': 16,
        'Icy Shielding Jewel': 18,
        'Heated Shielding Jewel': 20,
        'Light Shielding Jewel': 22,
        'Airy Shielding Jewel': 24,
        'Vapor Shielding Jewel': 26,
        'Dusty Shielding Jewel': 28,
        'Fiery Shielding Jewel': 30,
        'Watery Shielding Jewel': 32,
        'Vapor Battle Jewel': 34,
        'Fiery Battle Jewel': 36,
        'Earthen Battle Jewel': 38,
        'Airy Battle Jewel': 40,
        'Dusty Battle Jewel': 42,
        'Heated Battle Jewel': 44,
        'Watery War Sigil': 46,
        'Fiery War Sigil': 48,
        'Dusty War Sigil': 50,
        'Heated War Sigil': 52,
        'Earthen War Sigil': 54,
        'Airy War Sigil': 56,
        'Vapor War Sigil': 58,
        'Icy War Sigil': 60,
        'Fiery Fervor Sigil': 62,
        'Airy Fervor Sigil': 64,
        'Watery Fervor Sigil': 66,
        'Earthen Fervor Sigil': 68,
        'Vapor Fervor Sigil': 70,
        'Earthen Evocation Sigil': 72,
        'Icy Evocation Sigil': 74,
        'Fiery Evocation Sigil': 76,
        'Airy Evocation Sigil': 78,
        'Heated Evocation Sigil': 80,
        'Dusty Evocation Sigil': 82,
        'Vapor Evocation Sigil': 84,
        'Watery Evocation Sigil': 86,
        'Blood Essence Jewel': 88,
        'Mystical Essence Jewel': 90,
        'Earth Sigil': 92,
        'Ice Sigil': 94,
        'Fire Sigil': 96,
        'Air Sigil': 98,
        'Heat Sigil': 100,
        'Dust Sigil': 102,
        'Vapor Sigil': 104,
        'Water Sigil': 106,
        'Molten Magma War Sigil': 108,
        'Vacuous Fervor Sigil': 110,
        'Salt Crusted Fervor Sigil': 112,
        'Ashen Fervor Sigil': 114,
        'Steaming Fervor Sigil': 116,
        'Vacuous Sigil': 118,
        'Salt Crusted Sigil': 120,
        'Ashen Sigil': 122,
        'Brilliant Sigil': 124,
        'Finesse War Sigil': 126,
        'Finesse Fervor Sigil': 128,
        'Glacial War Sigil': 130,
        'Cinder War Sigil': 132,
        'Radiant Fervor Sigil': 134,
        'Magnetic Fervor Sigil': 136,
        'Clout Fervor Sigil': 138,
    }),

    'Hibernia': d2({
        'Fiery Essence Jewel': 0,
        'Earthen Essence Jewel': 2,
        'Vapor Essence Jewel': 4,
        'Airy Essence Jewel': 6,
        'Watery Essence Jewel': 8,
        'Heated Essence Jewel': 10,
        'Dusty Essence Jewel': 12,
        'Icy Essence Jewel': 14,
        'Earthen Shielding Jewel': 16,
        'Icy Shielding Jewel': 18,
        'Heated Shielding Jewel': 20,
        'Light Shielding Jewel': 22,
        'Airy Shielding Jewel': 24,
        'Vapor Shielding Jewel': 26,
        'Dusty Shielding Jewel': 28,
        'Fiery Shielding Jewel': 30,
        'Watery Shielding Jewel': 32,
        'Vapor Battle Jewel': 34,
        'Fiery Battle Jewel': 36,
        'Earthen Battle Jewel': 38,
        'Airy Battle Jewel': 40,
        'Dusty Battle Jewel': 42,
        'Heated Battle Jewel': 44,
        'Watery War Spell Stone': 46,
        'Fiery War Spell Stone': 48,
        'Dusty War Spell Stone': 50,
        'Heated War Spell Stone': 52,
        'Earthen War Spell Stone': 54,
        'Icy War Spell Stone': 56,
        'Airy War Spell Stone': 58,
        'Fiery Nature Spell Stone': 60,
        'Watery Nature Spell Stone': 62,
        'Earthen Nature Spell Stone': 64,
        'Airy Nature Spell Stone': 66,
        'Airy Arcane Spell Stone': 68,
        'Fiery Arcane Spell Stone': 70,
        'Watery Arcane Spell Stone': 72,
        'Vapor Arcane Spell Stone': 74,
        'Icy Arcane Spell Stone': 76,
        'Earthen Arcane Spell Stone': 78,
        'Blood Essence Jewel': 80,
        'Mystical Essence Jewel': 82,
        'Fire Spell Stone': 84,
        'Water Spell Stone': 86,
        'Vapor Spell Stone': 88,
        'Ice Spell Stone': 90,
        'Earth Spell Stone': 92,
        'Light War Spell Stone': 94,
        'Steaming Nature Spell Stone': 96,
        'Oozing Nature Spell Stone': 98,
        'Mineral Encrusted Nature Spell Stone': 100,
        'Steaming Spell Stone': 102,
        'Oozing Spell Stone': 104,
        'Mineral Encrusted Spell Stone': 106,
        'Spectral Spell Stone': 108,
        'Phantasmal Spell Stone': 110,
        'Ethereal Spell Stone': 112,
        'Spectral Arcane Spell Stone': 114,
        'Phantasmal Arcane Spell Stone': 116,
        'Ethereal Arcane Spell Stone': 118,
        'Shadowy Arcane Spell Stone': 120,
        'Embracing Arcane Spell Stone': 122,
        'Aberrant Arcane Spell Stone': 124,
        'Brilliant Spell Stone': 126,
        'Finesse War Spell Stone': 128,
        'Finesse Nature Spell Stone': 130,
        'Glacial War Spell Stone': 132,
        'Cinder War Spell Stone': 134,
        'Radiant Nature Spell Stone': 136,
        'Magnetic Nature Spell Stone': 138,
        'Clout Nature Spell Stone': 140,
    }),

    'Midgard': d2({
        'Fiery Essence Jewel': 0,
        'Earthen Essence Jewel': 2,
        'Vapor Essence Jewel': 4,
        'Airy Essence Jewel': 6,
        'Watery Essence Jewel': 8,
        'Heated Essence Jewel': 10,
        'Dusty Essence Jewel': 12,
        'Icy Essence Jewel': 14,
        'Earthen Shielding Jewel': 16,
        'Icy Shielding Jewel': 18,
        'Heated Shielding Jewel': 20,
        'Light Shielding Jewel': 22,
        'Airy Shielding Jewel': 24,
        'Vapor Shielding Jewel': 26,
        'Dusty Shielding Jewel': 28,
        'Fiery Shielding Jewel': 30,
        'Watery Shielding Jewel': 32,
        'Vapor Battle Jewel': 34,
        'Fiery Battle Jewel': 36,
        'Earthen Battle Jewel': 38,
        'Airy Battle Jewel': 40,
        'Dusty Battle Jewel': 42,
        'Heated Battle Jewel': 44,
        'Watery War Rune': 46,
        'Fiery War Rune': 48,
        'Earthen War Rune': 50,
        'Heated War Rune': 52,
        'Airy War Rune': 54,
        'Vapor War Rune': 56,
        'Icy War Rune': 58,
        'Earthen Primal Rune': 60,
        'Airy Primal Rune': 62,
        'Fiery Primal Rune': 64,
        'Icy Chaos Rune': 66,
        'Dusty Chaos Rune': 68,
        'Heated Chaos Rune': 70,
        'Vapor Chaos Rune': 72,
        'Watery Chaos Rune': 74,
        'Airy Chaos Rune': 76,
        'Fiery Chaos Rune': 78,
        'Blood Essence Jewel': 82,
        'Mystical Essence Jewel': 84,
        'Ice Rune': 86,
        'Dust Rune': 88,
        'Heat Rune': 90,
        'Vapor Rune': 92,
        'Lightning Charged War Rune': 94,
        'Ashen Primal Rune': 96,
        'Ashen Rune': 98,
        'Blighted Rune': 100,
        'Valiant Primal Rune': 104,
        'Blighted Primal Rune': 106,
        'Unholy Primal Rune': 108,
        'Brilliant Rune': 110,
        'Finesse War Rune': 112,
        'Finesse Primal Rune': 114,
        'Glacial War Rune': 116,
        'Cinder War Rune': 118,
        'Radiant Primal Rune': 120,
        'Magnetic Primal Rune': 122,
        'Clout Primal Rune': 124,
    }),
})

ImbueMultipliers = d2({
    'Stat': 1.0,
    'Resist': 2.0,
    'Skill': 5.0,
    'Hits': 0.25,
    'Power': 2.0,
    'Focus': 1.0,
    'Unused': 0.0,
})

QualityValues = t2(('94', '95', '96', '97', '98', '99', '100'))

OCStartPercentages = (0, 10, 20, 30, 50, 70)

ItemQualOCModifiers = d2({
    '94': 0,
    '95': 0,
    '96': 6,
    '97': 8,
    '98': 10,
    '99': 18,
    '100': 26,
})

ImbuePts = (
    1, 2, 2, 3, 4, 4, 5, 5, 6, 7,
    7, 8, 9, 9, 10, 10, 11, 12, 12, 13,
    13, 14, 15, 15, 16, 16, 17, 18, 18, 19,
    20, 20, 21, 21, 22, 23, 23, 24, 24, 25,
    26, 26, 27, 27, 28, 29, 29, 30, 31, 31,
    32,
)

BodyHitOdds = d2({
    'Chest': .40,
    'Legs': .25,
    'Arms': .15,
    'Head': .10,
    'Hands': .05,
    'Feet': .05,
})

PieceTabList = t2((
    'Chest', 'Arms', 'Head', 'Legs', 'Hands', 'Feet',
    'Right Hand', 'Left Hand', '2 Handed', 'Ranged', 'Spare',
))

JewelTabList = t2((
    'Neck', 'Cloak', 'Jewel', 'Belt',
    'Left Ring', 'Right Ring', 'Left Wrist', 'Right Wrist',
    'Mythical',
))

TabList = t2(PieceTabList + JewelTabList)

ArmorTabList = list(PieceTabList[:6])
ArmorTabList.append('Spare')
ArmorTabList = t2(ArmorTabList)
WeaponTabList = t2(PieceTabList[6:])
FocusTabList = t2(('2 Handed', 'Spare',))

FileExt = d2({
    'Neck': 'neck',
    'Cloak': 'cloak',
    'Belt': 'belt',
    'Jewel': 'jewel',
    'Left Ring': 'ring',
    'Right Ring': 'ring',
    'Left Wrist': ('bracer', 'wrist',),
    'Right Wrist': ('bracer', 'wrist',),
    'Chest': 'chest',
    'Arms': 'arms',
    'Head': 'helm',
    'Legs': 'legs',
    'Feet': 'boots',
    'Hands': 'hands',
    'Right Hand': 'wep',
    'Left Hand': ('lhwep', 'shield',),
    '2 Handed': ('2hwep', 'lhwep', 'wep',),
    'Ranged': 'ranged',
    'Mythical': 'myth',
    'Spare': '*',
})

ShieldTypes = t2((
    'Rowan', 'Elm', 'Oaken', 'Ironwood', 'Heartwood',
    'Runewood', 'Stonewood', 'Ebonwood', 'Dyrwood', 'Duskwood',
))

# Rename old slot types to new types, from older template and item files
#
FixTypeTable = d2({
    'PvE': 'PvE Bonus',
    'Hits': 'Stat',
    'Power': 'Stat',
})

# Rename old skills to new skills, from older template and item files
#
FixEffectsTable = d2({
    'Bonedancing': 'Bone Army',
    'PainWorking': 'Painworking',
    'Subterranean': 'Cave Magic',
    'BeastCraft': 'Beastcraft',
    'Arboreal': 'Arboreal Path',
    'Arboreal Focus': 'Arboreal Path',
    'Body Focus': 'Body Magic',
    'Cold Focus': 'Cold Magic',
    'Earth Focus': 'Earth Magic',
    'Fire Focus': 'Fire Magic',
    'Matter Focus': 'Matter Magic',
    'Mind Focus': 'Mind Magic',
    'Spirit Focus': 'Spirit Magic',
    'Wind Focus': 'Wind Magic',

    'Composite Bow': 'Archery',
    'Recurve Bow': 'Archery',
    'Longbow': 'Archery',

    'All Focus Bonus': 'All Spell Lines',
    'All Melee Skill Bonus': 'All Melee Weapon Skills',
    'All Magic Skill Bonus': 'All Magic Skills',
    'All Dual Wield Skill Bonus': 'All Dual Wield Skills',
    'Archery Skill Bonus': 'All Archery Skills',

    'AF Bonus': 'AF',
    'Archery Damage Bonus': 'Archery Damage',
    'Archery Range Bonus': 'Archery Range',
    'Archery Speed Bonus': 'Archery Speed',
    'Buff Bonus': 'Stat Buff Effectiveness',
    'Casting Range': 'Spell Range',
    'Casting Speed Bonus': 'Casting Speed',
    'Debuff Bonus': 'Stat Debuff Effectiveness',
    'Defensive Bonus': 'Defensive',
    'Healing Bonus': 'Healing Effectiveness',
    'Spell Damage Bonus': 'Spell Damage',
    'Magic Damage': 'Spell Damage',
    'Spell Duration Bonus': 'Duration of Spells',
    'Spell Range Bonus': 'Spell Range',
    'Style Damage Bonus': 'Style Damage',
    'Melee Damage Bonus': 'Melee Damage',
    'Melee Speed Bonus': 'Melee Combat Speed',
    'Power Percentage Bonus': '% Power Pool',

    'Strength Cap Increase': 'Strength',
    'Constitution Cap Increase': 'Constitution',
    'Dexterity Cap Increase': 'Dexterity',
    'Quickness Cap Increase': 'Quickness',
    'Intelligence Cap Increase': 'Intelligence',
    'Piety Cap Increase': 'Piety',
    'Charisma Cap Increase': 'Charisma',
    'Empathy Cap Increase': 'Empathy',
    'Acuity Cap Increase': 'Acuity',
    'Power Cap Increase': 'Power',
    'Hits Cap Increase': 'Hits',
    'AF Cap Increase': 'AF',

    'Reactionary Style Damage Bonus': 'Reactionary Style Damage',
    'Death XP Loss Reduction': 'Death Experience Loss Reduction',
    'Blocking': 'Block',

    'PvE': 'PvE Bonus',

    'Body Resist': 'Body',
    'Cold Resist': 'Cold',
    'Heat Resist': 'Heat',
    'Energy Resist': 'Energy',
    'Matter Resist': 'Matter',
    'Spirit Resist': 'Spirit',
    'Crush Resist': 'Crush',
    'Thrust Resist': 'Thrust',
    'Slash Resist': 'Slash',
})

if __name__ == "__main__":

    for (realm, realmtable) in list(GemTables.items()):

        if realm == "All":
            continue

        for (type, typetable) in list(realmtable.items()):
            for (effect, effecttable) in list(typetable.items()):
                try:
                    name = effecttable[0] + " " + effecttable[1]
                    tryit = HotkeyGems[realm][name]

                except:
                    sys.stdout.write("Missing %s %s entry\n" % (type, effect,))

    pass
