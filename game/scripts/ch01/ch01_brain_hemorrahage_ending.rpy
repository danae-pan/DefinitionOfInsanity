label ch01_brain_hemorrahage_ending:

    "I hesitate after hearing Herbalist's offer." 

    "The herbs in his shop could be exactly what I need." 

    "Ingredients that the hospital cannot provide..." 

    "But Mother called for me." 

    "No matter how important my research is..." 

    "I cannot ignore her." 

    doctor "Thank you, Herbalist." 

    doctor "I will visit your shop another time." 

    "I quickly return inside."  

    "I open the door." 

    doctor "Mother?" 

    "..." 

    "There is no answer." 

    if ch01_brain_hemorrahage_happend :

        "Oh no... Is this happening again?"

    "My heart begins to race." 

    "I rush toward her." 

    "She is lying in bed." 

    "Her breathing is uneven."

    "Her face is pale." 

    "She looks exhausted." 

    doctor "Mother..." 

    "I immediately check her condition." 

    if ch01_loop_count == 0:

        "Then I notice something." 

        "A broken glass lies on the floor." 

        "Water has spilled across the room." 

        "The bottle beside her bed is empty." 

        "..." 

        "She needed water." 

        "She tried to get it herself." 

        "While I was speaking with [Herbalist]..." 

        "She tried to stand." 

        "Her weakened body couldn't support her." 

        "She fell." 

        "Unable to call for help..." 

        "She forced herself back to bed." 

    else :

        "Its the same situation..."

        "The broken glass...."

        "The empty bottle..."

    "But the damage was already done." 

    "I place my hands on her." 

    "My training takes over." 

    "I check every possible sign." 

    "I search for any chance." 

    "Any way to help her." 

    "But deep down..." 

    "I already know." 

    "The fall caused severe damage." 

    "A brain hemorrhage." 

    if ch01_brain_hemorrahage_happend:

        "Exactly like last time..."

    "The hours pass slowly." 

    "I stay beside her." 

    "I try everything I can." 

    "But her condition continues to worsen." 

    "Until finally..." 

    "..." 

    "She is gone." 

    "I hold Mother's hand."

    if not ch01_met_herb_in_door:

        "I came back." 

        "I answered her call." 

        "I was here." 

        "Yet..." 

        doctor "I still couldn't save you."

    if ch01_loop_count == 0:
    
        "Eventually, reality returns." 

        "There are things that need to be done." 

        "I have to report her death." 

        "I have to prepare her body." 

        "I have to tell someone."

        "Wake"

        if not ch01_wake_happened:

            $ ch01_wake_happened == True

    else :
        
        "If I get another chance..." 

        "I will not repeat this." 

        "I will save her."

        scene black 

        "I close my eyes." 

        "Tomorrow..." 

        "I will do better."

    return