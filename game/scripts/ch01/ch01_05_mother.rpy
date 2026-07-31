label ch01_answer_mothers_call:

    if ch01_knock_knock :
        if not ch01_met_herb_in_door:

            show doctor default at left onlayer portraits

            doctor "I should ignore the sound. Mother called for me." 

            hide doctor default onlayer portraits

        show doctor default at left onlayer portraits

        doctor "Nothing else matters right now."

        hide doctor default onlayer portraits

        "He rushes toward her room."

    else :

        "He enters the house and hears his mother calling for him."
    
    scene bg ch01 mother 
    with fade

    show doctor default at left onlayer portraits

    doctor "\"Mother?\"" 

    hide doctor default onlayer portraits

    "He opens the door." 

    "She is struggling to breathe. Her condition has worsened." 

    "The pain in her eyes is more intense than before." 

    "He quickly moves to her side." 

    mother "\"Yosuke...\"" 

    "She reaches for his hand. He holds it gently." 

    mother "\"Did you... find something?\"" 

    "Her voice is weak. She already knows he has been searching." 

    mother "\"Something… to help me?\"" 

    show doctor default at left onlayer portraits

    doctor "The formula..." 

    if ch01_prepared_formula :

        doctor "It's ready. It is waiting in the laboratory." 

    else: 

        doctor "I should go prepare it quickly."

        hide doctor default onlayer portraits

        scene bg ch01 lab with fade

        "He enters the laboratory and sees the mess the cat has caused."

        "He begins preparing the formula again, repeating each step as carefully as before."

        "Before long, the new mixture is ready."

        show doctor default at left onlayer portraits

        doctor "I should return to Mother."

        "He takes a look at the bottle one last time before he leaves the lab."

    doctor "It has never been tested. I don't know the side effects." 

    doctor "I don't know if it will help her... Or if it will make everything worse." 

    doctor "As a doctor... I know what I should do. An untested treatment could harm her." 

    hide doctor default onlayer portraits 

    "He looks at his mother."

    "She is suffering."

    show doctor default at left onlayer portraits

    doctor "I cannot just stand here and watch." 

    hide doctor default onlayer portraits

    mother "\"Yosuke...\""

    "Her grip weakens."

    mother "\"Please...\""

    "He closes his eyes."

    show doctor default at left onlayer portraits

    doctor "The {a=glossary:formula_entry}formula{/a} could save her."

    doctor "Or it could take away the little time she has left."

    hide doctor default onlayer portraits

    "His hands tighten."

    show doctor default at left onlayer portraits

    doctor "I have to decide."

    hide doctor default onlayer portraits

    if ch01_check_formula :

        show doctor default at left onlayer portraits

        doctor "Last time I gave it to her she died..."

        hide doctor default onlayer portraits
    
    menu:

        "Try the formula":

            jump ch01_arrythmia_mixed_ending

        "Dont try the formula":

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

        show doctor default at left onlayer portraits

        doctor "I should go visit her now…"

        hide doctor default onlayer portraits
        
        scene bg ch01 mother with fade

        "He rushes to her bedside."

        "She is alive."

        show doctor default at left onlayer portraits

        doctor "Again..."

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        hide doctor default onlayer portraits

        "She looks as exhausted as she did during every previous attempt."

        show doctor default at left onlayer portraits

        doctor "I should open the windows."

        hide doctor default onlayer portraits

        mother "\"Good morning...\""

        "He turns and sees her trying to smile at him."

        show doctor default at left onlayer portraits

        doctor "\"Good morning, Mother.\""

        doctor "\"How are you feeling today?\""

        hide doctor default onlayer portraits

        mother "\"Better...\""

        "She tries to reach for his hand, but her arm trembles."

        "He gently takes her hand in his and smiles back."

        show doctor default at left onlayer portraits

        doctor "\"Let me run my tests first.\""

        doctor "\"Alright... Everything seems stable.\""

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

        hide doctor default onlayer portraits
    
    $ ch01_mother_checked = True

    menu :
        "Make breakfast":

            show doctor default at left onlayer portraits

            doctor "\"I'm going to make us some breakfast. I'll be back soon.\""

            hide doctor default onlayer portraits

            jump ch01_make_breakfast

        "Go to your lab":

            show doctor default at left onlayer portraits

            doctor "\"I'm going to my laboratory. Call me if you need anything.\""

            hide doctor default onlayer portraits

            jump ch01_straight_to_lab
