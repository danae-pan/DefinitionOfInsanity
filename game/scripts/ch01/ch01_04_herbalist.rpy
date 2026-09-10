label ch01_meet_herbalist_on_door:

    show doctor default at left onlayer portraits with dissolve

    doctor "I should answer the door first."

    doctor "It won't take long."

    if not met_herbalist:

        doctor "It's probably one of the neighbors checking on Mother."

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He opens the door." 

    if not met_herbalist:

        scene bg game_main with fade

        "A man wearing a green kimono smiles at him." 
    
    else:

        scene bg game_main with fade

        show doctor default at left onlayer portraits with dissolve

        doctor "Its the herbalist."

        doctor "He doesnt know we have met before."

        doctor "I have to be careful talking to him."

        hide doctor default onlayer portraits with dissolve
        
    "The scent of dried leaves and flowers fills the air." 

    show herbalist default at left onlayer portraits with dissolve

    herbalist "\"Goodmorning! You must be Dr. Yosuke.\""

    hide herbalist default onlayer portraits 

    show doctor default at left onlayer portraits 

    doctor "\"Goodmorning…\""

    doctor "\"Excuse me sir, who are you?\"" 

    hide doctor default onlayer portraits 

    show herbalist default at left onlayer portraits

    herbalist "\"My name is Kazuki.\"" 

    herbalist "\"I'm the herbalist from the next village. My shop is the first one you see in the central square.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Oh nice to meet you Mr. Kazuki. What brings you to our home?\""

    hide doctor default onlayer portraits

    $ ch01_met_herb_in_door = True

    $ met_herbalist = True
    
    jump ch01_herbalists_invitation

label ch01_go_to_hospital:

    $ ch01_went_to_hospital = True
    
    scene bg game_main with fade

    show doctor default at left onlayer portraits with dissolve

    doctor "The hospital is only ten minutes away." 

    doctor "If I leave now, I should be back before she needs me." 

    hide doctor default onlayer portraits with dissolve

    "He grabs his bag and heads for the hospital."  

    scene bg ch01 hospital with fade

    "The halls are unusually quiet." 

    "The doctors and nurses are taking advantage of the rare moment of peace." 

    "He makes his way to the medical storage room."  

    "He scans the shelves." 

    show doctor default at left onlayer portraits with dissolve

    $ hogo_root_entry.locked = False

    $ nagomi_root_entry.locked = False

    doctor "\"{a=glossary:nagomi_root_entry}Nagomi Root{/a}...\"" 

    doctor "\"Still enough left.\"" 

    doctor "\"{a=glossary:hogo_root_entry}Hogo Root{/a}...\""

    doctor "\"Good.\"" 

    hide doctor default onlayer portraits with dissolve

    "He gathers the herbs he needs and leaves the storage room."  

    #why we dont have a flag for the herbalist here?
    #kimono to be added to the glossary

    if not ch01_met_herb_in_door:

        "As he steps into the hallway, he notices an man wearing a kimono sitting quietly on a wooden bench." 

        "The man smiles as Yosuke approaches."

    else:

        "As he steps into the hallway, he notices Kazumi sitting quietly on a wooden bench."

        "He smiles as Yosuke approaches."

        show doctor default at left onlayer portraits with dissolve

        doctor "That's the Herbalist I met the other day."

        doctor "He is not aware of that."

        doctor "I should be careful to act like I haven't seen him before."

        hide doctor default at left onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"You must be Dr. Yosuke.\"" 

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Yes...\"" 

    doctor "\"Have we met before?\"" 

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"No we haven't.\"" 

    herbalist "\"My name is Kazuki.\""

    herbalist "\"I'm the herbalist from the neighboring village. My shop is the first one you see in the central square.\"" 

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"It's a pleasure to meet you.\"" 

    hide doctor default onlayer portraits with dissolve

    "Unlike Yosuke's medical training, the herbalist's knowledge comes from generations of experience."

    "It is practical wisdom, passed down from one healer to the next."

    show doctor default at left onlayer portraits with dissolve

    doctor "I'd like to stay and talk to him more." 

    doctor "His wisdom and kmowledge might help me to develop a better formula."

    doctor "But Mother is waiting for me at home." 

    doctor "I shouldn't stay away for too long."

    hide doctor default onlayer portraits

    $ ch01_met_herb_in_hospital = True

    $ met_herbalist = True

    menu :

        "Stay and chat":

            jump ch01_runs_late_at_hospital_comma_ending

        "Return home and make the formula":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I am sorry Kazuki, I am in a hurry.\""

            doctor "\"I will come by your store soon.\""

            hide doctor default onlayer portraits

            show herbalist default at left onlayer portraits

            herbalist "\"Will see you soon then.\""

            herbalist "\"Goodbye.\""

            hide herbalist default onlayer portraits with dissolve

            scene black with fade 

            "He quickly returns home worried about his mother."

            jump ch01_answer_mothers_call

label ch01_herbalists_invitation:

    show herbalist default at left onlayer portraits

    $ mrs_Sato_entry.locked = False
    
    herbalist "\"I was making a delivery to {a=glossary:mrs_Sato_entry}Mrs. Sato{/a}.\""

    herbalist "\"She mentioned your mother's condition.\"" 

    herbalist "\"Word travels quickly in a village this small.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"I suppose it does.\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"I know you're looking for a cure.\"" 

    herbalist "\"Unfortunately...\"" 

    herbalist "\"I don't have one.\"" 

    herbalist "\"But I might have something that could make her days a little easier.\""

    herbalist "\"I have a few herbs that physicians rarely bother with.\"" 

    herbalist "\"Some have been passed down through generations.\"" 

    herbalist "\"Perhaps you'll find them useful.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"That’s very nice of you.\""

    doctor "\"I will be interested to see what you have.\""
    
    doctor "\"Do you have them with you?\""

    hide doctor default onlayer portraits

    show herbalist default at left onlayer portraits

    herbalist "\"Unfortunatelly I don't carry those kinds of herbs with me but you can visit my store.\""
    
    herbalist "\"I'm heading there now.\""
    
    herbalist "\"You are welcome to join me.\""

    herbalist "\"It shouldn't take more than an hour to get there and back.\""

    hide herbalist default onlayer portraits

    if ch01_brain_hemorrhage_happened:

        show doctor default at left onlayer portraits

        doctor "Last time I didn't go with the herbalist my mother died from {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a} and there was nothing i could do… Maybe i should go with him."

        hide doctor default onlayer portraits

    menu: 
        "Go with the herbalist":
            jump ch01_arrythmia_good_ending

        "Return to your mother":
            jump ch01_brain_hemorrahage_ending