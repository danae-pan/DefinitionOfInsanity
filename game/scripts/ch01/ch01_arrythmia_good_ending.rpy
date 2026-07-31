label ch01_arrythmia_good_ending :

    "He glances back toward Mother's room."

    doctor "She called for me..." 

    if not met_herbalist:

        doctor "But if Kazuki really has herbs the hospital doesn't..."

        doctor "They could help me develop a better treatment."

    else:

        doctor "Kazuki said he has herbs that might help."

    if herbalist_visited:

        doctor "Kazuki has herbs that could help me develop a better formula."

    doctor "\"Alright.\""

    doctor "\"I'll come with you.\""

    "The neighboring village is about a thirty-minute walk away." 

    "As they walk, Kazuki tells Yosuke about the people he has treated over the years." 

    herbalist "\"I've never seen anyone cured.\"" 

    herbalist "\"But I've seen this illness many times.\"" 

    herbalist "\"It always begins differently...\"" 

    herbalist "\"Eventually, their muscles grow too weak to support them.\"" 

    herbalist "\"Many also lose the ability to swallow safely.\""  

    herbalist "\"Food and even water can become dangerous.\"" 

    herbalist "\"Later... they begin losing their balance.\"" 

    "Yosuke quietly commits every word to memory."

    "They eventually arrive at Kazuki's shop."

    scene bg ch01 herbstore

    "Shelves packed with dried herbs, roots, and flowers surround them." 

    "The air is filled with earthy, unfamiliar scents." 

    herbalist "\"These may interest you.\"" 

    "Yosuke examines the herbs carefully." 

    "One catches his attention." 

    $ junka_root_entry.locked = False

    doctor "\"{a=glossary:junka_root_entry}Junka Root{/a}...\""

    "Traditionally used to improve blood circulation." 

    "Another remedy sits beside it."

    $ tsuyomi_cap_entry.locked = False

    doctor "\"{a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}...\""

    "It is traditionally believed to strengthen the body's resilience."

    doctor "I can only afford one."

    menu:

        "Dong quai":

            doctor "\"I'll take the Junka Root...\""

        "Ganoderma lucidum":

            doctor "\"I'll take the Tsuyomi Cap...\""

    if ch01_cat_broke_formula:

         doctor "\"I would also like some {a=glossary:nagomi_root_entry}Nagomi Root{/a} and {a=glossary:hogo_root_entry}Hogo Root{/a}.\""

    doctor "\"Thank you, Kazuki. Until we meet again.\""

    herbalist "\"I hope you can help your mother, Yosuke. Be careful on your way home.\""

    $ took_herbs = True

    scene bg ch01 lab with fade
    
    "Yosuke finally returns home."

    "The house is quiet."

    "He sets the herbs down."

    doctor "\"Mother?\""

    "..."

    "There is no answer." 

    "He hurries toward her room."  

    scene bg ch01 mother with fade

    "She's lying in bed." 

    "The empty vial rests on the bedside table." 

    "His heart sinks." 

    doctor "\"Mother...\"" 

    "She slowly opens her eyes." 

    "Her breathing is shallow." 

    "He grab her wrist." 

    "His hands are already searching for a pulse." 

    doctor "\"It's irregular...\"" 

    "His eyes dart to the empty vial." 

    doctor "\"The formula...\"" 

    doctor "\"No...\"" 

    doctor "It contained {a=glossary:nagomi_root_entry}Nagomi Root{/a}."

    doctor "An experimental dose..."

    doctor "It was never meant to be taken without supervision."

    doctor "\"Mother, stay with me.\""

    "He desperately searches through his notes."

    doctor "There has to be something..."

    doctor "There has to be..."

    "..."

    doctor "Nothing."

    "Her heartbeat becomes weaker."

    "Weaker..."

    "..." 

    "Then it stops." 

    doctor "\"Mother...\""

    "He remain frozen beside her." 

    "..." 

    $ arrhythmia_entry.locked = False

    doctor "The {a=glossary:arrhythmia_entry}arrhythmia{/a}..."

    doctor "\"I did this.\""

    if ch01_loop_count == 0:

        "He holds Mother's hand, but she no longer responds." 

        "He waits." 

        doctor "\"Maybe...\"" 

        doctor "\"Maybe she will open her eyes.\"" 

        "..." 

        "But she doesn't." 

        doctor "How could I make such a mistake?" 

        $ ch01_knows_arrhythmia = True

        doctor "How am I supposed to live after this?"

        doctor "I know the truth." 

        doctor "I am a doctor." 

        doctor "I know what death looks like." 

        doctor "Yet I cannot accept it." 

        doctor "I close her eyes gently." 

        doctor "I'm sorry, Mother..." 

        "The house feels different now." 

        "Too quiet." 

        "Eventually, reality returns." 

        "There are things that need to be done." 

        doctor "I have to report her death." 

        doctor "I have to prepare her body." 

        doctor "I have to tell someone."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop