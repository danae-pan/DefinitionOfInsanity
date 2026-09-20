label ch01_straight_to_lab :

    scene bg ch01 lab_no_cat with fade

    call ch01_study_prepare_formula from _call_ch01_study_prepare_formula

    "A sudden noise breaks the silence."

    scene bg ch01 lab with fade

    "He looks up to see Mother's cat leaping from chair to chair."

    "Completely absorbed in chasing a fly that somehow found its way inside."

    show doctor default at left onlayer portraits with dissolve

    doctor "She pays no attention to the equipment around her..."

    doctor "\"Easy there, little one...\"" 

    doctor "Maybe I should let her outside."

    if kept_cat_in_lab_once :

        doctor "Last time I let her stay in the laboratory she broke the formula..."

    menu :

        "Let your cat outside":

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Come on, little one.\""

            hide doctor onlayer portraits with dissolve

            scene black with fade

            "He gently picks up the cat and carries her outside."

            scene bg ch01 lab_no_cat with fade

            show doctor default at left onlayer portraits with dissolve

            doctor "Today I need my full concentration. I can't afford any distractions."

            hide doctor onlayer portraits with dissolve

            jump ch01_mother_calls_knock_on_door
        
        "Keep your cat in the laboratory":

            jump ch01_keep_cat_in_lab_mother_calls

# Event You and your mother eat You head to your lab
# Choices
#   Lab choice (about the cat)

label ch01_eat_then_lab:

    #TODO: see if hiding the sprite here is necessary

    hide doctor onlayer portraits with dissolve

    "He helps her with her food while eating his own meal."

    menu :

        "Say story about cat" :

            show doctor default at left onlayer portraits with dissolve

            #doctor expression: neutral smile

            doctor "\"You know, your cat has been doing some strange things these past few days.\""

            hide doctor onlayer portraits with dissolve

            #mother expression: tired smile

            "She looks up at him , trying to smile."

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Yesterday I caught her sitting in front of the mirror for almost ten minutes.\""

            doctor "\"She was just staring at herself like she had discovered another cat living in the house.\""

            hide doctor onlayer portraits with dissolve
            
            "Her expression immediately brightens."

            #mother expression: slighty surprised smile

            mother "\"...Curious...\""

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Yeah. That's exactly what I thought.\""

            hide doctor onlayer portraits with dissolve

        "Say story about garden" :
            
            show doctor default at left onlayer portraits with dissolve

            doctor "\"I checked the flowers in the garden this morning.\""

            hide doctor onlayer portraits with dissolve

            "She looks up at him."

            show doctor smile at left onlayer portraits with dissolve

            $ ajisai_entry.locked = False

            doctor "\"The {a=glossary:ajisai_entry}ajisai{/a} you thought was dying...\""

            doctor "\"There are new leaves coming out.\"" 

            hide doctor onlayer portraits with dissolve

            "A tear forms in the corner of her eye." 

            mother "\"...Really?\""

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Yeah. Looks like it wasn't ready to give up just yet.\""

            hide doctor onlayer portraits with dissolve

    "After they finished eating..."

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"I'll leave you to rest now, Mother.\""
    
    doctor "\"Call me if you need anything, alright?\""
    
    doctor "\"I'll be in the laboratory.\""

    hide doctor onlayer portraits with dissolve
    
    scene black with fade

    "He returns to the laboratory."

    scene bg ch01 lab_no_cat with fade

    if ch01_loop_count == 0:

        "All the ingredients he brought from the hospital are still there."

        "Everything he needs to continue his research from home."

    else:

        "He takes a deep breath."

        "He looks at his supplies."

        show doctor default at left onlayer portraits with dissolve

        doctor "I should start working."

        hide doctor onlayer portraits with dissolve

    "His notes are waiting on the desk."

    "Then he notices movement in the corner of the room."

    #expression: skeptical
    #background: lab without the cat
    scene bg ch01 lab with fade

    "His Mother's cat is wondering around the laboratory."

    show doctor default at left onlayer portraits with dissolve

    doctor "Should I let her stay?"

    doctor "\"It would be nice to have some company...\""

    hide doctor onlayer portraits with dissolve

    "He looks around the empty laboratory."

    "The silence has become his only companion."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I can't let anything interfere with my research...\""

    hide doctor onlayer portraits with dissolve

    if kept_cat_in_lab_once:

        "Another memory returns."

        show doctor worried at left onlayer portraits with dissolve

        doctor "Last time i kept her inside see broke the formula. I should not risk it again."

        hide doctor onlayer portraits

    menu:

        "Take the cat outside":

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Come on, little one.\""

            hide doctor onlayer portraits with dissolve

            scene black with fade

            "He gently picks up the cat and carries her outside."

            scene bg ch01 lab_no_cat with fade

            show doctor default at left onlayer portraits with dissolve

            doctor "Today I need my full concentration. I can't afford any distractions."

            hide doctor onlayer portraits with dissolve
            
            call ch01_study_prepare_formula from _call_ch01_study_prepare_formula_1

            jump ch01_mother_calls_knock_on_door

        "Let the cat stay in the laboratory":

            $ ch01_cat_in_lab = True

            jump ch01_cat_becomes_noisy

label ch01_study_prepare_formula:

    "He sits at his chair and spreads his notes across the table."

    "His eyes move between the old research papers and the herbs carefully arranged in front of him."

    show doctor default at left onlayer portraits with dissolve

    "The treatment needs to work in three phases."

    "First, I need to prepare her body and create the best possible conditions for recovery."

    "Then, I need to stimulate the damaged nervous system... encourage healthy neurons to compensate for those that were lost."

    "And finally..."

    "If I can combine the effects of both phases, perhaps I can force the new pathways to synchronize with the rest of her nervous system."

    "There's no evidence that the last step will work."

    "But if I'm right..."

    $ nagomi_root_entry.locked = False

    doctor "\"{a=glossary:nagomi_root_entry}Nagomi Root{/a}...\""

    doctor "Phase 1. Preparing the body for recovery..."

    hide doctor onlayer portraits with dissolve

    "He picks up the jar and examines the remaining amount."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I have more than enough.\""

    $ anti_inflammatory_entry.locked = False

    doctor "Its {a=glossary:anti_inflammatory_entry}anti-inflammatory{/a} and soothing properties could help ease Mother's symptoms."

    hide doctor onlayer portraits with dissolve

    if not ch01_knows_licorice:

        $ ch01_knows_licorice = True

    if ch01_knows_arrhythmia : 

        "A memory interrupts his thoughts."

        show doctor worried at left onlayer portraits with dissolve

        doctor "I have strong indications that this can cause {a=glossary:arrhythmia_entry}arrhythmia{/a} to Mother... But I have nothing else to try..."

        hide doctor onlayer portraits with dissolve

    "His attention shifts to another jar."

    show doctor default at left onlayer portraits with dissolve

    $ hogo_root_entry.locked = False

    doctor "\"{a=glossary:hogo_root_entry}Hogo Root{/a}.\""

    doctor "Phase 2. Protecting the nervous system and encouraging it to adapt..."

    hide doctor onlayer portraits with dissolve

    "He checks the remaining supply."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Enough for just one dose.\""

    doctor "Some studies suggest it has neuroprotective effects."

    if not ch01_knows_polygala:
        
        $ ch01_knows_polygala = True

    doctor "If Nagomi Root can reduce the inflammation..."

    $ nervous_system_entry.locked = False

    doctor "...then perhaps Hogo Root can help protect the {a=glossary:nervous_system_entry}nervous system{/a}."

    doctor "\"..It's worth trying.\""

    hide doctor onlayer portraits with dissolve

    "He carefully measures every ingredient."

    "Every movement is precise."

    "The herbs are ground into a fine powder before being slowly mixed into the solution."

    "The color of the {a=glossary:formula_entry}formula{/a} changes as the ingredients dissolve."

    "Finally, he pours the finished mixture into a small glass vial."

    # we need another flag here to go inside the loop because the fact that he has repeated he day doesn't mean he prepared already the formula before.

    #TODO: check this condition when the fitst condition is true
    #didn;t work because it resets on each ending. replaced with check_apothecary flag
    if (ch01_loop_count >= 1 and ch01_check_apothecary == True) or (ch01_loop_count >= 1 and ch01_check_formula == True):

        "His hands stop for a moment."

        show doctor default at left onlayer portraits  with dissolve

        doctor "I did everything exactly as the last time." 

        hide doctor onlayer portraits with dissolve

    #TODO: check if this condition needs to be removed

    if ch01_cat_in_lab:

        "He notices movement nearby."

        scene bg ch01 lab with fade
        
        show doctor default at left onlayer portraits with dissolve

        doctor "I should be careful with the formula, the cat is inside the laboratory."

        hide doctor onlayer portraits with dissolve

    "He places the vial safely aside and reaches for his notebook."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Now...\"" 

    doctor "\"Let's make sure I didn't overlook anything.\"" 

    hide doctor onlayer portraits with dissolve

    "He compares every measurement with his notes." 

    "He reads through every page again." 

    $ ch01_prepared_formula = True

    return

    # jump ch01_mother_calls_knock_on_door

