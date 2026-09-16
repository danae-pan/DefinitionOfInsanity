label ch02_second_herb_without_instructions_ending:

    "The doctor gently squeezes his mother's hand."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I'll prepare something right away.\""

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He leaves the room and makes his way downstairs, heading first to the laboratory."

    scene bg ch01 lab with fade

    "The unfinished decoction is still warm."

    show doctor default at left onlayer portraits with dissolve

    doctor "Thankfully, it still needs a bit of time to be ready."

    doctor "Just enough time to prepare the meal."

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He heads to the kitchen."

    scene bg ch01 kitchen with fade

    "The cupboards are nearly empty."

    "He gathers the last of the rice and a handful of vegetables, placing them into a small pot."

    "As the meal cooks, his eyes repeatedly drift toward the laboratory."

    "Then toward the staircase."

    show doctor default at left onlayer portraits with dissolve

    doctor "Just a little longer."

    doctor "Everything will be ready soon."

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "When the food is finally prepared, he carries the tray upstairs."

    scene bg ch01 mother with fade

    "His mother struggles to sit upright."

    "He patiently supports her back, feeding her one small spoonful at a time."

    "Each swallow is slow and painful."

    "She coughs between bites, but eventually manages to finish the meal."

    "The doctor offers her water."

    "She drinks only a few small sips before exhaustion overtakes her."

    "Her breathing seems calmer now."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"You should rest.\""

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "She closes her eyes."

    "The doctor quietly returns to the laboratory."

    scene bg ch01 lab with fade

    "The decoction has finally reached the proper consistency."

    "He filters the herbs, carefully pours the medicine into a glass bottle, and seals it."

    scene black with fade

    "Without wasting another moment, he rushes back upstairs."

    scene bg ch01 mother with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I've finished it.\""

    hide doctor default onlayer portraits

    "He gently helps his mother drink the medicine."

    "Then he sits beside her bed, notebook in hand."

    "Watching."

    "Waiting."

    "Minutes pass."

    "He checks her pulse."

    "Still steady."

    "Her eyelids begin to droop."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\""

    hide doctor default onlayer portraits with dissolve

    "She doesn't answer."

    "He gently shakes her shoulder."

    "Nothing."

    "Her breathing grows slower."

    "She slips into an unnatural sleep."

    "The doctor reaches for her wrist once more."

    "The pulse is weaker now."

    "His heart begins to race."

    "The herbalist's warning echoes in his mind."

    show doctor default at left onlayer portraits with dissolve

    doctor "This herb should not be used after eating."

    hide doctor default onlayer portraits with dissolve

    if ch02_second_herb_with_instructions:

        doctor "But.."

        doctor "..when I did follow the instructions I was still not able to save her."

    "He checks her pupils."

    "Calls her name."

    "Attempts to wake her."

    "Nothing."

    "The medicine has no visible effect."

    "Instead, her condition continues to worsen."

    $ coma_entry.locked = False

    "The {a=glossary:coma_entry}coma{/a} deepens."

    "Minutes stretch into hours."

    "The room grows quieter."

    "Her breathing becomes slower until she reaches her last breath."

    "The doctor remains frozen beside the bed."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I wanted to ease your pain…\""

    hide doctor default onlayer portraits with dissolve

    "He takes her hand one last time."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Instead...\""

    doctor "\"...I took away your chance to recover again.\""

    hide doctor default onlayer portraits with dissolve

    "He slowly pulls the bedsheet over his mother's face."

    show doctor default at left onlayer portraits with dissolve

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "His legs carry him back to the laboratory almost on their own."

    scene bg ch01 lab with fade

    "The books remain open exactly where he had left them."

    "He sits heavily at the workbench."

    "He turns another page."

    "He reads the instructions again."

    "Searching for something he had overlooked."

    show doctor default at left onlayer portraits with dissolve

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken without eating…"

    hide doctor default onlayer portraits with dissolve

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    scene black with fade

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_second_herb_without_instructions = True

    $ ch02_previous_death = "second_herb_without_instructions"

    jump ch02_new_loop