# Event Your mother chokes during swallowing (dysphagia), she dies (end of fist chapter)
label ch01_dysphagia_ending:

    show doctor default at left onlayer portraits with dissolve

    #expression: neutral

    doctor "\"Alright... let's start with the soup.\""

    hide doctor default onlayer portraits with dissolve

    "He carefully begins feeding her."
    
    "After the soup, he picks up a piece of bread."

    show doctor default at left onlayer portraits with dissolve
    
    doctor "\"Here, Mother.\"" 

    hide doctor default onlayer portraits with dissolve

    #mother expression: eating

    "One bite..."

    "Then another..."

    "She suddenly stops."

    show doctor default at left onlayer portraits with dissolve

    #expression: worried

    doctor "At first, I thought she's only tired..."

    doctor "But something feels wrong."

    mother "\"...\""

    doctor "\"Mother?\""

    hide doctor default onlayer portraits with dissolve

    #mother expression: choking

    "She tries to breathe."
    
    "Then, she begins to choke."

    show doctor default at left onlayer portraits with dissolve

    #doctor expression: panicked

    doctor "\"What is going on?\""

    doctor "\"How did this happen?\"" 

    hide doctor default onlayer portraits with dissolve

    "He quickly tries to help her but the situation only gets worse." 

    show doctor default at left onlayer portraits with dissolve 

    doctor "\"Stay with me, Mother...\"" 

    doctor "I know what to do."
    
    doctor "I have studied this illness." 

    doctor "So why are my hands shaking?"

    hide doctor default onlayer portraits with dissolve
    
    "He tries everything he can."
    
    "But nothing is enough."

    "The room becomes silent. It is already too late."

    "Her final breath leaves her body in his arms." 

    show doctor default at left onlayer portraits with dissolve

    #doctor expression: panicked or worried

    doctor "\"No...\""  

    hide doctor default onlayer portraits with dissolve

    if ch01_loop_count == 0:

        #doctor expression: maybe sad/dissapointed

        "He holds Mother's hand, but she no longer responds." 

        show doctor default at left onlayer portraits with dissolve

        doctor "Maybe..."

        doctor "\"Maybe she'll open her eyes...\""

        hide doctor default onlayer portraits with dissolve

        "..."

        "But she does not." 

        show doctor default at left onlayer portraits with dissolve

        doctor "\"How could I make such a mistake?\""

        doctor "I've read about this before..."

        $ dysphagia_entry.locked = False
        $ knows_dysphagia = True

        doctor "{a=glossary:dysphagia_entry}Dysphagia{/a} was a symptom of this illness."

        doctor "I knew this."

        doctor "So why did I forget?"

        doctor "\"How am I supposed to live with this?\""

        doctor "I know the truth."

        doctor "I'm a doctor."

        doctor "\"I know what death looks like...\""

        hide doctor default onlayer portraits with dissolve

        "Yet he cannot accept it."

        "He gently closes her eyes." 

        show doctor default at left onlayer portraits with dissolve

        doctor "\"I'm sorry, Mother...\"" 

        doctor "I should have noticed..."

        doctor "I should have remembered..."

        doctor "\"I failed you...\""

        hide doctor default onlayer portraits with dissolve

        "Eventually, reality begins to settle in."

        "There are things that must be done."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"I have to report her death.\""

        doctor "\"I have to prepare her body.\""

        doctor "\"I have to tell someone!\""

        hide doctor default onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

        $ ch01_wake_happened = True

    elif ch01_loop_count == 1:

        "He holds Mother's hand as her warmth slowly fades."

        show doctor default at left onlayer portraits with dissolve

        #doctor expression: panicked

        doctor "Not again..."

        doctor "I can't let this happen again."

        if knows_dysphagia:

            #doctor expression: panicked

            hide doctor default onlayer portraits with dissolve

            "The memory burns into his mind."

            show doctor default at left onlayer portraits with dissolve

            doctor "The bread."

            doctor "The choking."

            doctor "The moment I failed..."

            doctor "I know what went wrong."

            doctor "I should have remembered."

            doctor "\"I should have seen it...\""

        else:

            doctor "I had read it before..."

            $ dysphagia_entry.locked = False
            $ knows_dysphagia = True

            doctor "{a=glossary:dysphagia_entry}Dysphagia{/a} was a symptom of this illness."

        #doctor expression: neutral

        doctor "I have to try again."

        doctor "\"I have to save her.\""

        hide doctor default onlayer portraits with dissolve

        "He gently places her hand back on the bed."

        show doctor default at left onlayer portraits with dissolve

        doctor "But I'm not finished."

        hide doctor default onlayer portraits with dissolve

        "He returns to his laboratory."

        scene bg ch01 lab

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistakes."

        "The symptoms."

        "The things he overlooked."

        show doctor default at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "\"I will save her.\""

        hide doctor default onlayer portraits with dissolve

        scene black

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    jump ch01_new_loop
