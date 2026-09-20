label ch01_answer_mothers_call:

    if ch01_knock_knock and not ch01_check_apothecary and not ch01_supplies_from_herbalist:
        if not ch01_met_herb_in_door:

            show doctor default at left onlayer portraits with dissolve

            doctor "Mother called for me." 

            doctor "Whoever is at the door can wait a little longer."

        doctor "Nothing else matters right now."

        hide doctor onlayer portraits with dissolve

        scene black with fade

        #SOUND

        play sound "audio/sfx/footsteps.mp3"
        
        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        "He rushes toward her room."

    elif ch01_check_apothecary and ch01_went_to_hospital:

        "He enters the house and hears his Mother calling for him."

    scene black with fade

    if not ch01_supplies_from_herbalist:
    
        show doctor default at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/footsteps.mp3"
        
        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        doctor "\"Mother?\"" 

        hide doctor onlayer portraits with dissolve

    "He opens the door." 

    show mother sick with dissolve

    #SOUND

    play sound "audio/sfx/mother_breath.mp3"
    
    pause 0.8

    play sound "audio/sfx/mother_breath.mp3"

    pause 1.2

    play sound "audio/sfx/mother_breath.mp3"

    "She is struggling to breathe. Her condition has worsened." 

    "The pain in her eyes is more intense than before." 

    "He quickly moves to her side." 

    mother "\"Yosuke...\"" 

    if ch01_prepare_food:

        mother "\"Is the food ready?\""

        mother "\"I'm really hungry...\""

        "Yosuke looks at his Mother, sadness covering his face."

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "She seems even weaker..."

        doctor "The cat... she distracted me and I didn't manage to finish preparing her meal."

        if ch01_supplies_from_herbalist:

            doctor "And then I had to lose more time going with Mr. Kazuki..."

        doctor "\"I'm sorry Mother.\""

        doctor "\"I had to run to the laboratory because the cat started making noises.\""

        doctor "\"I was afraid she broke something.\""

        mother "\"It's okey son...\""

        hide doctor onlayer portraits with dissolve

        "But he could see the weakness in her eyes..."


    "She reaches for his hand. He holds it gently." 

    mother "\"Did you... find something?\"" 

    "Her voice is weak. She already knows he has been searching." 

    mother "\"Something… to help me?\"" 

    show doctor default at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "The formula..." 

    if ch01_prepared_formula:

        doctor "It's ready. It is waiting in the laboratory." 

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"I will be back in a minute Mother.\""

        doctor "\"Just wait for me.\""

        hide doctor onlayer portraits with dissolve

        scene bg ch01 lab_no_cat with fade


    else: 

        if ch01_check_apothecary and not ch01_went_to_hospital and not ch01_supplies_from_herbalist:

            doctor "I already now I am out of stock."

            doctor "I will have to go to the hospital."
            
            show doctor worried at left onlayer portraits with dissolve

            #SOUND

            play sound "audio/sfx/breathe_male.mp3"

            doctor "But...her condition...is worse now."

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I need to go to the hospital now Mother.\""

            doctor "\"I will be back soon to help you.\""

            mother "\"Thank you my son. Be careful on your way there.\""

            hide doctor onlayer portraits with dissolve

            jump ch01_go_to_hospital


        if ch01_went_to_hospital:

            doctor "I have the ingredients from the hospital now.."

            doctor "But I should be careful with what I say."

            doctor "I don't want to get her hopes up yet."

            doctor "\"Have a bit more patience Mother.\""

            hide doctor onlayer portraits with dissolve

            #SOUND

            play sound "audio/sfx/breathe_male.mp3"

            "By the look in her eyes he knows she is worried."

            "He fixes her pillows to make her feel more comfortable."

            show doctor default at left onlayer portraits with dissolve

        if ch01_supplies_from_herbalist:

            doctor "I have necessary ammount of Hogo root now."

            doctor "I was right to take some from Mr. Kazuki's store..."

            #SOUND

            play sound "audio/sfx/breathe_male.mp3"

            doctor "Mother looks already too weak..."

            doctor "I have no time now to study the new herbs."

            doctor "I have to make the same formula."


        doctor "I should go prepare it quickly."

        hide doctor onlayer portraits with dissolve

        scene bg ch01 lab_no_cat with fade

        "He enters the laboratory and sees the mess the cat has caused."

        #SOUND

        play sound "audio/sfx/cutlery.mp3"

        "He begins preparing the formula again, repeating each step as carefully as before."

        "Before long, the new mixture is ready."

        show doctor default at left onlayer portraits with dissolve

        doctor "I should return to Mother."

        hide doctor onlayer portraits with dissolve

        "He takes a look at the bottle one last time."

        $ ch01_prepared_formula = True

    show doctor worried at left onlayer portraits with dissolve

    doctor "It has never been tested. I don't know the side effects." 

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "I don't know if it will help her... Or if it will make everything worse." 

    doctor "As a doctor... I know what I should do. An untested treatment could harm her." 

    hide doctor onlayer portraits with dissolve

    scene black with fade

    #SOUND

    play sound "audio/sfx/footsteps.mp3"
    
    pause 1.2

    play sound "audio/sfx/footsteps.mp3"

    pause 1.2

    play sound "audio/sfx/footsteps.mp3"

    "He heads to his Mother's room, leaving the vial behind."

    show mother sick with dissolve

    "He looks at her."

    "She is suffering."

    show doctor default at left onlayer portraits with dissolve

    doctor "I cannot just stand here and watch." 

    mother "\"Yosuke...\""

    hide doctor onlayer portraits with dissolve

    "Her grip weakens."

    mother "\"Please...\""

    scene black with fade

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    "He closes his eyes."

    show doctor worried at left onlayer portraits with dissolve

    doctor "The {a=glossary:formula_entry}formula{/a} could save her."

    doctor "Or it could take away the little time she has left..."

    hide doctor onlayer portraits with dissolve

    show mother default with dissolve

    "His hands tighten."

    show doctor default at left onlayer portraits with dissolve

    doctor "I have to decide."

    hide doctor onlayer portraits with dissolve

    if ch01_check_formula :

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/suspence.mp3"

        doctor "Last time I gave it to her she died..."

        hide doctor onlayer portraits with dissolve
    
    menu:

        "Try the formula":

            jump ch01_arrythmia_mixed_ending

        "Don't try the formula":

            jump ch01_coma_ending


