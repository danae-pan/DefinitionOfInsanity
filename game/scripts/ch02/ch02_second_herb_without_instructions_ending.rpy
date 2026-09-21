label ch02_second_herb_without_instructions_ending:

    "The doctor gently squeezes his Mother's hand."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I'll prepare something right away.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    #SOUND

    play sound "audio/sfx/footsteps.mp3"
    
    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    "He leaves the room and makes his way downstairs, heading first to the laboratory."

    scene bg ch01 lab_no_cat with fade

    "The unfinished decoction is still warm."

    show doctor default at left onlayer portraits with dissolve

    doctor "Thankfully, it still needs a bit of time to be ready."

    doctor "Just enough time to prepare the meal."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "He heads to the kitchen."

    scene bg ch01 kitchen with fade

    "The cupboards are nearly empty."

    "He gathers the last of the rice and a handful of vegetables, placing them into a small pot."

    #SOUND

    play sound "audio/sfx/water_boil.mp3"

    "As the meal cooks, his eyes repeatedly drift toward the laboratory."

    "Then toward the staircase."

    show doctor worried at left onlayer portraits with dissolve

    doctor "Just a little longer."

    doctor "Everything will be ready soon."

    hide doctor onlayer portraits with dissolve

    scene black with fade

    "When the food is finally prepared, he carries the tray upstairs."

    show mother sick with dissolve

    "His Mother struggles to sit upright."

    "He patiently supports her back, feeding her one small spoonful at a time."

    #SOUND

    play sound "audio/sfx/mother_pain.mp3"

    "Each swallow is slow and painful."

    show mother sick with dissolve 
     
    #SOUND

    play sound "audio/sfx/mother_cough.mp3"

    "She coughs between bites, but eventually manages to finish the meal."

    "The doctor offers her water."

    "She drinks only a few small sips before exhaustion overtakes her."

    #SOUND

    play sound "audio/sfx/mother_breathe.mp3" volume 0.5

    pause 1.0

    play sound "audio/sfx/mother_breathe.mp3" volume 0.5

    "Her breathing seems calmer now."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"You should rest.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    show mother default with dissolve

    "She closes her eyes."

    "The doctor quietly returns to the laboratory."

    scene bg ch01 lab_no_cat with fade

    "The decoction has finally reached the proper consistency."

    #SOUND

    play sound "audio/sfx/filling_glass.mp3"

    "He filters the herbs, carefully pours the medicine into a glass bottle, and seals it."

    scene black with fade

    "Without wasting another moment, he rushes back upstairs."

    #SOUND

    play sound "audio/sfx/run.mp3"
    
    pause 0.8

    play sound "audio/sfx/run.mp3"

    pause 0.8

    play sound "audio/sfx/run.mp3"

    show mother sick with dissolve

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I've finished it.\""

    hide doctor onlayer portraits

    "He gently helps his Mother drink the medicine."

    "Then he sits beside her bed, notebook in hand."

    "Watching."

    "Waiting."

    "Minutes pass."

    "He checks her pulse."

    "Still steady."

    show mother default with dissolve

    "Her eyelids begin to droop."

    show doctor worried at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Gasp.mp3"

    doctor "\"Mother?\""

    hide doctor onlayer portraits with dissolve

    "She doesn't answer."

    "He gently shakes her shoulder."

    "Nothing."

    #SOUND

    play sound "audio/sfx/mother_breathe.mp3" volume 0.6

    pause 1.4

    play sound "audio/sfx/mother_breathe.mp3" volume 0.5

    pause 1.6

    play sound "audio/sfx/mother_breathe.mp3" volume 0.4

    "Her breathing grows slower."

    #SOUND

    play sound "audio/sfx/suspence.mp3"

    "She slips into an unnatural sleep."

    "The doctor reaches for her wrist once more."

    "The pulse is weaker now."

    "His heart begins to race."

    "The herbalist's warning echoes in his mind."

    show doctor worried at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/breathe_male.mp3" 

    doctor "This herb should not be used after eating."

    if ch02_second_herb_with_instructions:

        show doctor panicked at left onlayer portraits with dissolve 
         
        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "But.."

        doctor "..when I did follow the instructions I was still not able to save her."

    hide doctor onlayer portraits with dissolve

    "He checks her pupils."

    "Calls her name."

    "Attempts to wake her."

    "Nothing."

    "The medicine has no visible effect."

    "Instead, her condition continues to worsen."

    $ coma_entry.locked = False

    #SOUND

    play sound "audio/sfx/heavy_suspence.mp3"

    "The {a=glossary:coma_entry}coma{/a} deepens."

    "Minutes stretch into hours."

    "The room grows quieter."

    "Her breathing becomes slower until she reaches her last breath."

    "The doctor remains frozen beside the bed."

    show doctor worried at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "\"I wanted to ease your pain…\""

    hide doctor onlayer portraits with dissolve

    "He takes her hand one last time."

    show doctor panicked at left onlayer portraits with dissolve

    doctor "\"Instead...\""

    #SOUND

    play sound "audio/sfx/Sigh.mp3"

    doctor "\"...I took away your chance to recover again.\""

    hide doctor onlayer portraits with dissolve

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

    $ ch02_second_herb_without_instructions = True

    $ ch02_previous_death = "second_herb_without_instructions"

    jump ch02_new_loop