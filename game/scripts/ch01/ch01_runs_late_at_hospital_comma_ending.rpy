label ch01_runs_late_at_hospital_comma_ending:

    show doctor default at left onlayer portraits

    doctor "The herbalist may have useful information about the illness and the herbs that could help."

    doctor "I should stay and speak with him."

    doctor "\"Please, Kazuki. What have you noticed over the years while treating your patients?\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"I've never seen anyone cured.\""

    herbalist "\"But I've seen this illness many times.\""

    herbalist "\"It always begins differently...\""

    herbalist "\"Eventually, their muscles become too weak to support them.\""

    herbalist "\"Many also lose the ability to swallow safely.\""

    herbalist "\"Food, and even water, can become dangerous.\""

    herbalist "\"Later... they begin losing their balance.\""

    hide herbalist default onlayer portraits

    "He quietly commits every word to memory."

    "They continue talking for a while longer."

    show doctor default at left onlayer portraits

    doctor "I've already been gone too long."

    doctor "I should return to Mother."

    doctor "\"I'll definitely visit your shop as soon as I can.\""

    doctor "\"I have to go now. Have a good day, Kazuki.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"I hope I see you again soon, Dr. Yosuke.\""

    herbalist "\"Good day to you as well.\""

    hide herbalist default onlayer portraits

    "He quickly heads home."

    "As soon as he enters the house, he notices the silence."

    show doctor default at left onlayer portraits

    doctor "No..."

    hide doctor default onlayer portraits

    "He rushes to Mother's room."

    scene bg ch01 mother with fade

    "She lies in bed, completely exhausted."

    show doctor default at left onlayer portraits

    doctor "I think I'm already too late..."

    hide doctor default onlayer portraits

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

    if ch01_loop_count == 0 :

        show doctor default at left onlayer portraits

        doctor "Maybe tomorrow she will wake up." 

        doctor "\"Maybe...\"" 

        hide doctor default onlayer portraits

    
    show doctor default at left onlayer portraits

    doctor "But deep down, I know."

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

    doctor "What if the formula could have saved her?"

    hide doctor default onlayer portraits

    if ch01_loop_count >= 1 :

        show doctor default at left onlayer portraits

        doctor "I should not let the cat in the laboratory any more."

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

            doctor "If I don't give her the formula, she falls into a {a=glossary:coma_entry}coma{/a} and dies..." 

            hide doctor default onlayer portraits
        
        else:

            show doctor default at left onlayer portraits

            doctor "I've read about this before..."

            doctor "This illness can end in a {a=glossary:coma_entry}coma{/a}."

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