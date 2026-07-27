# Event Your mother chokes during swallowing (dysphagia), she dies (end of fist chapter)
label ch01_dysphagia_ending:

    doctor "Alright... let's start with the soup." 

    "I carefully begin feeding her. After the soup, I pick up the bread."

    doctor "Here, Mother." 

    "One bite... Two bites..." 

    "She stops." 

    "At first, I think she is just tired... But something feels wrong."

    mother "..." 

    doctor "Mother?"

    "She tries to breathe... She starts choking."

    doctor "What is happening?" 

    doctor "How did this happen?" 

    "I quickly try to help her but the situation only gets worse." 

    doctor "Stay with me, Mother..." 

    "I know what to do. I have studied this illness countless times." 

    "So why are my hands shaking? I try everything I can. But nothing is enough."

    "The room becomes silent. It is already too late."

    "Her final breath leaves her body in my arms." 

    doctor "No..." 

    if ch01_loop_count == 0:

        "I hold Mother's hand, but she no longer responds." 

        "I wait. Maybe... Maybe she will open her eyes..." 

        "..." 

        "But she doesn't." 

        doctor "How could I make such a mistake?" 

        "I had read it before... Dysphagia was a symptom of this illness." 

        $ ch01_knows_dysphagia = True

        "I knew this. So why did I forget?" 

        "How am I supposed to live after this?"

        "I know the truth. I am a doctor. I know what death looks like." 

        "Yet I cannot accept it. I close her eyes gently." 

        doctor "I'm sorry, Mother..." 

        "I should have noticed... I should have remembered..." 

        "I spent years studying this illness... And still, I failed you." 

        "Eventually, reality returns." 

        "There are things that need to be done. I have to report her death." 

        "I have to prepare her body. I have to tell someone." 

        "Wake"

        $ ch01_wake_happened = True

    elif ch01_loop_count == 1:

        "I hold Mother's hand. Her warmth slowly fades." 

        "I close my eyes. Not again... I can't let this happen again." 

        if ch01_knows_dysphagia:

            "The memory burns into my mind." 

            "The bread. The choking. The moment I failed." 

            "I know what went wrong. I should have remembered. I should have seen it." 

        else:

            "I had read it before... Dysphagia was a symptom of this illness." 

            $ ch01_knows_dysphagia = True

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

    jump ch01_new_loop
