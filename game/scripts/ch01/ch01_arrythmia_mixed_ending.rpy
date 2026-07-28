label ch01_arrythmia_mixed_ending:

    doctor "I can't leave you like this, Mother." 

    if ch01_prepared_formula:

        "Watching her suffer while I have something that might help..." 

    else:

        "Watching her suffer while I can make something that might help..." 

    "I can't do nothing." 

    "The formula is untested." 

    "There are risks." 

    "As a doctor, I know that." 

    "But..." 

    "What if it works?" 

    if ch01_check_formula :

        "What if it works this time..."

    else:

        "What if it works?" 

    "What if this is the chance I have been searching for?" 

    "I tell myself the worst that can happen..." 

    "...is that the treatment simply doesn't work." 

    "At least I will have tried." 

    "I return to the laboratory." 

    if ch01_prepared_formula :

        "The formula containing Licorice Root is still there." 

    else: 

        "I quicly prepare the formula."

    "I hold the vial in my hands." 

    "My hands are shaking." 

    "Every decision I have made has led to this moment." 

    "I bring it back to Mother." 

    doctor "Mother..." 

    doctor "This might help you." 

    "I carefully give her the formula." 

    "She drinks it." 

    "Now there is nothing left to do but wait." 

    "Minutes pass." 

    "Then hours." 

    "I watch her closely." 

    "I hope." 

    "I pray that I made the right choice." 

    if ch01_check_formula:

        "But no the same thing repeats." 
    else:

        "But something is wrong." 
    
    "Her condition begins to worsen." 

    "I check her immediately." 

    "My medical instincts take over." 

    "No..." 

    "The symptoms..." 

    "The irregular heartbeat..." 

    doctor "No, no, no..." 

    "The formula triggered a fatal arrhythmia." 

    $ ch01_knows_arrhythmia = True

    "I do everything I can." 

    "I try everything I know." 

    "But nothing is enough." 

    "The room becomes quiet." 

    "Mother's hand slowly falls still." 

    "She is gone." 

    "..." 

    "I stare at the empty vial." 

    "The formula." 

    "The choice I made." 

    "I don't know what hurts more." 

    "Knowing that I might have caused this..." 

    "Or knowing that maybe nothing could have saved her anymore." 

    "Was the treatment the reason she died?" 

    "Or was her illness already beyond saving?"

    if ch01_loop_count == 0:
    
        "Eventually, reality returns." 

        "There are things that need to be done." 

        "I have to report her death." 

        "I have to prepare her body." 

        "I have to tell someone."

        "Wake"

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        "If I get another chance..." 

        "I will not repeat this." 

        "I will save her."

        scene black 

        "I close my eyes." 

        "Tomorrow..." 

        "I will do better."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop
    