label ch02_feed_the_cat :

    doctor "Just a few minutes."

    scene bg ch01 kitchen with fade

    "He heads to the kitchen, fills a small bowl with food and kneels beside the cat."

    "She eagerly begins eating while he gently strokes her back."

    "For the first time in days, the room feels almost peaceful."

    show doctor default at left onlayer portraits

    doctor "Feels good doesn’t it? Having a full stomach."

    hide doctor default onlayer portraits

    "He fills a second bowl with some water."

    doctor "Time to go back to the lab and continue working on the formula."

    "He keeps on stirring the decoction."

    doctor "The formula is finally ready."

    doctor "The extraction is complete."

    "He pours the mix slowly on a glass bottle."

    if ch02_first_herb_with_instructions :

        doctor "Last time I took the time and prepared dinner for Mother."

        doctor "As the instructions said.."

        doctor "..after eating."

        doctor "But I wasn’t fast enough and Mother already passed."

        doctor "Maybe now.."

        doctor"...after already making the formula once, I saved sometime."

    if ch02_first_herb_without_instructions :

        doctor "Last time I didn’t follow the instructions."

        doctor "I thought by taking the risk I would save time and Mother would have more chances of surviving."

    if ch02_first_herb_with_instructions or ch02_first_herb_without_instructions :

        doctor "But last time I did ask the herbalist for more information."

        doctor "He mentioned that it could be heavy on the stomach.."

        doctor "He wasn’t sure about the risks.."

        doctor "So many complications.."

        doctor "..I can’t ever know for sure."

    else :

        doctor "The herbalist said it should be taken after eating."

        doctor "But.."

        doctor "..if I make dinner know it might be too late to save her."

        doctor "Every minute counts."

    menu : 

        "Give formula to mother":

            jump ch02_first_herb_without_instructions_ending

        "Make dinner for mother":

            jump ch02_first_herb_with_instructions_ending

    return