from pathlib import Path

# dicts for creating pickles
from adventuringGear.adventuringgear_Ids import adventuringgear_Ids
from archetypes.archetypes_Ids import archetypes_Ids
from armor.armor_Ids import armor_Ids
from backgrounds.backgrounds_Ids import backgrounds_Ids
from classes.classes_Ids import classes_Ids
from classFeatures.classfeatures_Ids import classfeatures_Ids
from enhancedItems.enhanceditems_Ids import enhanceditems_Ids
from feats.feats_Ids import feats_Ids
from fightingMasteries.fightingmasteries_Ids import fightingmasteries_Ids
from fightingStyles.fightingstyles_Ids import fightingstyles_Ids
from forcePowers.forcepowers_Ids import forcepowers_Ids
from gamingSet.gamingset_Ids import gamingset_Ids
from lightsaberForms.lightsaberforms_Ids import lightsaberforms_Ids
from monsters.monsters_Ids import monsters_Ids
from species.species_Ids import species_Ids
from speciesTraits.speciestraits_Ids import speciestraits_Ids
from techPowers.techpowers_Ids import techpowers_Ids
from tradeGoods.tradegoods_Ids import tradegoods_Ids
from weapons.weapons_Ids import weapons_Ids

# paths for pickles
ag_path = Path(__file__).parent / "../adventuringGear/adventuringgear_Ids.pickle"
arch_path = Path(__file__).parent / "../archetypes/archetypes_Ids.pickle"
arm_path = Path(__file__).parent / "../armor/armor_Ids.pickle"
bg_path = Path(__file__).parent / "../backgrounds/backgrounds_Ids.pickle"
cls_path = Path(__file__).parent / "../classes/classes_Ids.pickle"
cf_path = Path(__file__).parent / "../classFeatures/classfeatures_Ids.pickle"
ei_path = Path(__file__).parent / "../enhancedItems/enhanceditems_Ids.pickle"
feat_path = Path(__file__).parent / "../feats/feats_Ids.pickle"
fm_path = Path(__file__).parent / "../fightingMasteries/fightingmasteries_Ids.pickle"
fs_path = Path(__file__).parent / "../fightingStyles/fightingstyles_Ids.pickle"
fp_path = Path(__file__).parent / "../forcePowers/forcepowers_Ids.pickle"
gs_path = Path(__file__).parent / "../gamingSet/gamingset_Ids.pickle"
lf_path = Path(__file__).parent / "../lightsaberForms/lightsaberforms_Ids.pickle"
mon_path = Path(__file__).parent / "../monsters/monsters_Ids.pickle"
spcs_path = Path(__file__).parent / "../species/species_Ids.pickle"
st_path = Path(__file__).parent / "../speciesTraits/speciestraits_Ids.pickle"
tp_path = Path(__file__).parent / "../techPowers/techpowers_Ids.pickle"
tg_path = Path(__file__).parent / "../tradeGoods/tradegoods_Ids.pickle"
weap_path = Path(__file__).parent / "../weapons/weapons_Ids.pickle"

# dict of pickle path variable to dict name
pickle_to_dict = {
    ag_path: adventuringgear_Ids,
    arch_path: archetypes_Ids,
    arm_path: armor_Ids,
    bg_path: backgrounds_Ids,
    cls_path: classes_Ids,
    cf_path: classfeatures_Ids,
    ei_path: enhanceditems_Ids,
    feat_path: feats_Ids,
    fm_path: fightingmasteries_Ids,
    fs_path: fightingstyles_Ids,
    fp_path: forcepowers_Ids,
    gs_path: gamingset_Ids,
    lf_path: lightsaberforms_Ids,
    mon_path: monsters_Ids,
    spcs_path: species_Ids,
    st_path: speciestraits_Ids,
    tp_path: techpowers_Ids,
    tg_path: tradegoods_Ids,
    weap_path: weapons_Ids
}
