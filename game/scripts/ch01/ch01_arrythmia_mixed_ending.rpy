label ch01_arrythmia_mixed_ending:

    doctor "\"I can't leave you like this, Mother.\"" 

    if ch01_prepared_formula:

        doctor "I can't keep watching her suffer while I have something that might help..." 

    else:

        doctor "I can't keep watching her suffer while I can make something that might help..." 

    doctor "I can't do nothing."

    doctor "The formula is untested."

    doctor "There are risks."

    doctor "As a doctor, I know that."

    doctor "But..."

    doctor "What if it works?"

    if ch01_check_formula :

        doctor "\"What if it works this time...\""

    else:

        doctor "\"What if it works?\"" 

    doctor "I tell myself that the worst that could happen..."

    doctor "...is that the treatment simply doesn't work."

    doctor "At least I'll have tried."

    "He returns to the laboratory."

    if ch01_prepared_formula:

        "The formula containing {a=glossary:nagomi_root_entry}Nagomi Root{/a} is still there."

    else:

        "He quickly prepares another dose of the {a=glossary:formula_entry}formula{/a}."

    "He holds the vial in his hands."

    "His hands are shaking."

    "Every decision he has made has led to this moment."

    "He brings the vial back to Mother."

    doctor "\"Mother...\""

    doctor "\"This might help you.\""

    "He carefully gives her the formula."

    "She drinks it."

    "Now there is nothing left to do but wait."

    "Minutes pass." 

    "Then hours." 

    "He watches her closely." 

    doctor "I hope.." 

    doctor "I pray that I made the right choice." 

    if ch01_check_formula:

        doctor "No..."

        doctor "The same thing is happening again."
    else:

        doctor "Something is wrong."
    
    "Her condition begins to worsen." 

    "He checks her immediately." 

    "His medical instincts take over." 

    doctor "\"No...\""

    doctor "The symptoms..."

    doctor "The irregular heartbeat..."

    doctor "\"No, no, no...\""

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

    doctor "The formula..." 

    doctor"The choice I made..." 

    doctor "I don't know what hurts more." 

    doctor "Knowing that I might have caused this..." 

    doctor "Or knowing that maybe nothing could have saved her anymore." 

    doctor "Was the treatment the reason she died?" 

    doctor "Or was her illness already beyond saving?"

    if ch01_loop_count == 0:
    
        "Eventually, reality begins to settle in." 

        "There are things that must be done." 

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "I will save her."

        scene black

        "He closes his eyes."

        doctor "\"Tomorrow...\""

        doctor "\"I'll do better.\""

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop
    