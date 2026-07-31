label ch01_coma_ending :

    "He brings the formula into Mother's room. He looks at it in his hands." 

    if ch01_check_formula:

        show doctor default at left onlayer portraits

        doctor "This formula has been proven dangerous before."

        hide doctor default onlayer portraits

    else:

        show doctor default at left onlayer portraits

        doctor "The answer I have been searching for..."

        doctor "It could be right in front of me." 

        hide doctor default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "But it has never been tested."

    doctor "I know the risks."

    doctor "If something goes wrong..."

    doctor "If the formula harms her, then I'll be the reason she suffers even more."

    doctor "Even if it could help her..."

    doctor "Even if it could be the cure..."

    doctor "I can't risk losing her because of something I created."

    hide doctor default onlayer portraits

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

        show doctor default at left onlayer portraits

        doctor "Maybe she'll wake up tomorrow."

        doctor "\"Maybe...\""
        
        hide doctor default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "But deep down, I know."

    doctor "There is nothing more I can do."

    hide doctor default onlayer portraits

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."doctor "But deep down, I know."

    show doctor default at left onlayer portraits

    doctor "There is nothing more I can do."

    hide doctor default onlayer portraits

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."

    if ch01_loop_count >= 1 :

        show doctor default at left onlayer portraits

        doctor "I lost her again..."

        hide doctor default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "I made the safest choice."

    doctor "But one question remains..."

    doctor "What if the formula could have saved her?"

    hide doctor default onlayer portraits

    if ch01_loop_count == 0 :

        "Eventually, reality begins to settle in." 

        "There are things that must be done."

        show doctor default at left onlayer portraits
        
        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        hide doctor default onlayer portraits

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        $ ch01_wake_happened = True

    else :

        if ch01_knows_coma :

            show doctor default at left onlayer portraits

            doctor "The memory burns into my mind."

            doctor "If I don't give her the formula, she falls into a coma and dies..."

            hide doctor default onlayer portraits

        else:

            show doctor default at left onlayer portraits

            doctor "I've read about this before."

            doctor "This illness can end in a coma."

            hide doctor default onlayer portraits

        show doctor default at left onlayer portraits
        
        doctor "I have to try again."

        doctor "I have to save her."

        hide doctor default onlayer portraits

        "He gently places her hand back on the bed."

        show doctor default at left onlayer portraits

        doctor "But I'm not finished."

        hide doctor default onlayer portraits

        "He returns to his laboratory."

        scene bg ch01 lab

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistake."

        "The symptoms."

        "The things he overlooked."

        show doctor default at left onlayer portraits

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "I will save her."

        hide doctor default onlayer portraits

        scene black 

        "He closes his eyes."

        show doctor default at left onlayer portraits

        doctor "\"Tomorrow...\""

        doctor "\"I'll do better.\""

        hide doctor default onlayer portraits

    if not ch01_knows_coma :

        $ ch01_knows_coma = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop