from cx_Freeze import Executable, setup

setup(name = 'KortsSpellcraftingCalculator', description = 'Kort\'s Spellcrafting Calculator', version='3.0.0',

    executables = [Executable('Spellcraft.pyw', base = 'console'),]

)
