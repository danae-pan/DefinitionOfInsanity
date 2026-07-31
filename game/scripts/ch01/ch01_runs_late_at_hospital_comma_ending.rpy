label ch01_runs_late_at_hospital_comma_ending:

    doctor "The herbalist may have useful information about the illness and the herbs that could help."

    doctor "I should stay and speak with him."

    doctor "\"Please, Kazuki. What have you noticed over the years while treating your patients?\""

    herbalist "\"I've never seen anyone cured.\""

    herbalist "\"But I've seen this illness many times.\""

    herbalist "\"It always begins differently...\""

    herbalist "\"Eventually, their muscles become too weak to support them.\""

    herbalist "\"Many also lose the ability to swallow safely.\""

    herbalist "\"Food, and even water, can become dangerous.\""

    herbalist "\"Later... they begin losing their balance.\""

    "He quietly commits every word to memory."

    "They continue talking for a while longer."

    doctor "I've already been gone too long."

    doctor "I should return to Mother."

    doctor "\"I'll definitely visit your shop as soon as I can.\""

    doctor "\"I have to go now. Have a good day, Kazuki.\""

    herbalist "\"I hope I see you again soon, Dr. Yosuke.\""

    herbalist "\"Good day to you as well.\""

    "He quickly heads home."

    "As soon as he enters the house, he notices the silence."

    doctor "No..."

    "He rushes to Mother's room."

    scene bg ch01 mother with fade

    "She lies in bed, completely exhausted."

    doctor "I think I'm already too late..."

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

        doctor "Maybe tomorrow she will wake up." 

        doctor "\"Maybe...\"" 

    doctor "But deep down, I know."

    doctor "There is nothing more I can do."

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."

    if ch01_loop_count >= 1 :

        doctor "I lost her again..."

    doctor "What if the formula could have saved her?"

    if ch01_loop_count >= 1 :

        doctor "I should not let the cat in the laboratory any more."

    if ch01_loop_count == 0 :

        "Eventually, reality begins to settle in."

        "There are things that must be done."

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        $ ch01_wake_happened = True

    else :

        if ch01_knows_coma :

            doctor "The memory burns into my mind."

            doctor "If I don't give her the formula, she falls into a {a=glossary:coma_entry}coma{/a} and dies..." 

        else:

            doctor "I've read about this before..."

            doctor "This illness can end in a {a=glossary:coma_entry}coma{/a}."

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