label ch02_used_taeru_ending:

    scene black with fade

    "The doctor picks up the bottle and hurries to his Mother's bedside."

    scene bg ch01 mother with fade

    "She smiles weakly as he enters, struggling to form a sentence."

    mother "My son..."

    show doctor default at left onlayer portraits with dissolve

    doctor "Don't speak Mother. I've prepared something for you."

    hide doctor default onlayer portraits with dissolve

    "He carefully helps her sit upright and supports the bottle with trembling hands."

    "She drinks every drop without complaint."

    "For several minutes... nothing happens."

    "The doctor begins writing observations."

    show doctor default at left onlayer portraits with dissolve

    doctor "Pulse... unchanged."

    doctor "Breathing... steady."

    hide doctor default onlayer portraits with dissolve

    "A sudden gasp interrupts his notes."

    "His Mother presses a hand against her head."

    "Her breathing becomes rapid."

    "She grips the bedsheets tightly."

    "Blood begins to run from one nostril."

    show doctor default at left onlayer portraits with dissolve

    doctor "No... that's impossible..."

    hide doctor default onlayer portraits with dissolve

    "She suddenly collapses back onto the pillow."

    "One side of her face becomes motionless."

    "The doctor checks her pulse with shaking fingers."

    "It is racing."

    "Then..."

    "Nothing."

    "Silence fills the room."

    $ brain_hemorrhage_entry.locked = False

    "The stimulation from the experimental formula triggered a sudden rise in blood pressure, causing a massive {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}."

    "The doctor slowly lowers his Mother's hand onto the bed."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"...I did this.\""

    hide doctor default onlayer portraits with dissolve

    "His hands still tremble from checking her pulse, though he already knows there is nothing left to find."

    "He slowly pulls the blanket over her face."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"That can't be...\""

    doctor "\"The reports mentioned changes in blood pressure, but they were supposed to be uncommon.\""

    hide doctor default onlayer portraits with dissolve

    "He lowers his head."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"...I knew there was a risk.\""

    doctor "\"...and I took it anyway.\""

    hide doctor default onlayer portraits with dissolve

    "He leaves his Mother's room, heading toward the laboratory."

    scene bg ch01 lab with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I made a mistake.\""

    hide doctor default onlayer portraits with dissolve

    "He sinks into his chair before staring silently at the open manuscript."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I need to understand what I failed to see.\""

    hide doctor default onlayer portraits with dissolve

    "His eyes wander across the scattered pages."

    "Was the dosage too high?"

    "Had her condition deteriorated further than he realized?"

    "If he could understand where he went wrong..."

    "...perhaps he could at least prevent another needless death."

    if ch02_knows_cat_is_sick:

        "He remembers the cat."

        "It had shown the same tremors."

        "The same loss of balance."

        "The same weakness."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"If I can not save Mother...\""

        hide doctor default onlayer portraits with dissolve

        "He swallows."

        show doctor default at left onlayer portraits with dissolve

        doctor "\"...perhaps I can still save you.\""

        hide doctor default onlayer portraits with dissolve

    "Another thought crosses his mind."

    show doctor default at left onlayer portraits with dissolve

    doctor "Perhaps tomorrow I will be given another chance."

    doctor "\"If Mother wakes once more, I cannot repeat today's mistake.\""

    hide doctor default onlayer portraits with dissolve

    "Unable to bear the silence of the house any longer, he buries himself in books."
    
    "An attempt to escape the weight of what he has done."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Please...\""

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "His eyes become heavy."

    "He finally falls asleep at the workbench."

    $ ch02_used_taeru_happened = True
    $ ch02_previous_death = "used_taeru"

    jump ch02_new_loop
