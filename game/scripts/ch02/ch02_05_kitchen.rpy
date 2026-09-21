label ch02_feed_the_cat :

    show doctor default at left onlayer portraits with dissolve 

    doctor "Just a few minutes."

    scene bg ch01 kitchen with fade

    #SOUND

    play sound "audio/sfx/footsteps.mp3"
    
    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    pause 1.0

    play sound "audio/sfx/footsteps.mp3"

    "He heads to the kitchen, fills a small bowl with food and kneels beside the cat."

    "She eagerly begins eating while he gently strokes her back."

    "For the first time in days, the room feels almost peaceful."

    show doctor smile at left onlayer portraits with dissolve

    #SOUND

    play sound "audio/sfx/cat_short.mp3"

    doctor "\"Feels good doesn’t it? Having a full stomach.\""

    hide doctor onlayer portraits with dissolve

    "He fills a second bowl with some water."

    show doctor default at left onlayer portraits with dissolve

    doctor "Time to go back to the lab and continue working on the formula."

    hide doctor onlayer portraits with dissolve

    scene bg ch01 lab_no_cat with fade

    "He keeps on stirring the decoction."

    show doctor default at left onlayer portraits with dissolve

    doctor "The formula is finally ready."

    doctor "The extraction is complete."

    hide doctor onlayer portraits with dissolve

    "He pours the mix slowly on a glass bottle."

    show doctor worried at left onlayer portraits with dissolve

    if ch02_first_herb_with_instructions :

        doctor "Last time I took the time and prepared dinner for Mother."

        doctor "As the instructions said.."

        doctor "..after eating."

        #SOUND

        play sound "audio/sfx/Sigh.mp3"

        doctor "But I wasn’t fast enough and Mother already passed."

        doctor "Maybe now.."

        doctor"...after already making the formula once, I saved sometime."

    if ch02_first_herb_without_instructions :

        doctor "Last time I didn’t follow the instructions."

        doctor "I thought by taking the risk I would save time and Mother would have more chances of surviving."

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions :

        show doctor default at left onlayer portraits with dissolve

        doctor "I did ask the herbalist for more information."

        doctor "He mentioned that it could be heavy on the stomach.."

        doctor "He wasn’t sure about the risks.."

        show doctor worried at left onlayer portraits with dissolve

        #SOUND

        play sound "audio/sfx/breathe_male.mp3"

        doctor "So many complications.."

        doctor "..I can’t ever know for sure."

    else :

        doctor "The herbalist said it should be taken after eating."

        doctor "But.."

        doctor "..if I make dinner know it might be too late to save her."

        doctor "Every minute counts."

    hide doctor onlayer portraits with dissolve

    menu : 

        "Give formula to Mother":

            jump ch02_first_herb_without_instructions_ending

        "Make dinner for Mother":

            jump ch02_first_herb_with_instructions_ending

    return