# Event Prepare miso soup
# Choices
#   Add bread 
#   Don't add bread
label ch01_make_breakfast :

    scene bg ch01 kitchen with fade

    if ch01_loop_count == 0 :

        "He steps into the kitchen."

        show doctor default at left onlayer portraits with dissolve

        doctor "A soup should help Mother feel better."

        hide doctor default onlayer portraits with dissolve
    
    elif ch01_loop_count == 1:

        "He steps into the kitchen."
    
        if not ch01_mother_checked :

            show doctor default at left onlayer portraits with dissolve
            
            doctor "My stomach is hurting so much..."
            
            doctor "Maybe a bowl of soup will help."

        
        else :

            show doctor default at left onlayer portraits

            doctor "A soup should help Mother feel better."
        
        doctor "Wait...something feels strange. I feel like I've done this before."

        doctor "\"I’m probably confused from the lack of sleep…\"" 

        hide doctor default onlayer portraits with dissolve

    else:

        "He steps into the kitchen."

        if not ch01_mother_checked :

            show doctor default at left onlayer portraits

            doctor "My stomach is hurting so much..."
            
            doctor "Maybe a bowl of soup will help."

        else :

            show doctor default at left onlayer portraits with dissolve

            doctor "A soup should help Mother feel better."

        doctor "This is happening again… I'm doing the same things again and again… but maybe I will get another chance.."

        hide doctor default onlayer portraits with dissolve

    "Ever since contaminated fish entered the food supply, everyday meals have become much more difficult."

    "He has learned to question every ingredient before putting it on the table."

    show doctor default at left onlayer portraits with dissolve
    
    doctor "Who would've imagined that one of our most common foods could become so dangerous?"

    hide doctor default onlayer portraits with dissolve
    
    "He notices a loaf of bread sitting inside the cupboard."

    if knows_dysphagia:

        "A memory flashes through his mind."

        $ dysphagia_entry.locked = False

        show doctor default at left onlayer portraits with dissolve

        doctor "The bread... Mother choked on it because of her {a=glossary:dysphagia_entry}dysphagia{/a}..."

        if ch01_mother_checked:

            show doctor default at left onlayer portraits with dissolve

            doctor "I have to be careful. I cannot make the same mistakes again."

            hide doctor default onlayer portraits with dissolve

    $ ch01_breakfast_made = True

    menu:

        "Add bread":
            
            show doctor default at left onlayer portraits with dissolve
            
            doctor "\"Alright, breakfast is ready.\""

            hide doctor default onlayer portraits with dissolve
            
            $ ch01_bread_added = True

            jump ch01_eat_breakfast

        "Don't add bread":

            show doctor default at left onlayer portraits with dissolve

            doctor "Better leave the bread out."

            if knows_dysphagia:

                doctor "I can't risk it. I won't make the same mistake again."

            hide doctor default onlayer portraits with dissolve

            jump ch01_eat_breakfast

label ch01_eat_breakfast:

    scene black 

    "He heads to his Mother's room with the breakfast tray in hand."

    scene bg ch01 mother with fade

    if ch01_loop_count == 0:
        
        if not ch01_mother_checked :

            show doctor default at left onlayer portraits with dissolve

            doctor "\"Mother...?\""

            hide doctor default onlayer portraits with dissolve

            "She is still asleep, her face worn with exhaustion."

            "He quietly places the soup on the bedside table and opens the window, letting fresh air fill the room."

            #mother opens her eyes (expression: tired)
            mother "\"Good morning...\"" 

            "She turns toward him with a faint smile. The illness has stolen so much of her strength."

            show doctor default at left onlayer portraits with dissolve

            #doctor expression: neutral smile
            
            doctor "\"Good morning, Mother.\""

            doctor "\"How are you feeling today?\""

            mother "\"Better...\""

            hide doctor default onlayer portraits with dissolve

            "She reaches for his hand, but her arm trembles. He gently takes her hand and smiles reassuringly."

            show doctor default at left onlayer portraits with dissolve

            #doctor expresssion: skeptical

            doctor "\"Let me run my tests first.\"" 

            doctor "\"Alright... Everything seems stable.\""
        
        #doctor expression: neutral smile
        doctor "\"Here.\""

        doctor "\"I made you miso soup. Your favorite.\""

        hide doctor default onlayer portraits with dissolve

    elif ch01_loop_count == 1:

        "He enters the room and sees her lying in bed."

        if not ch01_mother_checked:

            show doctor default at left onlayer portraits with dissolve

            doctor "Something feels wrong."

            if ch01_wake_happened:

                $ wake_entry.locked = False

                doctor "Why is she in these clothes? I dressed her yesterday… im sure.. for the {a=glossary:wake_entry}otsuya{/a}."

                hide doctor default onlayer portraits with dissolve

            hide doctor default onlayer portraits with dissolve

            "He rushes to her bedside and gently takes her hand."

            "It's warm."

            show doctor default at left onlayer portraits with dissolve

            #doctor expression: shocked

            doctor "She's alive...?"

            doctor "\"She's alive...!\""

            doctor "\"Mother...?\""

            doctor "\"Mother!\""

            #mother expression: tired

            mother "\"Son...?\""

            hide doctor default onlayer portraits with dissolve

            "Relief crashes over him."

            show doctor default at left onlayer portraits with dissolve

            doctor "This... this can't be happening."

            doctor "Did I really get another chance?"

            #doctor expression: neutral smile

            doctor "Calm down. Don't let her notice. Just act normal."

            hide doctor default onlayer portraits with dissolve
        
        else: 

            show doctor default at left onlayer portraits

            doctor "Stay calm."

            doctor "She can't know."  

            hide doctor default onlayer portraits

        "She looks just as exhausted as he remembers."

        "He places the soup beside her bed and opens the window."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother.\""

        #mother expression: tired smile

        mother "\"Good morning...\""

        doctor "\"How are you feeling today?\""

        mother "\"Better...\""

        hide doctor default onlayer portraits with dissolve

        "She reaches for his hand, but it trembles."

        "He gently holds it between his own."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor  "\"Alright... Everything seems stable.\""

        doctor "\"Here.\""

        doctor "\"I made you miso soup. Your favorite.\""

    else: 

        show doctor default at left onlayer portraits

        if not ch01_mother_checked:

            hide doctor default onlayer portraits

            "He rushes to her bedside."

            "She's alive."

            show doctor default at left onlayer portraits

            #doctor expression: skeptical

            doctor "Again..."

            hide doctor default onlayer portraits

        show doctor default at left onlayer portraits with dissolve

        doctor "Stay calm."

        doctor "Don't let her notice."

        doctor "I've done this before."

        hide doctor default onlayer portraits with dissolve

        "She looks just as exhausted as every other time."

        "He places the soup beside her bed and opens the window."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Good morning, Mother.\""

        doctor "\"How are you feeling today?\""

        #mother expression: tired smile

        mother "\"Better...\""

        hide doctor default onlayer portraits with dissolve

        "She reaches for his hand, her arm trembling."

        #expressipn: neutral smile

        "He gently holds it and smiles."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Let me run my tests first.\""

        doctor  "\"Alright... Everything seems stable.\""

        doctor "\"Here.\""

        doctor "\"I made you miso soup. Your favorite.\""

        hide doctor default onlayer portraits with dissolve

    if ch01_bread_added:

        jump ch01_dysphagia_ending
    
    else: 

        jump ch01_eat_then_lab

