label ch02_mother_cant_swallow_ending :

    "He turns back to the workbench."

    "He continues stirring the mixture, watching the colour deepen with each passing moment."

    show doctor default at left onlayer portraits with dissolve

    doctor "If I interrupt the preparation now I'll only lose more time."

    doctor "\"Almost there.\""

    hide doctor onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/filling_glass.mp3"

    "The doctor filters the herbs through a fine cloth before pouring the finished medicine into a bottle."

    "He seals it carefully."

    show doctor smile at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/breathe_male.mp3"

    doctor "\"Finally.\""

    hide doctor onlayer portraits with dissolve

    scene black with fade

    #SOUND

    play sound "audio/sfx/run.mp3"
    
    pause 0.8

    play sound "audio/sfx/run.mp3"

    pause 0.8

    play sound "audio/sfx/run.mp3"

    "Without another thought, he rushes upstairs."

    show doctor worried at left onlayer portraits with dissolve

    doctor "\"Mother...\""

    hide doctor onlayer portraits with dissolve

    show mother sick with dissolve

    #SOUND

    play sound "audio/sfx/suspence.mp3"

    "His Mother lies motionless."

    "One arm hangs weakly over the side of the bed."

    "The untouched glass of water remains on the bedside table."

    "The doctor immediately kneels beside her."

    "Her lips are cracked."

    #SOUND

    play sound "audio/sfx/mother_breath.mp3" volume 0.4
    
    pause 0.8

    play sound "audio/sfx/mother_breath.mp3" volume 0.4

    pause 1.2

    play sound "audio/sfx/mother_breath.mp3" volume 0.4

    "Her throat moves weakly."

    show mother sick with dissolve 
     
    "She is trying to swallow."

    "But nothing happens."

    "Even her own saliva no longer passes."

    "He quickly lifts her into his arms."
 
    show doctor panicked at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Gasp.mp3"

    doctor "\"Mother!\""

    hide doctor onlayer portraits with dissolve

    "The liquid trickles down her chin."

    "She can no longer swallow."

    if knows_dysphagia:

        $ dysphagia_entry.locked = False

        show doctor worried at left onlayer portraits with dissolve 
         
        doctor "Her {a=glossary:dysphagia_entry}dysphagia{/a}..."

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "It's gotten much worse."

        hide doctor onlayer portraits with dissolve

    else:

        show doctor worried at left onlayer portraits with dissolve 

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "Of course."

        $ dysphagia_entry.locked = False

        doctor "{a=glossary:dysphagia_entry}Dysphagia{/a}."

        doctor "The disease has progressed further than I thought."

        hide doctor onlayer portraits with dissolve

        $ knows_dysphagia = True

    "His hands begin to shake."

    show doctor panicked at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Socked.mp3"

    doctor "\"...No.\""

    hide doctor onlayer portraits with dissolve

    "He reaches for the glass of water."

    "Only now does he realize it has never been touched."

    "He wets her lips with trembling fingers."

    "Too late."

    #SOUND

    play sound "audio/sfx/mother_breath.mp3" volume 0.6
    
    pause 0.6

    play sound "audio/sfx/mother_breath.mp3" volume 0.4

    pause 0.4

    play sound "audio/sfx/mother_breath.mp3" volume 0.2

    "Her breathing becomes ragged."

    "Each breath shorter than the last."

    "He desperately tries to help her breathe."

    "Checks her airway."

    "Feels for a pulse."

    show doctor panicked at left onlayer portraits with dissolve 
     
    #SOUND

    play sound "audio/sfx/Socked.mp3"

    doctor "\"Mother!\""

    doctor "\"Stay with me!\""

    hide doctor onlayer portraits with dissolve

    show mother default with dissolve


    #SOUND

    play sound "audio/sfx/heavy_suspence.mp3"

    "Her chest rises once then nothing."

    "The doctor remains frozen beside the bed."

    "The bottle slips from his hand."

    "He bows his head."

    show doctor panicked at left onlayer portraits with dissolve

    doctor "\"You were calling for me.\""

    doctor "\"And I never came.\""

    hide doctor onlayer portraits with dissolve

    "For several long moments, he cannot move."

    "Finally, he gently pulls the bedsheet over her face."

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

    doctor "Understood why it said to be taken without eating..."

    hide doctor onlayer portraits with dissolve

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    scene black with fade

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_previous_death = "mother_cant_swallow"

    jump ch02_new_loop