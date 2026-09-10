label ch01_coma_ending :

    "He brings the formula into Mother's room. He looks at it in his hands." 

    if ch01_check_formula:

        show doctor default at left onlayer portraits with dissolve

        doctor "This formula has been proven dangerous before."

        doctor "I know the risks."

    else:

        show doctor default at left onlayer portraits

        doctor "The answer I have been searching for..."

        doctor "It could be right in front of me." 

        doctor "But it has never been tested."

    doctor "If something goes wrong..."

    doctor "If the formula harms her, then I'll be the reason she suffers even more."

    doctor "Even if it could help her..."

    doctor "Even if it could be the cure..."

    doctor "I can't risk losing her because of something I created."

    hide doctor default onlayer portraits with dissolve

    "He slowly lowers the {a=glossary:formula_entry}formula{/a} and sets it aside."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I'm sorry, Mother...\""

    doctor "\"I can't.\""

    hide doctor default onlayer portraits with dissolve

    if not ch01_knows_coma :

        "He chooses not to give her the formula and remains beside her."

    else :

        "He chooses not to give her the formula and remains beside her."

    "He monitors her condition and does everything he can to keep her comfortable."

    "But the illness does not stop."

    "Her body grows weaker."

    "Hours pass."

    "Then she stops responding."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\"" 

    hide doctor default onlayer portraits with dissolve

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

    show doctor default at left onlayer portraits with dissolve

    doctor "But deep down, I know."

    doctor "\"There is nothing more I can do.\""

    hide doctor default onlayer portraits with dissolve

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."

    if ch01_loop_count >= 1 :

        show doctor default at left onlayer portraits with dissolve

        doctor "I lost her again..."

    doctor "I made the safest choice."

    doctor "But one question remains..."

    if ch01_check_formula:

        doctor "\"What if the formula could have saved her this time?\""

    else:

        doctor "\"What if the formula could have saved her?\""

    if ch01_loop_count == 0 :

        hide doctor default onlayer portraits with dissolve

        "Eventually, reality begins to settle in." 

        "There are things that must be done."

        show doctor default at left onlayer portraits with dissolve
        
        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        hide doctor default onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        $ ch01_wake_happened = True

        show doctor default at left onlayer portraits with dissolve

    else :

        if ch01_knows_coma :

            doctor "The memory burns into my mind."

            $ coma_entry.locked = False

            doctor "If I don't give her the formula, she falls into a {a=glossary:coma_entry}coma{/a} and dies..."

        else:

            doctor "I've read about this before."

            #do i need this here?

            $ coma_entry.locked = False

            doctor "This illness can end in a {a=glossary:coma_entry}coma{/a}."
        
        doctor "I have to try again."

        doctor "I have to save her."

        hide doctor default onlayer portraits with dissolve

        "He gently places her hand back on the bed."

        show doctor default at left onlayer portraits with dissolve

        doctor "But I'm not finished."

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He returns to his laboratory."

        scene bg ch01 lab

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistakes."

        "The symptoms."

        "The things he overlooked."

        show doctor default at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "\"I will save her.\""

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    if not ch01_knows_coma :

        $ ch01_knows_coma = True

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_3

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop