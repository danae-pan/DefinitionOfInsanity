label ch01_arrythmia_good_ending :

    "I glance back toward Mother's room."

    "She called for me..." 

    if not met_herbalist:

        "But if Mr. Herbalist really has herbs the hospital doesn't..."

        "They could help me develop a better treatment." 

    else:

        "Herbalist said the last time he has some herbs that might help."

    if herbalist_visited:

        "Herbalist have herbs that will help me develop a better formula."

    doctor "Alright." 

    doctor "I'll come with you." 

    "The neighboring village is about a thirty-minute walk away." 

    "As we walk, Herbalist tells me about the people he has treated over the years." 

    herbalist "I've never seen anyone cured." 

    herbalist "But I've seen this illness many times." 

    herbalist "It always begins differently..." 

    herbalist "Eventually, their muscles grow too weak to support them." 

    herbalist "Many also lose the ability to swallow safely."  

    herbalist "Food and even water can become dangerous." 

    herbalist "Later... they begin losing their balance." 

    "I quietly commit every word to memory."  

    "We arrive at Herbalist's shop." 

    scene bg ch01 herbstore

    "Shelves packed with dried herbs, roots, and flowers surround us." 

    "The air is filled with earthy, unfamiliar scents." 

    herbalist "These may interest you." 

    "I examine the herbs carefully." 

    "One catches my eye." 

    doctor "Dong quai..." 

    "Traditionally used to improve blood circulation." 

    "Another sits beside it." 

    doctor "Ganoderma lucidum..." 

    "Reishi." 

    "Believed to strengthen the body's resilience." 

    "I can only afford one." 

    menu:

        "Dong quai":

            "I'll take the Dong quai..."

        "Ganoderma lucidum":

            "I'll take the Ganoderma lucidum..."

    if ch01_cat_broke_formula:

        "I also want some Licorice root and Polygala tenuifolia."

    doctor "Thank you Herbalist. Till we meet again" 

    herbalist "I hope you can help your mother Yosuke. Be safe walking home." 

    $ took_herbs = True
    
    "I finally return home." 

    "The house is quiet." 

    "I set the herbs down." 

    doctor "Mother?" 

    "..." 

    "There is no answer." 

    "I hurry toward her room."  

    "She's lying in bed." 

    "The empty vial rests on the bedside table." 

    "My heart sinks." 

    doctor "Mother..." 

    "She slowly opens her eyes." 

    "Her breathing is shallow." 

    "I grab her wrist." 

    "My hands are already searching for a pulse." 

    "It's irregular..." 

    "My eyes dart to the empty vial." 

    "The formula..." 

    "No..." 

    "It contained Licorice Root." 

    "An experimental dose..." 

    "It was never meant to be taken." 

    doctor "Mother, stay with me." 

    "I search my notes." 

    "There has to be something..." 

    "There has to be..." 

    "..." 

    "Nothing." 

    "Her heartbeat becomes weaker." 

    "Weaker..." 

    "..." 

    "It stops." 

    doctor "Mother..." 

    "I remain frozen beside her." 

    "..." 

    doctor "The arrhythmia..." 

    doctor "I did this."

    if ch01_loop_count == 0:

        "I hold Mother's hand, but she no longer responds." 

        "I wait." 

        "Maybe..." 

        "Maybe she will open her eyes." 

        "..." 

        "But she doesn't." 

        doctor "How could I make such a mistake?" 

        $ ch01_knows_arrhythmia = True

        "How am I supposed to live after this?"

        "I know the truth." 

        "I am a doctor." 

        "I know what death looks like." 

        "Yet I cannot accept it." 

        "I close her eyes gently." 

        doctor "I'm sorry, Mother..." 

        "The house feels different now." 

        "Too quiet." 

        "Eventually, reality returns." 

        "There are things that need to be done." 

        "I have to report her death." 

        "I have to prepare her body." 

        "I have to tell someone."

        "Wake"

    $ ch01_check_formula = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop