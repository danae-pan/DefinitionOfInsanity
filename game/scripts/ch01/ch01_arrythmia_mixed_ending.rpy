label ch01_arrythmia_mixed_ending:

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I can't leave you like this, Mother.\"" 

    if ch01_prepared_formula:

        doctor "I can't keep watching her suffer while I have something that might help..." 

    else:

        doctor "I can't keep watching her suffer while I can make something that might help..." 

    doctor "The formula is untested."

    doctor "There are risks."

    doctor "As a doctor, I know that."

    doctor "But..."

    if ch01_check_formula :

        doctor "What if it works this time..."

    else:

        doctor "What if it works?" 

    doctor "I tell myself that the worst that could happen..."

    doctor "...is that the treatment simply doesn't work."

    doctor "At least I'll have tried."

    doctor "\"I will be back Mother. Just wait for me.\""

    hide doctor default onlayer portraits with dissolve

    #to be removed??


    scene black with fade 

    "He returns to the laboratory."

    scene bg ch01 lab with fade

    if ch01_prepared_formula:

        show doctor default at left onlayer portraits with dissolve

        doctor "The formula containing {a=glossary:nagomi_root_entry}Nagomi Root{/a} is still there."

        hide doctor default onlayer portraits with dissolve

    else:

        "He quickly prepares another dose of the {a=glossary:formula_entry}formula{/a}."

    
    scene black with fade

    "He holds the vial in his hands."

    "His hands are shaking."

    "Every decision he has made has led to this moment."

    "He brings the vial back to Mother."

    scene bg ch01 mother with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    doctor "\"This might help you.\""

    hide doctor default onlayer portraits with dissolve

    "He carefully gives her the formula."

    "She drinks it."

    "Now there is nothing left to do but wait."

    "Minutes pass." 

    "Then hours." 

    "He watches her closely." 

    show doctor default at left onlayer portraits with dissolve

    doctor "I hope.." 

    doctor "I pray that I made the right choice." 

    if ch01_check_formula:

        doctor "No..."

        doctor "The same thing is happening again."
    else:

        hide doctor default onlayer portraits with dissolve

        "His mother seems unusualy unresponsive."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Something is wrong...\""

    hide doctor default onlayer portraits with dissolve
    
    "Her condition begins to worsen." 

    "He checks her immediately." 

    "His medical instincts take over." 

    show doctor default at left onlayer portraits with dissolve

    doctor "\"No...\""

    doctor "The symptoms..."

    doctor "The irregular heartbeat..."

    doctor "\"No, no, no...\""

    hide doctor default onlayer portraits with dissolve

    $ arrhythmia_entry.locked = False

    "The formula has triggered a fatal {a=glossary:arrhythmia_entry}arrhythmia{/a}."

    $ ch01_knows_arrhythmia = True

    "He does everything he can." 

    "He tries everything he knows." 

    "But nothing is enough." 

    "The room becomes quiet." 

    "Mother's hand slowly falls still." 

    "She is gone." 

    "..." 

    "He stares at the empty vial." 

    show doctor default at left onlayer portraits with dissolve

    doctor "The formula..." 

    doctor "The choice I made..." 

    doctor "I don't know what hurts more." 

    doctor "Knowing that I might have caused this..." 

    doctor "Or knowing that maybe nothing could have saved her anymore." 

    doctor "\"Was the treatment the reason she died?\""

    doctor "\"Or was her illness already beyond saving?\""

    if ch01_loop_count == 0:

        hide doctor default onlayer portraits with dissolve
    
        "Eventually, reality begins to settle in." 

        "There are things that must be done." 

        show doctor default at left onlayer portraits

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        hide doctor default onlayer portraits

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        show doctor default at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "\"I will save her.\""

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_1

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop
    