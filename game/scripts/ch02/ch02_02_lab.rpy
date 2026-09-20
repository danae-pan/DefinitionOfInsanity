label ch02_try_different_herb :

    scene bg ch01 lab_no_cat with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "I should not lose more time."

    call ch02_check_mother

    menu:
        "Visit Mr. Kazuki's store":
            jump ch02_go_to_herbalist

        "Head to the hospital":
            jump ch02_go_to_hospital
    
    return

label ch02_take_the_first :

    show doctor default at left onlayer portraits with dissolve

    $ junka_root_entry.locked = False

    doctor "\"I will take {a=glossary:junka_root_entry}Junka Root{/a}.\""

    doctor "\"Thank you Mr. Kazuki.\""

    doctor "\"Have a nice day.\""

    hide doctor onlayer portraits 

    show herbalist smile at left onlayer portraits

    herbalist "\"No need to thank me, I just hope it helps.\""

    herbalist "\"Goodbye, Dr. Yosuke.\""

    hide herbalist default onlayer portraits with dissolve

    scene bg ch01 lab_no_cat with fade

    $ kampo_entry.locked = False

    "The doctor returns home, walks into his laboratory and spreads several worn medical journals and {a=glossary:kampo_entry}Kampo{/a} manuscripts across the desk."

    show doctor worried at left onlayer portraits with dissolve
    
    if not ch02_used_taeru_happened:

        $ nagomi_root_entry.locked = False

        doctor "Along with my research I know one more thing... {a=glossary:nagomi_root_entry}Nagomi Root{/a} is too dangerous. "

        doctor "I will not make the same mistake again."

    else :

        #TODO: maybe add to the glossary the phases of the medicine

        $ nagomi_root_entry.locked = False

        $ taeru_root_entry.locked = False

        #TODO: add the condition for the first herb tried on the take second label

        if ch02_second_herb_with_instructions or ch02_second_herb_without_instructions:

            $ tsuyomi_cap_entry.locked = False

            doctor "I've already tried three different herbs."

            doctor "{a=glossary:nagomi_root_entry}Nagomi Root{/a}, {a=glossary:taeru_root_entry}Taeru Root{/a}, and {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}."

            doctor "None of them were able to save Mother."

            doctor "I won't make the same mistakes again."

        else:

            doctor "I've already tried two different herbs."

            doctor "{a=glossary:nagomi_root_entry}Nagomi Root{/a} and {a=glossary:taeru_root_entry}Taeru Root{/a}."

            doctor "I won't make the same mistakes again."

    hide doctor onlayer portraits with dissolve

    "He places the herbalist's pouches on the table and gently pours the dried herbs into his hand."

    show doctor default at left onlayer portraits with dissolve

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions:

        doctor "I've already tried Junka Root in the first phase of the treatment."

        if ch02_first_herb_with_instructions:

            doctor "Last time, I followed the instructions and made sure Mother ate first."

            doctor "But by the time the formula was ready, I was too late."

        if ch02_first_herb_without_instructions:

            doctor "When I ignored the instructions and gave it to Mother without eating first."

            doctor "It made her violently sick, and she choked."

        doctor "There must be another way to make this work."

    else:

        doctor "This tonic is said to strengthen the body by improving blood circulation."

        doctor "If the body cannot endure the treatment, restoring the nervous system is meaningless."

    hide doctor onlayer portraits with dissolve

    "He recalls what the herbalist said."

    show doctor worried at left onlayer portraits with dissolve

    if ch02_first_herb_without_instructions or ch02_first_herb_with_instructions:

        doctor "Eating beforehand is advised."

        doctor "Otherwise, it might upset the stomach."

        show doctor default at left onlayer portraits with dissolve

        doctor "But his advice wasn't conclusive."

        doctor "\"Either way, there is a risk to be taken.\""

    else:

        doctor "After eating..."

        doctor "\"I must remember that.\""

    hide doctor onlayer portraits with dissolve

    "He carefully places the Junka Root into the mortar before turning back to his notes."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Now... the second phase.\""

    hide doctor onlayer portraits with dissolve

    "He reaches for a small wooden box tucked away on the upper shelf."

    $ hogo_root_entry.locked = False

    "Inside lies the last of his {a=glossary:hogo_root_entry}Hogo Root{/a}."

    "He carefully examines the remaining dried roots."

    show doctor default at left onlayer portraits with dissolve

    doctor "I used this before..."

    doctor "I know there isn't much left."

    doctor "But it should be enough for one preparation."

    hide doctor onlayer portraits with dissolve

    "He opens one of his Kampo manuscripts and rereads a passage he had marked days before."

    show doctor default at left onlayer portraits with dissolve

    doctor "Some physicians believe Hogo Root calms the mind and supports the nervous system."

    doctor "If healthy neurons can compensate for those that have been damaged."

    doctor "Perhaps this will encourage that process."

    hide doctor onlayer portraits with dissolve

    "He places the Hogo Root into the mortar beside the Junka Root."

    "The pestle moves slowly in circles, reducing the dried herbs to a fine powder."

    "He transfers the mixture into a ceramic bowl and gradually pours hot water over it."

    "Steam rises as the herbs begin to infuse."

    "The laboratory fills with the aroma of the herbs."

    $ decoction_entry.locked = False

    "He stirs the {a=glossary:decoction_entry}decoction{/a}, carefully observing its colour and consistency."

    show doctor default at left onlayer portraits with dissolve

    doctor "The extraction isn't complete yet."

    doctor "\"Just a few more minutes...\""

    hide doctor onlayer portraits with dissolve

    scene bg ch01 lab with fade

    "A loud meow echoes through the laboratory."

    "The cat rubs itself against his leg, meowing repeatedly."

    if not ch02_knows_cat_is_sick :

        "Only then does he notice how thin it has become."

        show doctor default at left onlayer portraits with dissolve

        doctor "You've hardly eaten..."

        hide doctor onlayer portraits with dissolve

        "He kneels beside her."

        show doctor worried at left onlayer portraits with dissolve

        doctor "You've been showing the same symptoms... loss of balance... weakness..."

        $ ch02_knows_cat_is_sick = True

    else :

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"I know you are sick...\""

    if kept_cat_in_lab_once :

        doctor "\"You made a mess before.\""

        doctor "I should not let you inside the lab anymore."

    hide doctor onlayer portraits with dissolve

    "He sighs."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother needs this medicine...\""

    hide doctor onlayer portraits with dissolve

    "The cat meows once more."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"But if I leave you like this...\""

    doctor "\"...you'll only keep crying.\""

    hide doctor onlayer portraits with dissolve

    "He remains frozen between the workbench and the hungry animal at his feet."

    menu : 

        "Feed the cat":

            jump ch02_feed_the_cat

        "Keep working on the formula":

            jump ch02_cat_broke_formula_ending

    return 

label ch02_take_the_second :

    $ ch02_second_herb_taken = True

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I will take Tsuyomi Cap.\""

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Thank you Mr. Kazuki.\""

    doctor "\"Have a nice day.\""

    hide doctor onlayer portraits

    show herbalist smile at left onlayer portraits

    herbalist "\"No need to thank me, I just hope it helps.\""

    herbalist "\"Goodbye, Mr. Yosuke.\""

    hide herbalist default onlayer portraits with dissolve

    scene bg ch01 lab_no_cat with fade

    $ kampo_entry.locked = False

    "The doctor returns home, walks into his laboratory and spreads several worn medical journals and {a=glossary:kampo_entry}Kampo{/a} manuscripts across the desk."

    show doctor worried at left onlayer portraits with dissolve

    if not ch02_used_taeru_happened:

        $ nagomi_root_entry.locked = False

        doctor "Along with my research I know one more thing... {a=glossary:nagomi_root_entry}Nagomi Root{/a} is too dangerous. "

        doctor "I will not make the same mistake again."

    else :

        $ nagomi_root_entry.locked = False

        $ taeru_root_entry.locked = False

        $junka_root_entry.locked = False

        if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions:

                $ junka_root_entry.locked = False

                doctor "I've already tried three different herbs."

                doctor "{a=glossary:nagomi_root_entry}Nagomi Root{/a}, {a=glossary:taeru_root_entry}Taeru Root{/a}, and {a=glossary:junka_root_entry}Junka Root{/a}."

                doctor "None of them were able to save Mother."

                doctor "I won't make the same mistakes again."

        else:

            doctor "I've already tried two different herbs."

            doctor "{a=glossary:nagomi_root_entry}Nagomi Root{/a} and {a=glossary:taeru_root_entry}Taeru Root{/a}."

            doctor "I won't make the same mistakes again."

    show doctor default at left onlayer portraits with dissolve

    if ch02_second_herb_with_instructions or ch02_second_herb_without_instructions:

        doctor "I've already tried Tsuyomi Cap."

        if ch02_second_herb_with_instructions:

            doctor "Last time, I followed the instructions and made sure Mother didn't eat first."

            doctor "But I waited too long."

            doctor "By the time the formula was ready, she could no longer swallow."

        if ch02_second_herb_without_instructions:

            doctor "When I ignored the instructions and fed Mother first..."

            doctor "The medicine had no effect."

            doctor "Her condition continued to worsen."

        doctor "There must be another way to make this work."

    else:

        doctor "Tsuyomi Cap..."

        doctor "It is believed to strengthen the immune system and support recovery."

        doctor "If the body cannot endure the treatment..."

        doctor "...there is little hope of restoring the nervous system."

    hide doctor onlayer portraits with dissolve

    "He recalls what the herbalist said."

    show doctor worried at left onlayer portraits with dissolve

    if ch02_second_herb_with_instructions or ch02_second_herb_without_instructions:

        doctor "It should be taken on an empty stomach."

        doctor "Taking it after eating may interfere with its effects."

        show doctor default at left onlayer portraits with dissolve

        doctor "But his advice wasn't conclusive."

        doctor "\"Either way, there is a risk to be taken.\""

    else:

        doctor "On an empty stomach..."

        doctor "\"I must remember that.\""

    hide doctor onlayer portraits with dissolve

    "He unties the herbalist's pouch and gently pours the dried herb into his hand."

    "He studies the mushroom slices for a moment before placing them beside the mortar."

    $ ryoku_berry_entry.locked = False

    "Then, his eyes settle on the container with {a=glossary:ryoku_berry_entry}Ryoku Berry{/a}."

    show doctor default at left onlayer portraits with dissolve

    doctor "Ryoku Berry... it strengthens the body and may improve its resilience. "

    doctor "I only have a small amount left, but it should be enough."

    hide doctor onlayer portraits with dissolve

    "With his decision made, he places the Tsuyomi Cap and Ryoku Berry into the mortar."

    "He slowly mixes the dried herbs, reducing them to a fine powder."

    "He carefully transfers the mixture into a ceramic bowl before slowly pouring hot water over it."

    "Steam rises as the herbs begin to infuse."

    "The laboratory fills with the earthy scent of herbs."

    "The doctor observes the ceramic bowl."

    show doctor default at left onlayer portraits with dissolve

    doctor "Good. The extraction has begun."

    doctor "\"Just a little longer.\""

    hide doctor onlayer portraits with dissolve

    "The color of the mix is just as his research described."

    show doctor default at left onlayer portraits with dissolve

    doctor "This may actually work."

    hide doctor onlayer portraits with dissolve

    "Just then, a weak voice echoes from upstairs."

    mother "\"My son...\""

    "The doctor's hand stops."

    "He grips the wooden spoon a little tighter."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"She's awake...\""

    hide doctor onlayer portraits with dissolve

    "He glances back at the bowl."

    "The decoction is almost ready."

    "Interrupting the preparation now could alter the concentration."

    "He would have to begin again and he knows that Ryoku Berry might not be enough."

    "A second call reaches him."

    mother "\"My son...\""

    "Her voice is barely more than a whisper."

    "He lowers his eyes to the simmering mixture."

    show doctor default at left onlayer portraits with dissolve

    doctor "There isn't much left. "

    doctor "Just a few more minutes."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"If I stop now, all of this may have been for nothing...\""

    hide doctor onlayer portraits with dissolve

    menu : 

        "Go to her":

            jump ch02_mother_calls_for_food

        "Keep on working":

            jump ch02_mother_cant_swallow_ending


    return 