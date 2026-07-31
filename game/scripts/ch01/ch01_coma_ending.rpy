label ch01_coma_ending :

    "He brings the formula into Mother's room. He looks at it in his hands." 

    if ch01_check_formula:

        doctor "This formula has been proven dangerous before."

    else:

        doctor "The answer I have been searching for..."
        doctor "It could be right in front of me." 

    doctor "But it has never been tested."

    doctor "I know the risks."

    doctor "If something goes wrong..."

    doctor "If the formula harms her, then I'll be the reason she suffers even more."

    doctor "Even if it could help her..."

    doctor "Even if it could be the cure..."

    doctor "I can't risk losing her because of something I created."

    "He slowly lowers the {a=glossary:formula_entry}formula{/a} and sets it aside."

    show doctor default at left onlayer portraits

    doctor "\"I'm sorry, Mother...\""

    doctor "\"I can't.\""

    hide doctor default onlayer portraits

    if not ch01_knows_coma :

        "He chooses not to give her the formula and remains beside her."

    else :

        "He chooses not to give her the formula and remains beside her."

    "He monitors her condition and does everything he can to keep her comfortable."

    "But the illness does not stop."

    "Her body grows weaker."

    "Hours pass."

    "Then she stops responding."

    show doctor default at left onlayer portraits

    doctor "\"Mother?\"" 

    hide doctor default onlayer portraits

    "He checks her condition."

    "She is still alive, but she does not wake."

    $ coma_entry.locked = False

    "Her body has entered a {a=glossary:coma_entry}coma{/a}."

    "He remains beside her, waiting for her to open her eyes."

    if ch01_loop_count == 0:

        doctor "Maybe she'll wake up tomorrow."

        doctor "Maybe..."

    doctor "But deep down, I know."

    doctor "There is nothing more I can do."

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."doctor "But deep down, I know."

    doctor "There is nothing more I can do."

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."

    if ch01_loop_count >= 1 :

        doctor "I lost her again..."

    doctor doctor "I made the safest choice."

    doctor "But one question remains..."

    doctor "What if the formula could have saved her?"

    if ch01_loop_count == 0 :

        "Eventually, reality begins to settle in." 

        "There are things that must be done."
        
        octor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        $ ch01_wake_happened = True

    else :

        if ch01_knows_coma :

            doctor "The memory burns into my mind."

            doctor "If I don't give her the formula, she falls into a coma and dies..."

        else:

            doctor "I've read about this before."

            doctor "This illness can end in a coma."

        doctor "I have to try again."

        doctor "I have to save her."

        "He gently places her hand back on the bed."

        doctor "But I'm not finished."

        "He returns to his laboratory."

        scene bg ch01 lab

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistake."

        "The symptoms."

        "The things he overlooked."

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "I will save her."

        scene black 

        "He closes his eyes."

        doctor "\"Tomorrow...\""

        doctor "\"I'll do better.\""

    if not ch01_knows_coma :

        $ ch01_knows_coma = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop