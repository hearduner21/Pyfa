# shipBonusHeavyMissileKineticDamageCBC1
#
# Used by:
# Ship: Drake
# Ship: Nighthawk
# Ship: 幼龙级YC117年特别版
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battlecruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "kineticDamage", ship.getModifiedItemAttr("shipBonusCBC1") * level)
