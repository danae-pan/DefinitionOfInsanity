label ch01_meet_herbalist_on_door:

    show doctor default at left onlayer portraits with dissolve

    doctor "I should answer the door first."

    doctor "It won't take long."

    if not met_herbalist:

        doctor "It's probably one of the neighbors checking on Mother."

    elif ch01_met_herb_in_door: 

        doctor "It might be Mr. Kazuki"

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "He opens the door." 

    if not met_herbalist:

        scene bg game_main with fade

        $kimono_entry.locked = False

        "A man wearing a green {a=glossary:kimono_entry}kimono{/a} smiles at him." 
    
    else:

        scene bg game_main with fade

        show doctor default at left onlayer portraits with dissolve

        doctor "It's Mr. Kazuki."

        doctor "He doesn't know we have met before."

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

    herbalist "\"I'm the Herbalist from the neighboring village. My store is the first one you see in the central square.\""

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"Oh nice to meet you Mr. Kazuki. What brings you to our home?\""

    hide doctor default onlayer portraits

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

    doctor "I still have enough left back home." 

    doctor "\"I should get some just in case.\""

    doctor "\"{a=glossary:hogo_root_entry}Hogo Root{/a}...\""

    doctor "\"Good.\"" 

    hide doctor default onlayer portraits with dissolve

    "He gathers the herbs he needs and leaves the storage room."  

    #TODO: add a flag for the herbalist
    #TODO: add kimono t the glossary

    if not met_herbalist:

        $ kimono_entry.locked = False

        "As he steps into the hallway, he notices an man wearing a {a=glossary:kimono_entry}kimono{/a} sitting quietly on a wooden bench." 

        "The man smiles as Yosuke approaches."

        show herbalist default at left onlayer portraits with dissolve


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

    herbalist "\"I'm the Herbalist from the neighboring village. My store is the first one you see in the central square.\"" 

    hide herbalist default onlayer portraits

    show doctor default at left onlayer portraits

    doctor "\"It's a pleasure to meet you.\"" 

    hide doctor default onlayer portraits with dissolve

    "Unlike Yosuke's medical training, Mr. Kazuki's knowledge comes from generations of experience."

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

            #TODO: Fix the routes here, there are two seperate endings

            jump ch01_runs_late_at_hospital_comma_ending

        "Return home and make the formula":

            show doctor default at left onlayer portraits with dissolve

            doctor "\"I am sorry Mr. Kazuki, I am in a hurry.\""

            doctor "\"I will come by your store soon.\""

            hide doctor default onlayer portraits

            show herbalist default at left onlayer portraits

            herbalist "\"Will see you soon then.\""

            herbalist "\"Goodbye.\""

            hide herbalist default onlayer portraits with dissolve

            scene black with fade 

            "He quickly returns home worried about his Mother."

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

    #TODO: check whether thss condition plays correctly wiyh the flag being moved OK :)

    #This loop is when this route continues to "Return to your mother" choice

    #for this the condition/flag should not be reset after each chapter 1 ending

    if ch01_brain_hemorrhage_happened and ch01_met_herb_in_door:

        show doctor default at left onlayer portraits with dissolve

        $ brain_hemorrhage_entry.locked = False

        doctor "Last time I didn't go with the herbalist my mother died from {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}..."
        
        doctor "There was nothing I could do…"
        
        doctor "Maybe I should go with him."

        hide doctor default onlayer portraits with dissolve

    $ ch01_met_herb_in_door = True

    menu: 
        "Go with the Herbalist":

            "He glances back toward Mother's room."

            show doctor default at left onlayer portraits with dissolve

            doctor "She called for me..." 

            doctor "But..."

            hide doctor default onlayer portraits with dissolve

            jump ch01_arrythmia_good_ending

        "Answer your Mother's call":

            jump ch01_brain_hemorrahage_ending