label ch01_meet_herbalist_on_door:

    "I should answer the door first." 

    "It won't take long." 

    if not ch01_met_herbalist:

        "It's probably one of the neighbors checking on Mother."

    "I open the door." 

    if not ch01_met_herbalist:

        "A man wearing a green kimono smiles at me." 
    
    else:
        "Its the herbalist."

        "He doesnt know we have met before."

        "I have to be carefull talking to him"
        
    "The scent of dried leaves and flowers fills the air." 

    herbalist "Goodmorning! You must be Dr. Yosuke." 

    doctor "Goodmorning…"

    doctor "Excuse me sher who are you?" 

    herbalist "My name is Herbalist." 

    herbalist "I'm the herbalist from the next village. My shop is the first one you see in the central square."

    doctor "Oh nice to meet you Mr Herbalist. What brings you to our home?"
    
    $ ch01_met_herb_in_door = True

    $ ch01_met_herbalist = True
    
    jump ch01_herbalists_invitation

label ch01_go_to_hospital:

    "I look over the herbs remaining in my laboratory."

    "My supplies are not enough."

    "If I'm going to make the formula again, I'll need to restock." 

    "Mother is resting." 

    "The hospital is only ten minutes away." 

    "If I leave now, I should be back before she needs me." 

    "I grab my bag and head for the hospital."  

    "The halls are unusually quiet." 

    "The doctors and nurses are taking advantage of the rare moment of peace." 

    "I make my way to the medical storage room."  

    "I scan the shelves." 

    doctor "Licorice Root..." 

    doctor "Still enough left." 

    doctor "Polygala tenuifolia..." 

    doctor "Good." 

    "My eyes drift to another jar." 

    doctor "Panax ginseng..." 

    "Traditionally used to treat weakness and fatigue." 

    "The supply is almost gone." 

    "If I take it..." 

    "There may not be enough left for the hospital's patients." 

    "..." 

    "I leave it where it is." 

    "I gather the herbs I need and leave the storage room."  

    "As I step into the hallway, I notice an elderly man sitting quietly on a wooden bench." 

    "He smiles as I approach." 

    herbalist "You must be Dr. Yosuke." 

    doctor "Yes..." 

    doctor "Have we met before?" 

    herbalist "Not yet." 

    herbalist "My name is Herbalist."

    herbalist "I'm the herbalist from the neighboring village. My shop is the first one you see in the central square." 

    doctor "It's a pleasure to meet you." 

    "His experience is different from mine." 

    "Practical." 

    "Generations of knowledge instead of textbooks." 

    "I'd like to hear more." 

    "But Mother is waiting for me at home." 

    "I shouldn't stay away for too long."

    $ ch01_met_herb_in_hospital = True

    $ ch01_met_herbalist = True

label ch01_herbalists_invitation:
    
    herbalist "I was making a delivery to Mrs. Sato."

    herbalist "She mentioned your mother's condition." 

    herbalist "Word travels quickly in a village this small."

    doctor "I suppose it does."

    herbalist "I know you're looking for a cure." 

    herbalist "Unfortunately..." 

    herbalist "I don't have one." 

    doctor "..." 

    herbalist "But I might have something that could make her days a little easier."

    herbalist "I have a few herbs that physicians rarely bother with." 

    herbalist "Some have been passed down through generations." 

    herbalist "Perhaps you'll find them useful."

    doctor "What’s very nice of you. Yes i will be interested to see what you have. Do you have them with you?"

    herbalist "Unfortunatelly i dont carry these kinds of herbs with me but you can come with me in my shop. im heading there now. You will be back in an hour"

    if ch01_brain_hemorrhage_happened:

        "Last time I didn't go with the herbalist my mother died from brain hemorrhage and there was nothing i could do… Maybe i should go with him."

    menu: 
        "Go with the herbalist":
            jump ch01_arrythmia_good_ending

        "Return to your mother":
            jump ch01_brain_hemorrahage_ending