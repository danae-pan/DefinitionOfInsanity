label ch01_straight_to_lab :

    scene bg ch01 lab with fade

    call ch01_study_prepare_formula

    "A sudden noise breaks the silence."

    "He looks up to see Mother's cat leaping from chair to chair."

    "Completely absorbed in chasing a fly that somehow found its way inside, she pays no attention to the equipment around her."

    show doctor default at left onlayer portraits

    doctor "\"Easy there, little one...\"" 

    hide doctor default onlayer portraits

    doctor "Maybe I should let her outside."

    if kept_cat_in_lab_once :

        doctor "Last time i let her stay in the back she broke the {a=glossary:formula_entry}formula{/a}..."

    menu :

        "Let your cat outside":

            "He gently picks up the cat and carries her outside."

            doctor "Today I need my full concentration. I can't afford any distractions."

            jump ch01_mother_calls_knock_on_door
        
        "Keep your cat in the lab":

            jump ch01_keep_cat_in_lab_mother_calls

# Event You and your mother eat You head to your lab
# Choices
#   Lab choice (about the cat)

label ch01_eat_then_lab:

    "He helps her with her food while eating his own meal."

    menu :

        "Say story about cat" :

            show doctor default at left onlayer portraits

            doctor "\"You know, your cat has been doing some strange things these past few days.\""

            hide doctor default onlayer portraits

            "She looks up at him , trying to smile."

            show doctor default at left onlayer portraits

            doctor "\"Yesterday I caught her sitting in front of the mirror for almost ten minutes.\""

            doctor "\"She was just staring at herself like she had discovered another cat living in the house.\""

            hide doctor default onlayer portraits
            
            "Her expression immediately brightens."

            mother "\"...Curious...\""

            show doctor default at left onlayer portraits

            doctor "\"Yeah. That's exactly what I thought.\""

            hide doctor default onlayer portraits

        "Say story about garden" :
            
            show doctor default at left onlayer portraits

            doctor "\"I checked the flowers in the garden this morning.\""

            hide doctor default onlayer portraits

            "She looks up at him."

            show doctor default at left onlayer portraits

            doctor "\"The ajisai you thought was dying... \""

            doctor "\"There are new leaves coming out.\"" 

            hide doctor default onlayer portraits

            "A tear forms in the corner of her eye." 

            mother "\"...Really?\""

            show doctor default at left onlayer portraits

            doctor "\"Yeah. Looks like it wasn't ready to give up just yet.\""

            hide doctor default onlayer portraits

    "After they finished eating..."

    show doctor default at left onlayer portraits

    doctor "\"I'll leave you to rest now, Mother. Call me if you need anything, alright? I'll be in the laboratory.\""

    hide doctor default onlayer portraits
    
    scene bg ch01 lab

    "He returns to the laboratory."

    if ch01_loop_count == 0:

        "All the ingredients he brought from the hospital are still there."

        "Everything he needs to continue his research from home."

    else:

        "The ingredients are still exactly where he left them."

        "Nothing has been used."

        doctor "I guess… I should try again."

    "His notes are waiting on the desk."

    "Then he notices movement in the corner of the room."

    doctor "Should I let her stay?"

    doctor "It would be nice to have some company..."

    "He looks around the empty laboratory."

    "The silence has become his only companion."

    doctor "But I can't let anything interfere with my research."

    doctor "Not this time."

    if kept_cat_in_lab_once:

        "Another memory returns."

        doctor "Last time i kept her inside see broke the formula. I should not risk it again."

    menu:

        "Let your cat outside":

            show doctor default at left onlayer portraits

            doctor "\"Come on, little one.\""

            hide doctor default onlayer portraits

            "He gently picks up the cat and carries her outside."

            doctor "Today I need my full concentration. I can't afford any distractions."
            
            call ch01_study_prepare_formula

            jump ch01_mother_calls_knock_on_door

        "Keep your cat in the lab":

            $ ch01_cat_in_lab = True

            jump ch01_formula_cat_noisy

label ch01_study_prepare_formula:

    "He sits at the desk and spreads his notes across the table."

    "His eyes move between the old research papers and the herbs carefully arranged in front of him."

    show doctor default at left onlayer portraits

    $ nagomi_root_entry.locked = False

    doctor "\"{a=glossary:nagomi_root_entry}Nagomi Root{/a}...\""

    hide doctor default onlayer portraits

    "He picks up the jar and examines the remaining amount."

    doctor "\"Enough for one full dose.\""

    show doctor default at left onlayer portraits

    $ anti_inflammatory_entry.locked = False

    doctor "Its {a=glossary:anti_inflammatory_entry}anti-inflammatory{/a} and soothing properties could help ease Mother's symptoms."

    hide doctor default onlayer portraits

    if not ch01_knows_licorice:

        $ ch01_knows_licorice = True

    if ch01_knows_arrhythmia : 

        "A memory interrupts his thoughts."

        doctor "I have strong indications that this can cause {a=glossary:arrhythmia_entry}arrhythmia{/a} to mother... But i have nothing else to try..."

    "His attention shifts to another jar."

    show doctor default at left onlayer portraits

    $ hogo_root_entry.locked = False

    doctor "\"{a=glossary:hogo_root_entry}Hogo Root{/a}.\""

    hide doctor default onlayer portraits

    "He checks the remaining supply."

    doctor "\"Almost enough.\""

    show doctor default at left onlayer portraits

    doctor "Some studies suggest it has neuroprotective effects."

    if not ch01_knows_polygala:
        
        $ ch01_knows_polygala = True

    doctor "If Nagomi Root can reduce the inflammation..."

    doctor "...then perhaps Hogo Root can help protect the {a=glossary:nervous_system_entry}nervous system{/a}."

    doctor "..."

    doctor "It's worth trying."

    hide doctor default onlayer portraits

    "He carefully measures every ingredient."

    "Every movement is precise."

    "The herbs are ground into a fine powder before being slowly mixed into the solution."

    "The color of the {a=glossary:formula_entry}formula{/a} changes as the ingredients dissolve."

    "Finally, he pours the finished mixture into a small glass vial."

    if ch01_loop_count >= 1:

        "His hands stop for a moment."

        doctor "I did everything exactly as the last time." 

    if ch01_cat_in_lab:

        "He notices movement nearby."

        doctor "I should be careful with the formula, the cat is inside the lab."

    "He places the vial safely aside and reaches for his notebook."

    show doctor default at left onlayer portraits

    doctor "\"Now...\"" 

    doctor "\"Let's make sure I didn't overlook anything.\"" 

    hide doctor default onlayer portraits

    "He compares every measurement with his notes." 

    "He reads through every page again." 

    $ ch01_prepared_formula = True

    return

    # jump ch01_mother_calls_knock_on_door

