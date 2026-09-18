label ch01_runs_late_at_hospital_comma_ending:

    show doctor default at left onlayer portraits with dissolve

    doctor "The herbalist may have useful information about the illness and the herbs that could help."

    doctor "I should stay and speak with him."

    doctor "\"Mr. Kazuki, my Mother suffers from the same illness as all those patients in the hospital.\""
    
    doctor "\"What have you noticed over the years while treating your patients?\""

    hide doctor default onlayer portraits 

    show herbalist default at left onlayer portraits

    herbalist "\"I've never seen anyone cured.\""

    herbalist "\"But I've seen this illness many times.\""

    herbalist "\"It always begins differently...\""

    herbalist "\"Eventually, their muscles become too weak to support them.\""

    herbalist "\"Many also lose the ability to swallow safely.\""

    herbalist "\"Food, and even water, can become dangerous.\""

    herbalist "\"Later... they begin losing their balance.\""

    hide herbalist default onlayer portraits with dissolve

    "He quietly commits every word to memory."

    "They continue talking for a while longer."

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"If you're looking for a cure.\"" 

    herbalist "\"Unfortunately...\"" 

    herbalist "\"I don't have one.\"" 

    herbalist "\"But I might have something that could make her days a little easier.\""

    herbalist "\"I have a few herbs that physicians rarely bother with.\"" 

    herbalist "\"Some have been passed down through generations.\"" 

    herbalist "\"Perhaps you'll find them useful.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"That’s very nice of you.\""

    doctor "\"I will be interested to see what you have.\""
    
    doctor "\"Do you have them with you?\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"Unfortunatelly I don't carry those kinds of herbs with me but you can visit my store.\""
    
    herbalist "\"I'm heading there now.\""
    
    herbalist "\"You are welcome to join me.\""

    hide herbalist default onlayer portraits
    
    show doctor default at left onlayer portraits

    doctor "I've already been gone too long."

    doctor "I should return to Mother."

    doctor "But maybe those herbs Mr. Kazuki mentions help me develop a better formula..."

    hide doctor default onlayer portraits with dissolve

    menu:

        "Join the Herbalist":

            call ch01_arrythmia_good_ending

        "Return to your Mother":

            $ ch01_return_from_hospital = True

            show doctor default at left onlayer portraits

            doctor "\"I'll definitely visit your store as soon as I can.\""

            doctor "\"I have to go now. Have a good day, Mr. Kazuki.\""

            hide doctor default onlayer portraits

            show herbalist default at left onlayer portraits

            herbalist "\"I hope I see you again soon, Dr. Yosuke.\""

            herbalist "\"Good day to you as well.\""

            hide herbalist default onlayer portraits

            jump ch01_brain_hemorrahage_ending


    "He quickly heads home."

    scene bg game_main with fade

    "As soon as he enters the house, he notices the silence."

    show doctor default at left onlayer portraits with dissolve

    doctor "No..."

    hide doctor default onlayer portraits with dissolve

    "He rushes to his Mother's room."

    scene bg ch01 mother with fade

    "She lies in bed, completely exhausted."

    show doctor default at left onlayer portraits with dissolve

    doctor "I think I'm already too late..."

    hide doctor default onlayer portraits with dissolve

    "He monitors her condition and does everything he can to keep her comfortable."

    "But the illness does not stop."

    "Her body grows weaker."

    "Hours pass."

    "Then she stops responding."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\""

    hide doctor default onlayer portraits with dissolve

    "He checks her pulse."

    "She is still alive, but she does not wake."

    $ coma_entry.locked = False

    "Her body has entered a {a=glossary:coma_entry}coma{/a}."

    "He remains beside her, waiting for her to open her eyes." 

    show doctor default at left onlayer portraits with dissolve

    if ch01_loop_count == 0 :

        doctor "Maybe tomorrow she will wake up." 

        doctor "\"Maybe...\"" 

    doctor "But deep down, I know."

    doctor "There is nothing more I can do." 

    hide doctor default onlayer portraits with dissolve

    "Hours later, her breathing becomes weaker."

    "He holds her hand until the very end."

    "She passes away peacefully beside him."

    if ch01_loop_count >= 1 :

        show doctor default at left onlayer portraits

        doctor "I lost her again..."

        hide doctor default onlayer portraits

    show doctor default at left onlayer portraits with dissolve

    doctor "What if the formula could have saved her?"

    if took_herbs and ch01_went_to_hospital:

        doctor "Or what if the new herbs I got from Kazumi developed a better formula?"

        doctor "\"I lost track of time...\""

        doctor "But still..."

        doctor "I can't help but wonder."
 
    hide doctor default onlayer portraits with dissolve

    if ch01_loop_count >= 1 :

        show doctor default at left onlayer portraits

        doctor "I should not let the cat in the laboratory any more."

        hide doctor default onlayer portraits

    if ch01_loop_count == 0 :

        "Eventually, reality begins to settle in."

        "There are things that must be done."

        show doctor default at left onlayer portraits with dissolve

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        hide doctor default onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

        $ ch01_wake_happened = True

    else :

        if ch01_knows_coma :

            show doctor default at left onlayer portraits with dissolve

            doctor "The memory burns into my mind."

            doctor "If I don't give her the formula, she falls into a {a=glossary:coma_entry}coma{/a} and dies..." 
        
        else:

            show doctor default at left onlayer portraits with dissolve

            doctor "I've read about this before..."

            doctor "This illness can end in a {a=glossary:coma_entry}coma{/a}."

        show doctor default at left onlayer portraits with dissolve
        
        doctor "I have to try again."

        doctor "I have to save her."

        hide doctor default onlayer portraits with dissolve

        "He gently places her hand back on the bed."

        show doctor default at left onlayer portraits with dissolve

        doctor "But I'm not finished."

        hide doctor default onlayer portraits with dissolve

        "He returns to his laboratory."

        scene bg ch01 lab_no_cat with fade

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistakes."

        "The symptoms."

        "The things he overlooked."

        show doctor default at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "\"I will save her.\""

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    if not ch01_knows_coma :

        $ ch01_knows_coma = True

    $ ch01_previous_death = "coma"

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_4

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop