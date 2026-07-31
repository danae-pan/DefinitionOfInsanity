label ch02_try_different_herb :

    scene bg ch01 lab 

    doctor "I should not lose time. I need a different herb now."

    $ ch02_checked_mother = False
    $ ch02_route_choice = "try_herb"

    menu:
        "Go to the herbalist":
            jump ch02_go_to_herbalist

        "Go to the hospital":
            jump ch02_go_to_hospital
    
    return

label ch02_take_the_first :

    show doctor default at left onlayer portraits

    doctor "\"I will take {a=glossary:junka_root_entry}Junka Root{/a}.\""

    doctor "\"Thank you Mr. Herbalist.\""

    doctor "\"Have a nice day.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"No need to thank me, I just hope it helps.\""

    herbalist "\"Goodbye, Dr. Yosuke.\""

    hide herbalist default onlayer portraits

    scene bg ch01 lab with fade

    "The doctor returns home, walks into his laboratory and spreads several worn medical journals and {a=glossary:kampo_entry}Kampō{/a}  manuscripts across the desk."

    if ch02_use_panax :

        doctor "Along with my research I know one more thing... {a=glossary:nagomi_root_entry}Nagomi Root{/a} is too dangerous. "

        doctor "I will not make the same mistake again."

    else :

        doctor "I have done my research and I already used two herbs that led to Mother’s death."

        doctor "{a=glossary:nagomi_root_entry}Nagomi Root{/a} and Panax Ginseg."

        doctor "I will not make the same mistakes again."

    "He places the herbalist's pouches on the table and gently pours the dried herbs into his hand."

    doctor "This tonic is said to strengthen the body by improving blood circulation."

    doctor "If the body cannot endure the treatment, restoring the nervous system is meaningless."

    "He recalls what the herbalist said."

    if ch02_first_herb_without_instructions or ch02_first_herb_with_instructions :

        doctor "It is advised to take after eating.."

        doctor "..otherwise it might upset the stomach."

        doctor "But this is not a conclusive advice."

        doctor "\"Either way, there is a risk to be taken.\""

    doctor "After eating..."

    doctor "\"I must remember that.\""

    "He carefully places the Junka Root into the mortar before turning back to his notes."

    doctor "\"Now... the second phase.\""

    "He reaches for a small wooden box tucked away on the upper shelf."

    "Inside lies the last of his {a=glossary:hogo_root_entry}Hogo Root{/a}."

    "He carefully examines the remaining dried roots."

    doctor "There isn't much left..."

    doctor "It should be enough for one preparation."

    "He opens one of his Kampō manuscripts and rereads a passage he had marked days before."

    doctor "Some physicians believe Hogo Root calms the mind and supports the nervous system."

    doctor "If healthy neurons can compensate for those that have been damaged."

    doctor "Perhaps this will encourage that process."

    "He places the Hogo Root into the mortar beside the Junka Root."

    "The pestle moves slowly in circles, reducing the dried herbs to a fine powder."

    "He transfers the mixture into a ceramic bowl and gradually pours hot water over it."

    "Steam rises as the herbs begin to infuse."

    "The laboratory fills with the aroma of the herbs."

    "He gently stirs the {a=glossary:decoction_entry}decoction{/a}, carefully observing its colour and consistency."

    doctor "The extraction isn't complete yet."

    show doctor default at left onlayer portraits

    doctor "\"Just a few more minutes...\""

    "A loud meow echoes through the laboratory."

    hide doctor default onlayer portraits

    "The cat rubs itself against his leg, meowing repeatedly."

    if not ch02_sick_pet :

        "Only then does he notice how thin it has become."

        doctor "You've hardly eaten..."

        "He kneels beside it."

        doctor "You've been showing the same symptoms... loss of balance... weakness..."

    else :

        show doctor default at left onlayer portraits

        doctor "\"I know you are sick..\""

        hide doctor default onlayer portraits

    if kept_cat_in_lab_once :

        show doctor default at left onlayer portraits

        doctor "\"...you made a mess before.\""

        hide doctor default onlayer portraits

        doctor "I should not let you inside the lab anymore."

    if ch02_hungry_pet :

        show doctor default at left onlayer portraits

        doctor "\"And last I lose time feeding you..\""

        doctor "I should be careful with my choices."

        hide doctor default onlayer portraits

    "He sighs."

    show doctor default at left onlayer portraits

    doctor "\"Mother needs this medicine...\""

    hide doctor default onlayer portraits

    "The cat meows once more."

    show doctor default at left onlayer portraits

    doctor "\"...but if I leave you like this...\""

    doctor "\"...you'll only keep crying.\""

    hide doctor default onlayer portraits

    $ ch02_hungry_pet = True 

    $ ch02_sick_pet = True

    "He remains frozen between the workbench and the hungry animal at his feet."

    menu : 

        "Feed the cat":

            jump ch02_feed_the_cat

        "Keep working on the formula":

            jump ch02_cat_broke_formula_ending

    return 

label ch02_take_the_second :

    show doctor default at left onlayer portraits

    doctor "\"I will take {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}.\""

    doctor "\"Thank you Mr. Herbalist.\""

    doctor "\"Have a nice day.\""

    hide doctor default onlayer portraits

    show doctor default at left onlayer portraits

    herbalist "\"No need to thank me, I just hope it helps.\""

    herbalist "\"Goodbye, Mr. Herbalist.\""

    hide doctor default onlayer portraits 

    scene bg ch01 lab with fade

    "The doctor returns home, walks into his laboratory and spreads several worn medical journals and Kampō manuscripts across the desk."

    if ch02_use_panax :

        doctor "Along with my research I know one more thing... Nagomi Root is too dangerous."

        doctor "I will not make the same mistake again."

    else :

        doctor "I have done my research and I already used two herbs that led to Mother’s death."

        doctor "Nagomi Root and Panax Ginseg."

        doctor "I will not make the same mistakes again."

    if ch02_first_herb_without_instructions :

        doctor "Last time, I took Junka Root from the herbalist and used it for the first phase of the treatment."

        doctor "Now, it's time to focus on the second phase."

        doctor "I only hope Tsuyomi Cap will prove effective."

    "He unties the herbalist's pouch and gently pours the dried herb into his hand."

    doctor "Tsuyomu..."

    doctor "It is believed to strengthen the immune system and support recovery."

    "He studies the mushroom slices for a moment before placing them beside the mortar."

    doctor "If the body cannot endure the treatment.."

    doctor "..there is little hope of restoring the nervous system."

    "Then, his eyes settle on the container with Ryoku Berry."

    doctor "Ryoku Berry... it strengthens the body and may improve its resilience. "

    doctor "I only have a small amount left, but it should be enough."

    "With his decision made, he places the Tsuyomi Cap and Ryoku Berry into the mortar."

    "He slowly mixes the dried herbs, reducing them to a fine powder."

    "He carefully transfers the mixture into a ceramic bowl before slowly pouring hot water over it."

    "Steam rises as the herbs begin to infuse."

    "The laboratory fills with the earthy scent of herbs."

    "The doctor observes the ceramic bowl."

    doctor "Good. The extraction has begun.Then another."

    doctor "Just a little longer."

    "The color of the mix is just as his research described."

    doctor "This may actually work."

    "Just then, a weak voice echoes from upstairs."

    mother "\"My son...\""

    "The doctor's hand stops."

    "He grips the wooden spoon a little tighter."

    show doctor default at left onlayer portraits

    doctor "\"She's awake...\""

    hide doctor default onlayer portraits

    "He glances back at the bowl."

    "The decoction is almost ready."

    "Interrupting the preparation now could alter the concentration."

    "He would have to begin again and he knows that {a=glossary:ryoku_berry_entry}Ryoku Berry{/a} might not be enough."

    "A second call reaches him."

    mother "\"My son...\""

    "Her voice is barely more than a whisper."

    "He lowers his eyes to the simmering mixture."

    doctor "There isn't much left. "

    doctor "Just a few more minutes."

    doctor "If I stop now, all of this may have been for nothing."

    menu : 

        "Go to her":

            jump ch02_mother_calls_for_food

        "Keep on working":

            jump ch02_mother_cant_swallow_ending


    return 