label ch01_cat_becomes_noisy:

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Come on, little one.\""

    hide doctor onlayer portraits with dissolve

    "He gently picks up the cat."

    "She relaxes in his arms, purring softly."

    "For a moment, the laboratory feels less lonely."

    "He lets her walk around the room, exploring every corner."

    # it is probably alrady like that.

    scene bg ch01 lab with fade

    call ch01_study_prepare_formula from _call_ch01_study_prepare_formula_2
            
    "A sudden noise breaks the silence."

    "He looks up."

    "Mother's cat is jumping from chair to chair."

    "She's chasing a fly that somehow found its way into the laboratory." 

    if kept_cat_in_lab_once:

        "A familiar memory returns."

        show doctor worried at left onlayer portraits with dissolve

        doctor "I have seen this before... if I let her stay inside she maybe break the formula again."

        doctor "Do I risk it?"

        hide doctor onlayer portraits with dissolve

    else:

        show doctor default at left onlayer portraits with dissolve
        
        doctor "\"Easy there, little one...\"" 

        doctor "Maybe I should let her outside."

        hide doctor default onlayer portraits with dissolve

    menu:

        "Carry her outside":

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"Come on, little one.\""

            hide doctor  onlayer portraits with dissolve

            scene black with fade

            "He gently picks up the cat and carries her outside."

            scene bg ch01 lab_no_cat with fade

            show doctor default at left onlayer portraits with dissolve

            doctor "Today I need my full concentration. I can't afford any distractions."

            hide doctor onlayer portraits with dissolve

            jump ch01_mother_calls_knock_on_door

        "Let her stay":
            
            jump ch01_cat_breaks_formula

label ch01_cat_breaks_formula:

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Try to be quiet, little one. I don't want to escort you outside.\""

    doctor "Today I need my full concentration. I can't afford any distractions."

    hide doctor onlayer portraits with dissolve

    "He looks over his notes one more time."

    #change the lab background with the cat in it

    # probably already done

    scene bg ch01 lab with fade

    "Suddenly, the cat jumps onto his desk!"

    #TODO: check the places for the right bg

    scene bg ch01 lab with fade

    if kept_cat_in_lab_once:

        "Its happening again!"

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"No! Get out of here!\""

    hide doctor onlayer portraits with dissolve

    "But it's too late… She tries to leave form the desk but things get in her way."

    #noise of breaking glass

    "Bottles start breaking."

    show doctor worried at left onlayer portraits with dissolve

    #doctor expression panicked

    doctor "\"Not this one!\""

    hide doctor onlayer portraits with dissolve

    "The doctor tries to catch the formula but it falls in the ground and breaks."

    $ ch01_cat_broke_formula = True

    show doctor panicked at left onlayer portraits with dissolve

    doctor "\"No No No.\""

    doctor "\"This can't be happening!\""

    if kept_cat_in_lab_once:

        doctor "How could I make this mistake again?"

    #lab background without the cat
    hide doctor onlayer portraits with dissolve

    "He turns to find the cat, but she is nowhere to be found."

    show doctor panicked at left onlayer portraits with dissolve

    doctor "I have to make the formula again."

    doctor "I have to check what herbs I have at the apothecary."

    doctor "Or I could go to the hospital and replenish my herbs."

    hide doctor onlayer portraits with dissolve

    $ ch01_prepared_formula = False

    if not kept_cat_in_lab_once:

        $ kept_cat_in_lab_once = True

    menu:

        "Check your stock on your apothecary":

            jump ch01_check_on_the_apothecary

        "Go to the hospital to restore your herbs":

            jump ch01_go_to_hospital

