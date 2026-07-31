label ch01_arrythmia_good_ending :

    "He glances back toward Mother's room."

    show doctor default at left onlayer portraits

    doctor "She called for me..." 

    hide doctor default onlayer portraits

    if not met_herbalist:

        show doctor default at left onlayer portraits

        doctor "But if Kazuki really has herbs the hospital doesn't..."

        doctor "They could help me develop a better treatment."

        hide doctor default onlayer portraits

    else:

        show doctor default at left onlayer portraits

        doctor "Kazuki said he has herbs that might help."

        hide doctor default onlayer portraits

    if herbalist_visited:

        show doctor default at left onlayer portraits

        doctor "Kazuki has herbs that could help me develop a better formula."

        hide doctor default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Alright.\""

    doctor "\"I'll come with you.\""

    hide doctor default onlayer portraits

    "The neighboring village is about a thirty-minute walk away." 

    "As they walk, Kazuki tells Yosuke about the people he has treated over the years." 

    show herbalist default at left onlayer portraits

    herbalist "\"I've never seen anyone cured.\"" 

    herbalist "\"But I've seen this illness many times.\"" 

    herbalist "\"It always begins differently...\"" 

    herbalist "\"Eventually, their muscles grow too weak to support them.\"" 

    herbalist "\"Many also lose the ability to swallow safely.\""  

    herbalist "\"Food and even water can become dangerous.\"" 

    herbalist "\"Later... they begin losing their balance.\"" 

    hide herbalist default onlayer portraits

    "Yosuke quietly commits every word to memory."

    "They eventually arrive at Kazuki's shop."

    scene bg ch01 herbstore

    "Shelves packed with dried herbs, roots, and flowers surround them." 

    "The air is filled with earthy, unfamiliar scents." 

    show herbalist default at left onlayer portraits

    herbalist "\"These may interest you.\"" 

    hide herbalist default onlayer portraits

    "Yosuke examines the herbs carefully." 

    "One catches his attention." 

    $ junka_root_entry.locked = False

    show doctor default at left onlayer portraits

    doctor "\"{a=glossary:junka_root_entry}Junka Root{/a}...\""

    hide doctor default onlayer portraits

    "Traditionally used to improve blood circulation." 

    "Another remedy sits beside it."

    $ tsuyomi_cap_entry.locked = False

    show doctor default at left onlayer portraits

    doctor "\"{a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}...\""

    hide doctor default onlayer portraits

    "It is traditionally believed to strengthen the body's resilience."

    show doctor default at left onlayer portraits

    doctor "I can only afford one."

    hide doctor default onlayer portraits

    menu:

        "Dong quai":

            show doctor default at left onlayer portraits

            doctor "\"I'll take the Junka Root...\""

            hide doctor default onlayer portraits

        "Ganoderma lucidum":

            show doctor default at left onlayer portraits

            doctor "\"I'll take the Tsuyomi Cap...\""

            hide doctor default onlayer portraits

    if ch01_cat_broke_formula:

        show doctor default at left onlayer portraits

        doctor "\"I would also like some {a=glossary:nagomi_root_entry}Nagomi Root{/a} and {a=glossary:hogo_root_entry}Hogo Root{/a}.\""

        hide doctor default onlayer portraits


    show doctor default at left onlayer portraits

    doctor "\"Thank you, Kazuki. Until we meet again.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"I hope you can help your mother, Yosuke. Be careful on your way home.\""

    hide herbalist default onlayer portraits

    $ took_herbs = True

    scene bg ch01 lab with fade
    
    "Yosuke finally returns home."

    "The house is quiet."

    "He sets the herbs down."

    show doctor default at left onlayer portraits

    doctor "\"Mother?\""

    hide doctor default onlayer portraits

    "..."

    "There is no answer." 

    "He hurries toward her room."  

    scene bg ch01 mother with fade

    "She's lying in bed." 

    "The empty vial rests on the bedside table." 

    "His heart sinks." 

    show doctor default at left onlayer portraits

    doctor "\"Mother...\"" 

    hide doctor default onlayer portraits

    "She slowly opens her eyes." 

    "Her breathing is shallow." 

    "He grab her wrist." 

    "His hands are already searching for a pulse." 

    show doctor default at left onlayer portraits

    doctor "\"It's irregular...\"" 

    hide doctor default onlayer portraits

    "His eyes dart to the empty vial." 

    show doctor default at left onlayer portraits

    doctor "\"The formula...\"" 

    doctor "\"No...\"" 

    doctor "It contained {a=glossary:nagomi_root_entry}Nagomi Root{/a}."

    doctor "An experimental dose..."

    doctor "It was never meant to be taken without supervision."

    doctor "\"Mother, stay with me.\""

    hide doctor default onlayer portraits

    "He desperately searches through his notes."

    show doctor default at left onlayer portraits

    doctor "There has to be something..."

    doctor "There has to be..."

    hide doctor default onlayer portraits

    "..."

    show doctor default at left onlayer portraits

    doctor "Nothing."

    hide doctor default onlayer portraits

    "Her heartbeat becomes weaker."

    "Weaker..."

    "..." 

    "Then it stops." 

    show doctor default at left onlayer portraits

    doctor "\"Mother...\""

    hide doctor default onlayer portraits

    "He remain frozen beside her." 

    "..." 

    $ arrhythmia_entry.locked = False

    show doctor default at left onlayer portraits

    doctor "The {a=glossary:arrhythmia_entry}arrhythmia{/a}..."

    doctor "\"I did this.\""

    hide doctor default onlayer portraits

    if ch01_loop_count == 0:

        "He holds Mother's hand, but she no longer responds." 

        "He waits." 

        show doctor default at left onlayer portraits

        doctor "\"Maybe...\"" 

        doctor "\"Maybe she will open her eyes.\"" 

        hide doctor default onlayer portraits 

        "..." 

        "But she doesn't." 

        show doctor default at left onlayer portraits          

        doctor "How could I make such a mistake?" 

        $ ch01_knows_arrhythmia = True

        doctor "How am I supposed to live after this?"

        doctor "I know the truth." 

        doctor "I am a doctor." 

        doctor "I know what death looks like." 

        doctor "Yet I cannot accept it." 

        doctor "I close her eyes gently." 

        doctor "I'm sorry, Mother..." 

        hide doctor default onlayer portraits

        "The house feels different now." 

        "Too quiet." 

        "Eventually, reality returns." 

        "There are things that need to be done." 

        show doctor default at left onlayer portraits 

        doctor "I have to report her death." 

        doctor "I have to prepare her body." 

        doctor "I have to tell someone."

        hide doctor default onlayer portraits

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop