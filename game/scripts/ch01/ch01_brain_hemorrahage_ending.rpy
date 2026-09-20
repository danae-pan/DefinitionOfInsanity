label ch01_brain_hemorrahage_ending:

    "He hesitates after hearing Mr. Kazuki's offer." 

    show doctor default at left onlayer portraits with dissolve

    doctor "The herbs in Mr. Kazuki's store could be exactly what I need."

    doctor "Ingredients the hospital cannot provide..."

    doctor "But Mother called for me."

    doctor "No matter how important my research is..."

    doctor "I can't ignore her."

    if not ch01_went_to_hospital:

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"Thank you, Mr. Kazuki.\""

        doctor "\"I'll visit your store another time.\""

        hide doctor onlayer portraits

        show herbalist smile at left onlayer portraits

        herbalist "\"Alrigh then.\""

        herbalist "\"I hope I'll see you soon Mr. Yosuke.\""

        herbalist "\"Take care.\""

        hide herbalist onlayer portraits

        show doctor smile at left onlayer portraits

        doctor "\"Goodbye Mr. Kazuki.\""

        hide doctor onlayer portraits with dissolve

        "Mr. Kazuki turns around and walks away."

        "The Doctor wonders if he made the right choice..."


    else:

        hide doctor onlayer portraits with dissolve

        scene black with fade

        "He quickly returns home worried about his Mother."

        "He opens the door."

        scene bg game_main with fade

        show doctor default at left onlayer portraits with dissolve
    

    doctor "\"Mother?\""

    hide doctor onlayer portraits with dissolve

    "..." 

    "There is no answer." 

    "He quickly heads to his Mother's room."

    show mother default with dissolve

    "Her face is pale."

    "She looks exhausted."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    hide doctor onlayer portraits with dissolve

    show mother sick with dissolve

    "He immediately checks her condition."

    "Her breathing is uneven."

    if not ch01_brain_hemorrhage_happened:

        "Then he notices something."

        "A broken glass lies on the floor."

        "Water has spilled across the room."

        "The bottle beside her bed is empty."

        "..."

        show doctor panicked at left onlayer portraits with dissolve
        with punch

        doctor "She needed water and tried to get it herself..."

        doctor "While I was speaking with Mr. Kazuki..."

        doctor "\"Oh, Mother...\""

        doctor "Her weakened body couldn't support her."

        doctor "She fell."

        doctor "She wanted help but I was away..."

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"This is all my fault...\""

        doctor "\"I'm so sorry Mother.\""

        hide doctor onlayer portraits with dissolve

    else:

        show doctor panicked at left onlayer portraits with dissolve
        with vpunch

        doctor "It's the same scene as before..."

        doctor "The broken glass..."

        doctor "The empty bottle..."

        hide doctor onlayer portraits with dissolve

    "He places his hands on her."

    "His medical training takes over."

    "He checks every possible sign, searching for any chance to help her."

    show doctor worried at left onlayer portraits with dissolve

    doctor "But deep down..."

    doctor "I already know."

    $ brain_hemorrhage_entry.locked = False

    doctor "The fall caused severe damage."

    doctor "A {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}."

    hide doctor onlayer portraits with dissolve

    "The hours pass slowly."

    "He remains beside her and tries everything he can."

    "But her condition continues to worsen."

    "Until finally..."

    show mother default with dissolve

    "She is gone."

    "He holds Mother's hand."

    if ch01_met_herb_in_door:

        show doctor worried at left onlayer portraits with dissolve
        with vpunch

        doctor "I came back."

        doctor "I answered her call."

        doctor "I was here."

        doctor "And yet..."

        doctor "\"I still couldn't save you.\""

    if ch01_went_to_hospital and ch01_return_from_hospital:

       show doctor worried at left onlayer portraits with dissolve
       with vpunch

       doctor "I was too late.."

       doctor "I should've just taken the herbs and gone back to her."

       if ch01_loop_count > 0:

        doctor "\"I did it again...\""

        doctor "It's all my fault..."
       




    if ch01_loop_count == 0:

        hide doctor onlayer portraits with dissolve
    
        "Eventually, reality begins to settle in."

        "There are things that must be done."

        show doctor default at left onlayer portraits with dissolve

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"I have to tell someone...\""

        hide doctor onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        show doctor worried at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "\"I will save her.\""

        hide doctor onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

        hide doctor onlayer portraits with dissolve

    if not ch01_brain_hemorrhage_happened:

        $ ch01_brain_hemorrhage_happened = True

    $ ch01_previous_death = "brain_hemorrhage"

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop