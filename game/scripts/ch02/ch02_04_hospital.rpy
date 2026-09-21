label ch02_go_to_hospital :

    scene bg game_main with fade

    "The doctor puts on his coat and leaves the house."

    show doctor default at left onlayer portraits with dissolve

    doctor "The hospital is closer than the herbalist’s store. "

    doctor "It should take only 10 minutes walk to get there."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    #SOUND

    play sound "audio/sfx/footsteps_rock.mp3"

    pause 0.8

    play sound "audio/sfx/footsteps_rock.mp3"

    pause 0.8

    play sound "audio/sfx/footsteps_rock.mp3"

    "The doctor heads to the hospital. He walks in a fast pace, trying not to lose more time."
    
    scene bg ch01 hospital with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "I should go straight to the pharmacy. "

    if ch02_used_taeru_happened:

        doctor "Check the stock, take what’s needed and leave."

    else :

        doctor "I know that my chances are slight but I should check the stock anyway."

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "Maybe there is a herb that I didn’t notice before."

    doctor "I should avoid any conversation, otherwise I won't be able to avoid looking at the patients here."

    hide doctor onlayer portraits with dissolve

    "He arrives at the pharmacy."

    "For his good luck, no one is there at the moment."

    "He browses the available herbs on the selves."

    "Not many of them are left. The hospital runs out of stock fast because of the number of diseased people."

    if not ch02_used_taeru_happened:

        if not ch02_knows_taeru_in_stock: 

            show doctor default at left onlayer portraits with dissolve

            doctor "Nothing from the herbs are suitable for what I need.."

            show doctor dsmile at left onlayer portraits with dissolve

            doctor "\"Wait a minute!\""

            $ taeru_root_entry.locked = False

            doctor "There is a glass bottle of dry {a=glossary:taeru_root_entry}Taeru Root{/a}."

            $ ch02_knows_taeru_in_stock = True

            $ hogo_root_entry.locked = False

            # TODO: add info about the phases of the cure

            doctor "I could use this for phase two, replacing {a=glossary:hogo_root_entry}Hogo Root{/a} that I only have in a small amount."

            hide doctor onlayer portraits with dissolve

        else :

            $ taeru_root_entry.locked = False

            show doctor default at left onlayer portraits with dissolve

            doctor "The glass bottle of dry {a=glossary:taeru_root_entry}Taeru Root{/a} is still there."

            hide doctor onlayer portraits with dissolve


    else :

        "After some time he realizes that none of the herbs available are suitable for him." 

        $ taeru_root_entry.locked = False

        show doctor default at left onlayer portraits with dissolve

        doctor "{a=glossary:taeru_root_entry}Taeru Root{/a} is still there but I already know, I can’t use this one."

        doctor "I won’t make the same mistake again."

        doctor "I should go to the herbalist instead."

        $ ch02_coming_from_hospital = True 

        hide doctor onlayer portraits with dissolve

        jump ch02_go_to_herbalist

    "The doctor grabs the bottle and quickly heads home to prepare the {a=glossary:formula_entry}formula{/a}."

    scene bg ch01 lab_no_cat with fade 

    $ kampo_entry.locked = False

    #SOUND

    play sound "audio/sfx/footsteps.mp3"

    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    "He walks into his laboratory and spreads several worn medical journals and {a=glossary:kampo_entry}Kampo{/a} manuscripts across the desk."

    $ nagomi_root_entry.locked = False

    show doctor worried at left onlayer portraits with dissolve

    doctor "My previous attempts taught me one thing... {a=glossary:nagomi_root_entry}Nagomi Root{/a} seems too dangerous. "

    hide doctor onlayer portraits with dissolve

    $ ryoku_berry_entry.locked = False

    "His eyes settle on the container with {a=glossary:ryoku_berry_entry}Ryoku Berry{/a}."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Right...\""

    doctor "Ryoku Berry can replace Nagomi Root for the first phase."

    doctor "It strengthens the body and may improve its resilience."
    
    doctor "I didn't use this before before..."

    doctor "I only have a small amount left."
    
    doctor "But it should be enough."

    doctor "\"Now for the second phase...\""

    hide doctor onlayer portraits with dissolve

    "He pulls the small bottle of dried Taeru Root from his coat pocket, which he had obtained from the hospital."

    show doctor default at left onlayer portraits with dissolve

    doctor "It is known to restore strength and reduce fatigue..."
    
    doctor "Perhaps it can stimulate the healthy neurons to compensate for the damaged ones."

    hide doctor onlayer portraits with dissolve

    "He hesitates reading the next pages of the book in front of him."

    show doctor worried at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/suspence.mp3"

    doctor "The reports mention changes in blood pressure... but they are uncommon."

    hide doctor onlayer portraits with dissolve

    "He closes the book."

    "He decides not to lose more precious time."

    #SOUND

    play sound "audio/sfx/lab_noise.mp3"

    "He begins grinding the dried roots with a mortar and pestle until they become a fine powder."

    $ decoction_entry.locked = False

    "He combines the measured ingredients inside a ceramic bowl."
    
    "Adding hot water drop by drop, the mixture finally forms a dark herbal {a=glossary:decoction_entry}decoction{/a}."

    show doctor default at left onlayer portraits with dissolve
    
    doctor "Every measurement has to be exact."

    hide doctor onlayer portraits with dissolve

    "He pours the medicine into a small glass bottle."

    show doctor default at left onlayer portraits with dissolve

    doctor "If my theory is correct... this should be enough."

    hide doctor onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/cat_long.mp3"

    "A loud meow echoes through the laboratory."

    scene bg ch01 lab with fade

    "The cat rubs itself against his leg, meowing repeatedly."

    if not ch02_knows_cat_is_sick:

        "Only then does he notice how thin it has become."

        show doctor default at left onlayer portraits with dissolve

        doctor "You've hardly eaten..."

        hide doctor onlayer portraits with dissolve

        "He kneels beside it."

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "You've been showing the same symptoms... loss of balance... weakness..."

        hide doctor onlayer portraits with dissolve

        $ ch02_knows_cat_is_sick = True

    else :

        show doctor worried at left onlayer portraits with dissolve

        doctor "\"I know you are sick...\""

    if kept_cat_in_lab_once :

        doctor "\"You made a mess before.\""

        doctor "I should not let you inside the lab anymore."

    hide doctor onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/Sigh.mp3"

    "He sighs."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother needs this medicine...\""

    hide doctor onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/cat_short.mp3"

    "The cat meows once more."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\But if I leave you like this...\""

    doctor "\"...you'll only keep crying.\""

    hide doctor onlayer portraits

    "He remains frozen between the workbench and the hungry animal at his feet."

    menu :

        "Go to your Mother" :

            jump ch02_used_taeru_ending

        "Play with and feed the cat":

            jump ch02_cardiac_arrest_ending

    return