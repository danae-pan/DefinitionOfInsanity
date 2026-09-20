label ch01_start:

    if ch01_loop_count == 0:

        
        #SOUND

        play sound "audio/sfx/transition.mp3" volume 0.8

        scene chapter_1_title with fade

        pause 3

        scene black with dissolve

    scene bg ch01 lab with fade

    jump ch01_wake_up

label ch01_new_loop:

    $ ch01_loop_count += 1

    call ch01_reset_attempt_state from _call_ch01_reset_attempt_state

    jump ch01_start

label ch01_reset_attempt_state:

    # Reset choices/actions from the previous attempt.
    $ ch01_breakfast_made = False
    $ ch01_bread_added = False
    $ ch01_mother_checked = False
    $ ch01_cat_in_lab = False
    $ ch01_formula_finished = False
    $ ch01_prepare_food = False

    #TODO: check if thosr flags need reset
    #met herbalist in door probably needs reset
    $ ch01_met_herb_in_door = False
    # $ ch01_met_herb_in_hospital = False
    $ herbalist_visited = False

    $ ch01_cat_broke_formula = False
    $ ch01_prepared_formula = False
    $ ch01_went_to_hospital = False

    $ ch01_supplies_from_herbalist = False

    #$ ch01_return_from_hospital = False

    return

label ch01_wake_up:

    if ch01_loop_count == 0:

        

        call ch01_first_wakeup from _call_ch01_first_wakeup
        
    else:

        call ch01_loop_wakeup from _call_ch01_loop_wakeup
        
    menu:

        "Make breakfast":

            scene black with fade

            "He decides to prepare breakfast."
            
            jump ch01_make_breakfast

        "Check on your Mother":
            
            jump ch01_check_mother

label ch01_first_wakeup:

    "A new day begins... and Dr Yosuke wakes up."

    "Once agan, reallity hits him."

    "His Mother is suffering from a mysterious illness, one for which medicine has yet to discover a cure."

    scene bg ch01 lab_no_cat with fade

    show doctor worried at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/Sigh.mp3"

    doctor "I came back to help her survive, and the only way I can do that is by finding the cure myself."

    hide doctor onlayer portraits with dissolve

    "Years of study and countless experiments have brought him closer to several possible treatments."

    show doctor default at left onlayer portraits with dissolve
    
    doctor "One of these {a=glossary:formula_entry}formulas{/a} has to work."

    doctor "\"I just have to keep testing.\""

    hide doctor onlayer portraits with dissolve

    "A sharp pain twists his stomach."

    show doctor default at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "\"I probably didn't eat yesterday...\""

    hide doctor onlayer portraits with dissolve

    "The days have begun to blur together."
    
    "Endless hours spent moving between the laboratory and his Mother's bedside have made him lose all sense of time."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I should see if Mother is awake.\""

    hide doctor onlayer portraits with dissolve

    return

label ch01_loop_wakeup:

    "He slowly opens his eyes."

    if ch01_loop_count == 1:

        "For his entire life, he wished this day would never come."

        "His body feels heavy. His mind feels even heavier."

        "His Mother is dead."

    else: 

        "He wakes up in confusion."

        "Fragments of memories rush through his mind."
    
    "Everything comes back to him."

    #SOUND

    play sound "audio/sfx/Gasp.mp3"

    pause 1.0

    play sound "audio/sfx/suspence.mp3"

    call ch01_remember_previous_deaths from _call_ch01_remember_previous_deaths

    doctor "There's no time to dwell on it."

    doctor "I have too much to do."

    doctor "\"She is in the room… I could go see her.. \""

    hide doctor onlayer portraits with dissolve

    "A dull pain twists his stomach."

    show doctor default at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "\"I probably didn't eat yesterday...\""

    hide doctor onlayer portraits with dissolve

    return

label ch01_remember_previous_deaths:

    if ch01_wake_happened and ch01_loop_count == 1:

        show doctor panicked at left onlayer portraits with dissolve

        $ wake_entry.locked = False

        doctor "\"The {a=glossary:wake_entry}otsuya{/a}… The neighbors...\""

        show doctor default at left onlayer portraits with dissolve


    if knows_dysphagia and ch01_loop_count >=1 and not ch01_brain_hemorrhage_happened and not ch01_knows_arrhythmia and not ch01_knows_coma:

        show doctor worried at left onlayer portraits with dissolve

        $ dysphagia_entry.locked = False

        doctor "\"The {a=glossary:dysphagia_entry}dysphagia{/a}… The bread...\""

        show doctor default at left onlayer portraits with dissolve


    #TODO: check those two condirions
        
    if ch01_brain_hemorrhage_happened and ch01_loop_count >=1 and not knows_dysphagia  and not ch01_knows_arrhythmia and not ch01_knows_coma:

        show doctor worried at left onlayer portraits with dissolve

        doctor "The broken glass in the floor... Mother's fall..."

        show doctor default at left onlayer portraits with dissolve

    
    if ch01_knows_arrhythmia and ch01_loop_count >=1 and not knows_dysphagia  and not ch01_brain_hemorrhage_happened and not ch01_knows_coma:

        show doctor worried at left onlayer portraits with dissolve

        $ nagomi_root_entry.locked = False

        $ arrhythmia_entry.locked = False

        doctor "The {a=glossary:nagomi_root_entry}Nagomi Root{/a}... It caused her {a=glossary:arrhythmia_entry}arrhythmia{/a}..."

        show doctor default at left onlayer portraits with dissolve

    
    if ch01_knows_coma and ch01_loop_count >=1 and not knows_dysphagia  and not ch01_brain_hemorrhage_happened and not ch01_knows_arrhythmia:

        show doctor worried at left onlayer portraits with dissolve

        $ coma_entry.locked = False

        doctor "I didn't gave her the formula... She died from {a=glossary:coma_entry}coma{/a}..."

        show doctor default at left onlayer portraits with dissolve


    if (ch01_knows_arrhythmia
        + ch01_knows_coma
        + ch01_brain_hemorrhage_happened
        + knows_dysphagia >= 2):

        doctor "What am I supposed to do now?"

        doctor "\"How can I save her?\""

        hide doctor worried onlayer portraits with dissolve

        "He let's out a sigh worrying whether he will be able to save her before he runs out of time."

        show doctor default at left onlayer portraits with dissolve

    return


label ch01_remember_previous_death_for_ch02:

    if ch01_previous_death == "dysphagia":
        doctor "The dysphagia... The bread..."

    elif ch01_previous_death == "brain_hemorrhage":
        doctor "The broken glass on the floor... Mother's fall..."

    elif ch01_previous_death == "arrhythmia":
        doctor "The Nagomi Root... It caused her arrhythmia..."

    elif ch01_previous_death == "coma":
        doctor "I didn't give her the formula... She died from a coma..."

    return