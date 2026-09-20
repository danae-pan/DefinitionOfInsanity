label ch02_cat_broke_formula_ending :

    "The doctor looks down at the hungry cat."

    "It meows again, rubbing itself against his leg."

    "He closes his eyes for a brief moment."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"No...\""

    #TODO: check on the formuula mentioned

    doctor "Every minute I spend away from the formula is another minute Mother has to wait."

    hide doctor onlayer portraits with dissolve

    "He gently nudges the cat aside with his foot."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"You'll have to wait a little longer.\""

    hide doctor onlayer portraits with dissolve

    "The cat lets out another desperate cry."

    "The doctor turns back to the workbench."

    "The decoction is reaching the final stage."

    show doctor worried at left onlayer portraits with dissolve
    
    doctor "\"Just a little longer...\""

    hide doctor onlayer portraits with dissolve

    "The proportions have to be perfect."

    "The cat continues meowing behind him."

    "Louder."

    "More insistently."

    "The doctor ignores it."

    "He reaches for a clean bottle."

    "Drop by drop, the dark liquid begins to collect inside."

    show doctor smile at left onlayer portraits with dissolve
    
    doctor "\"Almost finished...\""

    hide doctor onlayer portraits with dissolve

    "A sudden thud echoes through the laboratory."

    scene bg ch01 lab with fade

    "Before he has time to react the cat leaps onto the workbench."

    "The doctor reaches out."

    show doctor worried at left onlayer portraits with dissolve with vpunch

    doctor "\"Wait!\""

    hide doctor onlayer portraits with dissolve

    "Too late."

    "The ceramic bowl tips over."

    "The bottle tumbles from the edge of the table."

    "It shatters against the wooden floor."

    "Dark liquid spreads across the room."

    "The doctor freezes."

    show doctor panicked at left onlayer portraits with dissolve with vpunch

    doctor "\"No...\""

    if kept_cat_in_lab_once:

        doctor "I can't believe she made a mess again..."

        doctor "I knew this happened before."

        doctor "So why I wasn't more careful?"

    hide doctor onlayer portraits with dissolve

    scene bg ch01 lab_no_cat with fade

    "He immediately drops to his knees."

    "He desperately tries to scoop the spilled medicine back into the broken bottle."

    "But the decoction has already soaked into the wooden floor."

    "The formula is ruined."

    "He slowly looks toward the shelf."

    "The wooden box that once held the last of the Hogo Root sits open."

    "Empty."

    "The pouch of Junka Root from the herbalist is empty as well."

    "There is nothing left."

    show doctor panicked at left onlayer portraits with dissolve with vpunch

    doctor "\"No...\""

    doctor "I don't have enough herbs to prepare another."

    hide doctor onlayer portraits with dissolve

    "The laboratory falls silent."

    "Only the sound of the cat quietly meowing remains."

    "The doctor gathers the broken pieces of the bottle."

    "There is nothing left to do."

    scene black with fade

    "He slowly stands and walks upstairs."

    "He enters his Mother's room."

    show mother default with dissolve

    "She is still awake."

    show mother smile with dissolve

    "She smiles faintly as he enters."

    "He forces a smile."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I'm here.\""

    hide doctor onlayer portraits with dissolve

    "He pulls a chair beside her bed and takes her hand in his."

    "The medicine will never be finished."

    "So he stays with her."

    "Holding her hand as the hours pass."

    "Eventually her breathing grows weaker."

    "Then slower."

    "Until, at last..."

    show mother default with dissolve

    "It stops."

    $ respiratory_failure_entry.locked = False

    "She dies from {a=glossary:respiratory_failure_entry}respiratory failure{/a}."

    "The doctor remains seated beside her long after the room has fallen silent."

    "Still holding her hand."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"...I couldn't save you.\""

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    hide doctor onlayer portraits with dissolve

    $ kept_cat_in_lab_once = True

    $ ch02_previous_death = "cat_broke_formula"

    jump ch02_new_loop