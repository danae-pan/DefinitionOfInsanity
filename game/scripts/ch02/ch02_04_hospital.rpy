label ch02_go_to_hospital :

    "The doctor puts on his coat and leaves the house."

    doctor "The hospital is closer than the herbalist’s shop. "

    doctor "It should take 10 minutes walk to get there."

    "The doctor heads to the hospital. He walks in a fast pace, trying not to lose more time."

    doctor "I should go straight to the pharmacy. "

    if use_panax :

        doctor "Check the stock, take what’s needed and leave."

    else :

        doctor "I know that my chances are slight but I should check the stock anyway."

        doctor "Maybe there is a herb that I didn’t notice before."

    doctor "I should avoid any conversation, otherwise I will won’t avoid looking at the patients here."

    "He arrives at the pharmacy."

    "For his good luck, no one is there at the moment."

    "He browses the available herbs on the selves."

    "Not many of them are left. The hospital runs out of stock fast because of the number of diseased people."

    if not ch02_use_panax :

        if not ch02_stock_panax :

            doctor "Nothing from the herbs are suitable for what I need.."

            doctor "Wait a minute!"

            doctor "There is a glass bottle of dry Ginseng Panax."

            doctor "I could use this for phase two, replacing Polygala tenuifolia that I only have in a small amount."

        else:

            doctor "The glass bottle of dry Ginseng Panax is still there."

    else :

        "After some time he realizes that none of the herbs available are suitable for him." 

        $ ch02_second_visit_hospital = True 

        doctor "Ginseng Panax is still there but I already know, I can’t use this one."

        doctor "I won’t make the same mistake again."

        doctor "I should go to the herbalist instead."

        jump ch02_go_to_herbalist

    "The doctor grabs the bottle and quickly heads home to prepare the formula."

    scene bg ch01 lab with fade 

    "He walks into his laboratory and spreads several worn medical journals and Kampō manuscripts across the desk."

    "Yesterday taught me one thing... Licorice root seems too dangerous. "

    "His eyes settle on the container with Schisandra chinensis."

    doctor "Schisandra can replace Licorise for the first phase."

    doctor "It strengthens the body and may improve its resilience. "

    doctor "I only have a small amount left, but it should be enough."

    doctor "Now for the second phase..."

    "He pulls the small bottle of dried Panax Ginseng root from his coat pocket, which he had obtained from the hospital."

    doctor "It is known to restore strength and reduce fatigue... perhaps it can stimulate the healthy neurons to compensate for the damaged ones."

    "He hesitates. reading the next pages of the book in front of him."

    doctor "The reports mention changes in blood pressure... but they are uncommon."

    "He closes the book."

    "He decides not to lose more precious time."

    "He begins grinding the dried roots with a mortar and pestle until they become a fine powder. "

    "Slowly, he combines the measured ingredients inside a ceramic bowl, adding hot water drop by drop until the mixture forms a dark herbal decoction."

    doctor "Every measurement has to be exact."

    "He pours the medicine into a small porcelain bottle."

    doctor "If my theory is correct... this should be enough."

    "A loud meow echoes through the laboratory."

    "The cat rubs itself against his leg, meowing repeatedly."

    if not ch02_sick_pet:

        "Only then does he notice how thin it has become."

        show doctor default at left onlayer portraits

        doctor "You've hardly eaten..."

        hide doctor default onlayer portraits

        "He kneels beside it."

        doctor "You've been showing the same symptoms... loss of balance... weakness..."

    else :

        show doctor default at left onlayer portraits

        doctor "I know you are sick..."

        hide doctor default onlayer portraits

    if kept_cat_in_lab_once :

        show doctor default at left onlayer portraits

        doctor "You made a mess before."

        doctor "I should not let you inside the lab anymore."

        hide doctor default onlayer portraits

    if ch02_hungry_pet :

        show doctor default at left onlayer portraits

        doctor "And last I lose time feeding you.."

        doctor "I should be careful with my choices."

        hide doctor default onlayer portraits

    "He sighs."

    doctor "Mother needs this medicine..."

    "The cat meows once more."

    doctor "...but if I leave you like this..."

    doctor "...you'll only keep crying."

    "He remains frozen between the workbench and the hungry animal at his feet."

    menu :

        "Go to your mother" :

            jump ch02_used_panax_ending 

        "Play with and feed the cat":

            jump ch02_cardiac_arrest_ending

    return