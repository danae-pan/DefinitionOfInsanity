# Event You and your mother eat You head to your lab
# Choices
#   Lab choice (about the cat)

label ch01_eat_then_lab:

    "He helps her with her food while eating his own meal."

    doctor "You know, your cat has been doing some strange things these past few days."

    "She looks up at me."

    doctor "Yesterday I caught her sitting in front of the mirror for almost ten minutes."

    doctor "She was just staring at herself like she had discovered another cat living in the house."

    "Her eyes immediately brighten."

    mother "...Curious..."

    doctor "Yeah." 

    doctor "That's exactly what I thought."

    doctor "Also... I checked the flowers in the garden this morning."

    "She looks up at me."

    doctor "The ajisai you thought was dying... "

    doctor "There are new leaves coming out." 

    "A tear forms in the corner of her eye." 

    mother "...Really?"

    doctor "Yeah. Looks like it wasn't ready to give up just yet."

    "After we finished eating..."

    doctor "I'll leave you to rest now, Mother. Call me if you need anything, alright? I'll be in the laboratory."

    "I enter the laboratory."

    if ch01_loop_count == 0:

        "All the ingredients I brought from the hospital are here. Everything I need to continue working from home."

    else:

        "All the ingredients are still here."

        "Nothing is used."

        "I guess… I should try again."

    "My notes for the formula are still waiting for me."

    "Then I see her."

    "Mother's cat quietly sneaks into the room and starts exploring."

    "Should I let her stay? It would be nice to have some company."

    "I spend so many hours here alone now."

    "But maybe I should take her outside. I can't let anything distract me from my research."

    if ch01_kept_cat_in_lab_once:

        "Last time i kept her inside see broke the formula."

        "I should not risk it again."

    menu:

        "Let your cat outside":

            doctor "Come on, little one."

            "I gently carry the cat outside before returning to the laboratory."

            "Today I need my full concentration. I can't afford any distractions."
            
            call ch01_study_prepare_formula

            jump ch01_mother_calls_knock_on_door

        "Keep your cat in the lab":

            $ ch01_cat_in_lab

            jump ch01_formula_cat_noisy

label ch01_study_prepare_formula:

    "I take my seat and spread my notes across the desk."

    "My eyes wander over the herbs laid out before me."

    doctor "Licorice Root..."

    "I still have enough for a full dose."

    doctor "Its anti-inflammatory and soothing properties could help ease Mother's symptoms."

    if not ch01_knows_licorice:

        $ ch01_knows_licorice = True

    if ch01_knows_arrythmia : 

        "I have strong indications that this can cause arrythmia to mother…"

        "But i have nothing else to try…"

    "My gaze shifts to another jar."

    doctor "Schisandra chinensis..."

    "Major tonic, it is also considered an adaptogonen."

    if not ch01_knows_schisandra :

        $ ch01_knows_schisandra = true

    "I don't have enough left." 

    "It wouldn't be enough to prepare a proper dose."

    "My eyes settle on one last herb."

    doctor "Polygala tenuifolia."

    "I have almost enough."

    doctor "Some studies suggest it has neuroprotective effects."

    if not ch01_knows_polygala:
        
        $ ch01_knows_polygala

    doctor "If Licorice Root can reduce the inflammation..."

    doctor "...then perhaps Polygala can help protect the nervous system." 

    "..."

    doctor "It's worth trying."

    "I carefully weigh each ingredient." 

    "I grind the herbs into a fine powder." 

    "I slowly add them to the solution." 

    "The mixture changes color as the herbs dissolve." 

    "I pour the finished formula into a small glass vial." 

    if loop_count >= 1:

        "I did everything exactly as the last time." 

    if ch01_cat_in_lab:

        "I should be carefull with the formula, the cat is inside the lab."

    "I set it aside and reach for my notebook." 

    doctor "Now..." 

    doctor "Let's make sure I didn't overlook anything." 

    "I compare every measurement with my notes." 

    "I read each page one more time." 

    $ ch01_prepared_formula = True

label ch01_cat_becomes_noisy:

    doctor "Come on, little one."

    "I candle her and she purrs back to me."

    "I let her wonder in the room , check things out."

    call ch01_study_prepare_formula
            
    "A sudden noise breaks the silence."

    "I look up." 

    "Mother's cat is jumping from chair to chair." 

    "She's chasing a fly that somehow found its way into the laboratory." 

    if ch01_kept_cat_in_lab_once:

        "I have seen this before... if I let her stay inside she maybe break the formula again."

        "Should I risk it?"

    else:
        
        doctor "Easy there, little one..." 

        "Maybe I should let her outside."

    menu:

        "Let your cat outside":

            "I gently carry the cat outside before returning to the laboratory."

            "Today I need my full concentration. I can't afford any distractions."

            jump ch01_mother_calls_knock_on_door

        "Keep your cat inside":
            
            jump ch01_cat_breaks_formula

label ch01_cat_breaks_formula:

    doctor "Try to be quiet little one, i dont want to escord you outside."

    "Today I need my full concentration. I can't afford any distractions."

    "I look my notes one more time."

    "Suddenly she appears up in my desc!"

    if ch01_kept_cat_in_lab_once:

        "Its happening again!"

    doctor "No! Get out of here!"

    "But its took late… She tries to leave form the desc but things get in her way."

    "Bottles start breaking."

    doctor "Not this one!"

    "I try to catch the formula but it falls in the ground and breaks."

    "No No No."

    "This can't be happening!"

    if ch01_kept_cat_in_lab_once:

        "How could i make this mistake again?"

    "I turn to find the cat but see is nowhere to be found."

    "I have to make the formula again."

    "I have to check on the apothecary what herbs i have remaining."

    "Or instead i could go to the hospital and restore all my herbs."

    $ ch01_prepared_formula = False

    if not ch01_kept_cat_in_lab_once:

        $ ch01_kept_cat_in_lab_once = True

    menu:

        "Check your stock on your apothecary":

            jump ch01_mother_calls_knock_on_door

        "Go to the hospital to restore your herbs":

            jump ch01_go_to_hospital


label ch01_mother_calls_knock_on_door:

    mother "Yosuke..." 

    "I hear Mother's weak voice calling from her room." 

    "I should check on her." 

    # audio *Knock... Knock...* 

    "..." 
    
    if not ch01_met_herb_in_door:

        "Someone is at the front door."

    else: 

        "Maybe its the herbalist again."

    menu:

        "Open the door":

            jump ch01_meet_herbalist_on_door

        "Answer your mother call":

            jump ch01_answer_mothers_call
