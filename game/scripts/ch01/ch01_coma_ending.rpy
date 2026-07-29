label ch01_coma_ending :

    "I bring the formula to the room. I look at it in my hands." 

    if ch01_check_formula:

        "This formula has been proven dangerous before."

    else:

        "The answer I have been searching for... It could be right in front of me." 

    "But it has never been tested. I know the risks. If something goes wrong..."  

    "If the formula harms her... Then I will be the reason she suffers even more." 

    "Even if the formula could help her... Even if it could be the cure..." 

    "I cannot risk losing her because of something I created. I slowly place the formula back." 

    show doctor default at left onlayer portraits

    doctor "I'm sorry, Mother..." 

    doctor "I can't." 

    hide doctor default onlayer portraits

    if not ch01_knows_coma :

        "For now, I choose not to give it to her. I stay beside her." 

    else :

        "I choose not to give her the formula once again..."

    "I monitor her condition. I do everything I can to make her comfortable." 

    "But the illness does not stop. Her body becomes weaker." 

    "Hours pass. Until... She stops responding." 

    show doctor default at left onlayer portraits

    doctor "Mother?" 

    hide doctor default onlayer portraits

    "I check her condition." 

    "She is still alive. But she doesn't wake up. Her body has entered a coma." 

    "I stay beside her, waiting. Maybe she will open her eyes." 

    if ch01_loop_count == 0 :

        "Maybe tomorrow she will wake up." 

        "Maybe..." 

    "But deep down, I know. There is nothing more I can do." 

    "Hours later..." 

    "Her breathing becomes weaker. I hold her hand until the very end." 

    "She passes away peacefully beside me..." 

    if ch01_loop_count >= 1 :

        "I lost her again..."

    "I made the safest choice. But... One question remains." 

    "What if the formula could have saved her?"

    if ch01_loop_count == 0 :

        "Eventually, reality returns." 

        "There are things that need to be done. I have to report her death." 

        "I have to prepare her body. I have to tell someone." 

        "Wake"

        $ ch01_wake_happened = True

    else :

        if ch01_knows_coma :

            "The memory burns into my mind." 

            "If i don't give her the formula she dies in coma..." 

        else:

            "I had read it before... This illness can end with comma."

        "I have to try again... I have to save her..." 

        "I gently place her hand back on the bed." 

        "But I am not finished. I return to my laboratory." 

        scene bg ch01 lab

        "I open my notes. My hands are shaking. I write down everything." 

        "The mistake. The symptoms. The things I overlooked." 

        "If I get another chance... I will not repeat this." 

        "I will save her."

        scene black 

        "I close my eyes." 

        "Tomorrow... I will do better." 

    if not ch01_knows_coma :

        $ ch01_knows_coma = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop