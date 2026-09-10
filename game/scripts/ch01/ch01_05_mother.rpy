label ch01_answer_mothers_call:

    if ch01_knock_knock and not ch01_check_apothecary:
        if not ch01_met_herb_in_door:

            show doctor default at left onlayer portraits with dissolve

            doctor "Mother called for me." 

            doctor "Whoever is at the door can wait a little longer."

        doctor "Nothing else matters right now."

        hide doctor default onlayer portraits with dissolve

        scene black with fade

        "He rushes toward her room."

    elif ch01_check_apothecary and ch01_went_to_hospital:

        "He enters the house and hears his mother calling for him."

    scene black with fade
    
    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\"" 

    hide doctor default onlayer portraits with dissolve

    "He opens the door." 

    scene bg ch01 mother 
    with fade

    #expression mother: tired no smile

    "She is struggling to breathe. Her condition has worsened." 

    "The pain in her eyes is more intense than before." 

    "He quickly moves to her side." 

    mother "\"Yosuke...\"" 

    "She reaches for his hand. He holds it gently." 

    mother "\"Did you... find something?\"" 

    "Her voice is weak. She already knows he has been searching." 

    mother "\"Something… to help me?\"" 

    show doctor default at left onlayer portraits with dissolve

    doctor "The formula..." 

    if ch01_prepared_formula:

        doctor "It's ready. It is waiting in the laboratory." 

        hide doctor default onlayer portraits with dissolve

        scene bg ch01 lab with fade


    else: 

        if ch01_check_apothecary and not ch01_went_to_hospital:

            doctor "I already now I am out of stock."

            doctor "I will have to go to the hospital."

            doctor "But...her condition...is worse now."

            doctor "\"I need to go to the hospital now Mother.\""

            doctor "\"I will be back soon to help you.\""

            mother "\"Thank you my son. Be careful on your way there.\""

            hide doctor default onlayer portraits with dissolve

            jump ch01_go_to_hospital

        if ch01_check_apothecary and ch01_went_to_hospital:

            doctor "I have the ingredients from the hospital now.."

            doctor "But I should be careful with what I say."

            doctor "I don't want to get her hopes up yet."

            doctor "\"Have a bit more patience Mother.\""

            hide doctor default onlayer portraits with dissolve

            "By the look in her eyes he knows she is worried."

            "He fixes her pillows to make her feel more comfortable."

            show doctor default at left onlayer portraits with dissolve


        doctor "I should go prepare it quickly."

        hide doctor default onlayer portraits with dissolve

        scene bg ch01 lab with fade

        "He enters the laboratory and sees the mess the cat has caused."

        "He begins preparing the formula again, repeating each step as carefully as before."

        "Before long, the new mixture is ready."

        show doctor default at left onlayer portraits with dissolve

        doctor "I should return to Mother."

        hide doctor default onlayer portraits with dissolve

        "He takes a look at the bottle one last time."

        $ ch01_prepared_formula = True

    show doctor default at left onlayer portraits with dissolve

    doctor "It has never been tested. I don't know the side effects." 

    doctor "I don't know if it will help her... Or if it will make everything worse." 

    doctor "As a doctor... I know what I should do. An untested treatment could harm her." 

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He heads to his mother's room, leaving the vial behind."

    scene bg ch01 mother with fade

    "He looks at her."

    "She is suffering."

    show doctor default at left onlayer portraits with dissolve

    doctor "I cannot just stand here and watch." 

    #mother expression: tired no smile

    mother "\"Yosuke...\""

    hide doctor default onlayer portraits with dissolve

    "Her grip weakens."

    mother "\"Please...\""

    "He closes his eyes."

    show doctor default at left onlayer portraits with dissolve

    doctor "The {a=glossary:formula_entry}formula{/a} could save her."

    doctor "Or it could take away the little time she has left..."

    hide doctor default onlayer portraits with dissolve

    "His hands tighten."

    show doctor default at left onlayer portraits with dissolve

    doctor "I have to decide."

    hide doctor default onlayer portraits with dissolve

    if ch01_check_formula :

        show doctor default at left onlayer portraits

        doctor "Last time I gave it to her she died..."

        hide doctor default onlayer portraits
    
    menu:

        "Try the formula":

            jump ch01_arrythmia_mixed_ending

        "Don't try the formula":

            jump ch01_coma_ending


