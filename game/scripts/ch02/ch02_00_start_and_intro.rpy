label ch02_new_loop:

    $ ch02_loop_count += 1

    jump ch02_start

label ch02_start:

    if (
        ch02_first_herb_without_instructions
        and ch02_first_herb_with_instructions
        and ch02_second_herb_without_instructions
        and ch02_second_herb_with_instructions
    ):
        jump ch02_ending

    call ch02_reset_runtime_state from _call_ch02_reset_runtime_state

    if ch02_loop_count == 0:

        scene chapter_2_title with fade

        pause 3

        scene black with dissolve


    jump ch02_intro

label ch02_reset_runtime_state:

    # Reset choices/actions from the previous attempt.
    $ ch02_cat_in_lab = False
    $ ch02_cat_broke_formula = False

    $ ch02_first_herb_taken = False
    $ ch02_second_herb_taken = False

   # $ ch02_used_panax = False

    $ ch02_mother_checked = False
    $ ch02_formula_prepared = False

    $ ch02_route_choice = None

    $ ch02_coming_from_hospital = False

    return

label ch02_intro:

    scene bg ch01 lab_no_cat with fade

    #TODO: Add chapter 2 label

    if ch02_loop_count == 0:

        #First time entering chapter 2

        if chapter_1_with_one_try:

            $ wake_entry.locked = False

            "He wakes up in a daze. He cannot believe his Mother is no more."

            doctor "How could I let this be? I don’t deserve to call myself a doctor."

            doctor "No time for this, I should prepare the death certificate and go to the municipality."
            
            doctor "But first, I should prepare my Mother for the {a=glossary:wake_entry}otsuya{/a}."

            "He heads to his Mother’s room and for his surprise, find her alive."

            doctor "Wait a second, what? Am I in a dream?"

            "He slaps himself, pinch his arm and he feels the pain."

            doctor "Maybe yesterday was just a nightmare? Maybe Mother never died."

            doctor "No way, I remember it clearly."

            doctor "This is an act of god, I should take advantage of this second chance to save her this time."
        
        else:

            #Remembers death from chapter 1

            "He wakes up in a daze. Slowly, everything comes back to him."
            
            show doctor default at left onlayer portraits with dissolve

            call ch01_remember_previous_death_for_ch02

            doctor "Mother might still be alive."

            hide doctor default onlayer portraits with dissolve


    else:

        #Remember death from chapter 2

        "He wakes up in a daze. Slowly, everything comes back to him."
        
        show doctor default at left onlayer portraits with dissolve

        call ch02_remember_previous_death

        doctor "But she might still be alive..."

        hide doctor default onlayer portraits with dissolve


    "He is thinking he should run some tests to check whether everything is okey."

    show doctor default at left onlayer portraits with dissolve
    
    doctor "Maybe I shouldn’t lose time.."

    doctor "Maybe I should start trying different herb instead."

    hide doctor default onlayer portraits with dissolve

    menu :

        "Check on your Mother":

            #TODO:reset the chosen from menu choices to their default state

            $ ch02_route_choice = "check_mother"

            jump ch02_check_mother

        "Try a different herb":

            $ ch02_route_choice = "try_herb"

            jump ch02_try_different_herb

    return

