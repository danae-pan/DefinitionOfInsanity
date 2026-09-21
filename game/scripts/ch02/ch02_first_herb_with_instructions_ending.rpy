label ch02_first_herb_with_instructions_ending:

    if ch02_first_herb_without_instructions :

        show doctor default at left onlayer portraits with dissolve

        doctor "Last time, I didn’t make dinner."

        doctor "In result.."

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "..I lost mother again."

        doctor "The herbalist wasn’t sure about the risks…"

        doctor "But better be safe than sorry."

        show doctor default at left onlayer portraits with dissolve

        doctor "If I'm going to trust his herbs..."

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "Then I must trust his instructions as well."

        hide doctor onlayer portraits with dissolve

    "He carefully places the bottle back on the workbench before making his way into the kitchen."

    scene bg ch01 kitchen with fade

    "The cupboards are almost empty."

    "He gathers what little rice and vegetables remain and places a pot over the fire."

    #TODO: add kitchen sound and filling bottle 

    #SOUND

    play sound "audio/sfx/water_boil.mp3"

    "As the water slowly begins to boil, he glances toward the staircase."

    show doctor default at left onlayer portraits with dissolve

    doctor "Just a little longer..."

    doctor "\"Please hold on.\""

    hide doctor onlayer portraits with dissolve

    "The minutes pass agonizingly slowly."

    "Finally, he removes the pot from the fire and places the meal onto a tray."

    "Beside it, he carefully sets the bottle."

    show doctor smile at left onlayer portraits with dissolve

    doctor "\"Everything is ready.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    #SOUND

    play sound "audio/sfx/run.mp3"
    
    pause 0.8

    play sound "audio/sfx/run.mp3"

    pause 0.8

    play sound "audio/sfx/run.mp3"

    "He hurries upstairs."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\""

    hide doctor onlayer portraits with dissolve

    "No answer."

    #SOUND

    play sound "audio/sfx/run.mp3"
    
    pause 0.8

    play sound "audio/sfx/run.mp3"

    pause 0.8

    play sound "audio/sfx/run.mp3"

    pause 0.6

    play sound "audio/sfx/open_door.mp3"

    "He quickens his pace and pushes open the bedroom door."

    show mother default with dissolve

    "The room is silent."

    "His Mother lies motionless in bed, exactly as he had left her."

    "The tray slips from his hands."

    #SOUND

    play sound "audio/sfx/bottle_trash.mp3"

    play sound "audio/sfx/noise.mp3"
    
    "The bowl shatters across the wooden floor."

    "Rice scatters across the room."

    show doctor worried at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Gasp.mp3"

    doctor "\"No...\""

    hide doctor onlayer portraits with dissolve

    "He rushes to her bedside."

    "His fingers search desperately for a pulse."

    "Nothing."

    "He leans close, hoping to hear even the faintest breath."

    "Nothing."

    "He gently shakes her shoulder."

    show doctor panicked at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Socked.mp3"

    doctor "\"Mother...\""

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "\"Please...\""

    hide doctor onlayer portraits with dissolve

    "No response."

    "The damage had progressed beyond recovery."

    #SOUND

    play sound "audio/sfx/heavy_suspence.mp3"

    "Her body had simply given out before he could begin the treatment."

    "The doctor remains kneeling beside the bed, unable to move."

    "His eyes drift toward the untouched meal and the unopened bottle of medicine lying among the broken pieces of porcelain."

    show doctor worried at left onlayer portraits with dissolve
    
    doctor "I followed the instructions…"

    hide doctor onlayer portraits with dissolve

    "His voice barely rises above a whisper."

    show doctor panicked at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/Sigh.mp3" volume 0.5

    doctor "\"...I was only trying to do it properly.\""

    hide doctor onlayer portraits with dissolve

    "He slowly pulls the bedsheet over his Mother's face."

    "He kneels there a while longer before gathering the broken pieces of the bowl from the floor."

    show doctor worried at left onlayer portraits with dissolve

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    doctor "If I do..I should make sure to cook dinner early in the morning."

    doctor "That way, I won’t lose time during the day."

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

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken after eating…"

    hide doctor onlayer portraits with dissolve

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    scene black with fade

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_first_herb_with_instructions = True

    $ ch02_previous_death = "first_herb_with_instructions"

    jump ch02_new_loop