label ch01_check_on_the_apothecary:

    show doctor default at left onlayer portraits with dissolve

    doctor "Hogo root was just enough for the dose I made."

    doctor "I might not be able to make another..."

    doctor "\"I should look anyway.\""

    hide doctor onlayer portraits with dissolve

    "He desperately search the shelves."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"No luck...\""

    doctor "I will have to go to the hospital for herbs after all."

    $ ch01_prepared_formula = False

    $ ch01_check_apothecary = True

    hide doctor onlayer portraits with dissolve

    jump ch01_mother_calls_knock_on_door

label ch01_mother_calls_knock_on_door:

    mother "\"Yosuke...\""

    if ch01_mother_called:

        "He hears his Mother calling for him again..."

    else: 

        "He hears Mother's weak voice calling from her room."

    show doctor default at left onlayer portraits with dissolve

    doctor "I should check on her."

    hide doctor onlayer portraits with dissolve

    # audio *Knock... Knock...* 

    "*Knock... Knock...*" 

    "A noise comes from the front door."

    $ ch01_knock_knock = True
    
    if not ch01_met_herb_in_door:

        show doctor default at left onlayer portraits with dissolve

        doctor "Someone is at the door?"

        hide doctor onlayer portraits with dissolve

    else: 

        show doctor default at left onlayer portraits with dissolve

        doctor "Maybe it's Mr. Kazuki again."

        hide doctor onlayer portraits

    menu:

        "Open the door":

            jump ch01_meet_herbalist_on_door

        "Answer your Mother call":

            jump ch01_answer_mothers_call

label ch01_keep_cat_in_lab_mother_calls:

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Come on, little one.\""

    hide doctor onlayer portraits with dissolve

    "He cradles her in his arms, and she purrs softly."

    "He lets her wander around the room..."

    scene bg ch01 lab with fade

    mother "\"Yosuke...\""

    $ ch01_mother_called = True

    "He hears Mother's weak voice calling from her room."

    show doctor default at left onlayer portraits with dissolve

    doctor "I should check on her."

    doctor "But I have so much work…"

    hide doctor onlayer portraits with dissolve

    $ ch01_cat_in_lab = True

    menu :

        "Continue studying":

            show doctor default at left onlayer portraits with dissolve

            doctor "I'll do one last check, then I'll go to her."

            hide doctor onlayer portraits

            jump ch01_mother_calls_knock_on_door

        "Go to her":

            jump ch01_check_mother_cat_in_lab

label ch01_check_mother_cat_in_lab :

    "He sets his notes aside."

    show doctor worried at left onlayer portraits with dissolve

    doctor "Mother sounded weaker this time."

    doctor "I can't ignore her."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He leaves the laboratory and walks to her room."

    show mother sick with dissolve

    "She is sitting up in bed."

    "Even breathing seems to tire her."

    mother "\"Yosuke...\""

    "He kneels beside her."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"How are you feeling?\""

    mother "\"...Hungry.\""

    hide doctor onlayer portraits with dissolve

    "She is not eating much..."

    "The illness has taken what little strength she had."

    "He glances toward the laboratory."

    "The formula is still untested."

    show doctor worried at left onlayer portraits with dissolve

    doctor "Every minute I spend away from my research delays my work."

    doctor "But every minute I stay in the laboratory..."

    doctor "...Mother suffers alone."

    doctor "I have to choose."

    hide doctor onlayer portraits with dissolve

    menu :

        "Prepare food for her":

            $ ch01_prepare_food = True
            #TODO: see if the following lines are needed in other routes that end up in the same menu choices
            show doctor default at left onlayer portraits with dissolve

            doctor "\"I will prepare something for you Mother.\""

            doctor "\"I will be back soon.\""

            mother "\"Thank you my son.\""

            hide doctor onlayer portraits with dissolve

            scene black with fade

            "He heads to the kitchen."

            scene bg ch01 kitchen with fade

            "He started preparing food when some noise from the lab distracted him."

            show doctor default at left onlayer portraits with dissolve

            doctor "That noise comes from the laboratory..."

            show doctor worried at left onlayer portraits with dissolve

            doctor "\"The cat! I left her inside!\""

            hide doctor onlayer portraits with dissolve

            scene black with fade

            "He quickly heads to his laboratory."

            scene bg ch01 lab with fade

            jump ch01_cat_breaks_formula

        "Return to study":

            scene bg ch01 lab_no_cat with fade

            "He returns to his lab to study some more about the formula he made..."

            jump ch01_mother_calls_knock_on_door