label ch01_check_mother :

    if ch01_loop_count == 0 :

        scene bg ch01 mother with fade

        "He enters her room."

        show doctor default at left onlayer portraits

        doctor "\"Mother…?\"" 

        hide doctor default onlayer portraits

        "She's still asleep. She looks exhausted."

        show doctor default at left onlayer portraits

        doctor "I should leave the soup on the bedside table and open the windows. The room needs some fresh air." 

        hide doctor default onlayer portraits

        mother "\"Good morning…\""

        "He turns to see her trying to smile at him."
        
        "This illness is slowly stealing her strength."

        show doctor default at left onlayer portraits

        doctor "\"Good morning, Mother\"" 

        doctor "\"How are you feeling today?\""

        hide doctor default onlayer portraits

        mother "\"Better…\""
        
        "She tries to reach for his hand, but her arm trembles."
        
        "He gently takes her hand in his and smile back."

        show doctor default at left onlayer portraits

        doctor "\"Let me run my tests first.\""

        doctor  "\"Alright… everything seems stable.\""

        doctor "She is stable, but that doesn’t mean that she is alright."
        
        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor default onlayer portraits

    elif ch01_loop_count == 1 :

        show doctor default at left onlayer portraits

        doctor "I should go visit her now…"

        hide doctor default onlayer portraits

        scene bg ch01 mother with fade

        show doctor default at left onlayer portraits

        doctor "Wait… This looks strange…"

        hide doctor default onlayer portraits

        if ch01_wake_happened :

            show doctor default at left onlayer portraits
            
            doctor "Why is she in these clothes?"

            doctor "I dressed her for the waek yesterday… I'm sure of it."

            hide doctor default onlayer portraits
        
        "He approaches her bedside and touches her hand."

        "It is warm."

        show doctor default at left onlayer portraits

        doctor "She's alive...?"

        doctor "\"Mother...?\""

        doctor "\"Mother!\""

        hide doctor default onlayer portraits

        mother "\"Son…?\""

        show doctor default at left onlayer portraits

        doctor "She's alive..."

        doctor "I can't believe it."

        doctor "Is this real?"

        doctor "Am I getting another chance?"

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        hide doctor default onlayer portraits

        mother "\"Good morning…\""

        show doctor default at left onlayer portraits

        doctor "\"Good morning, Mother\""

        doctor "\"How are you feeling today?\""

        hide doctor default onlayer portraits

        mother "\"Better…\""

        "She tries to reach for my hand, but her arm trembles."
        
        "He gently takes her hand in his and smile back"

        show doctor default at left onlayer portraits

        doctor "\"Let me run my tests first.\""

        doctor "\"Alright... Everything seems stable.\""

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor default onlayer portraits
    
    else :

        "He enters her room and rushes to her bedside."

        scene bg ch01 mother with fade

        "She is alive."

        show doctor default at left onlayer portraits with dissolve

        doctor "Again..."

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        hide doctor default onlayer portraits with dissolve

        "She looks as exhausted as every other time."

        show doctor default at left onlayer portraits with dissolve

        doctor "I should open the windows."

        hide doctor default onlayer portraits with dissolve

        #mother expression: tired smile

        mother "\"Good morning...\""

        "He turns and sees her trying to smile at him."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother.\""

        doctor "\"How are you feeling today?\""

        mother "\"Better...\""

        hide doctor default onlayer portraits with dissolve

        "She tries to reach for his hand, but her arm trembles."

        "He gently takes her hand in his and smiles back."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor "\"Alright... Everything seems stable.\""

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor default at left onlayer portraits with dissolve
    
    $ ch01_mother_checked = True

    menu :
        "Make breakfast":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I'm going to make us some breakfast. I'll be back soon.\""

            hide doctor default onlayer portraits with dissolve

            jump ch01_make_breakfast

        "Go to your lab":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I'm going to my laboratory. Call me if you need anything.\""

            hide doctor default onlayer portraits with dissolve

            jump ch01_straight_to_lab
