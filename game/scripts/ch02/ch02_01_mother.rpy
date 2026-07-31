label ch02_check_mother :

    scene bg ch01 mother

    "He checks her pulse and temperature, seems good. He fixes her pillow, making sure she’s comfortable."
    
    show doctor default at left onlayer portraits

    doctor "\"Mother, how are you feeling today?\""

    hide doctor default onlayer portraits

    doctor "She tries to smile, I can see it is difficult for her. "

    doctor "Her body won’t take the pain for much longer..I should hurry. "

    doctor "I run the usual tests, checking her pulse and pressure."

    doctor "Everything seems normal."

    if took_herbs :

        doctor "I wasn’t able to test any herbs that the herbalist gave me. Maybe I will have time to do that today if I rush now to him."

    if not ch02_use_panax :

        if not ch02_stock_panax :

            doctor "Or maybe I should head to the hospital, check the stock there."

        else :

            doctor "Or maybe I should head to the hospital, I remember {a=glossary:taeru_root_entry}Taeru Root{/a} was in stock."

            doctor "I could use this for phase two, replacing {a=glossary:hogo_root_entry}Hogo Root{/a} that I only have in a small amount."

        doctor "If there was more time, I would check on some patients too.."

        doctor "The situation worsens everyday..a cure must be found..and quickly."   

    else :

        doctor "No use going to the hospital anymore. "

        doctor "I already know what is in stock and using {a=glossary:taeru_root_entry}Taeru Root{/a} proved to be fatal at the end."

        doctor "But what if something changed?"

        doctor "What if every day is not exactly the same?"
    

    $ ch02_checked_mother = True
    $ ch02_route_choice = "check_mother"
    
    menu:
        "Go to the herbalist":
            jump ch02_go_to_herbalist

        "Go to the hospital":
            jump ch02_go_to_hospital

    return

label ch02_go_to_mother :

    return 

label ch02_mother_calls_for_food :

    "The doctor takes another look at the {a=glossary:decoction_entry}decoction{/a} before setting the wooden spoon aside."

    doctor "It can wait a few minutes.."

    doctor "..at least that is what I hope."

    "He leaves the laboratory and makes his way upstairs."

    "His mother is awake, though only barely."

    "She turns her head as he enters the room."

    "A faint smile appears on her face."

    "He kneels beside the bed."

    show doctor default at left onlayer portraits

    doctor "I'm here."

    hide doctor default onlayer portraits

    "She reaches for his hand."

    "Her fingers tremble."

    mother "I..."

    "She pauses, struggling to swallow."

    mother "...I'm so hungry."

    "The doctor gently supports her shoulders."

    show doctor default at left onlayer portraits

    doctor "I know."

    hide doctor default onlayer portraits

    "She closes her eyes tightly."

    mother "My throat..."

    mother "It hurts..."

    mother "Everything hurts."

    "He watches as she tries to swallow again."

    "Even that small movement seems painful."

    "Her lips are dry."

    "The disease is making it harder and harder for her to swallow."

    "She has barely eaten."

    "Barely drunk anything."

    "His thoughts return to the herbalist."

    doctor "The second herb should not be taken after eating."

    if ch02_second_herb_with_instructions:

        doctor "However, last time I did follow the instructions and still.."

        doctor "..I failed."

    "He looks at his mother."

    doctor "If I feed her now, the medicine may not work."

    doctor "But if I don't…she'll only grow weaker."

    "She squeezes his hand ever so slightly."

    mother "...please..."

    "He lowers his head."

    menu :

        "Prepare her food":

            jump ch02_second_herb_without_instructions_ending

        "Don't":

            jump ch02_second_herb_with_instructions_ending

    return