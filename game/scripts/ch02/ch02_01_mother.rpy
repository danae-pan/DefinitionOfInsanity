label ch02_check_mother :

    scene bg ch01 mother

    "He checks her pulse and temperature, seems good. He fixes her pillow, making sure she’s comfortable."
    
    show doctor default at left onlayer portraits

    doctor "Mother, how are you feeling today?"

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

            doctor "Or maybe I should head to the hospital, I remember Panax Ginseng was in stock."

            doctor "I could use this for phase two, replacing Polygala tenuifolia that I only have in a small amount."

        doctor "If there was more time, I would check on some patients too.."

        doctor "The situation worsens everyday..a cure must be found..and quickly."   

    else :

        doctor "No use going to the hospital anymore. "

        doctor "I already know what is in stock and using Panax Ginseg proved to be fatal at the end."

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