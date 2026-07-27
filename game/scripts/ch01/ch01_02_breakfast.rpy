# Event Prepare miso soup
# Choices
#   Add bread 
#   Don't add bread
label ch01_make_breakfast :

    scene bg ch01 kitchen

    if ch01_loop_count == 0 :

        "A soup would help Mother feel better." 
    
    elif ch01_loop_count == 1:
    
        if not ch01_mother_checked :

            "My stomach is hurting so much... Maybe some soup will help me..."
        
        else :

            "A soup would help Mother feel better." 
        
        "Wait... have I done this before already?"

        "I’m probably confused from the luck of sleep…" 

    else:

        if not ch01_mother_checked :

            "My stomach is hurting so much... Maybe some soup will help me..."      

        else :

            "A soup would help Mother feel better." 

        "This is happening again… im doing the same things again and again… but i have one more chance.."

    "Ever since the contamination in the fish was discovered, our food options have become limited." 

    "We have to be careful about what we include in our diet."

    "Who would have thought something like this could happen because of one of our most common foods?" 

    "There's some bread in the cupboard. Maybe I should add it to the soup." 
    
    if ch01_knows_dysphagia:

        "This is what caused dysphagia to mother..."

        if ch01_mother_checked:

            "I have to be carefull. I cannot make the same mistakes again."

    menu:

        "Add bread":

            "Alright, breakfast ready."
            
            $ ch01_bread_added = True

            jump ch01_eat_breakfast

        "Don't add bread":

            jump ch01_eat_breakfast

label ch01_eat_breakfast:

    scene bg ch01 mother

    if ch01_loop_count == 0:

        if not ch01_mother_checked :

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

        doctor "Come on."

        doctor " I made you miso soup. Your favorite."

    elif ch01_loop_count == 1:

        "I should go visit her now…"

        if not ch01_mother_checked:

            "Wait… This looks strange…"

            if ch01_wake_happened:

                "Why is she in these clothes? I dressed her yesterday… im sure.. for the wake"

            "Im going by her side… im taching her hand… Its warm… She is alive…?"

            doctor "Mother…?" 

            doctor "Mother!"

            mother "Son…?"

            "She's alive… i cannot believe it… is this real?"

            "Am I getting another chance?"

            "I have to calm down i should not upset her… I have to act normal"

            "I have to bring her breakfast."
        
        else: 

            "I have to calm down i should not upset her… I have to act normal"
        
        "She looks exhausted today as well." 

        "I should leave the soup on the bedside table and open the windows. The room needs some fresh air." 

        doctor "Good morning, Mother" 

        mother "Good morning..."

        doctor "How are you feeling today?"

        mother "Better…"

        "She tries to reach for my hand, but her arm trembles."

        "I gently take her hand in mine and smile back"

        doctor "Let me run my tests first."

        doctor  "Alright… everthing seems stable."

        doctor "Come on."

        doctor " I made you miso soup. Your favorite."

    else: 

        "I should go visit her now…"

        if not ch01_mother_checked:

            "I rush by her side"

            "See is alive."

            "Again"

        "I have to calm down i should not upset her… I have to act normal"

        "Again"

        "She looks exhausted today as well." 

        "I should leave the soup on the bedside table and open the windows. The room needs some fresh air." 

        doctor "Good morning, Mother" 

        doctor "How are you feeling today?"

        mother "Better…"

        "She tries to reach for my hand, but her arm trembles."

        "I gently take her hand in mine and smile back"

        doctor "Let me run my tests first."

        doctor  "Alright… everthing seems stable."

        doctor "Come on."

        doctor " I made you miso soup. Your favorite."

    if ch01_bread_added:

        jump ch01_dysphagia_ending
    
    else: 

        jump ch01_eat_then_lab

