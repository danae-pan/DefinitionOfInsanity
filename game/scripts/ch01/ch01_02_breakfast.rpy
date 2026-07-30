# Event Prepare miso soup
# Choices
#   Add bread 
#   Don't add bread
label ch01_make_breakfast :

    scene bg ch01 kitchen

    if ch01_loop_count == 0 :

        "He steps into the kitchen."

        doctor "A soup should help Mother feel better."
    
    elif ch01_loop_count == 1:

        "He steps into the kitchen."
    
        if not ch01_mother_checked :
            
            doctor "My stomach is hurting so much..."
            
            doctor "Maybe a bowl of soup will help."
        
        else :

            doctor "A soup should help Mother feel better."
        
        doctor "Wait... have I done this before already?"

        doctor "I’m probably confused from the lack of sleep…" 

    else:

        "He steps into the kitchen."

        if not ch01_mother_checked :

            doctor "My stomach is hurting so much..."
            
            doctor "Maybe a bowl of soup will help."

        else :

            doctor "A soup should help Mother feel better."

        doctor "This is happening again… im doing the same things again and again… but i have one more chance.."

    "Ever since contaminated fish entered the food supply, everyday meals have become much more difficult."

    "He has learned to question every ingredient before putting it on the table."

    doctor "Who would've imagined that one of our most common foods could become so dangerous?"

    "He notices a loaf of bread sitting inside the cupboard."

    if knows_dysphagia:

        "A memory flashes through his mind."

        doctor "The bread... This is what caused dysphagia to mother..."

        if ch01_mother_checked:

            doctor "I have to be careful. I cannot make the same mistakes again."

    $ ch01_breakfast_made = True

    menu:

        "Add bread":

            doctor "Alright, breakfast ready."
            
            $ ch01_bread_added = True

            jump ch01_eat_breakfast

        "Don't add bread":

            jump ch01_eat_breakfast

label ch01_eat_breakfast:

    scene bg ch01 mother

    if ch01_loop_count == 0:

        if not ch01_mother_checked :

            show doctor default at left onlayer portraits

            doctor "Mother…?" 

            hide doctor default onlayer portraits

            "She is still asleep, her face worn with exhaustion."

            "He quietly places the soup on the bedside table and opens the window, letting fresh air fill the room."

            mother "Good morning…"

            "She turns toward him with a faint smile. The illness has stolen so much of her strength."

            show doctor default at left onlayer portraits
            
            doctor "Good morning, Mother" 

            doctor "How are you feeling today?"

            hide doctor default onlayer portraits

            mother "Better…"

            "She reaches for his hand, but her arm trembles. He gently takes her hand and smiles reassuringly."

            show doctor default at left onlayer portraits

            doctor "Let me run my tests first."

            doctor  "Alright… everthing seems stable."

        show doctor default at left onlayer portraits
        
        doctor "Here."

        doctor " I made you miso soup. Your favorite."

        hide doctor default onlayer portraits

    elif ch01_loop_count == 1:

        doctor "I should go visit her now…"

        if not ch01_mother_checked:

            "As he enters the room, something feels wrong."

            if ch01_wake_happened:

                doctor "Why is she in these clothes? I dressed her yesterday… im sure.. for the wake"

            "He rushes to her bedside and gently takes her hand."

            "It's warm."

            doctor "She's alive...?"

            show doctor default at left onlayer portraits

            doctor "Mother…?" 

            doctor "Mother!"

            hide doctor default onlayer portraits

            mother "Son…?"

            "Relief crashes over him."

            doctor "This... this can't be happening."

            doctor "Did I really get another chance?"

            doctor "Calm down. Don't let her notice. Just act normal."
        
        else: 

            doctor "Stay calm."

            doctor "She can't know."  

        "She looks just as exhausted as he remembers."

        "He places the soup beside her bed and opens the window."

        show doctor default at left onlayer portraits 

        doctor "Good morning, Mother" 

        hide doctor default onlayer portraits

        mother "Good morning..."

        show doctor default at left onlayer portraits 

        doctor "How are you feeling today?"

        hide doctor default onlayer portraits

        mother "Better…"

        "She reaches for his hand, but it trembles."

        "He gently holds it between his own."

        show doctor default at left onlayer portraits

        doctor "Let me run my tests first."

        doctor  "Alright… everthing seems stable."

        doctor "Here."

        doctor " I made you miso soup. Your favorite."

        hide doctor default onlayer portraits

    else: 

        doctor "I should go visit her now…"

        if not ch01_mother_checked:

            "He rushes to her bedside."

            "She's alive."

            doctor "Again..."

        doctor "Stay calm."

        doctor "Don't let her notice."

        doctor "I've done this before."

        "She looks just as exhausted as every other time."

        "He places the soup beside her bed and opens the window."

        show doctor default at left onlayer portraits

        doctor "Good morning, Mother" 

        doctor "How are you feeling today?"

        hide doctor default onlayer portraits

        mother "Better…"

        "She reaches for his hand, her arm trembling."

        "He gently holds it and smiles."

        show doctor default at left onlayer portraits

        doctor "Let me run my tests first."

        doctor  "Alright… everthing seems stable."

        doctor "Here."

        doctor " I made you miso soup. Your favorite."

        hide doctor default onlayer portraits

    if ch01_bread_added:

        jump ch01_dysphagia_ending
    
    else: 

        jump ch01_eat_then_lab