label ch01_cat_becomes_noisy:

    show doctor default at left onlayer portraits

    doctor "Come on, little one."

    hide doctor default onlayer portraits

    "He gently picks up the cat."

    "She relaxes in his arms, purring softly."

    "For a moment, the laboratory feels less lonely."

    "He lets her walk around the room, exploring every corner."

    call ch01_study_prepare_formula
            
    "A sudden noise breaks the silence."

    "He looks up."

    "Mother's cat is jumping from chair to chair."

    "She's chasing a fly that somehow found its way into the laboratory." 

    if kept_cat_in_lab_once:

        "A familiar memory returns."

        doctor "I have seen this before... if I let her stay inside she maybe break the formula again."

        doctor "Do I risk it?"

    else:

        show doctor default at left onlayer portraits
        
        doctor "Easy there, little one..." 

        hide doctor default onlayer portraits

        doctor "Maybe I should let her outside."

    menu:

        "Let your cat outside":

            "He gently picks up the cat and carries her outside."

            doctor "Today I need my full concentration. I can't afford any distractions."

            jump ch01_mother_calls_knock_on_door

        "Keep your cat inside":
            
            jump ch01_cat_breaks_formula

label ch01_cat_breaks_formula:

    doctor "Try to be quiet, little one. I don't want to escort you outside."

    doctor "Today I need my full concentration. I can't afford any distractions."

    "He looks over his notes one more time."

    "Suddenly, the cat jumps onto his desk!"

    if kept_cat_in_lab_once:

        "Its happening again!"

    doctor "No! Get out of here!"

    "But it's took late… She tries to leave form the desc but things get in her way."

    "Bottles start breaking."

    doctor "Not this one!"

    "The doctor tries to catch the formula but it falls in the ground and breaks."

    doctor "No No No."

    doctor "This can't be happening!"

    if kept_cat_in_lab_once:

        doctor "How could i make this mistake again?"

    "He turns to find the cat, but she is nowhere to be found."

    doctor "I have to make the formula again."

    doctor "I have to check what herbs I have at the apothecary."

    doctor "Or I could go to the hospital and replenish my herbs."

    $ ch01_prepared_formula = False

    if not kept_cat_in_lab_once:

        $ kept_cat_in_lab_once = True

    menu:

        "Check your stock on your apothecary":

            jump ch01_mother_calls_knock_on_door

        "Go to the hospital to restore your herbs":

            jump ch01_go_to_hospital

label ch01_mother_calls_knock_on_door:

    mother "Yosuke..." 

    "He hears Mother's weak voice calling from her room."

    doctor "I should check on her."

    # audio *Knock... Knock...* 

    "*Knock... Knock...*" 

    $ ch01_knock_knock = True
    
    if not ch01_met_herb_in_door:

        "Someone is at the front door."

    else: 

        "Maybe it's the herbalist again."

    menu:

        "Open the door":

            jump ch01_meet_herbalist_on_door

        "Answer your mother call":

            jump ch01_answer_mothers_call

label ch01_keep_cat_in_lab_mother_calls :

    show doctor default at left onlayer portraits

    doctor "Come on, little one."

    hide doctor default onlayer portraits

    "He cradles her in his arms, and she purrs softly."

    "He lets her wander around the room..."

    mother "Yosuke..." 

    $ ch01_mother_called = True

    "He hears Mother's weak voice calling from her room."

    doctor "I should check on her."

    doctor "But i have so much work…"

    $ ch01_cat_in_lab = True

    menu :

        "Continue studying":

            doctor "I'll do one last check, then I'll go to her."

            jump ch01_mother_calls_knock_on_door

        "Go to her":

            jump ch01_check_mother_cat_in_lab

label ch01_check_mother_cat_in_lab :

    "He sets his notes aside."

    doctor "Mother sounded weaker this time."

    doctor "I can't ignore her."

    "He leaves the laboratory and walks to her room."

    "She is sitting up in bed."

    "Even breathing seems to tire her."

    mother "Yosuke..."

    "He kneels beside her."

    doctor "How are you feeling?"

    mother "...Hungry."

    "She hasn't eaten much since breakfast."

    "The illness has taken what little strength she had."

    "He glances toward the laboratory."

    "The formula is still untested."

    doctor "Every minute I spend away from my research delays my work."

    doctor "But every minute I stay in the laboratory..."

    doctor "...Mother suffers alone."

    doctor "I have to choose."

    menu :

        "Give her food":

            "He started preparing food when some noise from the lab distracted him."

            jump ch01_cat_breaks_formula

        "Return to study":

            scene bg ch01 lab with fade

            "He returns to his lab to study some more about the formula he made..."

            jump ch01_mother_calls_knock_on_door