label ch02_cardiac_arrest_ending:

    show doctor default at left onlayer portraits with dissolve

    doctor "Just a few minutes."

    hide doctor onlayer portraits with dissolve

    scene bg ch01 kitchen with fade

    "He heads to the kitchen, fills a small bowl with food and kneels beside the cat."

    "She eagerly begins eating while he gently strokes her back."

    "For the first time in days, the room feels almost peaceful."

    "A loud crash echoes from upstairs."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"...Mother?\""

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He sprints toward her room."

    show mother sick with dissolve 
    with vpunch

    "The bedroom door is half open."

    "His Mother is in bed, her entire body shaking violently."

    "Her arms and legs jerk uncontrollably."

    "Foam gathers at the corner of her mouth."

    show doctor panicked at left onlayer portraits with dissolve 
    with vpunch

    doctor "\"Mother! Stay with me!\""

    hide doctor onlayer portraits with dissolve

    "He kneels beside her, trying desperately to hold her still."

    "The convulsions suddenly stop."

    "For a brief moment..."

    "He believes it is over."

    "Then he reaches for her wrist."

    "No pulse."

    $ cardiac_arrest_entry.locked = False

    show mother default with dissolve

    "The seizure had placed too much strain on her heart, leading to {a=glossary:cardiac_arrest_entry}cardiac arrest{/a} before he could intervene."

    "The untouched bottle of medicine still waits downstairs."

    show doctor worried at left onlayer portraits with dissolve

    doctor "I only looked away for a moment..."

    hide doctor onlayer portraits with dissolve

    "The doctor kneels beside his Mother's bed for what feels like hours."

    "Eventually, he rises."

    "He cannot bring himself to look at her."

    "Every glance at the room reminds him that he chose to spend those precious minutes elsewhere."

    "His eyes meet the cat's."

    "The animal quietly watches him from the doorway."

    "Even its presence fills him with guilt."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"I should have been with her...\""

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    doctor "I have to do something to occupy myself…"

    doctor "...for this night to end quickly."

    hide doctor onlayer portraits with dissolve

    scene bg game_main with fade

    "He grabs his coat, heading to the hospital."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"If I stay here... I'll lose my mind.\""

    hide doctor onlayer portraits with dissolve

    scene bg ch01 hospital with fade

    "The hospital is as busy as ever."

    "Patients continue to arrive."

    "Children cry."

    "Nurses call for assistance."

    "The doctor throws himself into his work."

    "Each patient keeps his mind occupied for only a few moments before the image of his Mother returns."

    show doctor default at left onlayer portraits with dissolve

    doctor "I just hope tomorrow I will find her in bed alive again."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "Hours pass before exhaustion finally forces him home."

    "The house is silent."

    show mother default with dissolve

    "He slowly opens the door to his Mother's room."

    "Nothing has changed yet."

    "She still lies exactly where he left her, covered by the bedsheet."

    "He stands in the doorway."

    "Unable to move."

    show doctor default at left onlayer portraits with dissolve

    doctor "I should go to sleep."

    doctor "Soon, I will know whether I get another chance."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He quietly closes the door."

    "It will have to wait until tomorrow."

    "He walks to his own room and collapses onto the bed, too physically and emotionally exhausted to think."

    "A moment later, the cat jumps onto the mattress and curls up beside him."

    "He strokes her head."

    "A faint smile crosses his face, disappearing almost as quickly as it came."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"At least...\""

    doctor "\"...I'm not completely alone.\""

    hide doctor onlayer portraits with dissolve

    $ ch02_previous_death = "cardiac_arrest"

    jump ch02_new_loop