label ch01_answer_mothers_call:

    if not ch01_met_herb_in_door:

        "I ignore the sound." 

        "Mother called for me." 

    "Nothing else matters right now." 

    "I rush toward her room." 

    doctor "Mother?" 

    "I open the door." 

    "She is struggling to breathe." 

    "Her condition has worsened." 

    "I can see the pain in her eyes." 

    "She looks exhausted." 

    "More than before." 

    "I quickly move to her side." 

    mother "Yosuke..." 

    "She reaches for my hand." 

    "I hold it gently." 

    mother "Did you... find something?" 

    "Her voice is weak." 

    "She already knows I have been searching." 

    mother "Something… to help me?" 

    "I freeze." 

    "The formula..." 

    if ch01_prepared_formula :

        "It's ready." 

        "It is waiting in the laboratory." 

    else: 

        "I should go prepare it quickly."

    "But it has never been tested." 

    "I don't know the side effects." 

    "I don't know if it will help her..." 

    "Or if it will make everything worse." 

    "As a doctor..." 

    "I know what I should do." 

    "An untested treatment could harm her." 

    "But..." 

    "I look at Mother." 

    "She is suffering." 

    "I cannot just stand here and watch." 

    mother "Yosuke..." 

    "Her grip weakens." 

    mother "Please..." 

    "I close my eyes." 

    "The formula could save her." 

    "Or it could take away the little time she has left." 

    "My hands tighten." 

    "I have to decide."   

    if ch01_check_formula :

        "Last time I gave it to her she died..."
    
    menu:

        "Try the formula":

            jump ch01_arrythmia_mixed_ending

        "Dont try the formula":

            jump ch01_coma_ending


label ch01_check_mother :

    if ch01_loop_count == 0 :

        scene bg ch01 mother

        doctor "Mother…?" 

        "She's still asleep. She looks exhausted today as well."

        "I should leave the soup on the bedside table and open the windows. The room needs some fresh air." 

        mother "Good morning…"

        "I turn to see her trying to smile at me. This illness is slowly stealing her strength…"

        doctor "Good morning, Mother" 

        doctor "How are you feeling today?"

        mother "Better…"

        "She tries to reach for my hand, but her arm trembles. I gently take her hand in mine and smile back."

        doctor "Let me run my tests first."

        doctor  "Alright… everthing seems stable."

        "She is stable but that doesn’t mean that she is okay. I should find a solution soon."

        "But maybe I should make us some breakfast first."

    elif ch01_loop_count == 1 :

        "I should go visit her now…"

        scene bg ch01 mother

        "Wait… This looks strange…"

        if ch01_wake_happened :
            
            "Why is she in these clothes? I dressed her yesterday… im sure.. for the wake"
        
        "Im going by her side… im taching her hand… Its warm… She is alive…?"

        doctor "Mother…?"

        doctor "Mother!"

        mother "Son…?"

        "She's alive… i cannot believe it… is this real?"

        "Am I getting another chance?"

        "I have to calm down I should not upset her… I have to act normal"

        mother "Good morning…"

        doctor "Good morning, Mother"

        doctor "How are you feeling today?"

        mother "Better…"

        "She tries to reach for my hand, but her arm trembles. I gently take her hand in mine and smile back"

        doctor "Let me run my tests first."

        "She is stable but that doesn’t mean that she is okay. I should find a solution soon."

        "But maybe I should make us some breakfast first."
    
    else :

        "I should go visit her now…"
        
        scene bg ch01 mother

        "I rush by her side"

        "Again"

        "I have to calm down i should not upset her… I have to act normal"

        "Again"

        "She looks exhausted today as well."

        "I should open the windows."

        mother "Good morning…"

        "I turn to see her trying to smile at me."

        doctor "Good morning, Mother"

        doctor "How are you feeling today?"

        mother "Better…"

        "She tries to reach for my hand, but her arm trembles. I gently take her hand in mine and smile back"

        doctor "Let me run my tests first."

        "She is stable but that doesn’t mean that she is okay. I should find a solution soon."

        "But maybe I should make us some breakfast first."
    
    $ ch01_mother_checked = True

    menu :
        "Make breakfast":

            jump ch01_make_breakfast

        "Go to your lab":

            call ch01_study_prepare_formula
