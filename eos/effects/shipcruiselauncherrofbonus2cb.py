# shipCruiseLauncherROFBonus2CB
#
# Used by:
# Ships named like: Raven (5 of 6)
# Ship: 乌鸦级YC117年特别版
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Cruise",
                                  "speed", ship.getModifiedItemAttr("shipBonus2CB") * level)
