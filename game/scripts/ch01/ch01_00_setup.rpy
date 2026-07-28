image bg ch01 kitchen = im.Scale("images/backgrounds/kitchen_background.png", 1920, 1080)
image bg ch01 mother = im.Scale("images/backgrounds/mother_background.png", 1920, 1080)
image bg ch01 lab = im.Scale("images/backgrounds/lab_background.png", 1920, 1080)
image bg ch01 herbstore = im.Scale("images/backgrounds/herbstore_background.png", 1920, 1080)


default ch01_loop_count = 0
default ch01_chapter1_with_one_try = False

default ch01_kept_cat_in_lab_once = False
default ch01_went_to_hospital = False

default ch01_knows_dysphagia = False
default ch01_brain_hemorrhage_happened = False
default ch01_knows_arrhythmia = False
default ch01_knows_coma = False

default ch01_wake_happened = False

default ch01_knows_licorice = False
default ch01_knows_schisandra = False
default ch01_knows_polygala = False

# These flags will determine if the player can go to chapter 2
# If both of them are true then the player can continue to chapter 2
# These values will not reset when an ending happens

default ch01_met_herbalist = False # Future chapter flags
default ch01_check_formula = False # Future chapter flags
default ch01_jump_to_chapter_2 = False

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
default ch01_prepared_formula = False