label ch02_second_herb_with_instructions_ending:

    "He gently squeezes her hand."

    show doctor default at left onlayer portraits

    doctor "\"I know you need to eat mother\""

    doctor "\"But the herbalist was very clear.\""

    doctor "\"This medicine must not be taken after eating.\""

    hide doctor default onlayer portraits

    if ch02_second_herb_without_instructions:

        "Not to mention I already risked it and gave her a meal before.."

        "..and it costed her life."

    "She closes her eyes."

    "The doctor reaches for the glass of water beside the bed."

    "He carefully wets her lips with a damp cloth."
    
    show doctor default at left onlayer portraits
    
    doctor "\"Just a little longer.\""

    doctor "\"I'll finish the medicine first.\""

    hide doctor default onlayer portraits

    "He slowly stands."

    "For a moment, he hesitates at the bedroom door."

    "His mother looks impossibly frail beneath the blanket."

    show doctor default at left onlayer portraits

    doctor "\"...Forgive me.\""

    hide doctor default onlayer portraits

    "He quietly leaves the room and heads to the labatory."

    "He carefully stirs the mixture, watching the herbs release their final colour into the liquid."

    "Every few moments he glances toward the staircase."

    show doctor default at left onlayer portraits

    doctor "\"Almost there..\""

    hide doctor default onlayer portraits

    "He filters the herbs through a fine cloth before pouring the finished medicine into a bottle."

    "He seals it immediately."

    "Without wasting another second, he rushes upstairs."

    show doctor default at left onlayer portraits

    doctor "\"Mother...\""

    hide doctor default onlayer portraits

    "There is no reply."

    "He hurries to the bedside."

    "His mother lies motionless."

    "Her mouth is slightly open."

    "She struggles weakly to breathe."

    "The doctor quickly kneels beside her."

    "He lifts her head."
    
    show doctor default at left onlayer portraits

    doctor "\"I've finished it.\""

    doctor "\"You can drink now.\""

    hide doctor default onlayer portraits

    "He gently raises the bottle to her lips."

    "The medicine spills from the corner of her mouth."

    "She can no longer swallow."

    show doctor default at left onlayer portraits

    doctor "\"...No.\""

    hide doctor default onlayer portraits

    "He tries again."

    "Nothing."

    "Her throat no longer responds."

    "Her breathing becomes increasingly irregular."

    "The doctor checks her pulse."

    "Weak."

    show doctor default at left onlayer portraits

    doctor "\"Mother!\""

    hide doctor default onlayer portraits

    "Her chest rises just once."

    "Then stops."

    "The doctor remains frozen."

    "The bottle slips from his hand and rolls across the wooden floor."

    "He slowly lowers his mother's head back onto the pillow."

    doctor "I waited too long.."

    if ch02_second_herb_without_instructions:

        doctor "Turns out even if I decide to follow the instructions I still fail.."

        doctor "Just like before.."

    "He gently closes her eyes."

    "The room slowly falls silent."

    "He slowly pulls the bedsheet over his mother's face."

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    "His legs carry him back to the laboratory almost on their own."

    "The books remain open exactly where he had left them."

    "He sits heavily at the workbench."

    "He turns another page."

    "He reads the instructions again."

    "Searching for something he had overlooked."

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken without eating…"

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_second_herb_with_instructions = True

    jump ch02_start