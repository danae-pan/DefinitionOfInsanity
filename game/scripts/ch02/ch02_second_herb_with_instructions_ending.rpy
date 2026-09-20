label ch02_second_herb_with_instructions_ending:

    "He gently squeezes her hand."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"I know you need to eat Mother\""

    doctor "\"But the herbalist was very clear.\""

    doctor "\"This medicine must not be taken after eating.\""

    if ch02_second_herb_without_instructions:

        doctor "Not to mention I already risked it and gave her a meal before.."

        doctor "..and it costed her life."

    hide doctor onlayer portraits with dissolve

    show mother default with dissolve

    "She closes her eyes."

    "The doctor reaches for the glass of water beside the bed."

    "He carefully wets her lips with a damp cloth."
    
    show doctor worried at left onlayer portraits with dissolve
    
    doctor "\"Just a little longer.\""

    doctor "\"I'll finish the medicine first.\""

    hide doctor onlayer portraits with dissolve

    "He slowly stands."

    "For a moment, he hesitates at the bedroom door."

    "His Mother looks impossibly frail beneath the blanket."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"...Forgive me.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He quietly leaves the room and heads to the labatory."

    scene bg ch01 lab_no_cat with fade

    "He carefully stirs the mixture, watching the herbs release their final colour into the liquid."

    "Every few moments he glances toward the staircase."

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Almost there..\""

    hide doctor onlayer portraits with dissolve

    "He filters the herbs through a fine cloth before pouring the finished medicine into a bottle."

    "He seals it immediately."

    scene black with fade

    "Without wasting another second, he rushes upstairs."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    hide doctor onlayer portraits with dissolve

    "There is no reply."

    scene bg ch01 mother with fade

    "He hurries to the bedside."

    "His Mother lies motionless."

    "Her mouth is slightly open."

    show mother sick with dissolve 
    with vpunch

    "She struggles weakly to breathe."

    "The doctor quickly kneels beside her."

    "He lifts her head."
    
    show doctor worried at left onlayer portraits with dissolve 
    with vpunch

    doctor "\"I've finished it.\""

    doctor "\"You can drink now.\""

    hide doctor onlayer portraits with dissolve

    "He gently raises the bottle to her lips."

    "The medicine spills from the corner of her mouth."

    "She can no longer swallow."

    show doctor worried at left onlayer portraits with dissolve 
    with vpunch

    if knows_dysphagia:

        $ dysphagia_entry.locked = False

        doctor "Her {a=glossary:dysphagia_entry}dysphagia{/a}..."

        doctor "It's gotten worse."

    doctor "\"...No.\""

    hide doctor onlayer portraits with dissolve

    "He tries again."

    "Nothing."

    "Her throat no longer responds."

    "Her breathing becomes increasingly irregular."

    "The doctor checks her pulse."

    "Weak."

    show doctor panicked at left onlayer portraits with dissolve 
    with vpunch

    doctor "\"Mother!\""

    hide doctor onlayer portraits with dissolve

    "Her chest rises just once."

    show mother default with dissolve

    "Then stops."

    "The doctor remains frozen."

    "The bottle slips from his hand and rolls across the wooden floor."

    "He slowly lowers his Mother's head back onto the pillow."

    show doctor panicked at left onlayer portraits with dissolve

    doctor "I waited too long.."

    doctor "I followed the instructions..."

    doctor "But none of that matters if I can't finish the treatment in time."

    if ch02_second_herb_without_instructions:

        doctor "Turns out even if I decide to follow the instructions I still fail.."

        doctor "Just like before.."

    hide doctor onlayer portraits with dissolve

    "The room slowly falls silent."

    "He slowly pulls the bedsheet over his Mother's face."

    show doctor worried at left onlayer portraits with dissolve

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "His legs carry him back to the laboratory almost on their own."

    scene bg ch01 lab_no_cat with fade

    "The books remain open exactly where he had left them."

    "He sits heavily at the workbench."

    "He turns another page."

    "He reads the instructions again."

    "Searching for something he had overlooked."

    show doctor worried at left onlayer portraits with dissolve

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken without eating…"

    hide doctor onlayer portraits with dissolve

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    scene black with fade

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_second_herb_with_instructions = True

    $ ch02_previous_death = "second_herb_with_instructions"

    jump ch02_new_loop