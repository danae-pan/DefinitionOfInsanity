label ch01_runs_late_at_hospital_comma_ending:

    "Herbalist may have some usefull info about the illeness and the herbs that may herlp. I should stay and talk to him"

    doctor "Please herbalist tell me what you have noticed all these years in your patients?"

    herbalist "I've never seen anyone cured." 

    herbalist "But I've seen this illness many times." 

    herbalist "It always begins differently..." 

    herbalist "Eventually, their muscles grow too weak to support them." 

    herbalist "Many also lose the ability to swallow safely."  

    herbalist "Food and even water can become dangerous." 

    herbalist "Later... they begin losing their balance." 

    "I quietly commit every word to memory." 

    "We talk some more...but the time has passed, I should go back to mother."

    doctor "I will definately come by your shop as soon as i can."

    doctor "I have to go now. Have a good day Mr Herbalist."

    herbalist "I hope i see you again soon Dr Yosuke. Good day to you too."

    "I quicly head home."

    "As soon as i enter in the house I notice the silence."

    "I rush to mothers room."

    scene bg ch01 mother with fade

    "I see her in bed exhausted."

    "I believe its too late for her now..."

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

    "What if the formula could have saved her?"

    if ch01_loop_count >= 1 :

        "I should not let the cat in the laboratory any more."

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