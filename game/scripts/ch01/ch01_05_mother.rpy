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

        "I should go prepare it quicly."

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

        "Last time i gave it to her she died..."
    
    menu:

        "Try the formula":

        "Dont try the formula":
            