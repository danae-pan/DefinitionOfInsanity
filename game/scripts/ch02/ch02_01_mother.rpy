label ch02_check_mother :


    if ch02_route_choice == "check_mother":

        show mother default with dissolve

        "He checks her pulse and temperature."

        show doctor default at left onlayer portraits with dissolve

        doctor "Everything appears to be okey."

        hide doctor onlayer portraits with dissolve

        "He fixes her pillow, making sure she’s comfortable."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Mother, how are you feeling today?\""

        show mother smile with dissolve

        mother "\"I'm feeling better my son.\""

        doctor "She tries to smile, I can see it is difficult for her."

        doctor "Her body won’t take the pain for much longer..I should hurry. "

        hide doctor onlayer portraits with dissolve

        "He runs the usual tests, checking her pulse and pressure."

        show doctor default at left onlayer portraits with dissolve

    if ch02_route_choice == "check_mother" or ch02_route_choice == "try_herb":

        if took_herbs and not (
        ch02_first_herb_with_instructions
        or ch02_first_herb_without_instructions
        or ch02_second_herb_with_instructions
        or ch02_second_herb_without_instructions
        ):

            doctor "Last time I wasn’t able to test any herbs that the herbalist gave me."
            
            doctor "Maybe I will have time to do that today if I rush now to him."

        elif not took_herbs:

            doctor "Maybe I should go over to Mr. Kazuki's store."

            doctor "He might have something that could help Mother."


        elif (
        ch02_first_herb_with_instructions
        or ch02_first_herb_without_instructions
        or ch02_second_herb_with_instructions
        or ch02_second_herb_without_instructions
        ):

            doctor "Maybe I should go back to Mr. Kazuki's store."

            doctor "Perhaps there's another way I could use the herbs he gave me."

        if not ch02_used_taeru_happened:

            if not ch02_knows_taeru_in_stock: 

                show doctor worried at left onlayer portraits with dissolve

                doctor "I already tried the formula before..."

                doctor "It didn't help."

                show doctor default at left onlayer portraits with dissolve

                doctor "Maybe I should head to the hospital, check the stock for any other herbs there."

            else :

                $ taeru_root_entry.locked = False

                $ hogo_root_entry.locked = False

                doctor "Maybe I should head to the hospital, I remember {a=glossary:taeru_root_entry}Taeru Root{/a} was in stock."

                doctor "I could use this for phase two, replacing {a=glossary:hogo_root_entry}Hogo Root{/a} that I only have in a small amount."

            doctor "If there was more time, I would check on some patients too..."

            doctor "The situation worsens everyday...a cure must be found...and quickly."   

            hide doctor onlayer portraits with dissolve

        else :

            doctor "No use going to the hospital anymore. "

            $ taeru_root_entry.locked = False

            show doctor worried at left onlayer portraits with dissolve

            doctor "I already know what is in stock and using {a=glossary:taeru_root_entry}Taeru Root{/a} proved to be fatal at the end."

            doctor "But what if something changed?"

            doctor "\"What if every day is not exactly the same?\""

            hide doctor onlayer portraits with dissolve

    if ch02_route_choice == "try_herb":

        return
    
    
    hide doctor onlayer portraits with dissolve
    
    menu:

        "Go to the Herbalist":

            jump ch02_go_to_herbalist

        "Go to the hospital":
            jump ch02_go_to_hospital

    return

label ch02_go_to_mother :

    return 

label ch02_mother_calls_for_food :

    #TODO: check where decoction was mentioned on this route
    "The doctor takes another look at the decoction before setting the wooden spoon aside."

    show doctor default at left onlayer portraits with dissolve

    doctor "It can wait a few minutes.."

    doctor "..at least that is what I hope."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He leaves the laboratory and makes his way upstairs."

    show mother default with dissolve

    "His Mother is awake, though only barely."

    "She turns her head as he enters the room."

    "A faint smile appears on her face."

    "He kneels beside the bed."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I'm here.\""

    hide doctor onlayer portraits with dissolve

    "She reaches for his hand."

    "Her fingers tremble."

    show mother sick with dissolve

    mother "\"I...\""

    "She pauses, struggling to swallow."

    mother "\"...I'm so hungry.\""

    "The doctor gently supports her shoulders."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"I know...\""

    hide doctor onlayer portraits with dissolve

    "She closes her eyes tightly."

    show mother default with dissolve

    mother "\"My throat...\""

    mother "\"It hurts...\""

    mother "\"Everything hurts.\""

    "He watches as she tries to swallow again."

    "Even that small movement seems painful."

    "Her lips are dry."

    "The disease is making it harder and harder for her to swallow."

    "She has barely eaten."

    "Barely drunk anything."

    "His thoughts return to the herbalist."

    show doctor default at left onlayer portraits with dissolve

    doctor "The second herb should not be taken after eating."

    if ch02_second_herb_with_instructions:

        show doctor worried at left onlayer portraits with dissolve

        doctor "However, last time I did follow the instructions and still.."

        doctor "..I failed."

    hide doctor onlayer portraits with dissolve

    "He looks at his Mother."

    show doctor default at left onlayer portraits with dissolve

    doctor "If I feed her now, the medicine may not work."

    doctor "But if I don't…she'll only grow weaker."

    hide doctor onlayer portraits with dissolve

    "She squeezes his hand ever so slightly."

    show mother sick with dissolve

    mother "\"...please...\""

    "He lowers his head."

    menu :

        "Prepare her food":

            jump ch02_second_herb_without_instructions_ending

        "Don't":

            jump ch02_second_herb_with_instructions_ending

    return