label ch01_check_mother :

    if ch01_loop_count == 0 :

        scene black with fade

        #SOUND

        play sound "audio/sfx/footsteps.mp3"
        
        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        show mother default with dissolve

        "He enters his Mother's room."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Mother…?\"" 

        hide doctor onlayer portraits with dissolve

        "She's still asleep. She looks exhausted."

        show mother smile with dissolve

        mother "\"Good morning…\""

        "He turns to see her trying to smile at him."
        
        "This illness is slowly stealing her strength."

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother\"" 

        doctor "\"How are you feeling today?\""

        mother "\"Better…\""
        
        "She tries to reach for his hand, but her arm trembles."
        
        "He gently takes her hand in his and smile back."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor  "\"Alright… everything seems stable.\""

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "She is stable, but that doesn’t mean that she is alright."
        
        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor onlayer portraits with dissolve

    elif ch01_loop_count == 1 :

        show doctor default at left onlayer portraits with dissolve

        doctor "I should go visit her now…"

        hide doctor onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/footsteps.mp3"
        
        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        pause 1.0

        play sound "audio/sfx/footsteps.mp3"

        scene black with fade 

        show mother default with dissolve

        show doctor worried at left onlayer portraits with dissolve

        doctor "Wait… This looks strange…"

        if ch01_wake_happened:

            $ wake_entry.locked = False

            #SOUND

            play sound "audio/sfx/suspence.mp3"

            doctor "Why is she in these clothes?"
            
            doctor "I dressed her yesterday..."
            
            doctor "I am sure of it... for the {a=glossary:wake_entry}otsuya{/a}."

        hide doctor onlayer portraits with dissolve
        
        "He approaches her bedside and touches her hand."

        "It is warm."

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/Gasp.mp3"

        doctor "She's alive...?"

        doctor "\"Mother...?\""

        doctor "\"Mother!\""

        mother "\"Son…?\""

        show doctor smile at left onlayer portraits with dissolve

        doctor "She's alive..."

        doctor "I can't believe it."

        doctor "Is this real?"

        doctor "Am I getting another chance?"

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        show doctor default at left onlayer portraits with dissolve

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        show mother smile with dissolve

        mother "\"Good morning…\""

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother\""

        doctor "\"How are you feeling today?\""

        mother "\"Better…\""

        hide doctor onlayer portraits

        "She tries to reach for his hand, but her arm trembles."
        
        "He gently takes her hand in his and smile back"

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor "\"Alright... Everything seems stable.\""

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor onlayer portraits
    
    else :

        "He enters her room and rushes to her bedside."

        show mother default with dissolve

        "She is alive."

        show doctor default at left onlayer portraits with dissolve

        doctor "Again..."

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        hide doctor onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        "She looks as exhausted as every other time."

        show doctor default at left onlayer portraits with dissolve

        doctor "I should open the windows."

        hide doctor onlayer portraits with dissolve

        show mother smile with dissolve

        mother "\"Good morning...\""

        "He turns and sees her trying to smile at him."

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother.\""

        doctor "\"How are you feeling today?\""

        mother "\"Better...\""

        hide doctor onlayer portraits with dissolve

        "She tries to reach for his hand, but her arm trembles."

        "He gently takes her hand in his and smiles back."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor "\"Alright... Everything seems stable.\""

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor at left onlayer portraits with dissolve
    
    $ ch01_mother_checked = True

    menu :
        "Prepare breakfast":

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"I'm going to make us some breakfast. I'll be back soon.\""

            hide doctor onlayer portraits with dissolve

            jump ch01_make_breakfast

        "Go to your laboratory":

            show doctor smile at left onlayer portraits with dissolve

            doctor "\"I'm going to my laboratory. Call me if you need anything.\""

            hide doctor onlayer portraits with dissolve

            jump ch01_straight_to_lab
