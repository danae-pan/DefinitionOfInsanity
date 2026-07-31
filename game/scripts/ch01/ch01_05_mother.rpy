label ch01_answer_mothers_call:

    if ch01_knock_knock :
        if not ch01_met_herb_in_door:

            doctor "I should ignore the sound. Mother called for me." 

        doctor "Nothing else matters right now."

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

    doctor "The formula..." 

    if ch01_prepared_formula :

        doctor "It's ready. It is waiting in the laboratory." 

    else: 

        doctor "I should go prepare it quickly."

        scene bg ch01 lab with fade

        "He enters the laboratory and sees the mess the cat has caused."

        "He begins preparing the formula again, repeating each step as carefully as before."

        "Before long, the new mixture is ready."

        doctor "I should return to Mother."

        "He takes a look at the bottle one last time before he leaves the lab."

    doctor "It has never been tested. I don't know the side effects." 

    doctor "I don't know if it will help her... Or if it will make everything worse." 

    doctor "As a doctor... I know what I should do. An untested treatment could harm her."  

    "He looks at his mother."

    "She is suffering."

    doctor"I cannot just stand here and watch." 

    mother "\"Yosuke...\""

    "Her grip weakens."

    mother "\"Please...\""

    "He closes his eyes."

    doctor "The {a=glossary:formula_entry}formula{/a} could save her."

    doctor "Or it could take away the little time she has left."

    "His hands tighten."

    doctor "I have to decide."

    if ch01_check_formula :

        doctor "Last time I gave it to her she died..."
    
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

        mother "\"Good morning…\""

        hide doctor default onlayer portraits

        "He turns to see her trying to smile at him."
        
        "This illness is slowly stealing her strength."

        show doctor default at left onlayer portraits

        doctor "\"Good morning, Mother\"" 

        doctor "\"How are you feeling today?\""

        mother "\"Better…\""

        hide doctor default onlayer portraits
        
        "She tries to reach for his hand, but her arm trembles."
        
        "He gently takes her hand in his and smile back."

        show doctor default at left onlayer portraits

        doctor "\"Let me run my tests first.\""

        doctor  "\"Alright… everything seems stable.\""

        doctor "She is stable, but that doesn’t mean that she is alright."
        
        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."

    elif ch01_loop_count == 1 :

        doctor "I should go visit her now…"

        scene bg ch01 mother with fade

        doctor "Wait… This looks strange…"

        if ch01_wake_happened :
            
            doctor "Why is she in these clothes?"
            doctor "I dressed her for the waek yesterday… I'm sure of it."
        
        "He approaches her bedside and touches her hand."

        "It is warm."

        doctor "She's alive...?"

        show doctor default at left onlayer portraits

        doctor "\"Mother...?\""

        doctor "\"Mother!\""

        hide doctor default onlayer portraits

        mother "\"Son…?\""

        doctor "She's alive..."

        doctor "I can't believe it."

        doctor "Is this real?"

        doctor "Am I getting another chance?"

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

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

        hide doctor default onlayer portraits

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."
    
    else :

        doctor "I should go visit her now…"
        
        scene bg ch01 mother with fade

        "He rushes to her bedside."

        "She is alive."

        doctor "Again..."

        doctor "I have to calm down."

        doctor "I shouldn't upset her."

        doctor "I have to act normally."

        "She looks as exhausted as she did during every previous attempt."

        doctor "I should open the windows."

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

        hide doctor default onlayer portraits

        doctor "She's stable, but that doesn't mean she's alright."

        doctor "I need to find a solution soon."

        doctor "But perhaps I should make us some breakfast first."
    
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
