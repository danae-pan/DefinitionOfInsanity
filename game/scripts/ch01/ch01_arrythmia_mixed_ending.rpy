label ch01_arrythmia_mixed_ending:

    show doctor default at left onlayer portraits with dissolve

    doctor "I can't leave you like this, Mother." 

    if ch01_prepared_formula:

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "I can't keep watching her suffer while I have something that might help..." 

    else:

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "I can't keep watching her suffer while I can make something that might help..." 

    show doctor default at left onlayer portraits with dissolve

    doctor "The formula is untested."

    doctor "There are risks."

    doctor "As a doctor, I know that."

    doctor "But..."

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    show doctor worried at left onlayer portraits with dissolve

    if ch01_check_formula :

        doctor "What if it works this time..."

    else:

        doctor "What if it works?" 

    doctor "I tell myself that the worst that could happen..."

    doctor "...is that the treatment simply doesn't work."

    doctor "At least I'll have tried."

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"I will be back Mother. Just wait for me.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade 

    #SOUND

    play sound "audio/sfx/footsteps.mp3"
    
    pause 1.2

    play sound "audio/sfx/footsteps.mp3"

    pause 1.2

    play sound "audio/sfx/footsteps.mp3"

    "He returns to the laboratory."

    scene bg ch01 lab_no_cat with fade

    show doctor default at left onlayer portraits with dissolve

    $ nagomi_root_entry.locked = False

    doctor "The formula containing {a=glossary:nagomi_root_entry}Nagomi Root{/a} is still there."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He holds the vial in his hands."

    "His hands are shaking."

    "Every decision he has made has led to this moment."

    "He brings the vial back to Mother."

    show mother default with dissolve

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    doctor "\"This might help you.\""

    hide doctor onlayer portraits with dissolve

    show mother smile with dissolve

    "He carefully gives her the formula."

    "She drinks it."

    "Now there is nothing left to do but wait."

    "Minutes pass." 

    "Then hours." 

    "He watches her closely." 

    show doctor default at left onlayer portraits with dissolve

    doctor "I hope.." 

    doctor "I pray that I made the right choice." 

    show mother sick with dissolve

    #SOUND

    play sound "audio/sfx/suspence.mp3"

    if ch01_check_formula:

        show doctor worried at left onlayer portraits with dissolve

        doctor "No..."

        doctor "The same thing is happening again."
    else:

        hide doctor onlayer portraits with dissolve

        "His Mother seems unusualy unresponsive."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Something is wrong...\""

    hide doctor onlayer portraits with dissolve
    
    "Her condition begins to worsen." 

    "He checks her immediately." 

    "His medical instincts take over." 

    show doctor panicked at left onlayer portraits with dissolve
     

    #SOUND

    play sound "audio/sfx/Gasp.mp3"

    doctor "\"No...\""

    doctor "The symptoms..."

    doctor "The irregular heartbeat..."

    #SOUND

    play sound "audio/sfx/Socked.mp3"

    doctor "\"No, no, no...\""

    hide doctor onlayer portraits with dissolve

    $ arrhythmia_entry.locked = False

    "The formula has triggered a fatal {a=glossary:arrhythmia_entry}arrhythmia{/a}."

    $ ch01_knows_arrhythmia = True

    $ ch01_previous_death = "arrhythmia"

    "He does everything he can." 

    "He tries everything he knows." 

    "But nothing is enough." 

    "The room becomes quiet." 

    "Mother's hand slowly falls still." 

    show default smile with dissolve

    "She is gone." 

    "..." 

    "He stares at the empty vial." 

    show doctor panicked at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/Sigh.mp3"

    doctor "The formula..." 

    doctor "The choice I made..." 

    doctor "I don't know what hurts more." 

    doctor "Knowing that I might have caused this..." 

    doctor "Or knowing that maybe nothing could have saved her anymore." 

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"Was the treatment the reason she died?\""

    doctor "\"Or was her illness already beyond saving?\""

    if ch01_loop_count == 0:

        hide doctor onlayer portraits with dissolve
    
        "Eventually, reality begins to settle in." 

        "There are things that must be done." 

        show doctor default at left onlayer portraits with dissolve

        doctor "I have to report her death." 

        doctor "I have to prepare her body." 

        show doctor worried at left onlayer portraits with dissolve
        
        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "\"I have to tell someone...\""

        hide doctor onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "\"I will save her.\""

        hide doctor onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2_1

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop
    