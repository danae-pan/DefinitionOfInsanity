# --------------------------------------------------
# CHAPTER 2 - PERSISTENT LOOP KNOWLEDGE
# These flags DO NOT reset between attempts.
# --------------------------------------------------

default ch02_loop_count = 0

# Stores ONLY the ending from the previous loop.
default ch02_previous_death = None

# Endings / deaths already experienced
default ch02_used_taeru_happened = False

#Knowledge
default ch02_knows_taeru_in_stock = False
default ch02_knows_cat_is_sick = False
default herbalist_visited = False
# First herb - Junka Root
default ch02_first_herb_with_instructions = False
default ch02_first_herb_without_instructions = False
# Second herb - Tsuyomi Cap history
default ch02_second_herb_with_instructions = False
default ch02_second_herb_without_instructions = False


# --------------------------------------------------
# CHAPTER 2 - CURRENT ATTEMPT STATE
# These flags reset after every ending.
# -------------------------------------------------

default ch02_route_choice = None
default ch02_first_herb_taken = False
default ch02_second_herb_taken = False
default ch02_coming_from_hospital = False

label ch02_remember_previous_death:

    if ch02_previous_death == "cardiac_arrest":

        show doctor default at left onlayer portraits with dissolve

        $ cardiac_arrest_entry.locked = False

        doctor "Mother's seizure..."

        doctor "I left her alone while I fed the cat."

        doctor "By the time I heard the crash and reached her, it was already too late."

        doctor "She went into {a=glossary:cardiac_arrest_entry}cardiac arrest{/a} before I could help her."

    elif ch02_previous_death == "cat_broke_formula":

        doctor "The cat knocked over the formula..."

        doctor "I didn't have enough herbs to prepare another."

        doctor "Without treatment, Mother's condition worsened."

        $ respiratory_failure_entry.locked = False

        doctor "Eventually, she died from {a=glossary:respiratory_failure_entry}respiratory failure{/a}."

    elif ch02_previous_death == "first_herb_with_instructions":

        show doctor default at left onlayer portraits with dissolve

        $ junka_root_entry.locked = False

        doctor "The {a=glossary:junka_root_entry}Junka Root{/a}..."

        doctor "I followed the instructions and prepared Mother's meal first."

        doctor "But I took too long."

        doctor "Before I could give her the formula, her condition had already progressed too far."

        doctor "Next time, I need to prepare the meal earlier."

    elif ch02_previous_death == "first_herb_without_instructions":

        show doctor default at left onlayer portraits with dissolve

        $ junka_root_entry.locked = False

        doctor "The {a=glossary:junka_root_entry}Junka Root{/a}..."

        doctor "I ignored the instructions and gave it to Mother without eating first."

        doctor "It made her violently sick..."

        $ dysphagia_entry.locked = False

        doctor "With her {a=glossary:dysphagia_entry}dysphagia{/a}, she couldn't protect her airway."

        doctor "She choked on her own vomit."

        doctor "I should have followed the instructions."

    elif ch02_previous_death == "mother_cant_swallow":

        show doctor default at left onlayer portraits with dissolve

        $ dysphagia_entry.locked = False

        doctor "Mother's {a=glossary:dysphagia_entry}dysphagia{/a}..."

        doctor "It became so severe that she couldn't even swallow her own saliva."

        doctor "She was calling for me, and I ignored her."

        doctor "By the time I went back to her, it was already too late."

    elif ch02_previous_death == "second_herb_with_instructions":

        show doctor default at left onlayer portraits with dissolve

        $ tsuyomi_cap_entry.locked = False

        doctor "The {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}..."

        doctor "I followed the instructions."

        doctor "But I was too slow."

        doctor "By the time the formula was ready, Mother's condition had already deteriorated too far."

        doctor "Even the right treatment is useless if I can't give it to her in time."

    elif ch02_previous_death == "second_herb_without_instructions":

        show doctor default at left onlayer portraits with dissolve

        $ tsuyomi_cap_entry.locked = False

        $ coma_entry.locked = False

        doctor "The {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}..."

        doctor "I ignored the instructions and let Mother eat before giving her the formula."

        doctor "The medicine had no effect."

        doctor "She slipped into a {a=glossary:coma_entry}coma{/a}..."

        doctor "...and never woke up."

        doctor "I shouldn't ignore the instructions again."


    elif ch02_previous_death == "used_taeru":

        show doctor default at left onlayer portraits with dissolve

        $ taeru_root_entry.locked = False

        $ brain_hemorrhage_entry.locked = False

        doctor "The {a=glossary:taeru_root_entry}Taeru Root{/a}..."

        doctor "It affected her blood pressure..."

        doctor "Mother died from a {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}..."

    return