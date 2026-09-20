label ch01_arrythmia_good_ending :

    #TODO: See if I need to keep this block of code with a flag condition
    #was moved to where the choice was made

    # "He glances back toward Mother's room."

    # show doctor default at left onlayer portraits

    # doctor "She called for me..." 

    # hide doctor default onlayer portraits

    show doctor default at left onlayer portraits with dissolve

    if not met_herbalist:

        doctor "But if Mr. Kazuki really has herbs the hospital doesn't..."

        doctor "They could help me develop a better treatment."

    else:

        doctor "Mr. Kazuki said he has herbs that might help."

    if herbalist_visited:
        
        doctor "From the last time I visited..." 
        
        doctor "He might even have more herbs this time."
        
        doctor "Maybe I could develop a better formula..."

    
    

    doctor "\"Alright.\""

    doctor "\"I'll come with you.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "The neighboring village is about a thirty-minute walk away." 

    "As they walk, Mr. Kazuki tells Yosuke about the people he has treated over the years." 


    #TODO: ch01_went_to_hospital this flag sjould reset after each ending
    #This comdition is true when he meets the herbalist on the door and NOT at the hospital
    if not ch01_went_to_hospital:

        show herbalist default at left onlayer portraits with dissolve

        herbalist "\"I've never seen anyone cured.\"" 

        herbalist "\"But I've seen this illness many times.\"" 

        herbalist "\"It always begins differently...\"" 

        show herbalist sceptical at left onlayer portraits with dissolve

        herbalist "\"Eventually, the muscles grow too weak to offer any support.\"" 

        herbalist "\"Many also lose the ability to swallow safely.\""  

        herbalist "\"Food and even water can become dangerous.\"" 

        herbalist "\"Later... they begin losing their balance.\"" 

        hide herbalist onlayer portraits with dissolve

        "Yosuke quietly commits every word to memory."

    "They eventually arrive at Mr. Kazuki's store."

    scene bg ch01 herbstore with fade

    "Shelves packed with dried herbs, roots, and flowers surround them." 

    "The air is filled with earthy, unfamiliar scents." 

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"These may interest you.\"" 

    hide herbalist onlayer portraits with dissolve

    "Yosuke examines the herbs carefully." 

    "One catches his attention." 

    $ junka_root_entry.locked = False

    "He reads the label on the bottle."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"{a=glossary:junka_root_entry}Junka Root{/a}...\""

    hide doctor onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"This one is traditionally used to improve blood circulation.\"" 

    hide herbalist onlayer portraits with dissolve

    "Another remedy sits beside it."

    $ tsuyomi_cap_entry.locked = False

    show doctor default at left onlayer portraits with dissolve

    doctor "\"{a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}...\""

    hide doctor onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"Plenty of books praise Tsuyomi Cap for its ability to strengthen the body's resilience.\""

    hide herbalist onlayer portraits

    show doctor default at left onlayer portraits

    doctor "I can only afford one."

    if ch01_cat_broke_formula and not ch01_went_to_hospital:

        $ ch01_supplies_from_herbalist = True

        doctor "Better ask him for some Hogo root too.."

        doctor "The cat broke the formula..."

        doctor "Before I study about those new herbs I might need to try what I already know."

        doctor "\"Mr. Kazuki, I would like some Hogo root too.\""

        doctor "\"Do you happen to have any?\""

        hide doctor onlayer portraits

        show herbalist smile at left onlayer portraits

        herbalist "\"Yes, of course.\""

        herbalist "\"I have plenty, how much whould you want?\""

        hide herbalist onlayer portraits

        show doctor default at left onlayer portraits
        
        doctor "I just need enough for a dose for now at least."

        doctor "He said he has plenty."

        doctor "I can come again if needed."

        show doctor smile at left onlayer portraits with dissolve

        doctor "\"One bottle would be enough.\""

        doctor "\"Thank you again Mr. Kazuki.\""

        show doctor default at left onlayer portraits with dissolve

        doctor "\"Now, for the rest..\""


    hide doctor onlayer portraits with dissolve

    menu:

        "Junka Root":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I'll take the Junka Root...\""

        "Tsuyomi Cap":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I'll take the Tsuyomi Cap...\""


    #TODO: Remove those lines of code as this block is not reachable from any route

    #doctor "\"I would also like some {a=glossary:nagomi_root_entry}Nagomi Root{/a} and {a=glossary:hogo_root_entry}Hogo Root{/a}.\""

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Thank you, Mr. Kazuki. Until we meet again.\""

    hide doctor onlayer portraits

    show herbalist smile at left onlayer portraits

    herbalist "\"I hope you can help your Mother, Mr. Yosuke.\""
    
    herbalist "\"Be careful on your way home.\""

    hide herbalist onlayer portraits with dissolve

    $ took_herbs = True

    scene black with fade

    # "DEBUG hospital: [ch01_went_to_hospital]"
    # "DEBUG cat broke formula: [ch01_cat_broke_formula]"

    #TODO: check this return condition

    if ch01_went_to_hospital and ch01_cat_broke_formula:

        #"DEBUG: ENTERED RETURN CONDITION"

        return


    "Yosuke finally returns home and heads to his laboratory."

    scene bg ch01 lab_no_cat with fade

    "The house is quiet."

    "He sets the herbs down."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "..."

    "There is no answer." 

    "He hurries toward her room."  

    if not ch01_cat_broke_formula:

        show mother default with dissolve

        "She's lying in bed." 

        "The empty vial rests on the bedside table." 

        "His heart sinks." 

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"Mother...\"" 

        hide doctor onlayer portraits with dissolve

        show mother sick with dissolve

        "She slowly opens her eyes." 

        "Her breathing is shallow." 

        "He grab her wrist." 

        "His hands are already searching for a pulse." 

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"It's irregular...\"" 

        hide doctor onlayer portraits with dissolve

        "His eyes dart to the empty vial." 

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"The formula...\"" 

        doctor "\"No...\"" 

        $ nagomi_root_entry.locked = False

        doctor "It contained {a=glossary:nagomi_root_entry}Nagomi Root{/a}."

        doctor "An experimental dose..."

        show doctor panicked at left onlayer portraits with dissolve
        with vpunch

        doctor "It was never meant to be taken without supervision."

        doctor "\"Mother, stay with me.\""

        hide doctor onlayer portraits with dissolve

        "He desperately tries to recall anything from his notes that might be in use."

        #see if vpunvh has to be added everytime

        show doctor panicked at left onlayer portraits with dissolve

        doctor "There has to be something..."

        doctor "There has to be..."

        hide doctor onlayer portraits with dissolve

        "..."

        show doctor panicked at left onlayer portraits with dissolve

        doctor "Nothing."

        hide doctor onlayer portraits with dissolve

        "Her heartbeat becomes weaker."

        "Weaker..."

        "..." 

        "Then it stops." 

        show mother default with dissolve

        show doctor panicked at left onlayer portraits with dissolve
        with vpunch

        doctor "\"Mother...\""

        hide doctor onlayer portraits with dissolve

        "He remain frozen beside her." 

        "..." 

        $ arrhythmia_entry.locked = False

        show doctor panicked at left onlayer portraits with dissolve

        doctor "The {a=glossary:arrhythmia_entry}arrhythmia{/a}..."

        doctor "\"I did this.\""

        $ ch01_knows_arrhythmia = True

        $ ch01_previous_death = "arrhythmia"

        hide doctor onlayer portraits with dissolve

    else: 
        call ch01_answer_mothers_call


    if ch01_loop_count == 0:

        "He holds Mother's hand, but she no longer responds." 

        "He waits." 

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"Maybe...\"" 

        doctor "\"Maybe she will open her eyes.\"" 

        hide doctor onlayer portraits with dissolve

        "..." 

        "But she doesn't." 

        show doctor panicked at left onlayer portraits with dissolve      
        with vpunch

        doctor "How could I make such a mistake?" 

        doctor "How am I supposed to live after this?"

        doctor "I know the truth." 

        doctor "I am a doctor." 

        doctor "I know what death looks like." 

        doctor "Yet I cannot accept it."    

        doctor "\"I'm sorry, Mother...\"" 

        hide doctor onlayer portraits with dissolve

        "The house feels different now." 

        "Too quiet." 

        "Eventually, reality returns." 

        "There are things that need to be done." 

        show doctor default at left onlayer portraits with dissolve

        doctor "I have to report her death." 

        doctor "I have to prepare her body." 

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"I have to tell someone...\""

        hide doctor onlayer portraits with dissolve

        $ wake_entry.locked = False

        "He will have to arrange the {a=glossary:wake_entry}otsuya{/a}."

    else:

        scene black with fade

        "He returns to his laboratory."

        scene bg ch01 lab_no_cat with fade

        "He opens his notes."

        "His hands are shaking as he writes down everything."

        "The mistakes."

        "The symptoms."

        "The things he overlooked."

        show doctor worried at left onlayer portraits with dissolve

        doctor "If I get another chance..."

        doctor "I won't repeat this mistake."

        doctor "\"I will save her.\""

        hide doctor onlayer portraits with dissolve

        scene black with fade

        "He closes his eyes thinking that tomorrow will be different."

        "That he will do better."

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2 from _call_ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop