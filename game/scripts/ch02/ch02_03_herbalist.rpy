label ch02_go_to_herbalist :

    if ch02_second_visit_hospital == True:

        "The doctors leaves the hospital in a rush and heads to the herbalist’s shop."

        "After 20 minutes walk, he reaches the central square."

    else :

        "The doctor puts on his coat and leaves the house."

    if herbalist_visited :

        "I know now where to find the herbalist."

        "It is only 30 minutes walk, I better hurry."

        "He finally arrives at the small wooden shop."

    else :

        "It shouldn't be difficult to find the herbalist's shop."

        "He mentioned it was somewhere in the center of town."

        "If not... I can always ask someone."

    "After a 30 minutes walk, he reaches the central square."

    "His eyes scan the buildings one by one."

    "Then he spots it."

    "A small wooden shop with bundles of dried herbs hanging above the entrance"

    doctor "This must be it."

    scene bg ch01 herbstore with fade 

    "He steps inside."

    "The room is filled with the scent of dried plants and medicinal roots."

    "There is no one at the counter."

    "The doctor looks around."

    show doctor default at left onlayer portraits

    doctor "Hello? Is anyone here?"

    hide doctor default onlayer portraits

    "A voice calls from the back of the shop."

    herbalist "Just a moment! I'll be right there!"

    "After a few seconds, the herbalist appears, struggling to balance several glass jars and wooden boxes in his arms."

    herbalist "Oh! Good morning!"

    "He carefully places everything on the counter before smiling warmly."

    herbalist "What can I do for you today?"

    "The doctor hesitates."

    doctor "Right..."

    doctor "Yesterday never happened."

    doctor "To him, we've never met."

    "He clears his throat"

    show doctor default at left onlayer portraits

    doctor "Good morning. I'm Dr. (Name)."

    # TODO : If the doctor knows where the herb place is then he has already met the herbalist

    doctor "My mother has fallen ill after eating contaminated fish. Some colleagues at the hospital mentioned that you have herbal remedies that may help."

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "Ah, yes... yes, of course."

    hide herbalist default onlayer portraits

    "The herbalist begins searching through the clutter covering his workbench."

    show herbalist default at left onlayer portraits

    herbalist "Now where did I put them..."

    herbalist "Forgive the mess."

    herbalist "Ever since all these people started getting sick, I barely have enough time to organize the shop before another customer arrives."

    hide herbalist default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "Now where did I put them..."

    herbalist "Forgive the mess."

    herbalist "Ever since all these people started getting sick, I barely have enough time to organize the shop before another customer arrives."

    hide herbalist default onlayer portraits

    "He continues rummaging through jars and bundles of herbs."

    show herbalist default at left onlayer portraits

    herbalist "While I'm looking..."

    herbalist "How is your mother doing?"

    hide herbalist default onlayer portraits

    "The doctor's expression darkens."

    show doctor default at left onlayer portraits

    doctor "Not well."

    doctor "She was exposed for many years."

    doctor "I managed to ease some of her symptoms whenever I came home from the city..."

    doctor "...but that was before anyone knew contaminated fish was the cause."

    doctor "If I had known earlier..."

    doctor "...I could have changed her diet."

    doctor "...Maybe things would have been different."

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "I've heard about you."

    herbalist "You left for the city around 1930 to study medicine, didn't you?"

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "Yes."

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "Then perhaps fate was kinder to you than you realize."

    herbalist "You weren't here to eat the poisoned fish."

    herbalist "Now you've returned with the knowledge to help those who remained."

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "Perhaps..."

    doctor "But knowledge means very little when you cannot save your own family."

    doctor "My mother is all I have."

    hide doctor default onlayer portraits

    "The herbalist smiles gently."

    show herbalist default at left onlayer portraits

    herbalist "You cannot ask more of yourself than to do everything within your power."

    herbalist "Remember that."

    hide herbalist default onlayer portraits

    "He suddenly reaches beneath a shelf."

    show herbalist default at left onlayer portraits

    herbalist "Ah!"

    herbalist "Here they are."

    hide herbalist default onlayer portraits

    "He places two small containers on the counter."

    show herbalist default at left onlayer portraits

    herbalist "Unfortunately, my stock is running low."

    herbalist "I can only spare enough of one of these for now."

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "That's alright."

    doctor "Could you tell me, what are their properties?"

    hide doctor default onlayer portraits

    "The herbalist lifts the first pouch."

    show herbalist default at left onlayer portraits

    herbalist "This one is {a=glossary:junka_root_entry}Junka Root{/a}, a restorative tonic."

    herbalist "It promotes blood circulation and helps strengthen the body."

    herbalist "But it must be taken after eating."

    hide herbalist default onlayer portraits

    "He sets it down and picks up the second pouch."

    show herbalist default at left onlayer portraits

    herbalist "This is {a=glossary:tsuyomi_cap_entry}Tsuyomi Cap{/a}, it focuses on supporting the body's vitality."

    herbalist "It can be taken without food."
    
    hide herbalist default onlayer portraits

    "The doctor studies both herbs in silence."

    doctor "I know now, {a=glossary:nagomi_root_entry}Nagomi Root{/a} only makes things worse."

    if ch02_first_herb_with_instructions:

            doctor "Last time I got the tonic, hoping it could replaced it."

            doctor  "I followed the instructions and made dinner first.."

            doctor "But..."

            doctor "I was too late and Mother died."

            doctor "Maybe eating first is not necessary."

    elif ch02_first_herb_without_instructions:

            doctor "Last time I got the tonic, hoping it could replaced it."

            doctor "But I didn’t follow the instructions."

            doctor "I rushed it and gave the formula to Mother without eating."

            doctor "Maybe eating first is strictly necessary."

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions :

            doctor " I should ask him."

            show doctor default at left onlayer portraits

            doctor "Mr. Herbalist?"

            hide doctor default onlayer portraits

            show herbalist default at left onlayer portraits

            herbalist "Yes, doctor. Do you have any questions?"

            hide herbalist default onlayer portraits

            show doctor default at left onlayer portraits

            doctor "Yes, actually…"

            doctor "I was wondering, is eating necessary?"

            doctor "Or it can be also taken without?"

            doctor "Any risks I should know?"

            hide doctor default onlayer portraits

            show herbalist default at left onlayer portraits

            herbalist "To be honest, I only know that eating is advised."

            herbalist "Otherwise, it may upset the stomach."

            herbalist "I haven’t done much research on this specific herb, so I am not fully aware of other risks."

            herbalist "You can try without it, but if you ask my opinion you should follow the instructions."

            hide herbalist default onlayer portraits

    else :

            doctor "Perhaps the tonic could replace it..."

    "His gaze shifts to the second pouch."

    if not ch02_use_panax :

        doctor "Or maybe strengthening her body is exactly what my treatment is missing."

    else :

        doctor "This might prove to be a good alternative for the second phase."

        doctor "After my failed attempt with {a=glossary:taeru_root_entry}Taeru Root{/a}, I should proceed more cautiously."

    "He closes his eyes for a moment."

    doctor "Whatever I decide, it will have a level of risk."

    doctor "But time won’t wait for me."

    doctor "I should choose now."

    menu : 

        "Take the first":

            jump ch02_take_the_first
        
        "Take the second":

            jump ch02_take_the_second

    return