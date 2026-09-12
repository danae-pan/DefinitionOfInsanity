label ch01_brain_hemorrahage_ending:

    "He hesitates after hearing Mr. Kazuki's offer." 

    show doctor default at left onlayer portraits with dissolve

    doctor "The herbs in Mr. Kazuki's shop could be exactly what I need."

    doctor "Ingredients the hospital cannot provide..."

    doctor "But Mother called for me."

    doctor "No matter how important my research is..."

    doctor "I can't ignore her."

    #for 3, in game this condition works as expected

    if not ch01_went_to_hospital:

        doctor "\"Thank you, Mr. Kazuki.\""

        doctor "\"I'll visit your shop another time.\""

        hide doctor default onlayer portraits

        show herbalist default at left onlayer portraits

        herbaist "\"Alrigh then.\""

        herbalist "\"I hope I'll see you soon Mr. Yosuke.\""

        herbalist "\"Take care.\""

        hide herbalist default onlayer portraits

        show doctor default at left onlayer portraits

        doctor "\"Goodbye Mr. Kazuki.\""

        hide doctor default onlayer portraits with dissolve

        "Mr. Kazuki turns around and walks away."

        "The Doctor wonders if he made the right choice..."


    else:

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He quickly returns home worried about his Mother."

        "He opens the door."

        scene bg game_main with fade

        show doctor default at left onlayer portraits with dissolve
    

    doctor "\"Mother?\""

    hide doctor default onlayer portraits with dissolve

    "..." 

    "There is no answer." 

    "He quickly heads to his Mother's room."

    #No need for this, we already check this condition bellow.

    # if ch01_brain_hemorrhage_happened:

    #     show doctor default at left onlayer portraits with dissolve

    #     doctor "\"Oh no...\""

    #     doctor "\"Is this happening again?\""

    #     hide doctor default onlayer portraits with dissolve

    scene bg ch01 mother with fade

    "Her face is pale."

    "She looks exhausted."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    hide doctor default onlayer portraits with dissolve

    "He immediately checks her condition."

    "Her breathing is uneven."

    if not ch01_brain_hemorrhage_happened:

        "Then he notices something."

        "A broken glass lies on the floor."

        "Water has spilled across the room."

        "The bottle beside her bed is empty."

        "..."

        show doctor default at left onlayer portraits with dissolve

        doctor "She needed water and tried to get it herself..."

        doctor "While I was speaking with Mr. Kazuki..."

        doctor "\"Oh, Mother...\""

        doctor "Her weakened body couldn't support her."

        doctor "She fell."

        doctor "She wanted help but I was away..."

        doctor "\"This is all my fault...\""

        doctor "\"I'm so sorry Mother.\""

        hide doctor default onlayer portraits with dissolve

    else:

        show doctor default at left onlayer portraits with dissolve

        doctor "It's the same scene as before..."

        doctor "The broken glass..."

        doctor "The empty bottle..."

        hide doctor default onlayer portraits with dissolve

    "He places his hands on her."

    "His medical training takes over."

    "He checks every possible sign, searching for any chance to help her."

    show doctor default at left onlayer portraits with dissolve

    doctor "But deep down..."

    doctor "I already know."

    $ brain_hemorrhage_entry.locked = False

    doctor "The fall caused severe damage."

    doctor "A {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}."

    # if ch01_brain_hemorrhage_happened:

    #     #TODO: check if we need a flag here

    #     doctor "\"Exactly like last time...\""

    hide doctor default onlayer portraits with dissolve

    "The hours pass slowly."

    "He remains beside her and tries everything he can."

    "But her condition continues to worsen."

    "Until finally..."

    "She is gone."

    "He holds Mother's hand."

    #TODO: check if this will go corretly (OKEY)

    #TODO: check whether this block of code is needed

    # if not ch01_met_herb_in_door and not ch01_went_to_hospital:

    #     show doctor default at left onlayer portraits

    #     doctor "I came back."

    #     doctor "I answered her call."

    #     doctor "I was here."

    #     doctor "And yet..."

    #     doctor "\"I still couldn't save you.\""

    if ch01_went_to_hospital and ch01_return_from_hospital:

       show doctor default at left onlayer portraits with dissolve

       doctor "I was too late.."

       doctor "I should've just taken the herbs and gone back to her."

       if ch01_loop_count > 0:

        doctor "\"I did it again...\""

        doctor "It's all my fault..."
       




    if ch01_loop_count == 0:
    
        "Eventually, reality begins to settle in."

        "There are things that must be done."

        show doctor default at left onlayer portraits

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        hide doctor default onlayer portraits

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        #show doctor default at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "\"I will save her.\""

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

        hide doctor default onlayer portraits with dissolve

    if not ch01_brain_hemorrhage_happened:

        $ ch01_brain_hemorrhage_happened = True

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop