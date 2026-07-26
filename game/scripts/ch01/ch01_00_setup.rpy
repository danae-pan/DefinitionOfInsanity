image bg ch01 bedroom = im.Scale("images/backgrounds/background_bedroom.jpg", 1920, 1080)

default ch01_loop_count = 0

default ch01_kept_cat_in_lab_once = False
default ch01_went_to_hospital = False

default ch01_knows_dysphagia = False
default ch01_brain_hemorrahage_happend = False
default ch01_knows_arrythmia = False
default ch01_knows_comma = False

default ch01_wake_happened = False

default ch01_knows_licorice = False
default ch01_knows_schisandra = False
default ch01_knows_polygala = False

# These flags will determine if the player can go to chapter 2
# If both of them are true then the player can continue to chapter 2
# These values will not reset when an ending happens

default ch01_met_herbalist = False # Future chapter flags
default ch01_check_formula = False # Future chapter flags

# choices/actions from the previous attempt that will reset in every ending
default ch01_breakfast_made = False
default ch01_bread_added = False
default ch01_mother_checked = False
default ch01_cat_in_lab = False
default ch01_formula_finished = False
default ch01_met_herb_in_door = False
default ch01_met_herb_in_hospital = False
default ch01_went_to_shop = False
default ch01_cat_broke_formula = False