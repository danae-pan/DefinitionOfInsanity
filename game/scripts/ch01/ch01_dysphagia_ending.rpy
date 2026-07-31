# Event Your mother chokes during swallowing (dysphagia), she dies (end of fist chapter)
label ch01_dysphagia_ending:

    show doctor default at left onlayer portraits

    doctor "\"Alright... let's start with the soup.\""

    hide doctor default onlayer portraits

    "He carefully begins feeding her."
    
    "After the soup, he picks up a piece of bread."

    show doctor default at left onlayer portraits
    
    doctor "\"Here, Mother.\"" 

    hide doctor default onlayer portraits

    "One bite..."

    "Then another..."

    "She suddenly stops."

    doctor "At first, I thought she's only tired..."

    doctor "But something feels wrong."

    mother "\"...\""

    show doctor default at left onlayer portraits

    doctor "\"Mother?\""

    hide doctor default onlayer portraits

    "She tries to breathe."
    
    "Then, she begins to choke."

    show doctor default at left onlayer portraits

    doctor "\"What is happening?\""

    doctor "\"How did this happen?\"" 

    hide doctor default onlayer portraits

    "He quickly tries to help her but the situation only gets worse." 

    show doctor default at left onlayer portraits

    doctor "\"Stay with me, Mother...\"" 

    hide doctor default onlayer portraits

    doctor "I know what to do."
    
    doctor "I have studied this illness countless times." 

    doctor "So why are my hands shaking?"
    
    "He tries everything he can."
    
    "But nothing is enough."

    "The room becomes silent. It is already too late."

    "Her final breath leaves her body in my arms." 

    show doctor default at left onlayer portraits

    doctor "\"No...\"" 

    hide doctor default onlayer portraits

    if ch01_loop_count == 0:

        "He holds Mother's hand, but she no longer responds." 

        doctor "Maybe..."

        doctor "Maybe she'll open her eyes..."

        "..."

        "But she does not." 

        show doctor default at left onlayer portraits

        doctor "\"How could I make such a mistake?\""

        hide doctor default onlayer portraits

        doctor "I've read about this before..."

        $ dysphagia_entry.locked = False
        $ knows_dysphagia = True

        doctor "{a=glossary:dysphagia_entry}Dysphagia{/a} was a symptom of this illness."

        doctor "I knew this."

        doctor "So why did I forget?"

        doctor "How am I supposed to live with this?"

        doctor "I know the truth."

        doctor "I'm a doctor."

        doctor "I know what death looks like."

        "Yet he cannot accept it."

        "He gently closes her eyes." 

        show doctor default at left onlayer portraits

        doctor "\"I'm sorry, Mother...\"" 

        hide doctor default onlayer portraits

        doctor "I should have noticed..."

        doctor "I should have remembered..."

        doctor "I spent years studying this illness..."

        doctor "And still, I failed you."

        "Eventually, reality begins to settle in."

        "There are things that must be done."

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        $ ch01_wake_happened = True

    elif ch01_loop_count == 1:

        "He holds Mother's hand as her warmth slowly fades."

        doctor "Not again..."

        doctor "I can't let this happen again."

        if knows_dysphagia:

            doctor "The memory burns into my mind."

            doctor "The bread."

            doctor "The choking."

            doctor "The moment I failed."

            doctor "I know what went wrong."

            doctor "I should have remembered."

            doctor "I should have seen it."

        else:

            "I had read it before..."

            $ dysphagia_entry.locked = False
            $ knows_dysphagia = True

            doctor "{a=glossary:dysphagia_entry}Dysphagia{/a} was a symptom of this illness."

        doctor "I have to try again."

        doctor "I have to save her."

        "He gently places her hand back on the bed."

        doctor "But I'm not finished."

        "He returns to his laboratory."

        scene bg ch01 lab

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistake."

        "The symptoms."

        "The things he overlooked."

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "I will save her."

        scene black

        "He closes his eyes."

        doctor "\"Tomorrow...\""

        doctor "\"I'll do better.\""

    jump ch01_new_loop
