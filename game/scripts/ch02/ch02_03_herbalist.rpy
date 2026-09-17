label ch02_go_to_herbalist :

    scene black with fade

    if ch02_coming_from_hospital == True:

        "The doctors leaves the hospital in a rush and heads to the herbalist’s store."

        "After 20 minutes walk, he reaches the central square."

    else :

        "The doctor puts on his coat and leaves the house."

    if herbalist_visited :

        show doctor default at left onlayer portraits with dissolve

        doctor "I know now where to find the herbalist."

        if not ch02_coming_from_hospital:

            doctor "It is only 30 minutes walk, I better hurry."

        hide doctor default onlayer portraits with dissolve

        "He finally reaches the central square and heads to Mr. Kazuki's store."

    else :

        show doctor default at left onlayer portraits with dissolve

        doctor "It shouldn't be difficult to find the herbalist's store."

        doctor "He mentioned it was somewhere in the central square."

        doctor "If not... I can always ask someone."

        hide doctor default onlayer portraits with dissolve

        "After 30 minutes of walking, he reaches the central square."

        "His eyes scan the buildings one by one."

        "Then he spots it."

        "A small wooden store with bundles of dried herbs hanging above the entrance"

        show doctor default at left onlayer portraits with dissolve

        doctor "This must be it."

        hide doctor default onlayer portraits with dissolve

        $ herbalist_visited = True 


    scene bg ch01 herbstore with fade 

    "He steps inside."

    "The room is filled with the scent of dried plants and medicinal roots."

    "There is no one at the counter."

    "The doctor looks around."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Hello? Is anyone here?\""

    hide doctor default onlayer portraits with dissolve

    "A voice calls from the back of the store."

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"Just a moment! I'll be right there!\""

    hide herbalist default onlayer portraits with dissolve

    "After a few seconds, the Herbalist appears, struggling to balance several glass jars and wooden boxes in his arms."

    show herbalist default at left onlayer portraits with dissolve
    
    herbalist "\"Oh! Good morning!\""

    hide herbalist default onlayer portraits with dissolve

    "He carefully places everything on the counter before smiling warmly."

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"What can I do for you today?\""

    hide herbalist default onlayer portraits with dissolve

    "The doctor hesitates."

    show doctor default at left onlayer portraits with dissolve

    doctor "Right..."

    doctor "To him, we've never met."

    hide doctor default onlayer portraits with dissolve

    "He clears his throat"

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Good morning. I'm Dr.Kazuki.\""

    doctor "\"My Mother has fallen ill after eating contaminated fish.\""
    
    doctor "\"Some colleagues at the hospital mentioned that you have some herbs that may help.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"Ah, yes... yes, of course.\""

    hide herbalist default onlayer portraits with dissolve

    "The herbalist begins searching through the clutter covering his workbench."

    show herbalist default at left onlayer portraits

    herbalist "\"Now where did I put them...\""

    herbalist "\"Forgive the mess.\""

    herbalist "\"Ever since all these people started getting sick, I barely have enough time to organize the store before another customer arrives.\""

    hide herbalist default onlayer portraits

    "He continues rummaging through jars and bundles of herbs."

    show herbalist default at left onlayer portraits

    herbalist "\"While I'm looking...\""

    herbalist "\"How is your Mother doing?\""

    hide herbalist default onlayer portraits with dissolve

    "The doctor's expression darkens."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Not well.\""

    doctor "\"She was exposed for many years.\""

    doctor "\"I managed to ease some of her symptoms whenever I came home from the city...\""

    doctor "\"...but that was before anyone knew contaminated fish was the cause.\""

    doctor "\"If I had known earlier...\""

    doctor "\"...I could have changed her diet.\""

    doctor "\"Maybe things would have been different.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"I've heard about you.\""

    herbalist "\"You left for the city around 1930 to study medicine, didn't you?\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Yes.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"Then perhaps fate was kinder to you than you realize.\""

    herbalist "\"You weren't here to eat the poisoned fish.\""

    herbalist "\"Now you've returned with the knowledge to help those who remained.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Perhaps...\""

    doctor "\"But knowledge means very little when you cannot save your own family.\""

    doctor "\"My Mother is all I have.\""

    hide doctor default onlayer portraits with dissolve

    "The herbalist smiles gently."

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"You cannot ask more of yourself than to do everything within your power.\""

    herbalist "\"Remember that.\""

    hide herbalist default onlayer portraits with dissolve

    "He suddenly reaches beneath a shelf."

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"Ah!\""

    herbalist "\"Here they are.\""

    hide herbalist default onlayer portraits with dissolve

    "He places two small containers on the counter."

    show herbalist default at left onlayer portraits with dissolve

    #TODO: Maybe change this in the first chapter too. don't make it like the doctor can't afford it, it is just the herbalists

    herbalist "\"Unfortunately, my stock is running low.\""

    herbalist "\"I can only spare enough of one of these for now.\""

    hide herbalist default onlayer portraits with dissolve

    show doctor default at left onlayer portraits with dissolve

    doctor "\"That's alright.\""

    doctor "\"Could you tell me, what are their properties?\""

    hide doctor default onlayer portraits with dissolve

    #TODO: change the bottle's to pouches on ch1 herbalist's store

    "Mr. Kazuki lifts the first pouch."

    show herbalist default at left onlayer portraits with dissolve

    $ junka_root_entry.locked = False

    herbalist "\"This one is {a=glossary:junka_root_entry}Junka Root{/a}, a restorative tonic.\""

    herbalist "\"It promotes blood circulation and helps strengthen the body.\""

    herbalist "\"But it must be taken after eating.\""

    hide herbalist default onlayer portraits with dissolve

    "He sets it down and picks up the second pouch."

    show herbalist default at left onlayer portraits with dissolve

    $ tsuyomi_cap_entry.locked = False

    herbalist "\"This is {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}, it focuses on supporting the body's vitality.\""

    herbalist "\"It can be taken without food.\""
    
    hide herbalist default onlayer portraits with dissolve

    "The doctor studies both herbs in silence."

    show doctor default at left onlayer portraits with dissolve

    if ch02_previous_death == "cat_broke_formula":

        doctor "The cat knocked over the formula last time..."

        doctor "I wasn't even able to try the formula with the herb I chose."

    $ nagomi_root_entry.locked = False
    
    doctor "I know now, {a=glossary:nagomi_root_entry}Nagomi Root{/a} only makes things worse."

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions :

        doctor "I already got the tonic, hoping it could replaced it."

    if ch02_first_herb_with_instructions:

        doctor  "I followed the instructions and made dinner first.."

        doctor "But..."

        doctor "I was too late and Mother died."

        doctor "Maybe eating first is not necessary after all..."

    elif ch02_first_herb_without_instructions:

        doctor "And when I rushed it and gave the formula to Mother without eating..."

        doctor "Maybe eating first is strictly necessary."

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions :

        doctor "I should ask him."

        doctor "\"Mr. Kazuki?\""

        hide doctor default onlayer portraits

        show herbalist default at left onlayer portraits

        herbalist "\"Yes, Mr. Yosuke. Do you have any questions?\""

        hide herbalist default onlayer portraits

        show doctor default at left onlayer portraits

        doctor "\"Yes, actually...\""

        doctor "\"I was wondering, is eating necessary?\""

        doctor "\"Or it can be also taken without?\""

        doctor "\"Any risks I should know?\""

        hide doctor default onlayer portraits

        show herbalist default at left onlayer portraits

        herbalist "\"To be honest, I only know that eating is advised.\""

        herbalist "\"Otherwise, it may upset the stomach.\""

        herbalist "\"I haven’t done much research on this specific herb, so I am not fully aware of other risks.\""

        herbalist "\"You can try without it, but if you ask my opinion you should follow the instructions.\""

        hide herbalist default onlayer portraits with dissolve

    else :

        show doctor default at left onlayer portraits with dissolve

        doctor "Perhaps the tonic could replace it..."

        hide doctor default onlayer portraits with dissolve


    "His gaze shifts to the second pouch."

    show doctor default at left onlayer portraits with dissolve

    if not ch02_used_taeru_happened:

        doctor "Or maybe strengthening her body is exactly what my treatment is missing."

    else :

        doctor "This might prove to be a good alternative for the second phase."

        $ taeru_root_entry.locked = False

        doctor "Replacing {a=glossary:taeru_root_entry}Taeru Root{/a}..."

        doctor "After my failed attempt with it, I should proceed more cautiously."

    if ch02_second_herb_with_instructions or ch02_second_herb_without_instructions:
    
        doctor "Last time I tried Tsuyomi Cap."
        
    if ch02_second_herb_with_instructions:

        doctor "I followed the instructions and didn't let Mother eat first."

        doctor "But..."

        doctor "I waited too long, and by the time the medicine was ready, she could no longer swallow."

        doctor "Maybe taking it on an empty stomach isn't absolutely necessary..."

    elif ch02_second_herb_without_instructions:

        doctor "And when I made dinner for Mother..."

        doctor "The medicine had no effect, and her condition continued to worsen."

        doctor "Maybe taking it on an empty stomach is strictly necessary."

    if ch02_second_herb_with_instructions or ch02_second_herb_without_instructions:

        doctor "I should clarify something before I decide."

        doctor "\"Mr. Kazuki?\""

        hide doctor default onlayer portraits

        show herbalist default at left onlayer portraits

        herbalist "\"Yes, Dr. Yosuke?\""

        hide herbalist default onlayer portraits

        show doctor default at left onlayer portraits

        doctor "\"About the Tsuyomi Cap...\""

        doctor "\"You said it should be taken on an empty stomach.\""

        doctor "\"How important is that?\""

        doctor "\"Would eating beforehand make it dangerous?\""

        hide doctor default onlayer portraits

        show herbalist default at left onlayer portraits

        herbalist "\"I can't say for certain.\""

        herbalist "\"Taking it on an empty stomach is advised because food may interfere with its effects.\""

        herbalist "\"I haven't studied this herb enough to know whether there are other risks.\""

        herbalist "\"If you ask me, I would still follow the instructions.\""

        hide herbalist default onlayer portraits with dissolve


    hide doctor default onlayer portraits with dissolve
    
    scene black with fade

    "He closes his eyes for a moment."

    show doctor default at left onlayer portraits with dissolve

    doctor "Whatever I decide, it will have a level of risk."

    doctor "But time won’t wait for me."

    doctor "I should choose now."

    hide doctor default onlayer portraits with dissolve

    scene bg ch01 herbstore with fade 

    menu : 

        "Take the first":

            jump ch02_take_the_first
        
        "Take the second":

            jump ch02_take_the_second

    return